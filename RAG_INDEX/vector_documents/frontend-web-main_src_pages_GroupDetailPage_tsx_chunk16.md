# Knowledge Document: GroupDetailPage.tsx (Chunk 17/136)

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
  "chunk_index": 16,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
me;
    })[0] || goals[goals.length - 1];
    const latestGoalTasks = latestGoal ? allTasks.filter(task => task.goalId === latestGoal.id) : allTasks;

    return (
        <div style={{ minHeight: '100vh', background: 'var(--bg-primary)', padding: '24px clamp(16px, 3vw, 48px)', fontFamily: "'Inter', sans-serif", width: '100%', maxWidth: 'none', margin: 0 }}>
            {/* ===== HEADER ===== */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 16, flexWrap: 'wrap', marginBottom: 18, background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 20 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ width: 44, height: 44, borderRadius: 12, background: '#d4a574', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: 22, fontWeight: 800 }}>
                        <ion-icon name="cafe-outline"></ion-icon>
                    </div>
                    <div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                            <h1 style={{ margin: 0, fontSize: 22, fontWeight: 800, color: 'var(--text-primary)' }}>{team.name}</h1>
                            <span style={{ background: '#dcfce7', color: '#16a34a', padding: '3px 10px', borderRadius: 12, fontSize: 11, fontWeight: 700 }}>● ĐANG HOẠT ĐỘNG</span>
                        </div>
                        <p style={{ margin: '2px 0 0', fontSize: 13, color: 'var(--text-secondary)' }}>{team.description || 'Nhóm sản xuất'} • {team.memberCount} thành viên</p>
                    </div>
                </div>
                <div style={{ display: 'flex', gap: 10, alignItems: 'center' }}>
                    <style>
                        {`
                        @keyframes pulse-ai-btn {
                            0% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.7); }
                            70% { box-shadow: 0 0 0 10px rgba(245, 158, 11, 0); }
                            100% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0); }
                        }
                        `}
                    </style>
                    {team.inviteCode && (

```
