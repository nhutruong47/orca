# Knowledge Document: GroupDetailPage.tsx (Chunk 111/136)

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
  "chunk_index": 110,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
atus !== 'COMPLETED';
                                                            const inProgress = t.status === 'IN_PROGRESS';

                                                            let pillBg = '#262629';
                                                            let pillBorder = '1px solid #3a3a3c';
                                                            let pillColor = '#ffffff';

                                                            if (isTaskOverdue) {
                                                                pillBg = 'rgba(239,68,68,0.1)';
                                                                pillBorder = '1px solid #ef4444';
                                                                pillColor = '#ef4444';
                                                            } else if (inProgress) {
                                                                pillBg = 'rgba(245,158,11,0.1)';
                                                                pillBorder = '1px solid #f59e0b';
                                                                pillColor = '#f59e0b';
                                                            } else if (t.status === 'COMPLETED') {
                                                                pillBg = 'rgba(16,185,129,0.1)';
                                                                pillBorder = '1px solid #10b981';
                                                                pillColor = '#10b981';
                                                            }

                                                            return (
                                                                <div key={t.id} style={{ background: pillBg, border: pillBorder, color: pillColor, padding: '12px', borderRadius: 10, display: 'flex', flexDirection: 'column', gap: 8 }}>
                                                                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 8 }}>
                                                                        <span style={{ fontSize: 13, fontWeight: 700, color: '#ffffff' }}>{t.title}</span>
                                                                        <span style={{ fontSize: 10, fontWeight: 800, padding: '2px 6px', borderRadius: 6, background: '#1c1c1e', color: pillColor }}>

```
