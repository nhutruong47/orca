# Knowledge Document: types.ts (Chunk 2/7)

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
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in types.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, notification, production, admin, inventory, employee, chat

## Source Code Chunk
```ts
  leadTime?: string;
    yearsInOperation?: number;
    statusBadge?: string;
    employeeCount?: number;
    factorySize?: string;
    metadata?: string;

    // Invite
    inviteCode?: string;
}

// === Goals & Tasks ===
export interface AiTaskSuggestion {
    title: string;
    description: string;
    workload: number;
    priority: number;
    assigneeRole: 'Senior' | 'Junior' | 'Intern';
}

export interface AiParsedResult {
    phase: string;
    mainGoal: string;
    contingency: string;
    needsClarification: boolean;
    description: string;
    source: string;
    tasks: AiTaskSuggestion[];
}

export interface Goal {
    id: string;
    teamId: string;
    teamName: string;
    ownerId: string;
    ownerName: string;
    title: string;
    outputTarget: string;
    rawInstruction: string;
    aiParsedData: string; // JSON string of AiParsedResult
    priority: number;
    status: string;
    deadline: string;
    totalTasks: number;
    completedTasks: number;
    createdAt: string;
    chatLog?: string;
}

export interface Task {
    id: string;
    taskCode?: string;
    goalId: string;
    goalTitle: string;
    orderId?: string;
    orderCode?: string;
    batchId?: string;
    batchCode?: string;
    memberId: string;
    memberName: string;
    title: string;
    description: string;
    priority: number;
    status: string; // PENDING / BLOCKED / READY / IN_PROGRESS / WAITING_APPROVAL / COMPLETED / CANCELLED
    acceptanceStatus: string; // WAITING / ACCEPTED / REJECTED
    hourlyRate: number;
    workload: number;
    actualWorkload: number;
    completionPercentage: number;
    productionStage?: string;
    startTime?: string;
    dueTime?: string;
    teamId?: string;
    estimatedDurationMinutes?: number;
    actualStart?: string;
    actualEnd?: string;
    outputTarget?: number;
    actualOutput?: number;
    defectQuantity?: number;
    unit?: string;
    deadline: string;
    createdById?: string;
    createdByName?: string;
    createdByType?: string;
    updatedById?: string;
    updatedByName?: string;
    updatedByType?: string;
    updatedAt?: string;
    createdAt: string;
    backupMemberId?: string;
    backupMemberName?: string;
    supervisorId?: string;
    supervisorName?: string;
    dependencyTaskCodes?: string[];
    dependencyTaskTitles?: string[];
}

export interface ProductionOrder {
    id: string;

```
