# Knowledge Document: ProductionPlanPage.tsx (Chunk 13/22)

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
  "chunk_index": 12,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
 = target.id ? targetEdits[target.id] : undefined;
                                        const targetQty = edit?.target ?? (target.targetQuantity || target.targetRoastKg || 0);
                                        const actualQty = edit?.actual ?? (target.actualQuantity || target.actualRoastKg || 0);
                                        const cappedActual = Math.min(actualQty, targetQty);
                                        const livePct = targetQty > 0 ? Math.min(100, Math.round((cappedActual / targetQty) * 100)) : 0;

                                        const updateField = (field: 'actual' | 'target', value: number) => {
                                            if (!target.id) return;
                                            const current = edit || { actual: actualQty, target: targetQty };
                                            const next = { ...current, [field]: value };
                                            if (field === 'actual' && value > current.target) next.actual = current.target;
                                            if (field === 'target' && current.actual > value) next.actual = value;
                                            setTargetEdits(prev => ({ ...prev, [target.id!]: next }));
                                        };

                                        return (
                                            <div key={target.id} style={{
                                                padding: 16, background: isToday ? 'rgba(139,92,246,0.05)' : 'var(--bg-card)',
                                                border: `1px solid ${isToday ? 'rgba(139,92,246,0.3)' : 'var(--border)'}`,
                                                borderRadius: 14, borderLeft: isToday ? '4px solid #8b5cf6' : '4px solid var(--border)'
                                            }}>
                                                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 10 }}>
                                                    <div>
                                                        <span style={{ fontSize: 14, fontWeight: 700 }}>
                                                            {new Date(target.targetDate!).toLocaleDateString('vi-VN', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}

```
