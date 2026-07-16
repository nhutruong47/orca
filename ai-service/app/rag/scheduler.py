"""
Background re-index scheduler.

The RAG knowledge base needs to be kept fresh as the underlying data
(inventory, orders, etc.) changes. Rather than relying on the Java side to
push every mutation immediately, we run a periodic scheduler inside the AI
service that:

* Re-indexes all bundled sources (policies, faq, manual) on a slow tick.
* Re-indexes ingest sources (inventory, orders, products, teams, users)
  on a faster tick when their last indexed_at exceeds the freshness budget.
* Exposes a manual trigger via the API.

The scheduler is opt-in: set `ORCA_AUTO_INDEX_ON_BOOT=1` to start it when
the FastAPI app starts; the API surface (`/api/rag/scheduler/*`) is always
available to control the loop at runtime.
"""

from __future__ import annotations

import asyncio
import logging
import os
import threading
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


# Defaults — overridable via env or the public `configure` method.
DEFAULT_BUNDLED_INTERVAL_S = int(os.getenv("ORCA_INDEX_BUNDLED_INTERVAL_S", "3600"))      # 1h
DEFAULT_INGEST_INTERVAL_S = int(os.getenv("ORCA_INDEX_INGEST_INTERVAL_S", "900"))        # 15m
DEFAULT_FRESHNESS_BUDGET_S = int(os.getenv("ORCA_INDEX_FRESHNESS_BUDGET_S", "86400"))     # 24h
DEFAULT_BATCH_SIZE = int(os.getenv("ORCA_INDEX_BATCH_SIZE", "200"))


@dataclass
class SchedulerConfig:
    bundled_interval_s: int = DEFAULT_BUNDLED_INTERVAL_S
    ingest_interval_s: int = DEFAULT_INGEST_INTERVAL_S
    freshness_budget_s: int = DEFAULT_FRESHNESS_BUDGET_S
    batch_size: int = DEFAULT_BATCH_SIZE
    enabled: bool = False


@dataclass
class SchedulerStatus:
    running: bool = False
    last_bundled_at: Optional[float] = None
    last_ingest_at: Optional[float] = None
    last_bundled_duration_s: Optional[float] = None
    last_ingest_duration_s: Optional[float] = None
    last_error: Optional[str] = None
    next_bundled_at: Optional[float] = None
    next_ingest_at: Optional[float] = None
    history: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "running": self.running,
            "last_bundled_at": self.last_bundled_at,
            "last_ingest_at": self.last_ingest_at,
            "last_bundled_duration_s": self.last_bundled_duration_s,
            "last_ingest_duration_s": self.last_ingest_duration_s,
            "last_error": self.last_error,
            "next_bundled_at": self.next_bundled_at,
            "next_ingest_at": self.next_ingest_at,
            "history": list(self.history[-20:]),
        }


class BackgroundScheduler:
    """A tiny, dependency-free async scheduler.

    We deliberately avoid APScheduler / Celery beat to keep the AI service
    self-contained. The scheduler is single-process, safe to start/stop from
    the FastAPI lifecycle, and is no-op when no work is pending.
    """

    def __init__(self, config: Optional[SchedulerConfig] = None) -> None:
        self.config = config or SchedulerConfig()
        self.status = SchedulerStatus()
        self._task: Optional[asyncio.Task] = None
        self._stop_event: Optional[asyncio.Event] = None
        self._lock = threading.Lock()

    # ---- lifecycle ----

    async def start(self) -> None:
        with self._lock:
            if self._task is not None and not self._task.done():
                logger.info("Background scheduler already running")
                return
            self._stop_event = asyncio.Event()
            self.status.running = True
            self._task = asyncio.create_task(self._loop(), name="orca-indexer-scheduler")
            logger.info(
                "Background scheduler started: bundled=%ss ingest=%ss",
                self.config.bundled_interval_s,
                self.config.ingest_interval_s,
            )

    async def stop(self) -> None:
        with self._lock:
            if self._stop_event is not None:
                self._stop_event.set()
            task = self._task
            self._task = None
            self.status.running = False
        if task is not None:
            try:
                await asyncio.wait_for(task, timeout=5.0)
            except (asyncio.TimeoutError, asyncio.CancelledError):
                task.cancel()
            logger.info("Background scheduler stopped")

    def configure(self, **kwargs: Any) -> None:
        for k, v in kwargs.items():
            if not hasattr(self.config, k):
                raise ValueError(f"unknown scheduler config: {k}")
            setattr(self.config, k, v)

    # ---- public api ----

    def get_status(self) -> Dict[str, Any]:
        return self.status.to_dict()

    async def trigger_bundled(self) -> Dict[str, Any]:
        return await self._run_bundled()

    async def trigger_ingest(self) -> Dict[str, Any]:
        return await self._run_ingest()

    # ---- internals ----

    async def _loop(self) -> None:
        assert self._stop_event is not None
        stop_event = self._stop_event
        next_bundled = time.monotonic() + self.config.bundled_interval_s
        next_ingest = time.monotonic() + self.config.ingest_interval_s
        self.status.next_bundled_at = time.time() + self.config.bundled_interval_s
        self.status.next_ingest_at = time.time() + self.config.ingest_interval_s

        while not stop_event.is_set():
            now = time.monotonic()
            try:
                if now >= next_bundled:
                    await self._run_bundled()
                    next_bundled = time.monotonic() + self.config.bundled_interval_s
                    self.status.next_bundled_at = time.time() + self.config.bundled_interval_s
                if now >= next_ingest:
                    await self._run_ingest()
                    next_ingest = time.monotonic() + self.config.ingest_interval_s
                    self.status.next_ingest_at = time.time() + self.config.ingest_interval_s
            except Exception as exc:  # pragma: no cover - defensive
                logger.exception("Scheduler tick failed")
                self.status.last_error = str(exc)
                self._record_history("error", {"error": str(exc)})

            # Sleep in small slices so stop() can cancel quickly.
            try:
                await asyncio.wait_for(stop_event.wait(), timeout=1.0)
            except asyncio.TimeoutError:
                continue

    async def _run_bundled(self) -> Dict[str, Any]:
        started = time.monotonic()
        try:
            from app.rag.indexers import get_indexer_manager

            manager = get_indexer_manager()
            job_ids = await asyncio.to_thread(manager.run_bundled, replace=False)
            duration = time.monotonic() - started
            self.status.last_bundled_at = time.time()
            self.status.last_bundled_duration_s = round(duration, 3)
            self._record_history("bundled", {"jobs": job_ids, "duration_s": duration})
            return {"status": "ok", "jobs": job_ids, "duration_s": duration}
        except Exception as exc:
            logger.exception("bundled reindex failed")
            self.status.last_error = str(exc)
            self._record_history("bundled_error", {"error": str(exc)})
            return {"status": "error", "error": str(exc)}

    async def _run_ingest(self) -> Dict[str, Any]:
        started = time.monotonic()
        try:
            from app.rag.indexers import get_indexer_manager

            manager = get_indexer_manager()
            stats = await asyncio.to_thread(manager.refresh_stale_sources, self.config.freshness_budget_s)
            duration = time.monotonic() - started
            self.status.last_ingest_at = time.time()
            self.status.last_ingest_duration_s = round(duration, 3)
            self._record_history("ingest", {"stats": stats, "duration_s": duration})
            return {"status": "ok", "stats": stats, "duration_s": duration}
        except Exception as exc:
            logger.exception("ingest reindex failed")
            self.status.last_error = str(exc)
            self._record_history("ingest_error", {"error": str(exc)})
            return {"status": "error", "error": str(exc)}

    def _record_history(self, kind: str, payload: Dict[str, Any]) -> None:
        self.status.history.append(
            {
                "kind": kind,
                "ts": time.time(),
                **payload,
            }
        )
        # Bound the in-memory history.
        if len(self.status.history) > 200:
            del self.status.history[: len(self.status.history) - 200]


# Module-level singleton
_scheduler: Optional[BackgroundScheduler] = None


def get_scheduler() -> BackgroundScheduler:
    global _scheduler
    if _scheduler is None:
        _scheduler = BackgroundScheduler()
    return _scheduler


__all__ = [
    "BackgroundScheduler",
    "SchedulerConfig",
    "SchedulerStatus",
    "get_scheduler",
]
