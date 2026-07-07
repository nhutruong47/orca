# Knowledge Document: ProductionOrderPage.tsx (Chunk 9/19)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionOrderPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
          {order.completedQuantity != null && (
                                            <div style={{ fontSize: 12, color: '#10b981', marginTop: 4 }}>
                                                Da xong: {(order.completedQuantity).toLocaleString('vi-VN')} kg ({order.progressPercent?.toFixed(0)}%)
                                            </div>
                                        )}
                                        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 8, marginTop: 12, flexWrap: 'wrap' }}>
                                            <button
                                                onClick={() => startEdit(order)}
                                                style={{ padding: '7px 12px', borderRadius: 8, border: '1px solid var(--border)', background: 'var(--bg-input)', color: 'var(--text-primary)', fontSize: 12, fontWeight: 700, cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: 5 }}
                                            >
                                                <ion-icon name="create-outline" /> Sua
                                            </button>
                                            <button
                                                onClick={() => handleDelete(order)}
                                                disabled={saving}
                                                style={{ padding: '7px 12px', borderRadius: 8, border: '1px solid rgba(239,68,68,0.35)', background: 'rgba(239,68,68,0.10)', color: '#ef4444', fontSize: 12, fontWeight: 700, cursor: saving ? 'not-allowed' : 'pointer', display: 'inline-flex', alignItems: 'center', gap: 5 }}
                                            >
                                                <ion-icon name="trash-outline" /> Xoa
                                            </button>
                                        </div>
                                    </div>
                                </div>

                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 12, marginTop: 16, paddingTop: 16, borderTop: '1px solid var(--border)' }}>
                                    {[
                                        ['Ngay dat', order.orderDate],
                                        ['Bat dau', order.productionStartDate],

```
