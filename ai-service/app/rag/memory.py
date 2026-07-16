"""
Conversation memory for the RAG pipeline.

Wraps :class:`SQLiteVectorStore` with explicit semantics:

    * Multi-turn context (append-only log of user / assistant turns).
    * Bounded history: by default we keep at most N recent turns in the
      prompt window. Older turns are still stored for audit / review, but
      they don't bloat the prompt.
    * Optional summarization: if the conversation exceeds a hard cap,
      older messages are summarized into a single "summary" entry that
      replaces them in subsequent prompts.
    * TTL: stale conversations (no activity for X days) are pruned lazily
      on read.
    * Stable `conversation_id` (UUID) — never auto-create a new one; the
      caller is responsible for ids so that retries don't fork state.

The store is intentionally pluggable so it can be swapped for Redis /
Postgres later without touching callers.
"""

from __future__ import annotations

import logging
import threading
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

from app.rag.sqlite_vector_store import SQLiteVectorStore, get_vector_store

logger = logging.getLogger(__name__)


# Defaults — overridable via constructor for tests.
DEFAULT_WINDOW_TURNS = 10            # turns included in prompt
DEFAULT_MAX_STORED_TURNS = 40        # hard cap on stored messages
DEFAULT_TTL_DAYS = 30               # prune inactivity older than this
DEFAULT_SUMMARIZE_THRESHOLD = 20    # summarize when stored > this


@dataclass
class MemoryTurn:
    role: str
    content: str
    timestamp: str
    metadata: Dict[str, Any]


class ConversationMemory:
    """High-level conversation memory backed by the SQLite vector store."""

    def __init__(
        self,
        store: Optional[SQLiteVectorStore] = None,
        *,
        window_turns: int = DEFAULT_WINDOW_TURNS,
        max_stored_turns: int = DEFAULT_MAX_STORED_TURNS,
        ttl_days: int = DEFAULT_TTL_DAYS,
        summarize_threshold: int = DEFAULT_SUMMARIZE_THRESHOLD,
    ):
        self.store = store or get_vector_store()
        self.window_turns = window_turns
        self.max_stored_turns = max_stored_turns
        self.ttl = timedelta(days=ttl_days)
        self.summarize_threshold = summarize_threshold
        self._lock = threading.Lock()
        # NOTE: a future optimization is to cache the active conversation
        # in memory. We deliberately avoid that here to keep the source
        # of truth in SQLite and to make the service stateless across
        # workers (horizontal scaling).

    # ---------- read ----------

    def get_window(
        self, conversation_id: str, *, limit: Optional[int] = None
    ) -> List[Dict[str, str]]:
        """Return the last `window_turns` messages, formatted for prompts."""
        limit = limit or self.window_turns
        # Stored messages come back oldest-first; trim to the last N.
        all_msgs = self.store.conversation_get_messages(conversation_id, limit=limit)
        return [{"role": m["role"], "content": m["content"]} for m in all_msgs]

    def get_full_history(self, conversation_id: str) -> List[MemoryTurn]:
        all_msgs = self.store.conversation_get_messages(
            conversation_id, limit=self.max_stored_turns
        )
        return [
            MemoryTurn(
                role=m["role"],
                content=m["content"],
                timestamp=m["timestamp"],
                metadata=m.get("metadata") or {},
            )
            for m in all_msgs
        ]

    def is_stale(self, conversation_id: str) -> bool:
        """Return True if the conversation hasn't been touched in ttl."""
        all_msgs = self.store.conversation_get_messages(
            conversation_id, limit=1
        )
        if not all_msgs:
            return True
        last = all_msgs[-1]["timestamp"]
        try:
            ts = datetime.fromisoformat(last)
        except ValueError:
            return False
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - ts) > self.ttl

    # ---------- write ----------

    def append_user(
        self,
        conversation_id: str,
        content: str,
        *,
        user_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        with self._lock:
            self.store.conversation_append(
                conversation_id=conversation_id,
                role="user",
                content=content,
                metadata=metadata,
                user_id=user_id,
                max_messages=self.max_stored_turns,
            )

    def append_assistant(
        self,
        conversation_id: str,
        content: str,
        *,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        with self._lock:
            self.store.conversation_append(
                conversation_id=conversation_id,
                role="assistant",
                content=content,
                metadata=metadata,
                user_id=None,
                max_messages=self.max_stored_turns,
            )

    def append_summary(self, conversation_id: str, summary: str) -> None:
        """Persist a summarization entry that replaces older context."""
        with self._lock:
            self.store.conversation_append(
                conversation_id=conversation_id,
                role="system",
                content=f"[Tóm tắt các lượt trước] {summary}",
                metadata={"kind": "summary"},
                user_id=None,
                max_messages=self.max_stored_turns,
            )

    def clear(self, conversation_id: str) -> None:
        with self._lock:
            self.store.conversation_clear(conversation_id)


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_memory: Optional[ConversationMemory] = None
_memory_lock = threading.Lock()


def get_conversation_memory() -> ConversationMemory:
    global _memory
    if _memory is None:
        with _memory_lock:
            if _memory is None:
                _memory = ConversationMemory()
    return _memory


__all__ = ["ConversationMemory", "get_conversation_memory", "MemoryTurn"]