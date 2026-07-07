# Knowledge Document: GroupDetailPage.tsx (Chunk 16/136)

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
  "chunk_index": 15,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
          const items = await inventoryService.getByTeam(id!);
            setanys(items);
        } catch (e: any) { alert(e?.response?.data?.error || 'Lỗi xóa hàng'); }
    };

    if (!team) return (
        <div className="page-container" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 300 }}>
            <div style={{ textAlign: 'center', opacity: 0.5 }}>
                <div style={{ fontSize: 40, marginBottom: 12 }}><ion-icon name="time-outline" style={{ fontSize: '40px' }}></ion-icon></div>
                <p>Đang tải nhóm...</p>
            </div>
        </div>
    );

    // === COMPUTED DATA ===
    const totalTasks = allTasks.length;
    const inProgressTasks = allTasks.filter(t => t.status === 'IN_PROGRESS').length;
    const completedTasks = allTasks.filter(t => t.status === 'COMPLETED').length;
    const pendingTasks = allTasks.filter(t => t.status === 'PENDING').length;


    // Member stats
    const memberStats = (team.members || []).map((m, idx) => {
        const memberTasks = allTasks.filter(t => t.memberId === m.userId);
        const completed = memberTasks.filter(t => t.status === 'COMPLETED').length;
        const total = memberTasks.length;
        const pct = total ? Math.round((completed / total) * 100) : 0;
        return { ...m, completed, total, pct, color: MEMBER_COLORS[idx % MEMBER_COLORS.length] };
    });




    // Show the actual team roster for everyone. The previous filter hid all other
    // members for non-admin users, which made the group appear to have only one member.
    const visibleMemberStats = memberStats;
    const latestGoal = [...goals].sort((a, b) => {
        const aTime = a.createdAt ? new Date(a.createdAt).getTime() : 0;
        const bTime = b.createdAt ? new Date(b.createdAt).getTime() : 0;
        return bTime - aTime;
    })[0] || goals[goals.length - 1];
    const latestGoalTasks = latestGoal ? allTasks.filter(task => task.goalId === latestGoal.id) : allTasks;

    return (
        <div style={{ minHeight: '100vh', background: 'var(--bg-primary)', padding: '24px clamp(16px, 3vw, 48px)', fontFamily: "'Inter', sans-serif", width: '100%', maxWidth: 'none', margin: 0 }}>
            {/* ===== HEADER ===== */}

```
