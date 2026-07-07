# Knowledge Document: RAG_AUDIT.md (Chunk 3/10)

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
  "chunk_index": 2,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, production, admin, inventory, security, chat

## Source Code Chunk
```md
onstruction | ❌ MISSING |
| `CitationFormatter` | Source attribution | ❌ MISSING |
| `ConversationMemory` | Multi-turn context | ❌ MISSING |
| `DocumentIndexer` | Knowledge base management | ❌ MISSING |
| `KnowledgeSource` | Data source abstraction | ❌ MISSING |

### 3.2 Knowledge Sources (Not Integrated)

| Source | Entity | Chunk Strategy | Status |
|--------|--------|----------------|--------|
| Inventory | `InventoryItem` | By product category | ❌ NOT INDEXED |
| Orders | `ProductionOrder` | By status | ❌ NOT INDEXED |
| Products | `Product` | By type | ❌ NOT INDEXED |
| Users | `User` | By role | ❌ NOT INDEXED |
| Policies | `Policy` | By category | ❌ NOT INDEXED |
| FAQ | `FAQ` | By topic | ❌ NOT INDEXED |
| Manual | Documentation | By section | ❌ NOT INDEXED |

### 3.3 Vector Storage Requirements

```python
# MISSING: Embedding configuration
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EMBEDDING_DIMENSION = 384

# MISSING: Vector store configuration
VECTOR_STORE = "pgvector"  # or "qdrant", "chroma", etc.
```

---

## 4. Response Format Issues

### 4.1 Current Response Format

```typescript
// AiParseResult (groupService.ts line 211-223)
interface AiParseResult {
    title: string;
    description: string;
    quantity: string | null;
    quantityNumber: number | null;
    unit: string | null;
    deadline: string | null;
    priority: string;
    needsClarification: boolean;
    source: string;
    suggestedQuestions?: string[];
    tasks?: {...}[];
}
```

### 4.2 Required Response Format (Standardized)

```typescript
interface StandardizedAIResponse {
    // Core answer
    answer: string;                    // Main response text
    reasoningSummary: string;          // How AI arrived at answer
    
    // Knowledge attribution
    referencedKnowledge: {
        source: string;                // e.g., "Production Orders", "Inventory"
        documentId: string;            // Unique document reference
        excerpt: string;               // Relevant text chunk
        relevanceScore: number;        // 0-1 similarity score
    }[];
    
    // Confidence and quality
    confidence: {
        score: number;                // 0-1 overall confidence
        level: 'high' | 'medium' | 'low';
        reasons: string[];             // Why confidence is this level
    };
    
    // Actions
    suggestedActions: {

```
