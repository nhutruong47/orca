# Knowledge Document: GroupDetailPage.tsx (Chunk 132/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 131,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                          {(s.overtimeHours && s.overtimeHours > 0) ? (
                                                    <div style={{ fontSize: 11, color: '#f59e0b', fontWeight: 700 }}>+ {s.overtimeHours.toFixed(1)}h TC</div>
                                                ) : <div style={{ fontSize: 10, color: '#94a3b8' }}>giờ thường</div>}
                                            </div>

                                            {/* Hourly Rate */}
                                            <div style={{ textAlign: 'center' }}>
                                                {isEditing ? (
                                                    <div style={{ display: 'flex', alignItems: 'center', gap: 4, justifyContent: 'center' }}>
                                                        <input
                                                            type="number"
                                                            value={tempRate}
                                                            onChange={e => setTempRate(e.target.value)}
                                                            autoFocus
                                                            style={{ width: 60, padding: '4px 8px', borderRadius: 6, border: '1px solid #d4a574', fontSize: 13, textAlign: 'center', background: '#fff', color: '#1e293b' }}
                                                        />
                                                        <button onClick={() => handleRateSave(s.memberId)} style={{ padding: '4px 8px', background: '#10b981', color: '#fff', border: 'none', borderRadius: 6, fontSize: 12, cursor: 'pointer' }}>✓</button>
                                                        <button onClick={() => setEditingRate(null)} style={{ padding: '4px 8px', background: '#ef4444', color: '#fff', border: 'none', borderRadius: 6, fontSize: 12, cursor: 'pointer' }}>✕</button>
                                                    </div>
                                                ) : (
                                                    <div
                                                        onClick={() => handleRateEdit(s.memberId, s.hourlyRate)}
                                                        style={{
                                                            display: 'inline-flex', alignItems: 'center', gap: 4,

```
