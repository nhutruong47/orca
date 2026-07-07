# Knowledge Document: groupService.ts (Chunk 4/8)

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
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts
(`/api/production/orders/${orderId}`).then(r => r.data),

    updateOrder: (orderId: string, data: Partial<ProductionOrder>) =>
        api.patch<ProductionOrder>(`/api/production/orders/${orderId}`, data).then(r => r.data),

    deleteOrder: (orderId: string) =>
        api.delete(`/api/production/orders/${orderId}`).then(r => r.data),

    updateOrderStatus: (orderId: string, status: string) =>
        api.patch<ProductionOrder>(`/api/production/orders/${orderId}/status`, { status }).then(r => r.data),

    generatePlan: (orderId: string) =>
        api.post<ProductionPlan>(`/api/production/plans/orders/${orderId}/generate`).then(r => r.data),

    getPlan: (planId: string) =>
        api.get<ProductionPlan>(`/api/production/plans/${planId}`).then(r => r.data),

    getPlansByOrder: (orderId: string) =>
        api.get<ProductionPlan[]>(`/api/production/plans/orders/${orderId}`).then(r => r.data),

    approvePlan: (planId: string, approvedBy?: string) =>
        api.patch<ProductionPlan>(`/api/production/plans/${planId}/approve`, { approvedBy }).then(r => r.data),

    getDailyTargetsByPlan: (planId: string) =>
        api.get<DailyTarget[]>(`/api/production/plans/${planId}/daily-targets`).then(r => r.data),

    updateDailyActual: (targetId: string, data: {
        actualRoastKg?: number;
        actualQcKg?: number;
        actualQcFailKg?: number;
        actualPackagedKg?: number;
        actualPackages?: number;
        notes?: string;
        issues?: string;
    }) =>
        api.patch<DailyTarget>(`/api/production/plans/daily-targets/${targetId}`, data).then(r => r.data),

    getTodayTarget: (teamId: string) =>
        api.get<DailyTarget>(`/api/production/plans/today/${teamId}`).then(r => r.data).catch(() => null),

    getDashboard: (teamId: string) =>
        api.get<any>(`/api/production/dashboard/${teamId}`).then(r => r.data),

    getProductivity: (teamId: string, startDate: string, endDate: string) =>
        api.get<any>(`/api/production/dashboard/${teamId}/productivity`, {
            params: { startDate, endDate }
        }).then(r => r.data),

    // === NEW: Daily Production Board ===
    getDailyBoard: (teamId: string) =>
        api.get<any>(`/api/production/board/${teamId}/today`).then(r => r.data),

    getBoardByDate: (teamId: string, date: string) =>

```
