"""
Embedding service backed by sentence-transformers.

Supports multilingual embeddings for Vietnamese content.

Production behavior: the service lazy-loads the model on first use and
NEVER silently falls back to mock embeddings. If the model fails to load
or `embed()` fails, the exception propagates so the caller can decide
how to react (e.g. surface a 502 to the user). Mock embeddings are
*only* generated when explicitly requested via :meth:`embed_mock`,
which is used by tests.
"""

from __future__ import annotations

import logging
import os
import threading
from typing import List, Optional

logger = logging.getLogger(__name__)


class EmbeddingServiceError(RuntimeError):
    """Raised when the embedding service cannot produce vectors."""


class EmbeddingService:
    """Sentence-transformers-backed text vectorization."""

    DEFAULT_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    DEFAULT_DIM = 384

    def __init__(self, model_name: Optional[str] = None):
        self._model = None
        self._model_name = model_name or os.getenv("EMBEDDING_MODEL", self.DEFAULT_MODEL)
        self._dimension: Optional[int] = None
        self._lock = threading.Lock()
        self._initialized = False
        self._init_error: Optional[Exception] = None

    @property
    def model(self):
        if self._model is None:
            self._load_model()
        return self._model

    @property
    def dimension(self) -> int:
        if self._dimension is None:
            self._load_model()
        return self._dimension or self.DEFAULT_DIM

    @property
    def is_initialized(self) -> bool:
        return self._initialized and self._model is not None

    def _load_model(self) -> None:
        with self._lock:
            if self._model is not None:
                return
            try:
                from sentence_transformers import SentenceTransformer
                logger.info("Loading embedding model: %s", self._model_name)
                self._model = SentenceTransformer(self._model_name)
                self._dimension = self._model.get_sentence_embedding_dimension()
                self._initialized = True
                logger.info("Embedding model loaded. Dimension: %s", self._dimension)
            except Exception as exc:
                self._init_error = exc
                logger.error("Failed to load embedding model %s: %s", self._model_name, exc)
                raise EmbeddingServiceError(
                    f"Could not load embedding model '{self._model_name}': {exc}"
                ) from exc

    def embed(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings. Raises EmbeddingServiceError on failure."""
        if not texts:
            return []
        if self._model is None:
            # Triggers lazy load (which may raise EmbeddingServiceError).
            self.model
        try:
            import numpy as np
            vectors = self._model.encode(texts, convert_to_numpy=True)
            if isinstance(vectors, np.ndarray):
                return vectors.astype(float).tolist()
            return [list(map(float, v)) for v in vectors]
        except EmbeddingServiceError:
            raise
        except Exception as exc:
            logger.exception("Embedding generation failed")
            raise EmbeddingServiceError(f"Embedding generation failed: {exc}") from exc

    def embed_query(self, query: str) -> List[float]:
        """Embed a single query string."""
        return self.embed([query])[0]

    @staticmethod
    def embed_mock(texts: List[str], dimension: int = 384) -> List[List[float]]:
        """Deterministic mock embeddings for tests. Not used in production."""
        import hashlib
        import numpy as np
        out = []
        for t in texts:
            seed = int(hashlib.md5(t.encode("utf-8")).hexdigest()[:8], 16) % (2 ** 31 - 1)
            rng = np.random.default_rng(seed)
            vec = rng.standard_normal(dimension).astype(float)
            norm = float((vec ** 2).sum() ** 0.5) or 1.0
            vec = vec / norm
            out.append(vec.tolist())
        return out


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_embedding_service: Optional[EmbeddingService] = None
_embedding_lock = threading.Lock()


def get_embedding_service() -> EmbeddingService:
    global _embedding_service
    if _embedding_service is None:
        with _embedding_lock:
            if _embedding_service is None:
                _embedding_service = EmbeddingService()
    return _embedding_service


__all__ = ["EmbeddingService", "EmbeddingServiceError", "get_embedding_service"]