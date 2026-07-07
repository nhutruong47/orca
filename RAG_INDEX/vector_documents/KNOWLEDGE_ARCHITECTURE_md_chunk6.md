# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 7/9)

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
  "chunk_index": 6,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md

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

```
