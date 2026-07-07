# ORCA Platform - Knowledge Architecture

**Date:** July 7, 2026
**Status:** READY FOR IMPLEMENTATION

---

## Overview

This document defines the unified knowledge architecture for the ORCA platform, including all knowledge sources, indexing strategies, and metadata schemas.

---

## 1. Knowledge Sources Inventory

### 1.1 Source Types

| Source | Entity | Module | Update Frequency | Chunk Strategy |
|--------|--------|--------|----------------|---------------|
| Inventory | `InventoryItem` | Inventory | Real-time | By category |
| Production Orders | `ProductionOrder` | Production | Real-time | By status |
| Products | `Product` | Inventory | Manual | By type |
| Users | `User` | Admin | Real-time | By role |
| Teams | `Team` | Teams | Real-time | By team |
| Policies | `Policy` | Settings | Manual | By category |
| FAQ | `FAQ` | Help | Manual | By topic |
| Manual | `Documentation` | Help | Manual | By section |

### 1.2 Knowledge Source Schema

```typescript
interface KnowledgeDocument {
    // Identification
    id: string;                    // UUID v4
    source: KnowledgeSourceType;
    sourceId: string;              // Original entity ID
    version: number;                // Document version
    
    // Content
    content: string;              // Text content
    title: string;                 // Document title
    summary?: string;             // Auto-generated summary
    
    // Metadata
    metadata: KnowledgeMetadata;
    
    // Vector embedding
    embedding?: number[];         // Dense vector
    sparseEmbedding?: object;      // Sparse vector (optional)
    
    // Timestamps
    createdAt: string;             // ISO datetime
    updatedAt: string;            // ISO datetime
    indexedAt?: string;             // When indexed to vector store
    
    // Permissions
    permissions: KnowledgePermissions;
    
    // Chunking info
    chunkIndex: number;           // Position in original document
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
        strategy: 'semantic'         // Split by policy sections
    },
    faq: {
        source: 'faq',
        maxTokens: 384,
        overlapTokens: 0,
        strategy: 'fixed'            // Q&A pair as one chunk
    },
    manual: {
        source: 'manual',
        maxTokens: 1024,
        overlapTokens: 150,
        strategy: 'recursive'        // Deep splitting for long docs
    }
};
```

### 2.2 Chunking Examples

```typescript
// Inventory Item Example
const inventoryChunk = {
    id: 'inv_chunk_123_0',
    source: 'inventory',
    sourceId: 'INV-12345',
    content: `
        Sản phẩm: Cà phê Arabica Đà Lạt
        Loại: Hạt rang light
        Số lượng: 500 kg
        Giá: 180.000 VND/kg
        Mô tả: Cà phê Arabica trồng tại Đà Lạt, độ cao 1500m...
    `.trim(),
    title: 'Cà phê Arabica Đà Lạt',
    chunkIndex: 0,
    totalChunks: 1,
    metadata: {
        category: 'Cà phê hạt',
        tags: ['arabica', 'đà lạt', 'rang light'],
        contentType: 'reference',
        language: 'vi'
    }
};

// FAQ Example
const faqChunk = {
    id: 'faq_chunk_5_0',
    source: 'faq',
    sourceId: 'FAQ-5',
    content: `
        Câu hỏi: Làm sao để tạo đơn sản xuất mới?
        Trả lời: Để tạo đơn sản xuất mới, bạn cần:
        1. Truy cập trang Sản xuất
        2. Nhấn nút "Tạo đơn mới"
        3. Điền thông tin sản phẩm, số lượng, deadline
        4. Nhấn "Tạo" để hoàn tất
    `.trim(),
    title: 'Cách tạo đơn sản xuất',
    chunkIndex: 0,
    totalChunks: 1,
    metadata: {
        category: 'Sản xuất',
        tags: ['đơn sản xuất', 'tạo đơn', 'hướng dẫn'],
        contentType: 'faq',
        language: 'vi'
    }
};
```

---

## 3. Metadata Standards

### 3.1 Required Metadata Fields

Every knowledge document MUST include:

```typescript
const REQUIRED_METADATA = [
    'category',      // Primary classification
    'contentType',   // Type of content
    'language',      // Language code
    'verified',      // Verification status
];
```

### 3.2 Optional Metadata Fields

```typescript
const OPTIONAL_METADATA = [
    'tags',          // Additional keywords
    'teamId',        // Team association
    'author',        // Content creator
    'qualityScore',  // Automated quality
];
```

### 3.3 Category Taxonomy

```typescript
const KNOWLEDGE_CATEGORIES = {
    inventory: [
        'Nguyên liệu',
        'Thành phẩm',
        'Vật tư',
        'Bán thành phẩm'
    ],
    orders: [
        'Đơn hàng',
        'Yêu cầu sản xuất',
        'Đơn đặt hàng'
    ],
    production: [
        'Công đoạn',
        'Quy trình',
        'Máy móc',
        'Nhân sự'
    ],
    policies: [
        'An toàn lao động',
        'Quy trình',
        'Tiêu chuẩn',
        'Quy định'
    ],
    faq: [
        'Sản xuất',
        'Kho hàng',
        'Nhân sự',
        'Thanh toán',
        'Kỹ thuật'
    ]
};
```

---

## 4. Source Tracking

### 4.1 Document Provenance

```typescript
interface DocumentProvenance {
    documentId: string;
    source: KnowledgeSourceType;
    sourceId: string;
    
    // Original source info
    originalCreatedAt: string;
    originalUpdatedAt: string;
    
    // Indexing info
    indexedAt: string;
    indexedBy: string;
    indexVersion: number;
    
    // Update tracking
    lastSyncedAt?: string;
    syncStatus?: 'synced' | 'pending' | 'failed';
}
```

### 4.2 Source Attribution

```typescript
// Citation format for responses
interface SourceAttribution {
    documentId: string;
    source: KnowledgeSourceType;
    sourceId: string;
    title: string;
    excerpt: string;
    relevanceScore: number;
    url?: string;                  // Deep link to source
    
    // Metadata
    category?: string;
    lastUpdated?: string;
}
```

---

## 5. Update Strategies

### 5.1 Real-time Updates

For frequently changing data:

```typescript
const REALTIME_SOURCES: KnowledgeSourceType[] = [
    'inventory',
    'orders',
    'teams'
];

// Webhook handlers
async function handleInventoryUpdate(event: InventoryEvent) {
    const item = await fetchInventoryItem(event.itemId);
    const chunks = chunkDocument(item, CHUNK_STRATEGIES.inventory);
    
    for (const chunk of chunks) {
        await vectorStore.upsert(chunk.id, chunk.embedding, {
            ...chunk,
            updatedAt: new Date().toISOString()
        });
    }
}
```

### 5.2 Batch Updates

For stable data:

```typescript
const BATCH_UPDATE_SCHEDULE = {
    policies: '0 2 * * *',      // 2 AM daily
    faq: '0 3 * * 0',           // 3 AM weekly
    manual: '0 4 * * 0',         // 4 AM weekly
};

// Incremental sync
async function incrementalSync(source: KnowledgeSourceType) {
    const lastSync = await getLastSyncTime(source);
    const changes = await fetchChangesSince(source, lastSync);
    
    for (const change of changes) {
        await processChange(source, change);
    }
    
    await updateLastSyncTime(source);
}
```

### 5.3 Full Reindex

```typescript
async function fullReindex(source: KnowledgeSourceType) {
    const documents = await fetchAllDocuments(source);
    
    // Clear existing
    await vectorStore.deleteBySource(source);
    
    // Reindex all
    for (const doc of documents) {
        const chunks = chunkDocument(doc, CHUNK_STRATEGIES[source]);
        for (const chunk of chunks) {
            await vectorStore.insert(chunk.id, chunk.embedding, chunk);
        }
    }
    
    // Update metadata
    await updateIndexMetadata(source, {
        lastFullReindex: new Date().toISOString(),
        documentCount: documents.length
    });
}
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
    query: string,
    config: RetrievalConfig
): Promise<RetrievedDocument[]> {
    // Dense vector search
    const queryEmbedding = await embeddingService.embed(query);
    const denseResults = await vectorStore.search(
        queryEmbedding,
        config.maxDocuments * 2
    );
    
    // Sparse keyword search
    const sparseResults = await keywordSearch(query, {
        limit: config.maxDocuments * 2,
        sources: config.sources
    });
    
    // Combine with RRF (Reciprocal Rank Fusion)
    const fusedResults = reciprocalRankFusion(
        [denseResults, sparseResults],
        { k: 60 }
    );
    
    // Filter by minimum relevance
    const filteredResults = fusedResults.filter(
        r => r.relevanceScore >= config.minRelevanceScore
    );
    
    // Apply permissions
    const permittedResults = await filterByPermissions(
        filteredResults,
        config.userId,
        config.teamId
    );
    
    return permittedResults.slice(0, config.maxDocuments);
}
```

---

## 8. Quality Assurance

### 8.1 Quality Metrics

```typescript
interface QualityMetrics {
    completeness: number;          // All required fields present
    accuracy: number;               // Verified vs unverified
    freshness: number;               // How up-to-date
    relevance: number;              // Usage-based relevance
    
    overall: number;                // Weighted average
}

function calculateQualityScore(doc: KnowledgeDocument): QualityMetrics {
    const completeness = doc.metadata.category ? 1 : 0;
    const accuracy = doc.metadata.verified ? 1 : 0.5;
    
    const daysSinceUpdate = daysBetween(doc.updatedAt, new Date());
    const freshness = Math.max(0, 1 - daysSinceUpdate / 90);
    
    // Usage-based relevance (would come from analytics)
    const relevance = doc.metadata.qualityScore || 0.5;
    
    return {
        completeness,
        accuracy,
        freshness,
        relevance,
        overall: (completeness * 0.2 + accuracy * 0.3 + freshness * 0.2 + relevance * 0.3)
    };
}
```

### 8.2 Quality Checks

```typescript
async function validateDocument(doc: KnowledgeDocument): Promise<ValidationResult> {
    const errors: string[] = [];
    const warnings: string[] = [];
    
    // Required fields
    if (!doc.content || doc.content.length < 10) {
        errors.push('Content too short or empty');
    }
    
    if (!doc.metadata.category) {
        errors.push('Missing required field: category');
    }
    
    // Content quality
    if (doc.content.length > 10000) {
        warnings.push('Content very long, consider chunking');
    }
    
    // Freshness
    const daysOld = daysBetween(doc.updatedAt, new Date());
    if (daysOld > 180) {
        warnings.push(`Document is ${daysOld} days old`);
    }
    
    // Language consistency
    if (doc.metadata.language !== 'vi' && doc.metadata.language !== 'en') {
        warnings.push('Non-standard language code');
    }
    
    return {
        valid: errors.length === 0,
        errors,
        warnings,
        qualityScore: calculateQualityScore(doc)
    };
}
```

---

## 9. API Endpoints

### 9.1 Knowledge API

```typescript
// GET /api/knowledge/sources
// List all knowledge sources with stats

// GET /api/knowledge/search
// Query: q, sources[], maxDocuments, minScore
// Returns: RetrievedDocument[]

// GET /api/knowledge/:source/:id
// Get single document by source and ID

// POST /api/knowledge/index/:source
// Trigger reindexing for a source (admin only)

// DELETE /api/knowledge/:source/:id
// Remove document from index (admin only)

// GET /api/knowledge/stats
// Returns indexing statistics
```

### 9.2 Response Schema

```typescript
interface KnowledgeSearchResponse {
    query: string;
    documents: RetrievedDocument[];
    totalFound: number;
    searchTimeMs: number;
    
    // Metadata
    sources: string[];
    filters: RetrievalConfig;
    
    // Suggestions
    didYouMean?: string;
    relatedQueries?: string[];
}
```

---

## 10. Monitoring

### 10.1 Metrics

```typescript
interface KnowledgeMetrics {
    // Volume
    totalDocuments: number;
    documentsBySource: Record<KnowledgeSourceType, number>;
    totalChunks: number;
    
    // Quality
    averageQualityScore: number;
    unverifiedCount: number;
    staleCount: number;           // > 90 days old
    
    // Usage
    queriesLast24h: number;
    averageRetrievalCount: number;
    topSources: Array<{ source: string; count: number }>;
    
    // Performance
    averageQueryLatencyMs: number;
    indexingQueueSize: number;
}
```

### 10.2 Alerts

```typescript
const ALERT_THRESHOLDS = {
    quality: {
        minAverageScore: 0.6,
        maxUnverifiedRatio: 0.2
    },
    freshness: {
        maxStaleRatio: 0.1,
        maxDaysSinceUpdate: 180
    },
    performance: {
        maxQueryLatency: 500,       // ms
        maxIndexingQueue: 100
    }
};
```

---

## 11. Implementation Checklist

- [ ] Define schema for all knowledge sources
- [ ] Implement chunking strategies per source
- [ ] Set up vector database (Qdrant for dev)
- [ ] Create embedding pipeline
- [ ] Implement permission model
- [ ] Build indexing workers
- [ ] Create search API
- [ ] Add quality metrics
- [ ] Set up monitoring dashboard
- [ ] Write integration tests
