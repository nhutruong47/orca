# Knowledge Document: types.ts (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in types.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, notification, production, admin, inventory, employee, chat

## Source Code Chunk
```ts
   targetDate?: string;
    targetQuantity: number;
    actualQuantity: number;
    status: string;
    completionRate?: number;
    isHoliday?: boolean;
    targetRoastKg?: number;
    actualRoastKg?: number;
    targetQcKg?: number;
    actualQcKg?: number;
    targetPackagedKg?: number;
    actualPackagedKg?: number;
    notes?: string;
    issues?: string;
}

export interface ProductionPlan {
    id?: string;
    planCode?: string;
    teamId: string;
    orderId: string;
    dailyTargets: DailyTarget[];
    startDate: string;
    endDate: string;
    status: string;
    dailyTargetKg?: number;
    totalWorkingDays?: number;
    totalRoastKg?: number;
    totalQcKg?: number;
    totalPackagedKg?: number;
    totalPackages?: number;
    totalInputKg?: number;
    riskFactors?: string[];
    aiRecommendations?: string[];
}

// === Notifications ===
export interface AppNotification {
    id: string;
    title: string;
    message: string;
    type: string; // TASK_ASSIGNED / TASK_ACCEPTED / TASK_REJECTED
    taskId: string;
    read: boolean;
    createdAt: string;
}

// === Salary Report ===
export interface SalaryReport {
    memberId: string;
    memberName: string;
    totalTasks: number;
    completedTasks: number;
    totalWorkload: number;
    totalActualWorkload: number;
    regularHours?: number;
    overtimeHours?: number;
    hourlyRate: number;
    overtimeRate?: number;
    estimatedSalary: number;
}

// === Inventory ===
export interface InventoryItem {
    id: string;
    teamId: string;
    name: string;
    quantity: number;
    unit: string;
    lowStockThreshold: number;
    status: 'IN_STOCK' | 'LOW_STOCK' | 'OUT_OF_STOCK';
    lastUpdated: string;

    // Featured Product fields
    price?: string;
    description?: string;
    imageUrl?: string;
    origin?: string;
    roastLevel?: string;
    processing?: string;
    tasteNotes?: string;
    isFeatured?: boolean;
}

// === Admin ===
export interface AdminUser {
    id: string;
    username: string;
    fullName: string;
    email: string;
    role: 'ADMIN' | 'MEMBER';
    chipId: string;
    createdAt: string | null;
    aiPlan?: string;
    aiPlanExpiresAt?: string | null;
}

export interface AdminTeam {
    id: string;
    name: string;
    description: string;
    ownerId: string;
    ownerName: string;
    memberCount: number;
    createdAt: string | null;

```
