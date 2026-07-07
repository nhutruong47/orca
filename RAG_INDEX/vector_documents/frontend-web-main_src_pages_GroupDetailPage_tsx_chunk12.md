# Knowledge Document: GroupDetailPage.tsx (Chunk 13/136)

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
  "chunk_index": 12,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
yTeam(id);
            setGoals(g);
            Promise.all(g.map(goal => taskService.getByGoal(goal.id))).then(a => setAllTasks(a.flat()));
            setNewTaskTitle(''); setNewTaskDesc(''); setNewTaskWorkload(''); setNewTaskDueTime(''); setNewTaskPriority(2); setShowAddTask(false);
        } catch (e: any) { setError(e?.response?.data?.error || 'Lỗi'); } finally { setLoading(false); }
    };

    const startEditTask = (task: Task) => {
        setEditingTaskId(task.id);
        setEditTaskTitle(task.title || '');
        setEditTaskDesc(task.description || '');
        setEditTaskStage(task.productionStage || 'Roasting');
        setEditTaskUnit(task.unit || '');
        setEditTaskDueTime(toDatetimeInputValue(task.dueTime || task.deadline));
        setEditTaskPriority(task.priority || 2);
    };

    const cancelEditTask = () => {
        setEditingTaskId(null);
        setEditTaskTitle('');
        setEditTaskDesc('');
        setEditTaskStage('Roasting');
        setEditTaskUnit('');
        setEditTaskDueTime('');
        setEditTaskPriority(2);
    };

    const handleUpdateTask = async (taskId: string) => {
        if (!editTaskTitle.trim()) return;
        setLoading(true);
        try {
            const updatedUnit = (editTaskUnit && editTaskUnit.trim())
                ? editTaskUnit.trim()
                : inferUnitFromText(`${editTaskTitle} ${editTaskDesc}`, editTaskStage);
            await taskService.update(taskId, {
                title: editTaskTitle.trim(),
                description: editTaskDesc.trim(),
                priority: editTaskPriority,
                productionStage: editTaskStage,
                unit: updatedUnit,
                dueTime: editTaskDueTime || undefined,
                deadline: editTaskDueTime || undefined,
                updatedById: user?.id,
                updatedByType: 'MANAGER'
            });
            if (id) {
                const g = await goalService.getByTeam(id);
                setGoals(g);
                Promise.all(g.map(goal => taskService.getByGoal(goal.id))).then(a => setAllTasks(a.flat()));
            }
            cancelEditTask();
        } catch (e: any) { setError(e?.response?.data?.error || 'Lỗi'); } finally { setLoading(false); }
    };

    const handleDeleteTask = async (taskId: string) => {
        if (!confirm('Xóa task này?')) return;

```
