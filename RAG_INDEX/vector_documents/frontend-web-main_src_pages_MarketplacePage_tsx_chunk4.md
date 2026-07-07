# Knowledge Document: MarketplacePage.tsx (Chunk 5/70)

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
  "chunk_index": 4,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
',
    'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1497515114889-1c06568a37b8?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1511537190424-bbbab87ac5eb?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1512568400610-62da28bc8a13?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=900&q=85',
    'https://images.unsplash.com/photo-1507133750050-4a2ce37285f1?auto=format&fit=crop&w=900&q=85'
];

const getFactoryImageSeed = (factory: any) => {
    if (!factory) return 0;
    if (factory.id) {
        let hash = 0;
        for (let i = 0; i < factory.id.length; i++) {
            hash = factory.id.charCodeAt(i) + ((hash << 5) - hash);
        }
        return Math.abs(hash);
    }
    return (factory.name?.length || 0) + (factory.completedOrders || 0) + (factory.completedOrdersMock || 0);
};

const getFactoryCardImage = (factory: any) =>
    factory?.factoryImageUrl
    || factory?.factoryImages?.[0]
    || fallbackFactoryImages[getFactoryImageSeed(factory) % fallbackFactoryImages.length];

const handleFactoryImageError = (event: SyntheticEvent<HTMLImageElement>) => {
    const target = event.currentTarget;
    if (target.dataset.localFallback === 'true') return;
    target.dataset.localFallback = 'true';
    target.src = '/coffee-hero.png';
};

const marketplaceCategories = [
    { label: 'Tất cả', icon: 'all_inclusive' },
    { label: 'Nguyên liệu', icon: 'eco' },
    { label: 'Dịch vụ rang', icon: 'local_cafe' },
    { label: 'Dịch vụ đóng gói', icon: 'package' },
    { label: 'Dịch vụ trọn gói', icon: 'star' },
    { label: 'Đăng nhu cầu', icon: 'assignment' },
];

// Removed static featuredProducts array
const splitMultiValue = (value?: string | string[]) => {
    if (Array.isArray(value)) return value.filter(Boolean).map(item => item.trim()).filter(Boolean);
    if (!value) return [];
    return value.split(/[,;\n]/).map(item => item.trim()).filter(Boolean);

```
