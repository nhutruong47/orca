# Knowledge Document: prompt_builder.py (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production

## Source Code Chunk
```py
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
        
        return "\n".join(parts)
    
    def _build_history_context(
        self, 
        history: Optional[List[Dict[str, str]]]
    ) -> str:
        """Format conversation history"""
        if not history:
            return "CONVERSATION HISTORY: This is the start of our conversation."
        
        parts = ["CONVERSATION HISTORY:"]
        
        # Include last 5 messages
        for msg in history[-5:]:
            role = msg.get("role", "user").upper()
            content = msg.get("content", "")
            timestamp = msg.get("timestamp", "")
            
            parts.append(f"{role}: {content}")
            if timestamp:
                parts.append(f"[{timestamp}]")
            parts.append("")
        
        return "\n".join(parts)
    
    def _build_user_context(
        self, 
        context: Optional[Dict[str, Any]]
    ) -> str:
        """Format user/team context"""
        if not context:
            return ""
        
        parts = ["CURRENT CONTEXT:"]
        
        if team_name := context.get("team_name"):
            parts.append(f"- Team: {team_name}")
        
        if user_name := context.get("user_name"):
            parts.append(f"- User: {user_name}")
        
        if user_role := context.get("user_role"):
            parts.append(f"- Your role: {user_role}")
        
        if current_page := context.get("current_page"):
            parts.append(f"- Current view: {current_page}")
        
        if team_id := context.get("team_id"):
            parts.append(f"- Team ID: {team_id}")
        
        return "\n".join(parts) if len(parts) > 1 else ""
    
    def build_extraction_prompt(
        self,
        query: str,
        team_members: Optional[List[Dict[str, Any]]] = None
    ) -> str:
        """
        Build prompt for intent extraction.
        
        Args:
            query: User query to extract from
            team_members: Available team members for assignment suggestions
            

```
