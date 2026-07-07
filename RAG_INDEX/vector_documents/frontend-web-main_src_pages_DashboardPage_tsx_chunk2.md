# Knowledge Document: DashboardPage.tsx (Chunk 3/9)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "workspace",
  "tags": [
    "workspace",
    "factory",
    "dashboard",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
gần nhất' : 'Cần có nhóm xưởng',
            icon: CalendarDays,
            onClick: () => goToTeamFeature('/calendar'),
        },
        {
            label: 'Nhân sự',
            caption: primaryTeam ? 'Chấm công và ca làm' : 'Cần có nhóm xưởng',
            icon: UserRoundCog,
            onClick: () => goToTeamFeature('/workforce'),
        },
        {
            label: 'Tin nhắn nhóm',
            caption: primaryTeam ? 'Mở nhóm và khung chat' : 'Cần có nhóm xưởng',
            icon: MessageCircle,
            onClick: () => goToTeamFeature(''),
        },
        {
            label: 'Thị trường',
            caption: 'Tìm xưởng và đơn hợp tác',
            icon: Store,
            onClick: () => navigate('/marketplace'),
        },
    ];

    const stats = [
        {
            label: 'Nhóm xưởng',
            value: teams.length,
            caption: 'Không gian đang tham gia',
            icon: Factory,
            tone: 'teal',
        },
        {
            label: 'Việc đang làm',
            value: activeTasks.length,
            caption: 'Cần theo dõi hôm nay',
            icon: ClipboardList,
            tone: 'amber',
        },
        {
            label: 'Tiến độ',
            value: `${progress}%`,
            caption: `${completedTasks.length}/${myTasks.length} công việc hoàn thành`,
            icon: CheckCircle2,
            tone: 'green',
        },
        {
            label: 'Lịch hôm nay',
            value: getTodayLabel(),
            caption: 'Cập nhật theo múi giờ Việt Nam',
            icon: CalendarDays,
            tone: 'blue',
        },
    ];

    const openTeamWorkspace = (teamId: string | number) => {
        navigate(`/groups/${teamId}`);
    };

    const currentHour = new Date().getHours();
    const isOverloaded = activeTasks.length > 0 && currentHour >= 17;
    const totalTarget = myTasks.reduce((sum, task) => sum + (task.outputTarget || 0), 0);
    const totalActual = myTasks.reduce((sum, task) => sum + (task.actualOutput || 0), 0);
    const isOverachieving = totalTarget > 0 && totalActual > totalTarget;

    if (loading) {
        return (
            <div className="dashboard-page dashboard-loading">
                <div className="btn-spinner" />
                <p>Đang tải dashboard...</p>
            </div>
        );
    }

    return (
        <div className="dashboard-page">

```
