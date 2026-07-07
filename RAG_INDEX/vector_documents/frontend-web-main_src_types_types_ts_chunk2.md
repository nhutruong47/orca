# Knowledge Document: types.ts (Chunk 3/7)

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
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in types.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, notification, production, admin, inventory, employee, chat

## Source Code Chunk
```ts
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
    teamId?: string;
    orderCode: string;
    title: string;
    description?: string;
    customerName?: string;
    productType?: string;
    processType?: string;
    roastLevel?: string;
    packageSize?: string;
    totalPackages?: number;
    expectedYield?: number;
    expectedLoss?: number;
    orderDate?: string;
    confirmDate?: string;
    productionStartDate?: string;
    customerDeliveryDate?: string;
    safetyBufferDays?: number;
    recipientName?: string;
    recipientPhone?: string;
    shippingNote?: string;
    completedQuantity?: number;
    progressPercent?: number;
    internalDeadline?: string;
    inputRequired?: number;
    remainingQuantity?: number;
    outputTarget?: number;
    unit?: string;
    status: string;
    deadline?: string;
    createdAt: string;
    updatedAt?: string;
    contactPhoneAlt?: string;
    deliveryAddress?: string;
    preferredDeliveryFrom?: string;
    preferredDeliveryTo?: string;
    deliveryFailureAction?: string;
    deliveryNote?: string;
    cancelRequested?: boolean;
    buyerViewed?: boolean;
    sellerViewed?: boolean;
}

export interface ProductionBatch {
    id: string;
    teamId?: string;
    order?: ProductionOrder;
    batchCode: string;
    name: string;
    plannedQuantity?: number;
    actualQuantity?: number;
    unit?: string;
    status: string;
    startTime?: string;
    dueTime?: string;
    createdAt: string;
    updatedAt?: string;
}

// === Chat ===
export interface ChatMsg {
    id: string;
    teamId: string;
    senderId: string;
    senderName: string;
    recipientId?: string;
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

```
