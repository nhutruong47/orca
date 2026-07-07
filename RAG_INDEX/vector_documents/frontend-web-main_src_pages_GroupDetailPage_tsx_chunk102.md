# Knowledge Document: GroupDetailPage.tsx (Chunk 103/136)

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
  "chunk_index": 102,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ay: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                            <h3 style={{ margin: 0, fontSize: 18, fontWeight: 700, color: '#ffffff' }}>
                                                Tháng {month + 1}, {year}
                                            </h3>
                                            <div style={{ display: 'flex', gap: 8 }}>
                                                <button onClick={handlePrevMonth} style={{ width: 32, height: 32, borderRadius: 8, background: '#1e1e24', color: '#ffffff', border: '1px solid #2d2d34', cursor: 'pointer', display: 'grid', placeItems: 'center', transition: 'background 0.2s' }} onMouseEnter={e => e.currentTarget.style.background = '#2a2a32'} onMouseLeave={e => e.currentTarget.style.background = '#1e1e24'}>
                                                    <ion-icon name="chevron-back-outline" style={{ fontSize: 16 }}></ion-icon>
                                                </button>
                                                <button onClick={handleNextMonth} style={{ width: 32, height: 32, borderRadius: 8, background: '#1e1e24', color: '#ffffff', border: '1px solid #2d2d34', cursor: 'pointer', display: 'grid', placeItems: 'center', transition: 'background 0.2s' }} onMouseEnter={e => e.currentTarget.style.background = '#2a2a32'} onMouseLeave={e => e.currentTarget.style.background = '#1e1e24'}>
                                                    <ion-icon name="chevron-forward-outline" style={{ fontSize: 16 }}></ion-icon>
                                                </button>
                                            </div>
                                        </div>

                                        {/* Days Header */}
                                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: 8, textAlign: 'center', fontWeight: 600, fontSize: 13, color: '#8e8e93' }}>
                                            {['Th 2', 'Th 3', 'Th 4', 'Th 5', 'Th 6', 'Th 7', 'CN'].map(d => (
                                                <div key={d} style={{ padding: '6px 0' }}>{d}</div>
                                            ))}
                                        </div>

                                        {/* Days Grid */}

```
