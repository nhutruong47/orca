# Knowledge Document: rag_service.py (Chunk 2/6)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/rag_service.py",
  "language": "py",
  "module": "rag",
  "business_domain": "production",
  "tags": [
    "production",
    "admin",
    "inventory",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production, admin, inventory, security

## Source Code Chunk
```py
      "user_id": request.user_id
        }
        
        # Build prompt
        prompt = self.prompt_builder.build(
            query=query,
            retrieved_docs=retrieved_docs,
            conversation_history=history,
            context=context
        )
        
        # Generate response (placeholder - would call LLM)
        response_text = self._generate_response(prompt)
        
        # Calculate confidence
        confidence = self._calculate_confidence(retrieved_docs)
        
        # Format citations
        citations = self._format_citations(retrieved_docs)
        
        # Extract structured components
        answer, reasoning, suggestions = self._parse_response(response_text)
        
        # Add to conversation history
        if request.conversation_id:
            self._add_to_history(
                request.conversation_id,
                request.user_id,
                query,
                answer
            )
        
        processing_time = time.time() - start_time
        
        return StandardizedAIResponse(
            answer=answer,
            reasoning_summary=reasoning,
            referenced_knowledge=citations,
            confidence=confidence,
            suggested_actions=suggestions,
            metadata={
                "model": "gemini-1.5-pro",
                "tokens_used": len(prompt.split()) * 1.3,
                "processing_time_ms": int(processing_time * 1000),
                "documents_retrieved": len(retrieved_docs),
                "query": query
            }
        )
    
    def _sanitize_input(self, text: str) -> str:
        """Remove potential prompt injection patterns"""
        import re
        
        dangerous_patterns = [
            r"ignore previous instructions",
            r"disregard.*instructions",
            r"you are now.*different",
            r"forget.*instruction",
            r"new instructions:",
            r"override.*security",
            r"admin.*mode",
            r"developer.*mode",
            r"```system",
            r"```instructions",
        ]
        
        for pattern in dangerous_patterns:
            text = re.sub(pattern, "[FILTERED]", text, flags=re.IGNORECASE)
        
        return text.strip()
    
    def _retrieve(
        self,
        query_embedding: List[float],
        sources: Optional[List[str]] = None,

```
