# Knowledge Document: types.ts (Chunk 1/7)

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
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in types.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, notification, production, admin, inventory, employee, chat

## Source Code Chunk
```ts
// === Request DTOs ===
export interface LoginRequest {
    username: string;
    password: string;
}

export interface RegisterRequest {
    username: string;
    password: string;
}

// === Response DTOs ===
export interface AuthResponse {
    token: string;
    username: string;
    role: string;
}

export interface UserInfo {
    id: string;
    username: string;
    fullName: string;
    email: string;
    avatar?: string;
    role: string;
    chipId: string;
    aiPlan?: string;
    aiPlanExpiresAt?: string | null;
}

// === Auth State ===
export interface AuthState {
    user: UserInfo | null;
    token: string | null;
    isAuthenticated: boolean;
    isLoading: boolean;
}

// === Team/Group ===
export interface TeamMemberInfo {
    userId: string;
    username: string;
    fullName: string;
    groupRole: string; // OWNER / MEMBER
    joinedAt: string;
    jobLabels?: string[];
    totalTasks?: number;
    completedTasks?: number;
    completionRate?: number;
}

export interface Team {
    id: string;
    name: string;
    description: string;
    ownerId: string;
    ownerName: string;
    memberCount: number;
    members?: TeamMemberInfo[];
    createdAt: string;

    // Advertisement
    isPublished?: boolean;
    specialty?: string;
    capacity?: string;
    region?: string;
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

    // Trust
    completedOrders?: number;
    cancelledOrders?: number;
    totalOrders?: number;
    trustScore?: number;
    rating?: number;
    reviewCount?: number;

    // Detailed Factory Information
    moq?: string;
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


```
