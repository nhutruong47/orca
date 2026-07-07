# Knowledge Document: GroupDetailPage.tsx (Chunk 89/136)

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
  "chunk_index": 88,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
  {(() => {
                                            const rate = total > 0 ? Math.round((completed / total) * 100) : 0;
                                            const rad = 60;
                                            const circ = 2 * Math.PI * rad;
                                            const offset = circ - (rate / 100) * circ;
                                            return (
                                                <div style={{ display: 'flex', alignItems: 'center', gap: 24, padding: '12px 0' }}>
                                                    <div style={{ position: 'relative', width: 140, height: 140, flexShrink: 0 }}>
                                                        <svg style={{ transform: 'rotate(-90deg)', width: 140, height: 140 }}>
                                                            <circle cx="70" cy="70" r={rad} fill="transparent" stroke="var(--border, #334155)" strokeWidth="10" />
                                                            <circle cx="70" cy="70" r={rad} fill="transparent" stroke="url(#radialGoldGradMain)" strokeWidth="12" strokeDasharray={circ} strokeDashoffset={offset} strokeLinecap="round" style={{ transition: 'stroke-dashoffset 0.8s ease-in-out' }} />
                                                            <defs>
                                                                <linearGradient id="radialGoldGradMain" x1="0%" y1="0%" x2="100%" y2="100%">
                                                                    <stop offset="0%" stopColor="#f59e0b" />
                                                                    <stop offset="100%" stopColor="#d4a574" />
                                                                </linearGradient>
                                                            </defs>
                                                        </svg>
                                                        <div style={{ position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', color: 'var(--text-primary)' }}>
                                                            <span style={{ fontSize: 32, fontWeight: 900 }}>{rate}%</span>

```
