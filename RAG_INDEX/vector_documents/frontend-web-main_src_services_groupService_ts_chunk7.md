# Knowledge Document: groupService.ts (Chunk 8/8)

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
  "chunk_index": 7,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts
tions/read-all').then(r => r.data),
};

// === Inventory Service ===
import type { InventoryItem } from '../types/types';

export const inventoryService = {
    getByTeam: (teamId: string) =>
        api.get<InventoryItem[]>(`/api/inventory?teamId=${teamId}`).then(r => r.data),
    create: (data: Partial<InventoryItem>) =>
        api.post<InventoryItem>('/api/inventory', data).then(r => r.data),
    updateQuantity: (id: string, quantity: number) =>
        api.patch<InventoryItem>(`/api/inventory/${id}/quantity`, { quantity }).then(r => r.data),
    delete: (id: string) =>
        api.delete(`/api/inventory/${id}`).then(r => r.data),
    getFeaturedProducts: () =>
        api.get<InventoryItem[]>('/api/inventory/featured').then(r => r.data),
};

```
