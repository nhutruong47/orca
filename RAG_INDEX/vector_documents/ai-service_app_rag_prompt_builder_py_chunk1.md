# Knowledge Document: prompt_builder.py (Chunk 2/5)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/prompt_builder.py",
  "language": "py",
  "module": "rag",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production

## Source Code Chunk
```py
e with English in parentheses if needed
"""


class PromptBuilder:
    """
    Dynamic prompt builder for RAG queries.
    Constructs complete prompts from components.
    """
    
    def __init__(self):
        self.system_prompt = SYSTEM_PROMPT
        self.developer_prompt = DEVELOPER_PROMPT
    
    def build(
        self,
        query: str,
        retrieved_docs: List[RetrievedDocument],
        conversation_history: Optional[List[Dict[str, str]]] = None,
        context: Optional[Dict[str, Any]] = None,
        language: str = "vi"
    ) -> str:
        """
        Build complete prompt for LLM.
        
        Args:
            query: User query
            retrieved_docs: Retrieved knowledge documents
            conversation_history: Previous conversation messages
            context: Additional context (team, user, etc.)
            language: Response language code
            
        Returns:
            Complete prompt string
        """
        # Build knowledge context
        knowledge_context = self._build_knowledge_context(retrieved_docs)
        
        # Build conversation history
        history_context = self._build_history_context(conversation_history)
        
        # Build user context
        user_context = self._build_user_context(context)
        
        # Combine all parts
        full_prompt = f"""{self.system_prompt}

{knowledge_context}

{history_context}

{user_context}

{self.developer_prompt}

═══════════════════════════════════════════════════════════════
USER QUERY:
{query}

Please provide your response following the required format.
═══════════════════════════════════════════════════════════════
"""
        return full_prompt
    
    def _build_knowledge_context(
        self, 
        docs: List[RetrievedDocument]
    ) -> str:
        """Format retrieved documents as context"""
        if not docs:
            return "KNOWLEDGE BASE: No relevant documents found in the ORCA knowledge base."
        
        parts = ["RETRIEVED KNOWLEDGE:"]
        for i, doc in enumerate(docs, 1):
            meta = doc.document.metadata or {}
            source = meta.get("title", doc.document.source)
            category = meta.get("category", "General")
            
            parts.append(f"""
[{i}] {source} (relevance: {doc.relevance_score:.2f})
Category: {category}
---
{doc.document.content}
---""")
        

```
