# Knowledge Document: GroupDetailPage.tsx (Chunk 14/136)

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
  "chunk_index": 13,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx

                setGoals(g);
                Promise.all(g.map(goal => taskService.getByGoal(goal.id))).then(a => setAllTasks(a.flat()));
            }
            cancelEditTask();
        } catch (e: any) { setError(e?.response?.data?.error || 'Lỗi'); } finally { setLoading(false); }
    };

    const handleDeleteTask = async (taskId: string) => {
        if (!confirm('Xóa task này?')) return;
        await taskService.delete(taskId);
        if (id) {
            const g = await goalService.getByTeam(id);
            setGoals(g);
            Promise.all(g.map(goal => taskService.getByGoal(goal.id))).then(a => setAllTasks(a.flat()));
        }
    };

    const handleSaveAdSettings = async () => {
        if (!team) return;
        setLoading(true);
        try {
            if (isPublished) {
                const updated = await teamService.advertise(team.id, { specialty: adSpecialty, capacity: adCapacity, region: adRegion });
                setTeam(updated);
            } else {
                await teamService.unpublish(team.id);
                setTeam({ ...team, isPublished: false });
            }
            setShowAdSettings(false);
        } catch (e: any) { alert(e?.response?.data?.error || 'Lỗi'); } finally { setLoading(false); }
    };

    const handleDeleteTeam = async () => {
        if (!team) return;
        if (!confirm(`Bạn có chắc muốn xóa nhóm "${team.name}"?\n\nHành động không thể hoàn tác.`)) return;
        try { await teamService.deleteTeam(team.id); navigate('/groups'); } catch (e: any) { alert(e?.response?.data?.error || 'Lỗi'); }
    };

    const handleSaveLabels = async () => {
        if (!team || !selectedMemberForLabels) return;
        setLoading(true);
        try {
            const labelArray = editingLabels.split(',').map(l => l.trim()).filter(l => l.length > 0);
            const updatedLabels = await teamService.updateMemberLabels(team.id, selectedMemberForLabels.userId, labelArray);

            // Cập nhật state ui cho team member
            setTeam(prev => {
                if (!prev) return prev;
                return {
                    ...prev,
                    members: prev.members?.map(m => m.userId === selectedMemberForLabels.userId ? { ...m, jobLabels: updatedLabels } : m)
                };
            });
            setShowLabelModal(false);
        } catch (e: any) {

```
