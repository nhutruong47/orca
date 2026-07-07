# Knowledge Document: DailyBoardPage.tsx (Chunk 9/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DailyBoardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
       <div style={{ flex: 1, marginRight: 16 }}>
                                        <input
                                            type="range"
                                            min={0}
                                            max={100}
                                            value={row.progressPercent || 0}
                                            onChange={(e) => {
                                                const val = Number(e.target.value);
                                                setBoard((prev: any) => ({
                                                    ...prev,
                                                    orderRows: prev.orderRows?.map((r: any) =>
                                                        r.orderId === row.orderId ? { ...r, progressPercent: val } : r
                                                    ),
                                                }));
                                            }}
                                            onMouseUp={(e) => {
                                                const val = Number((e.target as HTMLInputElement).value);
                                                setUpdatingOrderId(row.orderId);
                                                productionService.updateOrder(row.orderId, { progressPercent: val })
                                                    .catch(() => alert('Khong the cap nhat tien do'))
                                                    .finally(() => setUpdatingOrderId(null));
                                            }}
                                            onTouchEnd={(e) => {
                                                const val = Number((e.target as HTMLInputElement).value);
                                                setUpdatingOrderId(row.orderId);
                                                productionService.updateOrder(row.orderId, { progressPercent: val })
                                                    .catch(() => alert('Khong the cap nhat tien do'))
                                                    .finally(() => setUpdatingOrderId(null));
                                            }}
                                            disabled={updatingOrderId === row.orderId}
                                            style={{

```
