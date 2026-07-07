# Knowledge Document: groupService.ts (Chunk 3/8)

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
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts
_TO_START') =>
        api.post<Task>(`/api/tasks/${id}/dependencies`, { dependsOnTaskId, dependencyType }).then(r => r.data),
    getDependencies: (id: string) =>
        api.get(`/api/tasks/${id}/dependencies`).then(r => r.data),
    delete: (id: string) => api.delete(`/api/tasks/${id}`),
    getChecklist: (taskId: string) =>
        api.get(`/api/tasks/${taskId}/checklists`).then(r => r.data),
    addChecklistItem: (taskId: string, content: string) =>
        api.post(`/api/tasks/${taskId}/checklists`, { content }).then(r => r.data),
    toggleChecklist: (checklistId: string) =>
        api.patch(`/api/tasks/checklists/${checklistId}/toggle`).then(r => r.data),
    getKpi: (memberId: string) =>
        api.get(`/api/tasks/member/${memberId}/kpi`).then(r => r.data),
    respondToTask: (taskId: string, accepted: boolean) =>
        api.patch<Task>(`/api/tasks/${taskId}/respond`, { accepted }).then(r => r.data),
    getSalaryReport: (teamId: string) =>
        api.get<SalaryReport[]>(`/api/tasks/salary/${teamId}`).then(r => r.data),
    exportSalaryExcel: (teamId: string) =>
        api.get(`/api/tasks/salary/${teamId}/export-excel`, { responseType: 'blob' }),
    payoutSalary: (teamId: string) =>
        api.post<{ message: string; totalEmployees: number; totalSalary: number; currency: string }>(
            `/api/tasks/salary/${teamId}/payout`
        ).then(r => r.data),
};

export const productionService = {
    getOrders: (teamId: string, activeOnly = false) =>
        api.get<ProductionOrder[]>(
            activeOnly
                ? `/api/production/teams/${teamId}/orders/active`
                : `/api/production/teams/${teamId}/orders`
        ).then(r => r.data),

    createOrder: (teamId: string, data: Partial<ProductionOrder>) =>
        api.post<ProductionOrder>(`/api/production/teams/${teamId}/orders`, data).then(r => r.data),

    getOrder: (orderId: string) =>
        api.get<ProductionOrder>(`/api/production/orders/${orderId}`).then(r => r.data),

    updateOrder: (orderId: string, data: Partial<ProductionOrder>) =>
        api.patch<ProductionOrder>(`/api/production/orders/${orderId}`, data).then(r => r.data),

    deleteOrder: (orderId: string) =>
        api.delete(`/api/production/orders/${orderId}`).then(r => r.data),

    updateOrderStatus: (orderId: string, status: string) =>

```
