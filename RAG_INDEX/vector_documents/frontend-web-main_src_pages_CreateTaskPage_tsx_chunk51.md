# Knowledge Document: CreateTaskPage.tsx (Chunk 52/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 51,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
= { ...newTasks[index], description: value };
        updateField('tasks', newTasks);
    };

    const updateTaskAssignee = (index: number, userId: string) => {
        const newTasks = [...(editedResult.tasks || [])];
        if (!userId) {
            newTasks[index] = {
                ...newTasks[index],
                suggestedAssignee: undefined,
                suggestedAssigneeId: null,
                suggestedReason: null,
                assignee: undefined,
            };
            updateField('tasks', newTasks);
            return;
        }

        const member = members.find(item => item.userId === userId);
        newTasks[index] = {
            ...newTasks[index],
            suggestedAssigneeId: userId,
            suggestedAssignee: member?.fullName || member?.username || 'Thành viên',
            suggestedReason: member?.jobLabels?.length
                ? `Bạn chọn thủ công. Nhãn hiện có: ${member.jobLabels.join(', ')}.`
                : 'Bạn chọn thủ công trên draft.',
            assignee: member?.username,
        };
        updateField('tasks', newTasks);
    };

    const clearTaskAssignee = (index: number) => {
        const newTasks = [...(editedResult.tasks || [])];
        newTasks[index] = {
            ...newTasks[index],
            suggestedAssignee: undefined,
            suggestedAssigneeId: null,
            suggestedReason: null,
            assignee: undefined,
        };
        updateField('tasks', newTasks);
    };

    const removeTask = (index: number) => {
        const newTasks = [...(editedResult.tasks || [])].filter((_, i) => i !== index);
        updateField('tasks', newTasks);
    };

    const addTask = () => {
        const newTasks = [...(editedResult.tasks || []), { title: 'Công việc mới', description: '', priority: 2, workload: 1, assignee: '' }];
        updateField('tasks', newTasks);
    };

    const assignedCount = (editedResult.tasks || []).filter(task => task.suggestedAssignee || task.assignee).length;
    const totalTasks = editedResult.tasks?.length || 0;
    const memberName = (member: TeamMemberInfo) => member.fullName || member.username || 'Thành viên';

    return (
        <div style={{
            width: '100%',
            background: 'var(--bg-card)',
            borderRadius: '24px',
            border: '1px solid var(--border)',

```
