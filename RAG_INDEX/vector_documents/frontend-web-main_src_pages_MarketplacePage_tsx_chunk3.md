# Knowledge Document: MarketplacePage.tsx (Chunk 4/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
    { value: 'Dark', label: 'Dark Roast' },
    { value: 'Espresso Roast', label: 'Espresso Roast' },
    { value: 'Custom', label: 'Theo profile riêng' },
];
const PACKAGING_FORMAT_OPTIONS = [
    { value: '100g', label: 'Túi 100g' },
    { value: '250g', label: 'Túi 250g' },
    { value: '500g', label: 'Túi 500g' },
    { value: '1kg', label: 'Túi 1kg' },
    { value: '5kg', label: 'Bao 5kg' },
    { value: '10kg', label: 'Bao 10kg' },
    { value: '20kg', label: 'Bao 20kg' },
    { value: '25kg', label: 'Bao 25kg' },
    { value: '50kg', label: 'Bao 50kg' },
    { value: 'Drip bag', label: 'Drip bag' },
    { value: 'Capsule', label: 'Capsule / Pod' },
    { value: 'Tin can', label: 'Lon thiếc' },
    { value: 'Private Label', label: 'Bao bì private label' },
    { value: 'Custom', label: 'Khác (Custom)' },
];

const profileTabLabels: Record<FactoryProfileTab, string> = {
    overview: 'Tổng quan',
    capabilities: 'Năng lực',
    equipment: 'Máy móc thiết bị',
    certificates: 'Chứng nhận',
    reviews: 'Đánh giá',
    portfolio: 'Dự án (Portfolio)',
    rfq: 'Gửi yêu cầu',
};

const verificationStatusLabel = (status: string) => {
    const labels: Record<string, string> = {
        NOT_SUBMITTED: 'Chưa gửi',
        PENDING: 'Đang chờ quản trị viên duyệt',
        APPROVED: 'Đã xác minh',
        REJECTED: 'Bị từ chối',
    };
    return labels[status] || status;
};

const fallbackFactoryImages = [
    'https://images.unsplash.com/photo-1447933601403-0c6688de566e?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1514432324607-a09d9b4aefda?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1504630083234-14187a9df0f5?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1498804103079-a6351b050096?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1497515114889-1c06568a37b8?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1511537190424-bbbab87ac5eb?auto=format&fit=crop&w=900&q=85',

```
