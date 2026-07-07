# Knowledge Document: GroupDetailPage.tsx (Chunk 29/136)

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
  "chunk_index": 28,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                 displayStatusKey = 'IN_PROGRESS';
                                    } else {
                                        displayStatusKey = 'PENDING';
                                    }
                                }
                                const status = STATUS_COLORS[displayStatusKey] || STATUS_COLORS.PENDING;
                                return (
                                    <tr key={task.id} style={{ borderBottom: '1px solid var(--border)' }}>
                                        <td style={{ padding: '10px 12px', color: 'var(--text-secondary)', fontSize: 13 }}>{index + 1}</td>
                                        <td style={{ padding: '10px 12px' }}>
                                            <div style={{ color: 'var(--text-primary)', fontWeight: 700, fontSize: 13 }}>{task.title}</div>
                                            <div style={{ color: 'var(--text-secondary)', fontSize: 11, marginTop: 2 }}>{task.productionStage || task.taskCode}</div>
                                            {task.dependencyTaskTitles && task.dependencyTaskTitles.length > 0 && <div style={{ color: '#dc2626', fontSize: 11, marginTop: 3 }}>Depends on: {task.dependencyTaskTitles.join(', ')}</div>}
                                        </td>
                                        <td style={{ padding: '10px 12px', color: 'var(--text-secondary)', fontSize: 13 }}>{task.memberName || '-'}</td>
                                        <td style={{ padding: '10px 12px', color: 'var(--text-secondary)', fontSize: 13 }}>{task.backupMemberName || '-'}</td>
                                        <td style={{ padding: '10px 12px' }}><span style={{ background: status.bg, color: status.color, padding: '4px 9px', borderRadius: 8, fontSize: 11, fontWeight: 800 }}>{status.label}</span></td>
                                        <td style={{ padding: '10px 12px', minWidth: 120 }}>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                                <div style={{ flex: 1, height: 6, background: 'var(--bg-secondary)', borderRadius: 999, overflow: 'hidden' }}>
                                                    <div style={{ height: '100%', width: `${progressPct}%`, background: status.color, borderRadius: 999 }} />

```
