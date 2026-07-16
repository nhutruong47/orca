"""
Vector store module.

This module used to ship a file-backed JSON vector store that became a
production blocker (no transactions, no filtering, no dedup, race
conditions). It has been replaced by a SQLite-backed implementation in
:mod:`app.rag.sqlite_vector_store`. The module-level helpers keep the
historical singleton signature so that existing imports work unchanged.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.rag.sqlite_vector_store import (
    SQLiteVectorStore,
    get_vector_store,
    get_legacy_vector_store,
)

# Re-export under the historical class name so any legacy callers still
# receive a VectorStore-like facade.
VectorStore = SQLiteVectorStore  # type: ignore[misc, assignment]


__all__ = ["VectorStore", "get_vector_store"]


def search(
    query_embedding: List[float],
    k: int = 5,
    sources: Optional[List[str]] = None,
    team_id: Optional[str] = None,
    min_score: float = 0.0,
) -> List[Any]:
    """Convenience wrapper used by the RAG pipeline."""
    return get_vector_store().search(
        query_embedding=query_embedding,
        k=k,
        sources=sources,
        team_id=team_id,
        min_score=min_score,
    )


def stats() -> Dict[str, Any]:
    return get_vector_store().get_stats()