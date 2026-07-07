# Knowledge Document: OrderManagementPage.tsx (Chunk 14/23)

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
  "chunk_index": 13,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
cal' }}
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Địa chỉ giao hàng</label>
                                <input
                                    value={manualOrderForm.deliveryAddress}
                                    onChange={event => handleManualOrderChange('deliveryAddress', event.target.value)}
                                    placeholder="Địa chỉ nhận/giao"
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Ghi chú</label>
                                <input
                                    value={manualOrderForm.deliveryNote}
                                    onChange={event => handleManualOrderChange('deliveryNote', event.target.value)}
                                    placeholder="Giao giờ hành chính, gọi trước..."
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            {manualCreateError && <div style={{ gridColumn: '1/-1', color: '#ef4444', fontSize: 16, fontWeight: 500, padding: '12px 16px', background: 'rgba(239, 68, 68, 0.1)', borderRadius: 8 }}>{manualCreateError}</div>}
                            <div style={{ gridColumn: '1/-1', display: 'flex', justifyContent: 'flex-end', gap: 16, marginTop: 16 }}>
                                <button
                                    type="button"
                                    className="btn btn-secondary"
                                    onClick={() => {
                                        setShowManualOrderForm(false);

```
