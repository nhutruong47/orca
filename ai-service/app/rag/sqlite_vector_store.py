"""
SQLite-backed vector store.

Why SQLite:
- Zero infrastructure (no separate DB server to provision or monitor).
- ACID transactions, WAL journaling, B-tree indexes — battle-tested in
  production by Apple, Google, every major browser, mobile apps and many
  SaaS platforms (Notion, Figma Cloud, Cloudflare Workers KV, etc.).
- Embedded in the Python standard library, so no new Python dependencies
  are required and the service stays self-contained.
- Scales comfortably to millions of rows; this AI knowledge corpus is
  far smaller (a few hundred to a few hundred thousand chunks).

Schema:
    documents(
        id          TEXT PRIMARY KEY,
        source      TEXT NOT NULL,
        source_id   TEXT NOT NULL,
        content     TEXT NOT NULL,
        metadata    TEXT NOT NULL,        -- JSON
        embedding   BLOB NOT NULL,        -- float32[] packed
        chunk_index INTEGER NOT NULL DEFAULT 0,
        team_id     TEXT,                 -- optional team scoping
        content_hash TEXT NOT NULL,       -- for deduplication
        created_at  TEXT NOT NULL,
        updated_at  TEXT NOT NULL
    )

    conversations(
        conversation_id TEXT PRIMARY KEY,
        user_id TEXT,
        last_seen_at TEXT NOT NULL
    )

    conversation_messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        metadata TEXT,
        timestamp TEXT NOT NULL,
        FOREIGN KEY(conversation_id) REFERENCES conversations(conversation_id) ON DELETE CASCADE
    )

    indexing_jobs(
        job_id TEXT PRIMARY KEY,
        source TEXT NOT NULL,
        status TEXT NOT NULL,
        documents_processed INTEGER NOT NULL DEFAULT 0,
        documents_total INTEGER NOT NULL DEFAULT 0,
        started_at TEXT,
        completed_at TEXT,
        error TEXT,
        requested_by TEXT,
        team_id TEXT
    )
"""

from __future__ import annotations

import json
import sqlite3
import struct
import threading
import time
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _pack_floats(values: Iterable[float]) -> bytes:
    arr = list(values)
    if not arr:
        return b""
    # float32 saves 2× vs float64 with negligible precision loss for embeddings.
    return struct.pack(f"<{len(arr)}f", *arr)


def _unpack_floats(blob: bytes) -> List[float]:
    if not blob:
        return []
    n = len(blob) // 4
    return list(struct.unpack(f"<{n}f", blob))


def _normalize(vec: List[float]) -> List[float]:
    s = 0.0
    for x in vec:
        s += x * x
    if s == 0.0:
        return vec
    norm = s ** 0.5
    return [x / norm for x in vec]


def _cosine(a: List[float], b: List[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = 0.0
    na = 0.0
    nb = 0.0
    for x, y in zip(a, b):
        dot += x * y
        na += x * x
        nb += y * y
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / ((na ** 0.5) * (nb ** 0.5))


def _content_hash(content: str) -> str:
    import hashlib
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Store
# ---------------------------------------------------------------------------

class SQLiteVectorStore:
    """Production-ready SQLite-backed vector + metadata store."""

    SCHEMA_VERSION = 2

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._init_schema()

    # ---- connection management ----

    @contextmanager
    def _conn(self):
        # check_same_thread=False lets FastAPI's threadpool share one connection.
        # We still serialize writes via a re-entrant lock.
        c = sqlite3.connect(str(self.db_path), check_same_thread=False)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA synchronous=NORMAL")
        c.execute("PRAGMA foreign_keys=ON")
        try:
            yield c
            c.commit()
        except Exception:
            c.rollback()
            raise
        finally:
            c.close()

    # ---- migration helpers ----

    def _add_column_if_missing(self, c, table: str, column: str, ddl: str) -> None:
        """Lightweight SQLite migration: add a column if it doesn't exist yet."""
        rows = c.execute(f"PRAGMA table_info({table})").fetchall()
        names = {r["name"] for r in rows}
        if column not in names:
            c.execute(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}")

    def _init_schema(self) -> None:
        with self._conn() as c:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS meta (
                    key   TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
                """
            )
            c.execute(
                "INSERT OR IGNORE INTO meta(key,value) VALUES ('schema_version', ?)",
                (str(self.SCHEMA_VERSION),),
            )

            c.execute(
                """
                CREATE TABLE IF NOT EXISTS documents (
                    id            TEXT PRIMARY KEY,
                    source        TEXT NOT NULL,
                    source_id     TEXT NOT NULL,
                    content       TEXT NOT NULL,
                    metadata      TEXT NOT NULL,
                    embedding     BLOB NOT NULL,
                    chunk_index   INTEGER NOT NULL DEFAULT 0,
                    team_id       TEXT,
                    content_hash  TEXT NOT NULL,
                    created_at    TEXT NOT NULL,
                    updated_at    TEXT NOT NULL
                )
                """
            )
            # -------- provenance + quality migration (idempotent) --------
            # SCHEMA_VERSION 2 introduces per-document provenance tracking and
            # quality scoring. New columns are nullable so existing rows are
            # preserved untouched.
            self._add_column_if_missing(c, "documents", "indexed_at", "TEXT")
            self._add_column_if_missing(c, "documents", "indexed_by", "TEXT")
            self._add_column_if_missing(
                c, "documents", "index_version", "INTEGER NOT NULL DEFAULT 1"
            )
            self._add_column_if_missing(
                c, "documents", "original_created_at", "TEXT"
            )
            self._add_column_if_missing(
                c, "documents", "original_updated_at", "TEXT"
            )
            self._add_column_if_missing(
                c, "documents", "quality_score", "REAL"
            )
            self._add_column_if_missing(
                c, "documents", "quality_components", "TEXT"
            )

            c.execute("CREATE INDEX IF NOT EXISTS idx_doc_source ON documents(source)")
            c.execute("CREATE INDEX IF NOT EXISTS idx_doc_team ON documents(team_id)")
            c.execute("CREATE INDEX IF NOT EXISTS idx_doc_srcid ON documents(source_id)")
            c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_doc_dedup ON documents(content_hash)")

            c.execute(
                """
                CREATE TABLE IF NOT EXISTS conversations (
                    conversation_id TEXT PRIMARY KEY,
                    user_id         TEXT,
                    last_seen_at    TEXT NOT NULL
                )
                """
            )

            c.execute(
                """
                CREATE TABLE IF NOT EXISTS conversation_messages (
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT NOT NULL,
                    role            TEXT NOT NULL,
                    content         TEXT NOT NULL,
                    metadata        TEXT,
                    timestamp       TEXT NOT NULL,
                    FOREIGN KEY(conversation_id) REFERENCES conversations(conversation_id) ON DELETE CASCADE
                )
                """
            )
            c.execute(
                "CREATE INDEX IF NOT EXISTS idx_conv_msgs ON conversation_messages(conversation_id, id)"
            )

            c.execute(
                """
                CREATE TABLE IF NOT EXISTS indexing_jobs (
                    job_id              TEXT PRIMARY KEY,
                    source              TEXT NOT NULL,
                    status              TEXT NOT NULL,
                    documents_processed INTEGER NOT NULL DEFAULT 0,
                    documents_total     INTEGER NOT NULL DEFAULT 0,
                    started_at          TEXT,
                    completed_at        TEXT,
                    error               TEXT,
                    requested_by        TEXT,
                    team_id             TEXT
                )
                """
            )
            c.execute(
                "CREATE INDEX IF NOT EXISTS idx_job_status ON indexing_jobs(status, started_at)"
            )

    # ---- CRUD: documents ----

    def upsert_document(
        self,
        doc_id: str,
        source: str,
        source_id: str,
        content: str,
        embedding: List[float],
        metadata: Optional[Dict[str, Any]] = None,
        team_id: Optional[str] = None,
        chunk_index: int = 0,
        indexed_by: Optional[str] = None,
        index_version: int = 1,
        original_created_at: Optional[str] = None,
        original_updated_at: Optional[str] = None,
        quality_score: Optional[float] = None,
        quality_components: Optional[Dict[str, float]] = None,
    ) -> None:
        meta_json = json.dumps(metadata or {}, ensure_ascii=False, default=str)
        quality_json = (
            json.dumps(quality_components, ensure_ascii=False, default=str)
            if quality_components is not None
            else None
        )
        emb_bytes = _pack_floats(embedding)
        now = _utcnow_iso()
        hash_ = _content_hash(content)

        with self._lock, self._conn() as c:
            c.execute(
                """
                INSERT INTO documents (
                    id, source, source_id, content, metadata,
                    embedding, chunk_index, team_id, content_hash,
                    created_at, updated_at,
                    indexed_at, indexed_by, index_version,
                    original_created_at, original_updated_at,
                    quality_score, quality_components
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    source = excluded.source,
                    source_id = excluded.source_id,
                    content = excluded.content,
                    metadata = excluded.metadata,
                    embedding = excluded.embedding,
                    chunk_index = excluded.chunk_index,
                    team_id = excluded.team_id,
                    content_hash = excluded.content_hash,
                    updated_at = excluded.updated_at,
                    indexed_at = excluded.indexed_at,
                    indexed_by = excluded.indexed_by,
                    index_version = excluded.index_version,
                    original_created_at = excluded.original_created_at,
                    original_updated_at = excluded.original_updated_at,
                    quality_score = excluded.quality_score,
                    quality_components = excluded.quality_components
                """,
                (
                    doc_id, source, source_id, content, meta_json,
                    emb_bytes, chunk_index, team_id, hash_,
                    now, now,
                    now, indexed_by, index_version,
                    original_created_at, original_updated_at,
                    quality_score, quality_json,
                ),
            )

    def bulk_upsert(self, docs: List[Dict[str, Any]]) -> int:
        """Insert/update many documents in one transaction.

        Each doc dict must contain: id, source, source_id, content, embedding.
        Optional: metadata, team_id, chunk_index, indexed_by, index_version,
        original_created_at, original_updated_at, quality_score,
        quality_components.
        """
        if not docs:
            return 0
        rows = []
        now = _utcnow_iso()
        for d in docs:
            meta_json = json.dumps(d.get("metadata") or {}, ensure_ascii=False, default=str)
            quality_components = d.get("quality_components")
            quality_json = (
                json.dumps(quality_components, ensure_ascii=False, default=str)
                if quality_components is not None
                else None
            )
            rows.append(
                (
                    d["id"],
                    d["source"],
                    d["source_id"],
                    d["content"],
                    meta_json,
                    _pack_floats(d["embedding"]),
                    int(d.get("chunk_index", 0)),
                    d.get("team_id"),
                    _content_hash(d["content"]),
                    now,
                    now,
                    now,
                    d.get("indexed_by"),
                    int(d.get("index_version", 1)),
                    d.get("original_created_at"),
                    d.get("original_updated_at"),
                    d.get("quality_score"),
                    quality_json,
                ),
            )
        with self._lock, self._conn() as c:
            c.executemany(
                """
                INSERT INTO documents (
                    id, source, source_id, content, metadata,
                    embedding, chunk_index, team_id, content_hash,
                    created_at, updated_at,
                    indexed_at, indexed_by, index_version,
                    original_created_at, original_updated_at,
                    quality_score, quality_components
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    source = excluded.source,
                    source_id = excluded.source_id,
                    content = excluded.content,
                    metadata = excluded.metadata,
                    embedding = excluded.embedding,
                    chunk_index = excluded.chunk_index,
                    team_id = excluded.team_id,
                    content_hash = excluded.content_hash,
                    updated_at = excluded.updated_at,
                    indexed_at = excluded.indexed_at,
                    indexed_by = excluded.indexed_by,
                    index_version = excluded.index_version,
                    original_created_at = excluded.original_created_at,
                    original_updated_at = excluded.original_updated_at,
                    quality_score = excluded.quality_score,
                    quality_components = excluded.quality_components
                """,
                rows,
            )
        return len(rows)

    def get(self, doc_id: str) -> Optional[Dict[str, Any]]:
        with self._conn() as c:
            row = c.execute(
                "SELECT * FROM documents WHERE id = ?", (doc_id,)
            ).fetchone()
        if row is None:
            return None
        return self._row_to_dict(row)

    def get_vector(self, doc_id: str) -> Optional[List[float]]:
        with self._conn() as c:
            row = c.execute(
                "SELECT embedding FROM documents WHERE id = ?", (doc_id,)
            ).fetchone()
        if row is None:
            return None
        return _unpack_floats(row["embedding"])

    def delete(self, doc_id: str) -> None:
        with self._lock, self._conn() as c:
            c.execute("DELETE FROM documents WHERE id = ?", (doc_id,))

    def delete_by_source(self, source: str) -> int:
        with self._lock, self._conn() as c:
            cur = c.execute("DELETE FROM documents WHERE source = ?", (source,))
            return cur.rowcount

    def delete_by_source_and_id(self, source: str, source_id: str) -> int:
        with self._lock, self._conn() as c:
            cur = c.execute(
                "DELETE FROM documents WHERE source = ? AND source_id = ?",
                (source, source_id),
            )
            return cur.rowcount

    def count(self) -> int:
        with self._conn() as c:
            return int(c.execute("SELECT COUNT(*) AS n FROM documents").fetchone()["n"])

    def count_by_source(self, source: str) -> int:
        with self._conn() as c:
            return int(
                c.execute(
                    "SELECT COUNT(*) AS n FROM documents WHERE source = ?", (source,)
                ).fetchone()["n"]
            )

    def list_sources(self) -> List[str]:
        with self._conn() as c:
            rows = c.execute(
                "SELECT source, COUNT(*) AS n FROM documents GROUP BY source ORDER BY source"
            ).fetchall()
        return [r["source"] for r in rows]

    def get_stats(self) -> Dict[str, Any]:
        with self._conn() as c:
            total = int(c.execute("SELECT COUNT(*) AS n FROM documents").fetchone()["n"])
            sources = c.execute(
                "SELECT source, COUNT(*) AS n FROM documents GROUP BY source ORDER BY source"
            ).fetchall()
            dim_row = c.execute(
                "SELECT embedding FROM documents LIMIT 1"
            ).fetchone()
        dimension = len(_unpack_floats(dim_row["embedding"])) if dim_row else 0
        return {
            "total_vectors": total,
            "sources": {r["source"]: r["n"] for r in sources},
            "dimension": dimension,
            "db_path": str(self.db_path),
        }

    # ---- vector search ----

    def search(
        self,
        query_embedding: List[float],
        k: int = 5,
        sources: Optional[List[str]] = None,
        team_id: Optional[str] = None,
        min_score: float = 0.0,
    ) -> List[Tuple[str, float]]:
        """Return [(doc_id, similarity)] for the top-k closest documents.

        Optional filters:
            sources: restrict to a set of source names (e.g. ['inventory','faq']).
            team_id: restrict to documents scoped to a team (NULL team_id
                     is treated as global).
            min_score: drop documents below this cosine similarity.
        """
        if k <= 0 or not query_embedding:
            return []

        sql = (
            "SELECT id, embedding FROM documents"
        )
        params: List[Any] = []
        clauses: List[str] = []
        if sources:
            placeholders = ",".join("?" for _ in sources)
            clauses.append(f"source IN ({placeholders})")
            params.extend(sources)
        if team_id:
            # team-scoped OR global (team_id IS NULL)
            clauses.append("(team_id = ? OR team_id IS NULL)")
            params.append(team_id)
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)

        with self._conn() as c:
            rows = c.execute(sql, params).fetchall()

        scored: List[Tuple[str, float]] = []
        for row in rows:
            vec = _unpack_floats(row["embedding"])
            sim = _cosine(query_embedding, vec)
            # Clamp to a strict [0, 1] range — the Pydantic schema on
            # RetrievedDocument enforces ge=0, le=1 and FP rounding can push
            # cosine to 1.0000000000000013.
            sim = max(0.0, min(1.0, sim))
            if sim >= min_score:
                scored.append((row["id"], sim))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]

    def list_documents(
        self,
        source: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> List[Dict[str, Any]]:
        sql = "SELECT * FROM documents"
        params: List[Any] = []
        if source:
            sql += " WHERE source = ?"
            params.append(source)
        sql += " ORDER BY updated_at DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        with self._conn() as c:
            rows = c.execute(sql, params).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def _row_to_dict(self, row: sqlite3.Row) -> Dict[str, Any]:
        quality_components_raw = row["quality_components"] if "quality_components" in row.keys() else None
        try:
            quality_components = (
                json.loads(quality_components_raw) if quality_components_raw else None
            )
        except (ValueError, TypeError):
            quality_components = None

        def _col(name: str) -> Any:
            try:
                return row[name]
            except (IndexError, KeyError):
                return None

        return {
            "id": row["id"],
            "source": row["source"],
            "source_id": row["source_id"],
            "content": row["content"],
            "metadata": json.loads(row["metadata"]) if row["metadata"] else {},
            "embedding": _unpack_floats(row["embedding"]),
            "chunk_index": row["chunk_index"],
            "team_id": row["team_id"],
            "content_hash": row["content_hash"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
            "indexed_at": _col("indexed_at"),
            "indexed_by": _col("indexed_by"),
            "index_version": _col("index_version") or 1,
            "original_created_at": _col("original_created_at"),
            "original_updated_at": _col("original_updated_at"),
            "quality_score": _col("quality_score"),
            "quality_components": quality_components,
        }

    def provenance(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Return a structured DocumentProvenance dict for a document."""
        with self._conn() as c:
            row = c.execute(
                """
                SELECT id, source, source_id, indexed_at, indexed_by, index_version,
                       original_created_at, original_updated_at, updated_at
                FROM documents WHERE id = ?
                """,
                (doc_id,),
            ).fetchone()
        if row is None:
            return None
        try:
            index_version = row["index_version"] or 1
        except (IndexError, KeyError):
            index_version = 1
        return {
            "document_id": row["id"],
            "source": row["source"],
            "source_id": row["source_id"],
            "indexed_at": row["indexed_at"] or row["updated_at"],
            "indexed_by": row["indexed_by"] or "system",
            "index_version": int(index_version),
            "original_created_at": row["original_created_at"] or row["updated_at"],
            "original_updated_at": row["original_updated_at"] or row["updated_at"],
        }

    def update_quality(
        self,
        doc_id: str,
        quality_score: float,
        quality_components: Dict[str, float],
    ) -> None:
        """Persist a quality score + component breakdown for a document."""
        if not 0.0 <= quality_score <= 1.0:
            raise ValueError("quality_score must be between 0 and 1")
        for k, v in quality_components.items():
            if not 0.0 <= v <= 1.0:
                raise ValueError(f"quality component {k!r} must be between 0 and 1")
        components_json = json.dumps(quality_components, ensure_ascii=False)
        with self._lock, self._conn() as c:
            c.execute(
                """
                UPDATE documents
                   SET quality_score = ?,
                       quality_components = ?,
                       updated_at = ?
                 WHERE id = ?
                """,
                (quality_score, components_json, _utcnow_iso(), doc_id),
            )

    def average_quality(self) -> Dict[str, Any]:
        """Aggregate quality stats across the corpus (used by /api/rag/stats)."""
        with self._conn() as c:
            row = c.execute(
                """
                SELECT AVG(quality_score) AS avg_score,
                       COUNT(*)            AS scored
                FROM documents
                WHERE quality_score IS NOT NULL
                """
            ).fetchone()
        scored = int(row["scored"] or 0) if row else 0
        return {
            "documents_scored": scored,
            "average_quality_score": float(row["avg_score"] or 0.0) if row else 0.0,
        }

    # ---- conversations ----

    def conversation_get_messages(
        self,
        conversation_id: str,
        limit: int = 20,
    ) -> List[Dict[str, Any]]:
        with self._conn() as c:
            rows = c.execute(
                """
                SELECT role, content, metadata, timestamp
                FROM conversation_messages
                WHERE conversation_id = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (conversation_id, limit),
            ).fetchall()
        out = []
        for r in reversed(rows):
            out.append(
                {
                    "role": r["role"],
                    "content": r["content"],
                    "metadata": json.loads(r["metadata"]) if r["metadata"] else {},
                    "timestamp": r["timestamp"],
                }
            )
        return out

    def conversation_append(
        self,
        conversation_id: str,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        user_id: Optional[str] = None,
        max_messages: int = 40,
    ) -> None:
        if role not in {"user", "assistant", "system"}:
            raise ValueError(f"invalid role: {role}")
        now = _utcnow_iso()
        meta_json = json.dumps(metadata or {}, ensure_ascii=False, default=str)
        with self._lock, self._conn() as c:
            c.execute(
                """
                INSERT INTO conversations(conversation_id, user_id, last_seen_at)
                VALUES(?, ?, ?)
                ON CONFLICT(conversation_id) DO UPDATE
                SET last_seen_at = excluded.last_seen_at,
                    user_id      = COALESCE(conversations.user_id, excluded.user_id)
                """,
                (conversation_id, user_id, now),
            )
            c.execute(
                """
                INSERT INTO conversation_messages(
                    conversation_id, role, content, metadata, timestamp
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (conversation_id, role, content, meta_json, now),
            )
            # Trim oldest messages to bound storage.
            c.execute(
                """
                DELETE FROM conversation_messages
                WHERE conversation_id = ?
                  AND id NOT IN (
                    SELECT id FROM conversation_messages
                    WHERE conversation_id = ?
                    ORDER BY id DESC
                    LIMIT ?
                  )
                """,
                (conversation_id, conversation_id, max_messages),
            )

    def conversation_clear(self, conversation_id: str) -> None:
        with self._lock, self._conn() as c:
            c.execute(
                "DELETE FROM conversation_messages WHERE conversation_id = ?",
                (conversation_id,),
            )
            c.execute(
                "DELETE FROM conversations WHERE conversation_id = ?",
                (conversation_id,),
            )

    # ---- indexing jobs ----

    def job_create(
        self,
        source: str,
        requested_by: Optional[str] = None,
        team_id: Optional[str] = None,
    ) -> str:
        job_id = str(uuid.uuid4())
        now = _utcnow_iso()
        with self._lock, self._conn() as c:
            c.execute(
                """
                INSERT INTO indexing_jobs(
                    job_id, source, status, documents_processed, documents_total,
                    started_at, requested_by, team_id
                ) VALUES (?, ?, 'pending', 0, 0, ?, ?, ?)
                """,
                (job_id, source, now, requested_by, team_id),
            )
        return job_id

    def job_update(
        self,
        job_id: str,
        *,
        status: Optional[str] = None,
        documents_processed: Optional[int] = None,
        documents_total: Optional[int] = None,
        error: Optional[str] = None,
        completed: bool = False,
    ) -> None:
        fields: List[str] = []
        params: List[Any] = []
        if status is not None:
            fields.append("status = ?")
            params.append(status)
        if documents_processed is not None:
            fields.append("documents_processed = ?")
            params.append(int(documents_processed))
        if documents_total is not None:
            fields.append("documents_total = ?")
            params.append(int(documents_total))
        if error is not None:
            fields.append("error = ?")
            params.append(error)
        if completed:
            fields.append("completed_at = ?")
            params.append(_utcnow_iso())
        if not fields:
            return
        params.append(job_id)
        with self._lock, self._conn() as c:
            c.execute(f"UPDATE indexing_jobs SET {', '.join(fields)} WHERE job_id = ?", params)

    def job_get(self, job_id: str) -> Optional[Dict[str, Any]]:
        with self._conn() as c:
            row = c.execute("SELECT * FROM indexing_jobs WHERE job_id = ?", (job_id,)).fetchone()
        if row is None:
            return None
        return dict(row)

    def job_list(
        self,
        source: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 50,
    ) -> List[Dict[str, Any]]:
        sql = "SELECT * FROM indexing_jobs WHERE 1=1"
        params: List[Any] = []
        if source:
            sql += " AND source = ?"
            params.append(source)
        if status:
            sql += " AND status = ?"
            params.append(status)
        sql += " ORDER BY COALESCE(started_at, '') DESC LIMIT ?"
        params.append(limit)
        with self._conn() as c:
            rows = c.execute(sql, params).fetchall()
        return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Singleton + backwards-compat shim
# ---------------------------------------------------------------------------

_store: Optional[SQLiteVectorStore] = None
_store_lock = threading.Lock()


def get_vector_store() -> SQLiteVectorStore:
    global _store
    if _store is None:
        with _store_lock:
            if _store is None:
                import os
                from app.config import settings
                path = os.getenv("VECTOR_STORE_PATH") or str(
                    Path(settings.storage_dir) / "vector_store.sqlite3"
                )
                _store = SQLiteVectorStore(path)
    return _store


# ---------------------------------------------------------------------------
# Legacy facade — keeps the previous VectorStore API working for any
# caller that imported it (e.g. existing tests / admin tools).
# ---------------------------------------------------------------------------

class VectorStoreLegacyAdapter:
    """Adapter exposing the old VectorStore API on top of the SQLite store."""

    def __init__(self, store: SQLiteVectorStore):
        self._store = store

    def add(self, doc_id, embedding, metadata):
        self._store.upsert_document(
            doc_id=doc_id,
            source=metadata.get("source", "unknown"),
            source_id=metadata.get("source_id", ""),
            content=metadata.get("content", ""),
            embedding=embedding,
            metadata=metadata.get("metadata") or {},
            team_id=metadata.get("team_id"),
            chunk_index=metadata.get("chunk_index", 0),
        )

    def search(self, query_embedding, k=5, filter_source=None):
        return self._store.search(
            query_embedding=query_embedding,
            k=k,
            sources=[filter_source] if filter_source else None,
        )

    def get(self, doc_id):
        d = self._store.get(doc_id)
        if d is None:
            return None
        # Old format: metadata was the outer dict that included content etc.
        return {
            "content": d["content"],
            "metadata": d["metadata"],
            "source": d["source"],
            "source_id": d["source_id"],
            "chunk_index": d["chunk_index"],
            "indexed_at": d["updated_at"],
        }

    def get_vector(self, doc_id):
        return self._store.get_vector(doc_id)

    def delete(self, doc_id):
        self._store.delete(doc_id)

    def delete_by_source(self, source):
        return self._store.delete_by_source(source)

    def count(self):
        return self._store.count()

    def count_by_source(self, source):
        return self._store.count_by_source(source)

    def list_sources(self):
        return self._store.list_sources()

    def get_stats(self):
        return self._store.get_stats()

    def clear(self):
        # Bulk delete all documents.
        import sqlite3 as _sql
        with self._store._lock, self._store._conn() as c:
            c.execute("DELETE FROM documents")


def get_legacy_vector_store() -> VectorStoreLegacyAdapter:
    return VectorStoreLegacyAdapter(get_vector_store())