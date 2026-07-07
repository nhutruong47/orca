# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 4/9)

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
  "chunk_index": 3,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md
ớng dẫn'],
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

```
