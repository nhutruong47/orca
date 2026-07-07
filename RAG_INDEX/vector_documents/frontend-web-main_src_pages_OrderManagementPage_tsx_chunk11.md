# Knowledge Document: OrderManagementPage.tsx (Chunk 12/23)

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
  "chunk_index": 11,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Khách / xưởng đặt *</label>
                                <input
                                    value={manualOrderForm.customerName}
                                    onChange={event => handleManualOrderChange('customerName', event.target.value)}
                                    placeholder="Tên khách hoặc xưởng đặt"
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Số điện thoại</label>
                                <input
                                    value={manualOrderForm.contactPhone}
                                    onChange={event => handleManualOrderChange('contactPhone', event.target.value)}
                                    placeholder="SĐT liên hệ"
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Số lượng</label>
                                <input
                                    type="number"
                                    min={1}
                                    value={manualOrderForm.quantity}
                                    onChange={event => handleManualOrderChange('quantity', Number(event.target.value))}
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            <div>

```
