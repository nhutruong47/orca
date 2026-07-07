# Knowledge Document: KNOWLEDGE_ARCHITECTURE.md (Chunk 3/9)

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
  "chunk_index": 2,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, dashboard, production, admin, inventory

## Source Code Chunk
```md
hs then sentences
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


```
