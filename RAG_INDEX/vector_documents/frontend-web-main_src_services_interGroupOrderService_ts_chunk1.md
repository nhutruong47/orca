# Knowledge Document: interGroupOrderService.ts (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/services/interGroupOrderService.ts",
  "language": "ts",
  "module": "services",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```ts
       deliveryStatus: 'ON_TIME' | 'LATE' | 'NOT_DELIVERED';
        rating: number;
        comment: string;
    }) =>
        api.post<InterGroupOrder>(`/api/inter-group-orders/${orderId}/buyer-confirm`, payload).then(r => r.data),

    markViewed: (orderIds: string[], role: 'BUYER' | 'SELLER') =>
        api.post('/api/inter-group-orders/mark-viewed', { orderIds, role }).then(r => r.data),
};

export const reviewService = {
    getByTeam: (teamId: string) =>
        api.get<Review[]>(`/api/reviews/team/${teamId}`).then(r => r.data),

    getSummary: (teamId: string) =>
        api.get<ReviewSummary>(`/api/reviews/team/${teamId}/summary`).then(r => r.data),

    update: (reviewId: string, payload: {
        rating: number;
        comment: string;
        deliveryResult: 'ON_TIME' | 'LATE' | 'NOT_DELIVERED';
    }) =>
        api.put<Review>(`/api/reviews/${reviewId}`, payload).then(r => r.data),

    remove: (reviewId: string) =>
        api.delete(`/api/reviews/${reviewId}`).then(r => r.data),
};

export const manufacturingRequestService = {
    getAll: () =>
        api.get<any[]>('/api/manufacturing-requests').then(r => r.data),
    create: (data: any) =>
        api.post<any>('/api/manufacturing-requests', data).then(r => r.data),
};

```
