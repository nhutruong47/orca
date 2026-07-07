# Knowledge Document: GroupDetailPage.tsx (Chunk 12/136)

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
  "chunk_index": 11,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
itle.trim()) return;
        if (useAi && !trialActive) { setError('AI đã hết hạn dùng thử!'); return; }
        setLoading(true);
        try {
            setError('');
            await goalService.create({ teamId: id, title: goalTitle, outputTarget: goalTarget, deadline: goalDeadline || undefined, useAi } as any);
            const g = await goalService.getByTeam(id);
            setGoals(g);
            Promise.all(g.map(goal => taskService.getByGoal(goal.id))).then(a => setAllTasks(a.flat()));
            setShowCreateGoal(false);
            setGoalTitle(''); setGoalTarget(''); setGoalDeadline('');
        } catch (e: any) { setError(e?.response?.data?.error || 'Lỗi'); } finally { setLoading(false); }
    };



    const handleAddTask = async () => {
        if (!id || !newTaskTitle.trim()) return;
        setLoading(true);
        try {
            let goalId = selectedGoalId;
            if (!goalId) {
                const manualGoal = await goalService.create({
                    teamId: id,
                    title: 'Công việc thủ công',
                    outputTarget: 'Các công việc được thêm thủ công trong bảng.'
                } as any);
                goalId = manualGoal.id;
                setSelectedGoalId(goalId);
            }
            const inferredUnit = (newTaskUnit && newTaskUnit.trim()) || inferUnitFromText(`${newTaskTitle} ${newTaskDesc}`, newTaskStage);
            await taskService.create({
                goalId,
                title: newTaskTitle,
                description: newTaskDesc,
                workload: Number(newTaskWorkload) || 0,
                priority: newTaskPriority,
                productionStage: newTaskStage,
                unit: inferredUnit,
                dueTime: newTaskDueTime || undefined,
                deadline: newTaskDueTime || undefined,
                createdById: user?.id,
                createdByType: 'MANAGER'
            });
            const g = await goalService.getByTeam(id);
            setGoals(g);
            Promise.all(g.map(goal => taskService.getByGoal(goal.id))).then(a => setAllTasks(a.flat()));
            setNewTaskTitle(''); setNewTaskDesc(''); setNewTaskWorkload(''); setNewTaskDueTime(''); setNewTaskPriority(2); setShowAddTask(false);
        } catch (e: any) { setError(e?.response?.data?.error || 'Lỗi'); } finally { setLoading(false); }
    };


```
