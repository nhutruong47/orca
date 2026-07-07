# Knowledge Document: groupService.ts (Chunk 2/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/services/groupService.ts",
  "language": "ts",
  "module": "services",
  "business_domain": "report",
  "tags": [
    "report",
    "analytics",
    "dashboard",
    "chat",
    "production",
    "inventory",
    "employee",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts

    getDetail: (id: string) => api.get<Goal>(`/api/goals/${id}`).then(r => r.data),
    create: (data: Partial<Goal>) =>
        api.post<Goal>('/api/goals', data).then(r => r.data),
    updateStatus: (id: string, status: string) =>
        api.patch<Goal>(`/api/goals/${id}/status`, { status }).then(r => r.data),
    delete: (id: string) => api.delete(`/api/goals/${id}`),
};

// === Task API ===
export const taskService = {
    getByGoal: (goalId: string) =>
        api.get<Task[]>(`/api/tasks/by-goal/${goalId}`).then(r => r.data),
    getDetail: (id: string) => api.get<Task>(`/api/tasks/${id}`).then(r => r.data),
    getMyTasks: (memberId: string) =>
        api.get<Task[]>(`/api/tasks/member/${memberId}`).then(r => r.data),
    create: (data: Partial<Task>) =>
        api.post<Task>('/api/tasks', data).then(r => r.data),
    update: (id: string, data: Partial<Task>) =>
        api.patch<Task>(`/api/tasks/${id}`, data).then(r => r.data),
    updateStatus: (id: string, status: string) =>
        api.patch<Task>(`/api/tasks/${id}/status`, { status }).then(r => r.data),
    updateProgress: (id: string, percentage: number) =>
        api.patch<Task>(`/api/tasks/${id}/progress`, { percentage }).then(r => r.data),
    assign: (id: string, memberId: string) =>
        api.patch<Task>(`/api/tasks/${id}/assign`, { memberId }).then(r => r.data),
    setBackup: (id: string, memberId: string) =>
        api.patch<Task>(`/api/tasks/${id}/backup`, { memberId }).then(r => r.data),
    setSupervisor: (id: string, memberId: string) =>
        api.patch<Task>(`/api/tasks/${id}/supervisor`, { memberId }).then(r => r.data),
    transfer: (id: string, toMemberId: string, reason?: string) =>
        api.patch<Task>(`/api/tasks/${id}/transfer`, { toMemberId, reason, actorType: 'MANAGER' }).then(r => r.data),
    getTransfers: (id: string) =>
        api.get(`/api/tasks/${id}/transfers`).then(r => r.data),
    addDependency: (id: string, dependsOnTaskId: string, dependencyType = 'FINISH_TO_START') =>
        api.post<Task>(`/api/tasks/${id}/dependencies`, { dependsOnTaskId, dependencyType }).then(r => r.data),
    getDependencies: (id: string) =>
        api.get(`/api/tasks/${id}/dependencies`).then(r => r.data),
    delete: (id: string) => api.delete(`/api/tasks/${id}`),
    getChecklist: (taskId: string) =>
        api.get(`/api/tasks/${taskId}/checklists`).then(r => r.data),

```
