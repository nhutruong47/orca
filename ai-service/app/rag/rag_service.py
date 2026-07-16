"""
Production-grade RAG service.

Pipeline:

    1. Sanitize user query (prompt-injection protection).
    2. Embed the cleaned query via the configured EmbeddingService.
    3. Retrieve top-K documents from the SQLite vector store with optional
       source / team filters.
    4. Build a deterministic, structured prompt that includes:
         - System + developer prompts (language: Vietnamese by default)
         - Conversation history (multi-turn context, bounded window)
         - User/team context (from request)
         - Retrieved knowledge (with source attribution)
         - The user's query
    5. Call Gemini through :func:`_call_gemini_text`. We instruct the LLM
       to respond in a strict JSON schema so we can parse answer,
       reasoning, confidence, suggested_actions reliably.
    6. Persist the conversation turn (user + assistant) so multi-turn
       works across requests.
    7. Return a :class:`StandardizedAIResponse` with citations,
       suggested actions, confidence and metadata.

Failure modes:
    * Empty knowledge base -> we still answer, but with low confidence
      and an explicit "no docs found" hint in the answer.
    * LLM down -> 502 with a friendly Vietnamese error message.
    * Sanitizer blocks the query -> 400 with the redaction summary.
"""

from __future__ import annotations

import json
import logging
import re
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

from app.config import settings
from app.gemini_ai import _call_gemini_text
from app.rag.embedding import EmbeddingService, get_embedding_service
from app.rag.memory import ConversationMemory, get_conversation_memory
from app.rag.models import (
    IndexingJob,
    KnowledgeDocument,
    RAGRequest,
    RetrievedDocument,
    StandardizedAIResponse,
)
from app.rag.prompt_builder import PromptBuilder
from app.rag.sanitizer import sanitize_user_query
from app.rag.sqlite_vector_store import SQLiteVectorStore, get_vector_store

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# LLM output schema
# ---------------------------------------------------------------------------

_RESPONSE_SCHEMA_HINT = """
{
  "answer": "Câu trả lời bằng tiếng Việt, ngắn gọn, đi thẳng vào vấn đề.",
  "reasoning_summary": "Giải thích ngắn gọn bạn suy luận như thế nào từ kiến thức đã truy xuất (1-3 câu).",
  "confidence": {
    "score": 0.0,         // 0.0 đến 1.0
    "level": "high|medium|low",
    "reasons": ["lý do 1", "lý do 2"]
  },
  "referenced_knowledge": [
    {
      "title": "Tiêu đề tài liệu",
      "excerpt": "Trích đoạn ngắn",
      "relevance_score": 0.0
    }
  ],
  "suggested_actions": [
    {
      "label": "Nhãn hiển thị (tiếng Việt)",
      "type": "navigate|create_task|open_modal|external",
      "payload": {}
    }
  ]
}
""".strip()


_SAFETY_BLOCK_TEXT = (
    "Yêu cầu của bạn chứa nội dung vi phạm chính sách sử dụng AI của ORCA "
    "(ví dụ: cố gắng bypass hệ thống, đóng vai trò khác, hoặc chèn mã "
    "điều khiển). Vui lòng đặt câu hỏi khác liên quan tới sản xuất hoặc "
    "vận hành nhà máy."
)


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------

class RAGService:
    def __init__(
        self,
        *,
        embedding_service: Optional[EmbeddingService] = None,
        vector_store: Optional[SQLiteVectorStore] = None,
        prompt_builder: Optional[PromptBuilder] = None,
        memory: Optional[ConversationMemory] = None,
    ) -> None:
        self.embedding_service = embedding_service or get_embedding_service()
        self.vector_store = vector_store or get_vector_store()
        self.prompt_builder = prompt_builder or PromptBuilder()
        self.memory = memory or get_conversation_memory()

    # -----------------------------------------------------------------
    # Public entrypoint
    # -----------------------------------------------------------------

    def query(self, request: RAGRequest) -> StandardizedAIResponse:
        start = time.time()
        sanitization = sanitize_user_query(request.query)
        if sanitization.blocked:
            # Hard block — don't even hit the LLM.
            return self._blocked_response(sanitization, request, start)

        query = sanitization.text
        if not query:
            raise ValueError("Empty query after sanitization.")

        # 1. Conversation history (before we append this turn).
        history: Optional[List[Dict[str, str]]] = None
        if request.conversation_id:
            if not self.memory.is_stale(request.conversation_id):
                history = self.memory.get_window(request.conversation_id)

        # 2. Embed + retrieve.
        try:
            query_embedding = self.embedding_service.embed_query(query)
        except Exception as exc:
            logger.exception("Embedding failed for query")
            raise RuntimeError(f"Không thể tạo embedding: {exc}") from exc

        retrieved = self._retrieve(
            query_embedding=query_embedding,
            sources=request.sources,
            team_id=request.team_id,
            max_docs=request.max_documents,
        )

        # 3. Build prompt.
        prompt = self.prompt_builder.build(
            query=query,
            retrieved_docs=retrieved,
            conversation_history=history,
            context={
                "team_id": request.team_id,
                "user_id": request.user_id,
            },
            language="vi",
        )
        # Append a strict response-schema reminder so Gemini answers in JSON.
        prompt = (
            prompt
            + "\n\nRESPONSE FORMAT (BẮT BUỘC - JSON thuần):\n"
            + _RESPONSE_SCHEMA_HINT
            + "\n\nTrả về DUY NHẤT một đối tượng JSON hợp lệ. Không giải thích ngoài JSON."
        )

        # 4. Call LLM.
        try:
            response_text = self._generate_response(prompt)
        except Exception as exc:
            logger.exception("LLM generation failed")
            raise RuntimeError(f"Không thể sinh câu trả lời: {exc}") from exc

        # 5. Parse answer.
        parsed = self._parse_llm_response(response_text, retrieved)

        # 6. Persist conversation turn.
        if request.conversation_id:
            try:
                self.memory.append_user(
                    conversation_id=request.conversation_id,
                    content=query,
                    user_id=request.user_id,
                    metadata={"sources": request.sources},
                )
                self.memory.append_assistant(
                    conversation_id=request.conversation_id,
                    content=parsed["answer"],
                    metadata={"references": [c["document_id"] for c in parsed["citations"]]},
                )
            except Exception:
                # Conversation persistence must never break the answer path.
                logger.exception("Failed to persist conversation turn")

        # 7. Build response.
        elapsed_ms = int((time.time() - start) * 1000)
        return StandardizedAIResponse(
            answer=parsed["answer"],
            reasoning_summary=parsed["reasoning"],
            referenced_knowledge=parsed["citations"],
            confidence=parsed["confidence"],
            suggested_actions=parsed["suggested_actions"],
            metadata={
                "model": settings.gemini_model,
                "processing_time_ms": elapsed_ms,
                "documents_retrieved": len(retrieved),
                "query": query,
                "sanitization": {
                    "is_safe": sanitization.is_safe,
                    "redactions": sanitization.redaction_count,
                    "detections": sanitization.detections,
                },
                "team_id": request.team_id,
                "user_id": request.user_id,
                "conversation_id": request.conversation_id,
                "sources_filter": request.sources,
            },
        )

    # -----------------------------------------------------------------
    # Indexer bridge — used by HTTP layer
    # -----------------------------------------------------------------

    def index_document(
        self,
        *,
        doc_id: str,
        source: str,
        source_id: str,
        content: str,
        metadata: Dict[str, Any],
        team_id: Optional[str] = None,
        chunk_index: int = 0,
    ) -> None:
        from app.rag.indexer import chunk_text
        # Reuse the chunker so indexer ingest and ad-hoc ingest behave the same.
        if not content:
            return
        chunks = chunk_text(content)
        if not chunks:
            return
        for idx, text in enumerate(chunks):
            vector = self.embedding_service.embed([text])[0]
            doc_id_final = f"{doc_id}#{idx}" if len(chunks) > 1 else doc_id
            self.vector_store.upsert_document(
                doc_id=doc_id_final,
                source=source,
                source_id=source_id,
                content=text,
                embedding=vector,
                metadata={**metadata, "chunk_index": idx},
                team_id=team_id,
                chunk_index=idx,
            )

    def get_stats(self) -> Dict[str, Any]:
        vector_stats = self.vector_store.get_stats()
        return {
            "documents_indexed": vector_stats["total_vectors"],
            "sources": vector_stats["sources"],
            "embedding_dimension": self.embedding_service.dimension,
            "embedding_model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        }

    # -----------------------------------------------------------------
    # Internals
    # -----------------------------------------------------------------

    def _retrieve(
        self,
        *,
        query_embedding: List[float],
        sources: Optional[List[str]],
        team_id: Optional[str],
        max_docs: int,
    ) -> List[RetrievedDocument]:
        # Over-fetch slightly so we can drop low-relevance docs after.
        raw = self.vector_store.search(
            query_embedding=query_embedding,
            k=max(20, max_docs * 3),
            sources=sources,
            team_id=team_id,
            min_score=0.0,
        )

        retrieved: List[RetrievedDocument] = []
        rank = 1
        for doc_id, score in raw:
            doc = self.vector_store.get(doc_id)
            if not doc:
                continue
            retrieved.append(
                RetrievedDocument(
                    document=KnowledgeDocument(
                        id=doc["id"],
                        source=doc["source"],
                        source_id=doc["source_id"],
                        content=doc["content"],
                        metadata=doc["metadata"],
                        chunk_index=doc["chunk_index"],
                    ),
                    relevance_score=float(score),
                    rank=rank,
                )
            )
            rank += 1
            if len(retrieved) >= max_docs:
                break
        return retrieved

    def _generate_response(self, prompt: str) -> str:
        if settings.ai_v2_mode == "mock":
            # Explicit mock mode only — never reached in production.
            return json.dumps(
                {
                    "answer": "Chế độ mock đang bật. Vui lòng tắt AI_V2_MODE=mock để dùng Gemini thật.",
                    "reasoning_summary": "Mock response (ai_v2_mode=mock).",
                    "confidence": {"score": 0.0, "level": "low", "reasons": ["mock_mode"]},
                    "referenced_knowledge": [],
                    "suggested_actions": [],
                },
                ensure_ascii=False,
            )
        return _call_gemini_text(prompt, max_output_tokens=2048)

    def _parse_llm_response(
        self,
        response_text: str,
        retrieved: List[RetrievedDocument],
    ) -> Dict[str, Any]:
        data = self._safe_json_loads(response_text)
        if data is None:
            # Fallback: answer is the raw text.
            return {
                "answer": response_text.strip() or "Tôi không thể sinh câu trả lời.",
                "reasoning": "Mô hình trả về văn bản thuần; không suy luận có cấu trúc.",
                "confidence": {
                    "score": 0.3,
                    "level": "low",
                    "reasons": ["LLM returned free-form text"],
                },
                "citations": self._format_citations(retrieved),
                "suggested_actions": [],
            }

        answer = (data.get("answer") or "").strip() or "Tôi không thể sinh câu trả lời."
        reasoning = (data.get("reasoning_summary") or data.get("reasoning") or "").strip()
        conf = data.get("confidence") or {}
        if not isinstance(conf, dict):
            conf = {}
        try:
            score = float(conf.get("score", 0.0))
        except (TypeError, ValueError):
            score = 0.0
        confidence = {
            "score": round(max(0.0, min(1.0, score)), 3),
            "level": conf.get("level") or self._score_to_level(score),
            "reasons": conf.get("reasons") or [],
        }
        if not confidence["reasons"]:
            confidence["reasons"] = self._confidence_reasons(retrieved, score)

        # Citations: trust the LLM-provided list if any, else fall back to retrieval.
        citations = self._format_citations(retrieved)
        llm_refs = data.get("referenced_knowledge") or []
        if isinstance(llm_refs, list) and llm_refs:
            for ref in llm_refs[: len(citations)]:
                if not isinstance(ref, dict):
                    continue
                idx = llm_refs.index(ref)
                if idx >= len(citations):
                    break
                if ref.get("title"):
                    citations[idx]["title"] = str(ref["title"])
                if ref.get("excerpt"):
                    citations[idx]["excerpt"] = str(ref["excerpt"])[:280]
                if isinstance(ref.get("relevance_score"), (int, float)):
                    citations[idx]["relevance_score"] = float(ref["relevance_score"])

        actions_in = data.get("suggested_actions") or []
        actions = [a for a in actions_in if isinstance(a, dict)] if isinstance(actions_in, list) else []

        return {
            "answer": answer,
            "reasoning": reasoning or "Dựa trên thông tin được truy xuất từ cơ sở tri thức ORCA.",
            "confidence": confidence,
            "citations": citations,
            "suggested_actions": actions[:5],
        }

    def _format_citations(self, docs: List[RetrievedDocument]) -> List[Dict[str, Any]]:
        citations: List[Dict[str, Any]] = []
        for d in docs:
            meta = d.document.metadata or {}
            # Pull provenance + quality from the underlying store row, so the
            # frontend can show freshness, last-updated, and a quality score
            # next to each citation.
            raw = self.vector_store.get(d.document.id) or {}
            quality = raw.get("quality_score")
            quality_components = raw.get("quality_components")
            citations.append(
                {
                    "document_id": d.document.id,
                    "source": d.document.source,
                    "source_id": d.document.source_id,
                    "title": meta.get("title", d.document.source),
                    "category": meta.get("category", "General"),
                    "excerpt": self._truncate(d.document.content, 200),
                    "relevance_score": round(float(d.relevance_score), 4),
                    "rank": d.rank,
                    "url": meta.get("url") or self._generate_url(d.document),
                    "last_updated": meta.get("last_updated"),
                    "indexed_at": raw.get("indexed_at"),
                    "indexed_by": raw.get("indexed_by"),
                    "index_version": raw.get("index_version") or 1,
                    "quality_score": round(float(quality), 3) if quality is not None else None,
                    "quality_components": quality_components or None,
                }
            )
        return citations

    @staticmethod
    def _truncate(text: str, n: int) -> str:
        if len(text) <= n:
            return text
        return text[:n].rsplit(" ", 1)[0] + "..."

    @staticmethod
    def _generate_url(doc: KnowledgeDocument) -> str:
        mapping = {
            "inventory": f"/inventory/item/{doc.source_id}",
            "orders": f"/orders/{doc.source_id}",
            "products": f"/products/{doc.source_id}",
            "teams": f"/teams/{doc.source_id}",
            "users": f"/users/{doc.source_id}",
            "policies": "/settings/policies",
            "faq": "/faq",
            "manual": "/manuals",
        }
        return mapping.get(doc.source, "/")

    @staticmethod
    def _score_to_level(score: float) -> str:
        if score >= 0.75:
            return "high"
        if score >= 0.45:
            return "medium"
        return "low"

    @staticmethod
    def _confidence_reasons(docs: List[RetrievedDocument], score: float) -> List[str]:
        if not docs:
            return ["Không tìm thấy tài liệu liên quan trong cơ sở tri thức."]
        avg = sum(d.relevance_score for d in docs) / max(len(docs), 1)
        return [
            f"Độ liên quan trung bình: {avg:.2f}",
            f"Số tài liệu truy xuất: {len(docs)}",
        ]

    @staticmethod
    def _safe_json_loads(text: str) -> Optional[Dict[str, Any]]:
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass
        match = re.search(r"\{[\s\S]*\}", text)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                return None
        return None

    def _blocked_response(
        self,
        sanitization,
        request: RAGRequest,
        start: float,
    ) -> StandardizedAIResponse:
        elapsed_ms = int((time.time() - start) * 1000)
        return StandardizedAIResponse(
            answer=_SAFETY_BLOCK_TEXT,
            reasoning_summary="Yêu cầu bị chặn bởi bộ lọc an toàn (prompt-injection).",
            referenced_knowledge=[],
            confidence={"score": 0.0, "level": "low", "reasons": ["policy_block"]},
            suggested_actions=[],
            metadata={
                "model": settings.gemini_model,
                "processing_time_ms": elapsed_ms,
                "documents_retrieved": 0,
                "query": sanitization.text,
                "sanitization": {
                    "is_safe": False,
                    "blocked": True,
                    "redactions": sanitization.redaction_count,
                    "detections": sanitization.detections,
                    "notes": sanitization.notes,
                },
                "team_id": request.team_id,
                "user_id": request.user_id,
                "conversation_id": request.conversation_id,
                "sources_filter": request.sources,
            },
        )


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_rag_service: Optional[RAGService] = None
_rag_lock = None  # created lazily to avoid import-order issues


def get_rag_service() -> RAGService:
    global _rag_service
    if _rag_service is None:
        import threading
        global _rag_lock
        if _rag_lock is None:
            _rag_lock = threading.Lock()
        with _rag_lock:
            if _rag_service is None:
                _rag_service = RAGService()
    return _rag_service


# ---------------------------------------------------------------------------
# IndexingJob re-export so external callers can keep using the schema model
# ---------------------------------------------------------------------------

__all__ = [
    "RAGService",
    "get_rag_service",
    "IndexingJob",
]