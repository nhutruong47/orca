# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 8/17)

## Metadata
```json
{
  "file_path": "RAG_REFACTOR_PLAN.md",
  "language": "md",
  "module": "orca",
  "business_domain": "authorization",
  "tags": [
    "authorization",
    "production",
    "factory",
    "inventory",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 7,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
pend(
                f"""
[{i}] {source} (relevance: {doc.relevance_score:.2f})
{meta.get('category', 'General')}
---
{doc.document.content}
---"""
            )
        
        return "\n".join(parts)
    
    def _build_history_context(self, history: Optional[List[dict]]) -> str:
        if not history:
            return "CONVERSATION HISTORY: This is the start of our conversation."
        
        parts = ["CONVERSATION HISTORY:"]
        for msg in history[-5:]:  # Last 5 messages
            role = msg.get("role", "user").upper()
            content = msg.get("content", "")
            parts.append(f"{role}: {content}")
        
        return "\n".join(parts)
    
    def _build_user_context(self, context: Optional[dict]) -> str:
        if not context:
            return ""
        
        parts = ["CURRENT CONTEXT:"]
        if team_name := context.get("team_name"):
            parts.append(f"- Team: {team_name}")
        if user_role := context.get("user_role"):
            parts.append(f"- Your role: {user_role}")
        if current_page := context.get("current_page"):
            parts.append(f"- Current view: {current_page}")
        
        return "\n".join(parts) if len(parts) > 1 else ""
```

#### Task 1.6: Create Conversation Memory

```python
# ai-service/app/rag/memory.py

from typing import List, Optional
from datetime import datetime
import json
import os

class ConversationMemory:
    """Manage conversation history and context"""
    
    def __init__(self, storage_path: str = "./data/conversations"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
    
    def get_history(self, conversation_id: str) -> List[dict]:
        """Get conversation history"""
        filepath = os.path.join(self.storage_path, f"{conversation_id}.json")
        if os.path.exists(filepath):
            with open(filepath) as f:
                return json.load(f).get("messages", [])
        return []
    
    def add_message(self, conversation_id: str, role: str, content: str):
        """Add a message to conversation"""
        filepath = os.path.join(self.storage_path, f"{conversation_id}.json")
        
        if os.path.exists(filepath):
            with open(filepath) as f:
                data = json.load(f)
        else:
            data = {"messages": [], "created_at": datetime.utcnow().isoformat()}

```
