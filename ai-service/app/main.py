"""
ORCA AI Service — main FastAPI app.

Production endpoints:

    GET  /health
    POST /extract                 (legacy: extract intent/fields)
    POST /plan                    (legacy: build task plan)
    POST /revise                  (legacy: revise task plan)

    POST /api/rag/query           (RAG over the ORCA knowledge base)
    GET  /api/rag/stats
    GET  /api/rag/sources
    GET  /api/rag/jobs
    GET  /api/rag/jobs/{job_id}
    POST /api/rag/index/{source}  (reindex a bundled source)
    POST /api/rag/index/all       (reindex every bundled source)
    POST /api/rag/ingest/{source} (push records from the Java backend)

    POST /api/rag/conversations/{id}/messages   (append a turn)
    GET  /api/rag/conversations/{id}/messages   (read history)
    DELETE /api/rag/conversations/{id}          (clear history)

    POST /api/ai/assistant/query  (thin wrapper for the frontend)
"""

from __future__ import annotations

import logging
import os
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.config import settings
from app.gemini_ai import (
    GeminiExtractError,
    GeminiPlanError,
    GeminiPlanInputError,
    GeminiReviseError,
    extract as gemini_extract,
    plan as gemini_plan,
    revise as gemini_revise,
)
from app.mock_ai import extract as mock_extract, plan as mock_plan, revise as mock_revise
from app.models import ExtractRequest, ExtractResponse, PlanDraftResponse, PlanRequest, ReviseRequest

# RAG imports
from app.rag.models import RAGRequest, StandardizedAIResponse
from app.rag.rag_service import get_rag_service
from app.rag.indexers import get_indexer_manager
from app.rag.memory import get_conversation_memory
from app.rag.scheduler import get_scheduler

logger = logging.getLogger("orca_ai")
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s :: %(message)s",
)


# ---------------------------------------------------------------------------
# CORS
# ---------------------------------------------------------------------------

def _allowed_origins() -> List[str]:
    raw = settings.cors_allowed_origins.strip()
    if not raw:
        return [
            "http://localhost:5173",
            "http://localhost:3000",
            "http://127.0.0.1:5173",
            "http://127.0.0.1:3000",
        ]
    return [origin.strip() for origin in raw.split(",") if origin.strip()]


app = FastAPI(title="ORCA AI Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins(),
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------

@app.get("/health")
def health() -> Dict[str, str]:
    model = settings.vertex_model if settings.ai_provider in {"vertex", "vertex_ai"} else settings.gemini_model
    try:
        from app.rag.sqlite_vector_store import get_vector_store
        stats = get_vector_store().get_stats()
        documents_indexed = str(stats.get("total_vectors", 0))
    except Exception:
        documents_indexed = "unknown"
    return {
        "status": "ok",
        "mode": settings.ai_v2_mode,
        "provider": settings.ai_provider,
        "model": model,
        "documents_indexed": documents_indexed,
    }


# ---------------------------------------------------------------------------
# Legacy AI surface (extract / plan / revise)
# ---------------------------------------------------------------------------

@app.post("/extract", response_model=ExtractResponse)
def extract(request: ExtractRequest) -> ExtractResponse:
    if settings.ai_v2_mode == "mock":
        return mock_extract(request)
    if settings.ai_v2_mode == "gemini":
        try:
            return gemini_extract(request)
        except GeminiExtractError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
    raise HTTPException(status_code=400, detail=f"Unsupported AI_V2_MODE: {settings.ai_v2_mode}")


@app.post("/plan", response_model=PlanDraftResponse)
def plan(request: PlanRequest) -> PlanDraftResponse:
    if request.intent == "UNKNOWN":
        raise HTTPException(status_code=400, detail="Cannot create a plan for UNKNOWN intent.")
    if settings.ai_v2_mode == "mock":
        try:
            return mock_plan(request)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
    if settings.ai_v2_mode == "gemini":
        try:
            return gemini_plan(request)
        except GeminiPlanInputError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except GeminiPlanError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
    raise HTTPException(status_code=400, detail=f"Unsupported AI_V2_MODE: {settings.ai_v2_mode}")


@app.post("/revise", response_model=PlanDraftResponse)
def revise(request: ReviseRequest) -> PlanDraftResponse:
    if settings.ai_v2_mode == "mock":
        return mock_revise(request)
    if settings.ai_v2_mode == "gemini":
        try:
            return gemini_revise(request)
        except GeminiReviseError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
    raise HTTPException(status_code=400, detail=f"Unsupported AI_V2_MODE: {settings.ai_v2_mode}")


# ---------------------------------------------------------------------------
# RAG
# ---------------------------------------------------------------------------

@app.post("/api/rag/query", response_model=StandardizedAIResponse)
def rag_query(request: RAGRequest) -> StandardizedAIResponse:
    """Query the RAG system with a natural-language question."""
    try:
        return get_rag_service().query(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/api/rag/stats")
def rag_stats() -> Dict[str, Any]:
    try:
        return get_rag_service().get_stats()
    except Exception as exc:
        logger.exception("rag_stats failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/rag/sources")
def rag_sources() -> Dict[str, Any]:
    try:
        stats = get_rag_service().get_stats()
        return {
            "sources": list(stats.get("sources", {}).keys()),
            "documents_by_source": stats.get("sources", {}),
            "total_documents": stats.get("documents_indexed", 0),
        }
    except Exception as exc:
        logger.exception("rag_sources failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/rag/jobs")
def rag_jobs_list(
    source: Optional[str] = Query(default=None),
    status: Optional[str] = Query(default=None),
    limit: int = Query(default=50, ge=1, le=200),
) -> Dict[str, Any]:
    from app.rag.sqlite_vector_store import get_vector_store
    jobs = get_vector_store().job_list(source=source, status=status, limit=limit)
    return {"jobs": jobs, "count": len(jobs)}


@app.get("/api/rag/jobs/{job_id}")
def rag_jobs_get(job_id: str) -> Dict[str, Any]:
    from app.rag.sqlite_vector_store import get_vector_store
    job = get_vector_store().job_get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"job not found: {job_id}")
    return job


@app.post("/api/rag/index/{source_type}")
def rag_index(source_type: str) -> Dict[str, Any]:
    """Trigger (re)indexing for a bundled source.

    Valid source_type values: policies, faq, manual, all.
    Anything else returns 400.
    """
    source_type = source_type.lower()
    if source_type not in {"policies", "faq", "manual", "all"}:
        raise HTTPException(
            status_code=400,
            detail=(
                f"unknown bundled source '{source_type}'. "
                "Use 'policies', 'faq', 'manual', or 'all'."
            ),
        )

    manager = get_indexer_manager()
    try:
        if source_type == "all":
            job_ids = manager.run_bundled(replace=True)
            return {
                "status": "indexing_started",
                "source": "all",
                "jobs": job_ids,
                "message": "Reindexing policies + faq + manuals has been queued.",
            }
        if source_type == "policies":
            ids = manager.run_bundled(replace=True)
            return {"status": "indexing_started", "source": "policies", "jobs": ids}
        if source_type == "faq":
            ids = manager.run_bundled(replace=True)
            return {"status": "indexing_started", "source": "faq", "jobs": ids}
        ids = manager.run_bundled(replace=True)
        return {"status": "indexing_started", "source": "manual", "jobs": ids}
    except Exception as exc:
        logger.exception("rag_index failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/api/rag/index/all")
def rag_index_all() -> Dict[str, Any]:
    return rag_index("all")


class IngestRecord(BaseModel):
    id: str
    title: Optional[str] = None
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class IngestRequest(BaseModel):
    records: List[IngestRecord]
    team_id: Optional[str] = None
    replace: bool = False


@app.post("/api/rag/ingest/{source_type}")
def rag_ingest(source_type: str, request: IngestRequest) -> Dict[str, Any]:
    """Push records from the Java backend into the RAG store.

    Valid source_type values: inventory, orders, products, teams, users.
    """
    source_type = source_type.lower()
    if source_type not in {"inventory", "orders", "products", "teams", "users"}:
        raise HTTPException(
            status_code=400,
            detail=(
                f"unknown ingest source '{source_type}'. "
                "Use 'inventory', 'orders', 'products', 'teams', or 'users'."
            ),
        )

    manager = get_indexer_manager()
    try:
        payload = [r.model_dump() for r in request.records]
        job_id = manager.ingest_records(
            source=source_type,
            records=payload,
            team_id=request.team_id,
            replace=request.replace,
        )
        return {
            "status": "ingestion_started",
            "source": source_type,
            "job_id": job_id,
            "record_count": len(payload),
        }
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("rag_ingest failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


# ---------------------------------------------------------------------------
# Conversations
# ---------------------------------------------------------------------------

class AppendMessageRequest(BaseModel):
    role: str
    content: str
    user_id: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


@app.post("/api/rag/conversations/{conversation_id}/messages")
def append_conversation_message(
    conversation_id: str, request: AppendMessageRequest
) -> Dict[str, Any]:
    memory = get_conversation_memory()
    try:
        if request.role == "user":
            memory.append_user(
                conversation_id=conversation_id,
                content=request.content,
                user_id=request.user_id,
                metadata=request.metadata,
            )
        elif request.role == "assistant":
            memory.append_assistant(
                conversation_id=conversation_id,
                content=request.content,
                metadata=request.metadata,
            )
        elif request.role == "system":
            memory.append_summary(conversation_id, request.content)
        else:
            raise HTTPException(status_code=400, detail=f"invalid role: {request.role}")
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Failed to append conversation message")
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return {"status": "ok", "conversation_id": conversation_id}


@app.get("/api/rag/conversations/{conversation_id}/messages")
def get_conversation_messages(
    conversation_id: str,
    limit: int = Query(default=20, ge=1, le=100),
) -> Dict[str, Any]:
    memory = get_conversation_memory()
    msgs = memory.get_window(conversation_id, limit=limit)
    return {"conversation_id": conversation_id, "messages": msgs, "count": len(msgs)}


@app.delete("/api/rag/conversations/{conversation_id}")
def clear_conversation(conversation_id: str) -> Dict[str, Any]:
    memory = get_conversation_memory()
    memory.clear(conversation_id)
    return {"status": "ok", "conversation_id": conversation_id, "cleared": True}


# ---------------------------------------------------------------------------
# Convenience: assistant surface used by the frontend
# ---------------------------------------------------------------------------

@app.post("/api/ai/assistant/query", response_model=StandardizedAIResponse)
def ai_assistant_query(
    query: str = Body(..., embed=True),
    team_id: Optional[str] = Body(default=None),
    user_id: Optional[str] = Body(default=None),
    conversation_id: Optional[str] = Body(default=None),
    sources: Optional[List[str]] = Body(default=None),
    max_documents: int = Body(default=5, ge=1, le=20),
) -> StandardizedAIResponse:
    """Thin wrapper around /api/rag/query for the frontend AI panel."""
    req = RAGRequest(
        query=query,
        team_id=team_id or "",
        user_id=user_id or "",
        conversation_id=conversation_id,
        sources=sources,
        max_documents=max_documents,
    )
    return rag_query(req)


# ---------------------------------------------------------------------------
# Background scheduler lifecycle
# ---------------------------------------------------------------------------

@app.on_event("startup")
async def _on_startup() -> None:
    scheduler = get_scheduler()
    if os.getenv("ORCA_AUTO_INDEX_ON_BOOT", "1") not in {"0", "false", "False"}:
        try:
            await scheduler.start()
        except Exception:  # pragma: no cover - defensive
            logger.exception("Failed to start background scheduler")


@app.on_event("shutdown")
async def _on_shutdown() -> None:
    scheduler = get_scheduler()
    try:
        await scheduler.stop()
    except Exception:  # pragma: no cover - defensive
        logger.exception("Failed to stop background scheduler")


@app.get("/api/rag/scheduler")
def rag_scheduler_status() -> Dict[str, Any]:
    return get_scheduler().get_status()


@app.post("/api/rag/scheduler/start")
async def rag_scheduler_start() -> Dict[str, Any]:
    await get_scheduler().start()
    return get_scheduler().get_status()


@app.post("/api/rag/scheduler/stop")
async def rag_scheduler_stop() -> Dict[str, Any]:
    await get_scheduler().stop()
    return get_scheduler().get_status()


@app.post("/api/rag/scheduler/run-bundled")
async def rag_scheduler_run_bundled() -> Dict[str, Any]:
    return await get_scheduler().trigger_bundled()


@app.post("/api/rag/scheduler/run-ingest")
async def rag_scheduler_run_ingest() -> Dict[str, Any]:
    return await get_scheduler().trigger_ingest()


@app.get("/api/rag/document/{doc_id}/provenance")
def rag_document_provenance(doc_id: str) -> Dict[str, Any]:
    from app.rag.sqlite_vector_store import get_vector_store

    prov = get_vector_store().provenance(doc_id)
    if prov is None:
        raise HTTPException(status_code=404, detail=f"document not found: {doc_id}")
    return prov


@app.get("/api/rag/quality")
def rag_quality_summary() -> Dict[str, Any]:
    from app.rag.sqlite_vector_store import get_vector_store

    return get_vector_store().average_quality()