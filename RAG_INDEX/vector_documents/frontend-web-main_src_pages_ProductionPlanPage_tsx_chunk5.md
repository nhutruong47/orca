# Knowledge Document: ProductionPlanPage.tsx (Chunk 6/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
 '1px solid var(--border)', borderRadius: 14, padding: 20, marginBottom: 24 }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                            <div>
                                <div style={{ fontSize: 12, color: 'var(--text-muted)', marginBottom: 4 }}>{selectedOrder.orderCode} · {selectedOrder.productType}</div>
                                <div style={{ fontSize: 18, fontWeight: 800, marginBottom: 4 }}>{selectedOrder.title}</div>
                                <div style={{ fontSize: 13, color: 'var(--text-secondary)' }}>
                                    Khach: {selectedOrder.customerName || '-'} · San luong: {(selectedOrder.outputTarget || 0).toLocaleString()} kg
                                </div>
                                <div style={{ fontSize: 13, color: 'var(--text-secondary)', marginTop: 4 }}>
                                    {selectedOrder.internalDeadline && `Han noi bo: ${new Date(selectedOrder.internalDeadline).toLocaleDateString('vi-VN')} · `}
                                    {selectedOrder.customerDeliveryDate && `Giao hang: ${new Date(selectedOrder.customerDeliveryDate).toLocaleDateString('vi-VN')}`}
                                </div>
                            </div>
                            <div style={{ textAlign: 'right' }}>
                                {selectedOrder.inputRequired && (
                                    <div style={{ fontSize: 13, color: 'var(--text-muted)' }}>Nguyen lieu can</div>
                                )}
                                {selectedOrder.inputRequired && (
                                    <div style={{ fontSize: 20, fontWeight: 800, color: '#10b981' }}>{(selectedOrder.inputRequired).toLocaleString()} kg</div>
                                )}
                                <div style={{ marginTop: 6, fontSize: 12, color: '#10b981', fontWeight: 600 }}>
                                    Con lai: {(selectedOrder.remainingQuantity || 0).toLocaleString()} kg
                                </div>
                            </div>
                        </div>
                        {selectedOrder.progressPercent !== undefined && selectedOrder.progressPercent > 0 && (
                            <div style={{ marginTop: 16 }}>

```
