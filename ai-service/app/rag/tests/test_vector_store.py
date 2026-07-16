"""Integration-style smoke tests for the SQLite vector store.

These exercise the real schema and the new provenance / quality columns
without requiring a separate test database. Each test uses a tmp path so
they are fully isolated.
"""
import os
import tempfile

import pytest


@pytest.fixture
def tmp_store(monkeypatch):
    """Create a fresh SQLiteVectorStore for each test."""
    from app.rag.sqlite_vector_store import SQLiteVectorStore

    fd, path = tempfile.mkstemp(suffix=".sqlite")
    os.close(fd)
    try:
        store = SQLiteVectorStore(path)
        yield store
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


def _vec(seed: int):
    """Return a deterministic 4-dim unit-ish vector."""
    import math

    raw = [math.sin(seed + i * 0.31) for i in range(4)]
    norm = math.sqrt(sum(x * x for x in raw)) or 1.0
    return [x / norm for x in raw]


def test_schema_includes_provenance_columns(tmp_store):
    import sqlite3

    con = sqlite3.connect(str(tmp_store.db_path))
    rows = con.execute("PRAGMA table_info(documents)").fetchall()
    cols = {r[1] for r in rows}
    con.close()
    expected = {
        "indexed_at",
        "indexed_by",
        "index_version",
        "original_created_at",
        "original_updated_at",
        "quality_score",
        "quality_components",
    }
    missing = expected - cols
    assert not missing, f"Missing provenance columns: {missing}"


def test_upsert_round_trips_quality_and_provenance(tmp_store):
    tmp_store.upsert_document(
        doc_id="inventory:abc#0:deadbeef",
        source="inventory",
        source_id="abc",
        content="Hạt cà phê Robusta 1kg tại kho HCM",
        embedding=_vec(1),
        metadata={"title": "Cà phê Robusta", "category": "inventory"},
        team_id="team-1",
        indexed_by="smoke-test",
        index_version=1,
        original_updated_at="2026-01-15T00:00:00Z",
        quality_score=0.83,
        quality_components={
            "completeness": 0.9,
            "accuracy": 0.85,
            "freshness": 0.7,
            "relevance": 0.85,
        },
    )
    row = tmp_store.get("inventory:abc#0:deadbeef")
    assert row is not None
    assert row["indexed_by"] == "smoke-test"
    assert row["index_version"] == 1
    assert row["quality_score"] == pytest.approx(0.83)
    assert row["quality_components"]["freshness"] == pytest.approx(0.7)


def test_provenance_helper(tmp_store):
    tmp_store.upsert_document(
        doc_id="faq:q1#0:cafef00d",
        source="faq",
        source_id="q1",
        content="Câu hỏi thường gặp",
        embedding=_vec(2),
        indexed_by="ingest",
    )
    prov = tmp_store.provenance("faq:q1#0:cafef00d")
    assert prov is not None
    assert prov["source"] == "faq"
    assert prov["indexed_by"] == "ingest"
    assert prov["index_version"] >= 1


def test_update_quality_persists(tmp_store):
    tmp_store.upsert_document(
        doc_id="manual:m1#0:1234",
        source="manual",
        source_id="m1",
        content="Hướng dẫn rang cà phê",
        embedding=_vec(3),
    )
    tmp_store.update_quality(
        "manual:m1#0:1234",
        quality_score=0.91,
        quality_components={
            "completeness": 0.95,
            "accuracy": 0.9,
            "freshness": 0.85,
            "relevance": 0.95,
        },
    )
    row = tmp_store.get("manual:m1#0:1234")
    assert row["quality_score"] == pytest.approx(0.91)
    assert row["quality_components"]["completeness"] == pytest.approx(0.95)


def test_average_quality_aggregates(tmp_store):
    tmp_store.upsert_document(
        doc_id="p:p1#0:aaaa",
        source="policies",
        source_id="p1",
        content="Chính sách nghỉ phép",
        embedding=_vec(4),
        quality_score=0.9,
        quality_components={"completeness": 1.0, "accuracy": 0.9, "freshness": 0.8, "relevance": 0.9},
    )
    tmp_store.upsert_document(
        doc_id="p:p2#0:bbbb",
        source="policies",
        source_id="p2",
        content="Chính sách lương",
        embedding=_vec(5),
        quality_score=0.7,
        quality_components={"completeness": 0.7, "accuracy": 0.7, "freshness": 0.7, "relevance": 0.7},
    )
    stats = tmp_store.average_quality()
    assert stats["documents_scored"] == 2
    assert 0.7 <= stats["average_quality_score"] <= 0.9
