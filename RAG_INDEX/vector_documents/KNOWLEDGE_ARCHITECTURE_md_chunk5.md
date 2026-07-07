# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 6/9)

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
  "chunk_index": 5,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md

```

---

## 6. Permission Model

### 6.1 Permission Levels

```typescript
const PERMISSION_LEVELS = {
    ADMIN: {
        canRead: ['*'],                 // All sources
        canWrite: ['*'],
        canDelete: ['*'],
        canManage: ['*']
    },
    MANAGER: {
        canRead: ['inventory', 'orders', 'products', 'teams', 'policies'],
        canWrite: ['inventory', 'orders', 'products'],
        canDelete: ['inventory'],
        canManage: []
    },
    MEMBER: {
        canRead: ['inventory', 'orders', 'faq', 'manual'],
        canWrite: [],
        canDelete: [],
        canManage: []
    },
    VIEWER: {
        canRead: ['faq', 'manual'],
        canWrite: [],
        canDelete: [],
        canManage: []
    }
};
```

### 6.2 Permission Enforcement

```typescript
async function retrieveWithPermissions(
    queryEmbedding: number[],
    userId: string,
    teamId?: string
): Promise<RetrievedDocument[]> {
    // Get user permissions
    const user = await getUser(userId);
    const userRole = user.role;
    const userTeams = user.teamIds || [];
    
    // Get allowed sources for role
    const allowedSources = PERMISSION_LEVELS[userRole].canRead;
    
    // Retrieve from allowed sources only
    const results = await vectorStore.search(
        queryEmbedding,
        {
            filter: {
                source: { $in: allowedSources },
                $or: [
                    { 'permissions.isPublic': true },
                    { 'permissions.teams': { $in: userTeams } },
                    { 'permissions.userId': userId },
                    { 'permissions.roles': userRole }
                ]
            }
        }
    );
    
    return results;
}
```

---

## 7. Search & Retrieval

### 7.1 Retrieval Configuration

```typescript
interface RetrievalConfig {
    maxDocuments: number;         // Max docs to retrieve
    minRelevanceScore: number;    // Minimum similarity
    rerankTopK: number;          // Top K for reranking
    
    // Source filters
    sources?: KnowledgeSourceType[];
    
    // Time filters
    dateFrom?: string;
    dateTo?: string;
    
    // Permission filters
    userId?: string;
    teamId?: string;
}

const DEFAULT_RETRIEVAL_CONFIG: RetrievalConfig = {
    maxDocuments: 10,
    minRelevanceScore: 0.5,
    rerankTopK: 20
};
```

### 7.2 Hybrid Search

```typescript
async function hybridSearch(

```
