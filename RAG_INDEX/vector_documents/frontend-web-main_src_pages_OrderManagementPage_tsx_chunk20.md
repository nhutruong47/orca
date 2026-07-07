# Knowledge Document: OrderManagementPage.tsx (Chunk 21/23)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/OrderManagementPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 20,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                            background: 'rgba(255,255,255,0.03)',
                                                border: '1px solid var(--border-color)',
                                                borderRadius: 8,
                                                padding: '16px 20px',
                                                marginTop: 4,
                                            }}>
                                                <h4 style={{ margin: '0 0 12px 0', fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: 6 }}>
                                                    <ion-icon name="location-outline" style={{ fontSize: '16px' }}></ion-icon>
                                                    Thông tin giao nhận hàng
                                                </h4>
                                                {(!order.contactPhone && !order.deliveryAddress) ? (
                                                    <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', margin: 0 }}>Chưa có thông tin giao hàng cho đơn này.</p>
                                                ) : (
                                                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', gap: '10px 24px', fontSize: '0.85rem' }}>
                                                        {order.contactPhone && (
                                                            <div>
                                                                <span style={{ color: 'var(--text-secondary)' }}>SĐT liên hệ:</span>
                                                                <strong style={{ marginLeft: 6 }}>{order.contactPhone}</strong>
                                                            </div>
                                                        )}
                                                        {order.contactPhoneAlt && (
                                                            <div>
                                                                <span style={{ color: 'var(--text-secondary)' }}>SĐT phụ:</span>
                                                                <strong style={{ marginLeft: 6 }}>{order.contactPhoneAlt}</strong>
                                                            </div>
                                                        )}

```
