# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 8/9)

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
  "chunk_index": 7,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md
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

```
