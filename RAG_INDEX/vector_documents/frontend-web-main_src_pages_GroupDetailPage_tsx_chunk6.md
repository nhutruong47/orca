# Knowledge Document: GroupDetailPage.tsx (Chunk 7/136)

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
  "chunk_index": 6,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx

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
    }, [id]);

    useEffect(() => {
        if (id && user?.id) {
            loadTodayAttendance();
        }
    }, [id, user?.id, loadTodayAttendance]);

    const currentUserMember = team?.members?.find(m => m.userId === user?.id);
    const userRoles = currentUserMember?.jobLabels?.filter(l => l.trim().length > 0) || [];
    const hasRole = userRoles.length > 0;
    const hasTasks = allTasks.some(t => t.memberId === user?.id);
    const canCheckIn = hasRole && hasTasks;

    const handleCheckIn = async () => {
        if (!id || !user?.id) return;
        if (!canCheckIn) {
            alert('Bạn cần được phân vai trò và công việc trước khi vào ca!');
            return;
        }
        setLoadingAttendance(true);
        try {
            const rawStage = userRoles.length > 0 ? userRoles[0].toUpperCase() : '';
            let stage = 'RANG';
            if (rawStage.includes('RANH') || rawStage.includes('CHỌN') || rawStage.includes('CHON')) stage = 'RANH_VA_CHON';
            else if (rawStage.includes('XAY') || rawStage.includes('XÂY')) stage = 'XAY';
            else if (rawStage.includes('DONG') || rawStage.includes('ĐÓNG') || rawStage.includes('GÓI') || rawStage.includes('GOI')) stage = 'DONG_GOI';
            else if (rawStage.includes('QA') || rawStage.includes('QC') || rawStage.includes('KIỂM') || rawStage.includes('KIEM')) stage = 'QA';
            
            const result = await attendanceService.checkIn(id, {
                shiftType: 'NGAY',
                stage: stage as any,
                breakMinutes: 0
            });
            setMyAttendance(result);
            alert('Vào ca thành công!');
        } catch (e: any) {
            alert(e.response?.data?.error || e.message || 'Lỗi vào ca');
        } finally {
            setLoadingAttendance(false);
        }
    };

    const handleCheckOut = async () => {
        if (!id || !user?.id) return;
        setLoadingAttendance(true);
        try {

```
