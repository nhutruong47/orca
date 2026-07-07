# Knowledge Document: ProductionPlanPage.tsx (Chunk 18/22)

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
  "chunk_index": 17,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
 (
                                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 28 }}>
                                    <div style={{ marginBottom: 20 }}>
                                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)', marginBottom: 8 }}>Chon ca lam viec</label>
                                        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                                            {(Object.entries(SHIFT_LABELS) as [ShiftType, string][]).map(([key, label]) => (
                                                <button key={key} onClick={() => setShiftType(key)}
                                                    style={{
                                                        padding: '8px 16px', borderRadius: 10, border: `2px solid ${shiftType === key ? '#10b981' : 'var(--border)'}`,
                                                        background: shiftType === key ? 'rgba(16,185,129,0.1)' : 'var(--bg-input)',
                                                        color: shiftType === key ? '#10b981' : 'var(--text-secondary)', fontSize: 13, fontWeight: 600, cursor: 'pointer'
                                                    }}>
                                                    {label}
                                                </button>
                                            ))}
                                        </div>
                                    </div>

                                    <div style={{ marginBottom: 20 }}>
                                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)', marginBottom: 8 }}>Cong doan lam viec</label>
                                        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                                            {(Object.entries(STAGE_LABELS) as [ProductionStage, string][]).map(([key, label]) => (
                                                <button key={key} onClick={() => setStage(key)}
                                                    style={{
                                                        padding: '8px 16px', borderRadius: 10, border: `2px solid ${stage === key ? '#3b82f6' : 'var(--border)'}`,

```
