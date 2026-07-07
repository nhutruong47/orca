# Knowledge Document: DashboardPage.tsx (Chunk 2/9)

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
  "chunk_index": 1,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
 Promise.resolve([]),
        ]).then(([teamData, tasksData]) => {
            setTeams(teamData || []);
            setMyTasks(tasksData || []);
            if (teamData && teamData.length > 0) {
                Promise.all(teamData.map((t: Team) => goalService.getByTeam(t.id).catch(() => [])))
                .then(goalsArray => {
                    const allGoals: Record<string, Goal[]> = {};
                    teamData.forEach((t: Team, i: number) => {
                        allGoals[t.id] = goalsArray[i] || [];
                    });
                    setTeamGoals(allGoals);
                });
            }
        }).finally(() => setLoading(false));
    }, [user?.id]);

    const activeTasks = useMemo(() => myTasks.filter(task => task.status !== 'COMPLETED'), [myTasks]);
    const completedTasks = useMemo(() => myTasks.filter(task => task.status === 'COMPLETED'), [myTasks]);
    const progress = myTasks.length ? Math.round((completedTasks.length / myTasks.length) * 100) : 0;
    const recentTasks = myTasks.slice(0, 5);
    const displayName = user?.fullName || user?.username || 'ORCA';
    const primaryTeam = teams[0];

    const goToTeamFeature = (featurePath: string) => {
        if (!primaryTeam) {
            navigate('/groups');
            return;
        }
        navigate(`/groups/${primaryTeam.id}${featurePath}`);
    };

    const quickActions = [
        {
            label: 'Tạo công việc',
            caption: primaryTeam ? 'Giao task trong nhóm đầu tiên' : 'Chọn nhóm để tạo task',
            icon: ClipboardList,
            onClick: () => goToTeamFeature('/create-task'),
        },
        {
            label: 'Đơn hàng',
            caption: 'Theo dõi mua bán và xử lý đơn',
            icon: PackageCheck,
            onClick: () => navigate('/orders'),
        },
        {
            label: 'Lịch sản xuất',
            caption: primaryTeam ? 'Xem lịch của nhóm gần nhất' : 'Cần có nhóm xưởng',
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

```
