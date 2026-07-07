# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 2/9)

## Metadata
```json
{
  "file_path": "KNOWLEDGE_ARCHITECTURE.md",
  "language": "md",
  "module": "orca",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "dashboard",
    "production",
    "admin",
    "inventory"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md
totalChunks: number;           // Total chunks in document
    parentDocumentId?: string;     // Parent document (for chunks)
}

type KnowledgeSourceType = 
    | 'inventory'
    | 'orders'
    | 'products'
    | 'users'
    | 'teams'
    | 'policies'
    | 'faq'
    | 'manual';

interface KnowledgeMetadata {
    // Classification
    category: string;
    tags: string[];
    
    // Content type
    contentType: 'procedural' | 'reference' | 'policy' | 'faq' | 'data';
    
    // Context
    teamId?: string;
    department?: string;
    
    // Quality
    qualityScore?: number;         // 0-1 automated quality
    verified: boolean;
    verifiedBy?: string;
    
    // Language
    language: string;              // ISO 639-1 (default: 'vi')
    
    // Additional
    author?: string;
    lastEditor?: string;
}

interface KnowledgePermissions {
    // Role-based access
    roles: ('ADMIN' | 'MANAGER' | 'MEMBER' | 'VIEWER')[];
    
    // Team-based access
    teams?: string[];             // Empty = all teams
    
    // User-specific access
    userId?: string;
    
    // Public access
    isPublic: boolean;
}
```

---

## 2. Chunking Strategy

### 2.1 Chunking Rules

```typescript
interface ChunkStrategy {
    source: KnowledgeSourceType;
    maxTokens: number;            // Maximum tokens per chunk
    overlapTokens: number;         // Overlap between chunks
    strategy: 'fixed' | 'semantic' | 'recursive';
}

const CHUNK_STRATEGIES: Record<KnowledgeSourceType, ChunkStrategy> = {
    inventory: {
        source: 'inventory',
        maxTokens: 512,
        overlapTokens: 50,
        strategy: 'semantic'        // Split by logical sections
    },
    orders: {
        source: 'orders',
        maxTokens: 768,
        overlapTokens: 100,
        strategy: 'semantic'         // Split by order sections
    },
    products: {
        source: 'products',
        maxTokens: 1024,
        overlapTokens: 100,
        strategy: 'recursive'        // Split by paragraphs then sentences
    },
    users: {
        source: 'users',
        maxTokens: 256,
        overlapTokens: 0,
        strategy: 'fixed'           // One chunk per user
    },
    teams: {
        source: 'teams',
        maxTokens: 512,
        overlapTokens: 50,
        strategy: 'semantic'
    },
    policies: {
        source: 'policies',
        maxTokens: 1024,
        overlapTokens: 100,

```
