# Knowledge Document: groupService.ts (Chunk 7/8)

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
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts
 string | null;
    suggestedReason?: string | null;
}

export interface AiV2PlanDraft {
    goalTitle: string;
    outputTarget: string;
    deadline?: string | null;
    priority: number;
    tasks: AiV2TaskDraft[];
}

export const aiWorkflowService = {
    extract: (teamId: string, text: string) =>
        api.post<AiV2ExtractResponse>('/api/ai/v2/extract', { teamId, text }).then(r => r.data),
    plan: (teamId: string, intent: AiV2ExtractResponse['intent'], fields: Record<string, any>) =>
        api.post<AiV2PlanDraft>('/api/ai/v2/plan', { teamId, intent, fields }).then(r => r.data),
    revise: (teamId: string, instruction: string, draft: AiV2PlanDraft) =>
        api.post<AiV2PlanDraft>('/api/ai/v2/revise', { teamId, instruction, draft }).then(r => r.data),
};

// === Chat Service ===
import type { ChatMsg } from '../types/types';

export const chatService = {
    getGroupMessages: (teamId: string) =>
        api.get<ChatMsg[]>(`/api/teams/${teamId}/chat`).then(r => r.data),
    getDirectMessages: (teamId: string, userId: string) =>
        api.get<ChatMsg[]>(`/api/teams/${teamId}/chat/dm/${userId}`).then(r => r.data),
    getDmPreviews: (teamId: string) =>
        api.get<ChatMsg[]>(`/api/teams/${teamId}/chat/dm-previews`).then(r => r.data),
    sendMessage: (teamId: string, content: string, recipientId?: string) =>
        api.post<ChatMsg>(`/api/teams/${teamId}/chat`, { content, recipientId }).then(r => r.data),
    getOnlineUsers: () =>
        api.get<string[]>('/api/presence/online').then(r => r.data),
};

// === Notification Service ===
export const notificationService = {
    getAll: () =>
        api.get<AppNotification[]>('/api/notifications').then(r => r.data),
    getUnreadCount: () =>
        api.get<{ count: number }>('/api/notifications/unread-count').then(r => r.data),
    markAsRead: (id: string) =>
        api.patch(`/api/notifications/${id}/read`).then(r => r.data),
    markAllRead: () =>
        api.patch('/api/notifications/read-all').then(r => r.data),
};

// === Inventory Service ===
import type { InventoryItem } from '../types/types';

export const inventoryService = {
    getByTeam: (teamId: string) =>
        api.get<InventoryItem[]>(`/api/inventory?teamId=${teamId}`).then(r => r.data),
    create: (data: Partial<InventoryItem>) =>
        api.post<InventoryItem>('/api/inventory', data).then(r => r.data),

```
