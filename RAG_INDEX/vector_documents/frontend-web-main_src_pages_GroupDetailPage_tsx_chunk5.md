# Knowledge Document: GroupDetailPage.tsx (Chunk 6/136)

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
  "chunk_index": 5,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
.error('Error parsing metadata', e); }
            }
        }).catch(() => { });
        goalService.getByTeam(id).then(g => {
            setGoals(g);
            // Load all tasks for all goals
            Promise.all(g.map(goal => taskService.getByGoal(goal.id)))
                .then(taskArrays => setAllTasks(taskArrays.flat()))
                .catch(() => { });
        }).catch(() => { });
        inventoryService.getByTeam(id).then(data => { console.log('[INVENTORY] Loaded', data?.length, 'items for team', id, data); setanys(data || []); }).catch(err => { console.error('[INVENTORY] Error loading inventory:', err); });
        getTrialStatus().then(s => { setTrialActive(s.aiTrialActive); setTrialDays(s.daysRemaining); }).catch(() => { });
    }, [id]);

    // Attendance state
    const [myAttendance, setMyAttendance] = useState<any>(null);
    const [showAttendanceHistory, setShowAttendanceHistory] = useState(false);
    const [attendanceHistory, setAttendanceHistory] = useState<any[]>([]);
    const [loadingAttendance, setLoadingAttendance] = useState(false);
    
    // Team Attendance
    const [showTeamAttendance, setShowTeamAttendance] = useState(false);
    const [teamAttendanceData, setTeamAttendanceData] = useState<any[]>([]);
    const [editingAttendance, setEditingAttendance] = useState<{ id: string, checkInTime: string, checkOutTime: string } | null>(null);

    const loadTodayAttendance = useCallback(async () => {
        if (!id || !user?.id) return;
        try {
            const att = await attendanceService.getTodayAttendance(id);
            setMyAttendance(att);
        } catch (e) {
            console.error('Lỗi tải thông tin chấm công hôm nay:', e);
        }
    }, [id, user?.id]);

    const loadAttendanceHistory = useCallback(async () => {
        if (!id || !user?.id) return;
        try {
            const history = await attendanceService.getHistory(id);
            setAttendanceHistory(history || []);
        } catch (e) {
            console.error('Lỗi tải lịch sử chấm công:', e);
        }
    }, [id, user?.id]);

    const loadTeamAttendance = useCallback(async () => {
        if (!id) return;
        try {
            const data = await attendanceService.getTeamHistory(id);
            setTeamAttendanceData(data || []);
        } catch (e) {
            console.error('Lỗi tải quản lý chấm công:', e);
        }

```
