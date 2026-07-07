# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 1/9)

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
  "chunk_index": 0,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md
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

```
