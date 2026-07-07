# Knowledge Document: OrderManagementPage.tsx (Chunk 22/23)

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
  "chunk_index": 21,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
        <div>
                                                                <span style={{ color: 'var(--text-secondary)' }}>SĐT phụ:</span>
                                                                <strong style={{ marginLeft: 6 }}>{order.contactPhoneAlt}</strong>
                                                            </div>
                                                        )}
                                                        {order.deliveryAddress && (
                                                            <div style={{ gridColumn: 'span 2' }}>
                                                                <span style={{ color: 'var(--text-secondary)' }}>Địa chỉ giao:</span>
                                                                <strong style={{ marginLeft: 6 }}>{order.deliveryAddress}</strong>
                                                            </div>
                                                        )}
                                                        {formatDeliveryTime(order.preferredDeliveryFrom, order.preferredDeliveryTo) && (
                                                            <div style={{ gridColumn: 'span 2' }}>
                                                                <span style={{ color: 'var(--text-secondary)' }}>Giờ giao mong muốn:</span>
                                                                <strong style={{ marginLeft: 6 }}>{formatDeliveryTime(order.preferredDeliveryFrom, order.preferredDeliveryTo)}</strong>
                                                            </div>
                                                        )}
                                                        {order.deliveryFailureAction && (
                                                            <div>
                                                                <span style={{ color: 'var(--text-secondary)' }}>Nếu không giao được:</span>
                                                                <strong style={{ marginLeft: 6 }}>{deliveryFailureLabel(order.deliveryFailureAction)}</strong>
                                                            </div>
                                                        )}
                                                        {order.deliveryNote && (

```
