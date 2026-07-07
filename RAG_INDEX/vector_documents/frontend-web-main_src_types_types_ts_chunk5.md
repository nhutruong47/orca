# Knowledge Document: types.ts (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in types.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, notification, production, admin, inventory, employee, chat

## Source Code Chunk
```ts
 string;
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
    published: boolean;
    specialty: string;
    capacity: string;
    region: string;
    factoryType?: string;
    capacityValue?: number;
    capacityUnit?: string;
    factoryImageUrl?: string;
    factoryImages?: string[];
    verificationStatus?: 'NOT_SUBMITTED' | 'PENDING' | 'APPROVED' | 'REJECTED';
    businessLicense?: string;
    businessAddress?: string;
    websiteUrl?: string;
    facebookUrl?: string;
    certificates?: string[];
    certificationDocument?: string;
    verificationRejectReason?: string;
    completedOrders: number;
    cancelledOrders: number;
    totalOrders: number;
    trustScore: number;
}

export interface AdminOrder {
    id: string;
    title: string;
    description: string;
    buyerTeamId: string;
    buyerTeamName: string;
    sellerTeamId: string;
    sellerTeamName: string;
    quantity: number;
    deadline: string | null;
    status: string;
    linkedGoalId: string | null;
    createdAt: string | null;
    cancelledBy: string;
}

export interface AdminTask {
    id: string;
    title: string;
    description: string;
    goalId: string;
    goalTitle: string;
    teamId: string;
    teamName: string;
    memberId: string;
    memberName: string;
    priority: number;
    status: 'PENDING' | 'BLOCKED' | 'READY' | 'IN_PROGRESS' | 'WAITING_APPROVAL' | 'COMPLETED' | 'CANCELLED';
    acceptanceStatus: string;
    completionPercentage: number;
    deadline: string | null;
    createdAt: string | null;
}

export interface AdminPayment {
    id: string;
    txnRef: string;
    userId: string;
    username: string;
    fullName: string;
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

```
