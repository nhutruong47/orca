# Knowledge Document: types.ts (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in types.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, notification, production, admin, inventory, employee, chat

## Source Code Chunk
```ts
 recipientName?: string;
    content: string;
    createdAt: string;
}

export interface AiChatLogMsg {
    role: 'user' | 'assistant';
    content: string;
    timestamp: string;
}

// === Inter-Group Orders ===
export interface InterGroupOrder {
    id: string;
    buyerTeamId?: string | null;
    buyerTeamName?: string | null;
    buyerUserId?: string | null;
    buyerUserName?: string | null;
    sellerTeamId: string;
    sellerTeamName: string;
    title: string;
    description: string;
    quantity: number;
    deadline: string;
    status: string; // PENDING, ACCEPTED, REJECTED, COMPLETED, CANCELED
    linkedGoalId?: string;
    createdAt: string;
    buyerTrustScore?: number;
    cancelledBy?: string;
    // Delivery profile
    contactPhone?: string;
    contactPhoneAlt?: string;
    deliveryAddress?: string;
    preferredDeliveryFrom?: string;
    preferredDeliveryTo?: string;
    deliveryFailureAction?: string; // RETRY_LATER, LEAVE_AT_DOOR, RETURN_TO_SENDER, CONTACT_ALTERNATIVE
    deliveryNote?: string;
    cancelRequested?: boolean;
    buyerViewed?: boolean;
    sellerViewed?: boolean;
    deliveryStatus?: string;
    deliveryConfirmed?: boolean;
}

// === Reviews ===
export interface Review {
    id: string;
    teamId: string;
    userId: string;
    userName: string;
    rating: number;
    comment: string;
    createdAt: string;
    qualityScore?: number;
    timeScore?: number;
    communicationScore?: number;
    supportScore?: number;
    replyText?: string;
    deliveryResult?: string;
    buyerTeamId?: string;
    buyerTeamName?: string;
    buyerUserId?: string;
    buyerUserName?: string;
}

export interface ReviewSummary {
    avgRating: number;
    reviewCount: number;
    onTimeRate: number;
    completedOrders: number;
    totalOrders: number;
    onTimeOrders: number;
    lateOrders: number;
    starCounts: Record<number, number>;
}

// === Production Plans ===
export interface DailyTarget {
    id?: string;
    date: string;
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

```
