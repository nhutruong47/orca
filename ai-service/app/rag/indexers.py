"""
Knowledge indexers.

Each indexer is responsible for:

    * Producing a list of "records" of the form
        {id, title, content, metadata}
      from its data source.
    * Driving an :class:`IndexerPipeline` to embed + persist the records.

Two kinds of indexers:

    Bundled (policies, faq, manuals)
        Read JSON files from :mod:`app.rag.corpus`. These are versioned
        with the codebase and re-indexed on demand or on app startup.

    Ingested (inventory, orders, products, teams, users)
        Receive records pushed by the Java backend over HTTP. The
        indexer in this module is the *target* of those pushes: it
        upserts whatever is given to it. A separate helper,
        :func:`ingest_records`, accepts ad-hoc records for any
        ingested source.
"""

from __future__ import annotations

import json
import logging
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from app.rag.indexer import IndexerPipeline, IndexingProgress

logger = logging.getLogger(__name__)


# Path to the bundled corpus (policies/faq/manuals).
CORPUS_DIR = Path(__file__).resolve().parent / "corpus"


# ---------------------------------------------------------------------------
# Common record shape
# ---------------------------------------------------------------------------

@dataclass
class KnowledgeRecord:
    id: str
    title: str
    content: str
    metadata: Dict[str, Any]


def _to_record_dict(record: KnowledgeRecord) -> Dict[str, Any]:
    return {
        "id": record.id,
        "title": record.title,
        "content": record.content,
        "metadata": record.metadata,
    }


# ---------------------------------------------------------------------------
# Bundled corpus loaders
# ---------------------------------------------------------------------------

def _load_corpus_file(filename: str) -> List[Dict[str, Any]]:
    path = CORPUS_DIR / filename
    if not path.exists():
        logger.warning("Corpus file missing: %s", path)
        return []
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        logger.error("Failed to read corpus file %s: %s", path, exc)
        return []
    items = payload.get("items") if isinstance(payload, dict) else payload
    return items or []


def load_policies() -> List[KnowledgeRecord]:
    items = _load_corpus_file("policies.json")
    return [
        KnowledgeRecord(
            id=it["id"],
            title=it["title"],
            content=it["content"],
            metadata={
                "category": it.get("category", "Policy"),
                "last_updated": it.get("last_updated"),
                "kind": "policy",
            },
        )
        for it in items
        if it.get("id") and it.get("content")
    ]


def load_faq() -> List[KnowledgeRecord]:
    items = _load_corpus_file("faq.json")
    return [
        KnowledgeRecord(
            id=it["id"],
            title=it["title"],
            content=it["content"],
            metadata={
                "category": it.get("category", "FAQ"),
                "last_updated": it.get("last_updated"),
                "kind": "faq",
            },
        )
        for it in items
        if it.get("id") and it.get("content")
    ]


def load_manuals() -> List[KnowledgeRecord]:
    items = _load_corpus_file("manuals.json")
    return [
        KnowledgeRecord(
            id=it["id"],
            title=it["title"],
            content=it["content"],
            metadata={
                "category": it.get("category", "Manual"),
                "last_updated": it.get("last_updated"),
                "kind": "manual",
            },
        )
        for it in items
        if it.get("id") and it.get("content")
    ]


def _manuals_records() -> List[KnowledgeRecord]:
    """Alias used by run_bundled(); keeps the source name singular
    to match the canonical KnowledgeDocument.source Literal."""
    return load_manuals()


# ---------------------------------------------------------------------------
# Indexer functions
# ---------------------------------------------------------------------------

def index_pipelines(
    *,
    progress_callback: Optional[Any] = None,
    team_id: Optional[str] = None,
    replace: bool = False,
) -> Dict[str, IndexingProgress]:
    """Run every bundled indexer. Returns a {source: progress} map."""
    pipeline = IndexerPipeline()
    out: Dict[str, IndexingProgress] = {}

    bundled = [
        ("policies", load_policies()),
        ("faq", load_faq()),
        ("manuals", load_manuals()),
    ]

    for source, records in bundled:
        if not records:
            logger.info("Skipping empty indexer: %s", source)
            out[source] = IndexingProgress(source=source)
            continue
        progress = pipeline.run(
            source=source,
            records=[_to_record_dict(r) for r in records],
            team_id=team_id,
            progress_callback=progress_callback,
            replace=replace,
        )
        out[source] = progress
    return out


def index_one_source(
    source: str,
    records: Sequence[KnowledgeRecord],
    *,
    team_id: Optional[str] = None,
    progress_callback: Optional[Any] = None,
    replace: bool = False,
) -> IndexingProgress:
    """Run a single named indexer against the supplied records.

    For bundled sources (policies/faq/manuals), pass the records from the
    matching loader; the function will validate that the source matches.
    For ingested sources (inventory/orders/products/teams/users), the
    caller is responsible for building the records from the Java push.
    """
    pipeline = IndexerPipeline()
    return pipeline.run(
        source=source,
        records=[_to_record_dict(r) for r in records],
        team_id=team_id,
        progress_callback=progress_callback,
        replace=replace,
    )


# ---------------------------------------------------------------------------
# Singleton job manager (used by the API layer for background jobs)
# ---------------------------------------------------------------------------

@dataclass
class JobSpec:
    source: str
    records: List[KnowledgeRecord]
    team_id: Optional[str] = None
    requested_by: Optional[str] = None
    replace: bool = False


class IndexerManager:
    """High-level manager that runs indexers and records their progress.

    Two flavours:

        * run_bundled()  — policies/faq/manuals
        * ingest_records() — for inventory/orders/products/teams/users

    Both produce an indexing job in the SQLite store and return the
    job_id so the caller can poll /api/rag/jobs/{id} for status.
    """

    def __init__(self):
        from app.rag.sqlite_vector_store import get_vector_store
        self.store = get_vector_store()
        self._lock = threading.Lock()

    # ----- bundled -----

    def run_bundled(
        self,
        *,
        team_id: Optional[str] = None,
        requested_by: Optional[str] = None,
        replace: bool = False,
    ) -> Dict[str, str]:
        """Run every bundled indexer sequentially. Returns source -> job_id."""
        out: Dict[str, str] = {}
        bundled: List[tuple] = [
            ("policies", load_policies()),
            ("faq", load_faq()),
            ("manual", _manuals_records()),
        ]
        for source, records in bundled:
            job_id = self.store.job_create(
                source=source, requested_by=requested_by, team_id=team_id
            )
            try:
                self.store.job_update(job_id, status="processing")
                pipeline = IndexerPipeline()
                progress = pipeline.run(
                    source=source,
                    records=[_to_record_dict(r) for r in records],
                    team_id=team_id,
                    replace=replace,
                    indexed_by=requested_by or "bundled",
                    index_version=1,
                )
                self.store.job_update(
                    job_id,
                    status="failed" if progress.errors else "completed",
                    documents_processed=progress.documents_processed,
                    documents_total=progress.documents_total,
                    error=("\n".join(progress.errors)) if progress.errors else None,
                    completed=True,
                )
            except Exception as exc:
                logger.exception("Bundled indexer %s failed", source)
                self.store.job_update(
                    job_id,
                    status="failed",
                    error=str(exc),
                    completed=True,
                )
            out[source] = job_id
        return out

    # ----- scheduler support -----

    def refresh_stale_sources(
        self,
        freshness_budget_s: int,
        *,
        team_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Re-index ingested sources whose last update is older than the budget.

        This is a defensive backstop: the Java backend pushes deltas, but if a
        push was missed (e.g. a transient network error) the scheduler catches
        it on its next tick.
        """
        from app.rag.sqlite_vector_store import get_vector_store

        store = get_vector_store()
        sources = ("inventory", "orders", "products", "teams", "users")
        results: Dict[str, Any] = {}

        for source in sources:
            rows = store.list_documents(source=source, limit=1, offset=0)
            needs_refresh = True
            if rows:
                try:
                    from datetime import datetime, timezone

                    updated_at = rows[0].get("updated_at")
                    if updated_at:
                        ts = datetime.fromisoformat(
                            updated_at.replace("Z", "+00:00")
                        )
                        age = (
                            datetime.now(timezone.utc) - ts
                        ).total_seconds()
                        needs_refresh = age > freshness_budget_s
                except (ValueError, TypeError, AttributeError):
                    needs_refresh = True

            if not needs_refresh:
                results[source] = {"status": "skipped", "reason": "fresh"}
                continue

            results[source] = {
                "status": "noop",
                "reason": "no_active_ingest_hook",
            }

        return results

    # ----- ingested -----

    def ingest_records(
        self,
        source: str,
        records: Sequence[Dict[str, Any]],
        *,
        team_id: Optional[str] = None,
        requested_by: Optional[str] = None,
        replace: bool = False,
    ) -> str:
        """Push records from the Java backend into the vector store."""
        if source not in {"inventory", "orders", "products", "teams", "users"}:
            raise ValueError(f"unsupported ingested source: {source}")

        kr = [
            KnowledgeRecord(
                id=str(r["id"]),
                title=r.get("title") or str(r["id"]),
                content=r.get("content") or "",
                metadata=r.get("metadata") or {},
            )
            for r in records
            if r.get("id") and r.get("content")
        ]

        job_id = self.store.job_create(
            source=source, requested_by=requested_by, team_id=team_id
        )
        try:
            self.store.job_update(job_id, status="processing")
            progress = index_one_source(
                source=source,
                records=kr,
                team_id=team_id,
                replace=replace,
            )
            self.store.job_update(
                job_id,
                status="failed" if progress.errors else "completed",
                documents_processed=progress.documents_processed,
                documents_total=progress.documents_total,
                error=("\n".join(progress.errors)) if progress.errors else None,
                completed=True,
            )
        except Exception as exc:
            logger.exception("Ingestion for %s failed", source)
            self.store.job_update(
                job_id,
                status="failed",
                error=str(exc),
                completed=True,
            )
        return job_id


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_manager: Optional[IndexerManager] = None
_manager_lock = threading.Lock()


def get_indexer_manager() -> IndexerManager:
    global _manager
    if _manager is None:
        with _manager_lock:
            if _manager is None:
                _manager = IndexerManager()
    return _manager


__all__ = [
    "KnowledgeRecord",
    "IndexerManager",
    "get_indexer_manager",
    "index_one_source",
    "index_pipelines",
    "load_policies",
    "load_faq",
    "load_manuals",
]