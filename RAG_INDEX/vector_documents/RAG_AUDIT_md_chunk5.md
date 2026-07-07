# Knowledge Document: RAG_AUDIT.md (Chunk 6/10)

## Metadata
```json
{
  "file_path": "RAG_AUDIT.md",
  "language": "md",
  "module": "orca",
  "business_domain": "report",
  "tags": [
    "report",
    "payment",
    "factory",
    "production",
    "admin",
    "inventory",
    "security",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 5,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, production, admin, inventory, security, chat

## Source Code Chunk
```md
───────┐    ┌──────────────┐    ┌──────────────────┐    │
│  │ Embedding   │───▶│  Retriever   │───▶│  PromptBuilder   │    │
│  │ Service     │    │              │    │                  │    │
│  └─────────────┘    └──────────────┘    └────────┬─────────┘    │
│                                                  │               │
│                                                  ▼               │
│                          ┌──────────────────────────────────┐    │
│                          │      ConversationMemory          │    │
│                          │  (maintains context across turns) │    │
│                          └──────────────────────────────────┘    │
│                                                  │               │
│                                                  ▼               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   LLM (Gemini)                           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                  │               │
│                                                  ▼               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              CitationFormatter                            │   │
│  │  (attaches sources to response)                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                  │               │
│                                                  ▼               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │            StandardizedAIResponse                         │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Knowledge Base Structure

```typescript
interface KnowledgeDocument {
    id: string;                    // UUID
    source: 'inventory' | 'orders' | 'products' | 'users' | 'policies' | 'faq';
    sourceId: string;              // Reference to original entity
    content: string;               // Text content
    metadata: {
        title: string;
        category: string;
        tags: string[];
        lastUpdated: string;
        version: number;
    };
    embedding?: number[];          // Vector representation

```
