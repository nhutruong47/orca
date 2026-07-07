# Knowledge Document: types.ts (Chunk 7/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/types/types.ts",
  "language": "ts",
  "module": "types",
  "business_domain": "report",
  "tags": [
    "report",
    "payment",
    "factory",
    "notification",
    "production",
    "admin",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in types.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, notification, production, admin, inventory, employee, chat

## Source Code Chunk
```ts
lName: string;
    email: string;
    planId: string;
    amount: number;
    status: string;
    bankCode: string;
    paymentMethod?: string;
    createdAt: string | null;
    paidAt: string | null;
}

export interface AdminOverview {
    totalUsers: number;
    adminUsers: number;
    memberUsers: number;
    newUsersThisMonth: number;
    newUsersPreviousMonth: number;
    totalTeams: number;
    publishedTeams: number;
    newTeamsThisMonth: number;
    newTeamsPreviousMonth: number;
    totalGoals: number;
    activeGoals: number;
    totalTasks: number;
    completedTasks: number;
    overdueTasks: number;
    totalOrders: number;
    activeOrders: number;
    totalProductionOrders: number;
    activeProductionOrders: number;
    overdueProductionOrders: number;
    totalBatches: number;
    activeBatches: number;
    completedBatches: number;
    paidPayments: number;
    totalPayments: number;
    revenueThisMonth: number;
    revenuePreviousMonth: number;
    revenueThisYear: number;
    revenuePreviousYear: number;
    revenueTotal: number;
    orderStatusCounts: Record<string, number>;
    productionOrderStatusCounts: Record<string, number>;
    batchStatusCounts: Record<string, number>;
    taskStatusCounts: Record<string, number>;
    recentUsers: AdminUser[];
    recentTeams: AdminTeam[];
}

```
