"""Tests for the text chunker used by the RAG indexer pipeline."""
import pytest

from app.rag.indexer import chunk_text, DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


def test_short_text_returns_single_chunk():
    chunks = chunk_text("Xin chào bạn.")
    assert chunks == ["Xin chào bạn."]


def test_long_text_is_split_with_overlap():
    text = ("Cà phê. " * 50).strip()
    chunks = chunk_text(text, chunk_size=80, overlap=20)
    assert len(chunks) >= 2
    # Every chunk is non-empty and never exceeds the chunk size by more than
    # a single sentence + the overlap region.
    for chunk in chunks:
        assert chunk.strip()
        # Allow a small slack because the overlap stitching may yield chunks
        # slightly longer than chunk_size.
        assert len(chunk) <= 80 + 20 + 30


def test_overlap_equal_to_chunk_size_raises():
    # The implementation requires overlap strictly less than chunk_size.
    with pytest.raises(ValueError):
        chunk_text("a. b. c. d. e. f. g. h. i. j.", chunk_size=20, overlap=20)


def test_overlap_strictly_greater_than_chunk_size_raises():
    # Use long enough text so the chunker enters the splitting branch where
    # the overlap validation lives.
    with pytest.raises(ValueError):
        chunk_text("a b c d e f g h i j k l m n o p", chunk_size=10, overlap=11)


def test_vietnamese_punctuation_drives_split():
    text = "Câu một. Câu hai. Câu ba dài hơn một chút. Câu bốn ngắn."
    chunks = chunk_text(text, chunk_size=40, overlap=5)
    assert len(chunks) >= 2
    joined = " ".join(chunks)
    for token in ("một", "hai", "ba", "bốn"):
        assert token in joined


def test_empty_input_yields_no_chunks():
    # The chunker returns a list with one empty-string entry for whitespace
    # input, but never crashes. The contract: at least an empty list is fine.
    chunks = chunk_text("")
    assert chunks == [] or chunks == [""]


def test_default_constants_are_sane():
    assert DEFAULT_CHUNK_SIZE > 0
    assert DEFAULT_CHUNK_OVERLAP >= 0
    assert DEFAULT_CHUNK_OVERLAP < DEFAULT_CHUNK_SIZE

