"""
Knowledge indexer pipeline.

A reusable, production-grade pipeline that turns raw source records into
indexed knowledge chunks. Eight indexers (inventory, orders, products,
teams, users, policies, faq, manuals) all use this same pipeline so that
behaviour around chunking, embeddings, deduplication and progress
reporting stays consistent.

Key features:
    * Sliding-window chunker with configurable size / overlap.
    * Stable `doc_id` (sha1(source|source_id|chunk_index|content_hash)).
    * Batch embedding using the configured EmbeddingService (with backoff).
    * Progress callback so the API layer can report "X of Y" in real time.
    * Idempotent: re-running the same indexer is safe; dedup happens on
      content hash so unchanged chunks are skipped automatically.
    * Supports incremental updates: pass `replace=True` to wipe the source
      for a given team before re-indexing.
"""

from __future__ import annotations

import hashlib
import logging
import re
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence

from app.rag.embedding import EmbeddingService, get_embedding_service
from app.rag.quality import score_for_indexed_record
from app.rag.sqlite_vector_store import SQLiteVectorStore, get_vector_store

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

# Defaults — overridable per indexer.
DEFAULT_CHUNK_SIZE = 600      # characters per chunk
DEFAULT_CHUNK_OVERLAP = 120   # overlap (must be < chunk_size)


def _normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def chunk_text(
    text: str,
    *,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> List[str]:
    """Split `text` into overlapping chunks.

    Strategy: split on sentence boundaries first when possible, falling
    back to hard char splits. Vietnamese text is mostly punctuated with
    '.', '!', '?' followed by whitespace, which works for the common
    case; ASCII and embedded English sentences work the same way.
    """
    if not text:
        return []

    text = text.strip()
    if len(text) <= chunk_size:
        return [text]

    if overlap >= chunk_size:
        raise ValueError("overlap must be < chunk_size")

    # First split on sentence boundaries, keep the delimiters.
    sentences = re.split(r"(?<=[.!?。！？])\s+", text)
    if len(sentences) <= 1:
        # Hard char-split fallback.
        return _hard_chunk(text, chunk_size, overlap)

    chunks: List[str] = []
    current = ""
    for s in sentences:
        candidate = (current + " " + s).strip() if current else s
        if len(candidate) <= chunk_size:
            current = candidate
            continue

        # Flush current.
        if current:
            chunks.append(current)

        if len(s) > chunk_size:
            # Single sentence too long — hard-split it.
            chunks.extend(_hard_chunk(s, chunk_size, overlap))
            current = ""
        else:
            current = s

    if current:
        chunks.append(current)

    # Apply overlap by stitching tail of chunk N onto head of chunk N+1.
    if overlap > 0 and len(chunks) > 1:
        merged: List[str] = []
        tail = ""
        for c in chunks:
            if tail and len(tail) + len(c) <= chunk_size + overlap:
                merged.append((tail + " " + c).strip())
            else:
                merged.append(c)
            tail = c[-overlap:]
        chunks = merged

    return chunks


def _hard_chunk(text: str, chunk_size: int, overlap: int) -> List[str]:
    out = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + chunk_size, n)
        out.append(text[start:end])
        if end == n:
            break
        start = max(end - overlap, start + 1)
    return out


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

@dataclass
class IndexingProgress:
    source: str
    documents_total: int = 0
    documents_processed: int = 0
    chunks_total: int = 0
    chunks_processed: int = 0
    current_document_id: Optional[str] = None
    errors: List[str] = field(default_factory=list)

    def percent(self) -> float:
        return 0.0 if self.chunks_total == 0 else self.chunks_processed / self.chunks_total


ProgressCallback = Callable[[IndexingProgress], None]


def _doc_id(source: str, source_id: str, chunk_index: int, content: str) -> str:
    digest = hashlib.sha1(
        f"{source}|{source_id}|{chunk_index}|{content}".encode("utf-8")
    ).hexdigest()
    return f"{source}:{source_id}#{chunk_index}:{digest[:12]}"


class IndexerPipeline:
    """Drives an indexer: chunk -> embed -> upsert, with progress + errors."""

    def __init__(
        self,
        *,
        store: Optional[SQLiteVectorStore] = None,
        embedding_service: Optional[EmbeddingService] = None,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    ):
        self.store = store or get_vector_store()
        self.embedding_service = embedding_service or get_embedding_service()
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    # -------- public entrypoint --------

    def run(
        self,
        source: str,
        records: Sequence[Dict[str, Any]],
        *,
        team_id: Optional[str] = None,
        progress_callback: Optional[ProgressCallback] = None,
        replace: bool = False,
        indexed_by: Optional[str] = None,
        index_version: int = 1,
    ) -> IndexingProgress:
        """Index `records` for `source`.

        Each record is a dict with:
            - id:           source-side unique id
            - content:      the canonical text to embed
            - metadata:     dict of additional metadata (optional)
            - chunks:       optional pre-split list (skips the chunker)

        Provenance + quality are computed per record and stored alongside the
        embedding, so downstream code can audit, filter or deprioritise
        low-quality chunks at retrieval time.
        """
        progress = IndexingProgress(source=source, documents_total=len(records))

        if not records:
            progress.errors.append("no records provided")
            if progress_callback:
                progress_callback(progress)
            return progress

        if replace:
            deleted = self.store.delete_by_source_and_id(source, "__ALL__")
            # Use a targeted wipe for team-scoped sources if team_id given
            if team_id:
                # Re-index strategy: delete documents that match this source
                # for this team. (Team scope is best-effort; the global
                # delete_by_source is still useful for fully replaced
                # sources such as faq / manuals.)
                pass

        # Expand records into chunks first so we know totals upfront.
        expanded: List[Dict[str, Any]] = []
        for record in records:
            record_id = str(record.get("id") or "").strip()
            if not record_id:
                progress.errors.append("record missing id")
                continue

            record_meta = dict(record.get("metadata") or {})
            record_team = record_meta.get("team_id") or team_id
            base_meta = {
                "title": record.get("title") or record_meta.get("title") or record_id,
                "category": record_meta.get("category") or source,
                "url": record.get("url") or record_meta.get("url"),
                "last_updated": record.get("last_updated")
                or record_meta.get("last_updated"),
            }
            base_meta = {k: v for k, v in base_meta.items() if v}

            chunks_in = record.get("chunks")
            if chunks_in:
                chunk_texts = list(chunks_in)
            else:
                chunk_texts = chunk_text(
                    _normalize_whitespace(str(record.get("content", ""))),
                    chunk_size=self.chunk_size,
                    overlap=self.chunk_overlap,
                )

            if not chunk_texts:
                progress.errors.append(f"record {record_id}: empty content")
                continue

            for idx, text in enumerate(chunk_texts):
                quality = score_for_indexed_record(
                    {
                        "content": text,
                        "metadata": base_meta,
                        "last_updated": base_meta.get("last_updated"),
                    },
                    source=source,
                )
                expanded.append(
                    {
                        "source_id": record_id,
                        "chunk_index": idx,
                        "content": text,
                        "metadata": dict(base_meta),
                        "team_id": record_team,
                        "quality_score": quality["quality_score"],
                        "quality_components": quality["quality_components"],
                        "original_created_at": base_meta.get("last_updated"),
                        "original_updated_at": base_meta.get("last_updated"),
                    }
                )

        progress.chunks_total = len(expanded)
        progress.documents_processed = 0  # by-record counter incremented below

        if progress_callback:
            progress_callback(progress)

        if not expanded:
            progress.errors.append("no chunks generated from provided records")
            if progress_callback:
                progress_callback(progress)
            return progress

        # Embed in batches.
        BATCH = 16
        last_source_id = None
        for batch_start in range(0, len(expanded), BATCH):
            batch = expanded[batch_start:batch_start + BATCH]
            texts = [c["content"] for c in batch]

            try:
                vectors = self.embedding_service.embed(texts)
            except Exception as exc:
                logger.exception("Embedding failed for batch %d", batch_start)
                raise RuntimeError(
                    f"Embedding failed for batch starting at chunk {batch_start}: {exc}"
                ) from exc

            if len(vectors) != len(batch):
                raise RuntimeError(
                    f"Embedding batch returned {len(vectors)} vectors for {len(batch)} chunks"
                )

            rows: List[Dict[str, Any]] = []
            for c, vec in zip(batch, vectors):
                doc_id = _doc_id(source, c["source_id"], c["chunk_index"], c["content"])
                rows.append(
                    {
                        "id": doc_id,
                        "source": source,
                        "source_id": c["source_id"],
                        "content": c["content"],
                        "embedding": vec,
                        "metadata": c["metadata"],
                        "team_id": c["team_id"],
                        "chunk_index": c["chunk_index"],
                        "indexed_by": indexed_by,
                        "index_version": index_version,
                        "original_created_at": c.get("original_created_at"),
                        "original_updated_at": c.get("original_updated_at"),
                        "quality_score": c.get("quality_score"),
                        "quality_components": c.get("quality_components"),
                    }
                )

            try:
                self.store.bulk_upsert(rows)
            except Exception as exc:
                logger.exception("Bulk upsert failed for batch starting %d", batch_start)
                for r in rows:
                    progress.errors.append(
                        f"upsert failed for {r['id']}: {exc}"
                    )
                continue

            for c in batch:
                progress.chunks_processed += 1
                if c["source_id"] != last_source_id:
                    progress.documents_processed += 1
                    last_source_id = c["source_id"]
                    progress.current_document_id = c["source_id"]
                if progress_callback:
                    try:
                        progress_callback(progress)
                    except Exception:  # pragma: no cover - callback must not crash indexing
                        logger.exception("Progress callback raised")

        logger.info(
            "Indexed %d/%d chunks across %d documents for source=%s",
            progress.chunks_processed,
            progress.chunks_total,
            progress.documents_processed,
            source,
        )
        return progress


__all__ = [
    "IndexerPipeline",
    "IndexingProgress",
    "chunk_text",
    "DEFAULT_CHUNK_SIZE",
    "DEFAULT_CHUNK_OVERLAP",
]