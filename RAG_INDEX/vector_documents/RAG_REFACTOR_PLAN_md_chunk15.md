# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 16/17)

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
  "chunk_index": 15,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
c () => {
        return api.get('/api/rag/stats').then(r => r.data);
    },
    
    triggerIndexing: async (sourceType: string) => {
        return api.post(`/api/rag/index/${sourceType}`).then(r => r.data);
    }
};
```

### 3.2 Updated Chat Panel

```typescript
// src/components/AIChatPanel.tsx

import { ragService, type StandardizedAIResponse, type RAGRequest } from '../services/ragService';
import { CitationFormatter } from './ai/CitationFormatter';
import { ConfidenceIndicator } from './ai/ConfidenceIndicator';
import { SuggestedActions } from './ai/SuggestedActions';

export function AIChatPanel({ teamId, userId }: { teamId: string; userId: string }) {
    const [messages, setMessages] = useState<Message[]>([]);
    const [conversationId] = useState(() => generateUUID());
    
    const handleSend = async (query: string) => {
        // Add user message
        setMessages(prev => [...prev, { role: 'user', content: query }]);
        
        // Call RAG service
        const request: RAGRequest = {
            query,
            teamId,
            userId,
            conversationId,
            maxDocuments: 5
        };
        
        const response = await ragService.query(request);
        
        // Add AI response
        setMessages(prev => [...prev, {
            role: 'assistant',
            content: response.answer,
            response: response
        }]);
    };
    
    // Render with confidence, citations, and actions
    const renderMessage = (msg: Message) => (
        <div className="chat-message">
            <div className="chat-bubble">
                {msg.content}
            </div>
            
            {msg.response && (
                <>
                    <ConfidenceIndicator confidence={msg.response.confidence} />
                    <CitationFormatter sources={msg.response.referencedKnowledge} />
                    <SuggestedActions actions={msg.response.suggestedActions} />
                </>
            )}
        </div>
    );
}
```

---

## 4. Testing Plan

### Unit Tests
- [ ] EmbeddingService: Correct vector generation
- [ ] Retriever: Relevant documents returned
- [ ] PromptBuilder: Correct prompt formatting
- [ ] ConversationMemory: History persistence
- [ ] CitationFormatter: Correct citation format

### Integration Tests
- [ ] RAG query end-to-end
- [ ] Knowledge indexing pipeline

```
