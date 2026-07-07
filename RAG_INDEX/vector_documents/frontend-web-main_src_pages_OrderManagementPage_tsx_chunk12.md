# Knowledge Document: OrderManagementPage.tsx (Chunk 13/23)

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
  "chunk_index": 12,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
dleManualOrderChange('quantity', Number(event.target.value))}
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Hạn chót</label>
                                <input
                                    type="date"
                                    value={manualOrderForm.deadline}
                                    onChange={event => handleManualOrderChange('deadline', event.target.value)}
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            <div style={{ gridColumn: '1/-1' }}>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Mô tả đơn</label>
                                <textarea
                                    value={manualOrderForm.description}
                                    onChange={event => handleManualOrderChange('description', event.target.value)}
                                    placeholder="Mặt hàng, quy cách, yêu cầu gia công/bán hàng..."
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none', minHeight: 120, resize: 'vertical' }}
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Địa chỉ giao hàng</label>
                                <input
                                    value={manualOrderForm.deliveryAddress}

```
