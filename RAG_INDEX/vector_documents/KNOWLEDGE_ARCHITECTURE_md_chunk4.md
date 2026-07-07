# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 5/9)

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
  "chunk_index": 4,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md
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

```
