# Knowledge Document: interGroupOrderService.ts (Chunk 1/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/services/interGroupOrderService.ts",
  "language": "ts",
  "module": "services",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```ts
import api from './api';
import type { InterGroupOrder, Review, ReviewSummary } from '../types/types';

export const interGroupOrderService = {
    getOutboundOrders: (buyerTeamId: string) =>
        api.get<InterGroupOrder[]>(`/api/inter-group-orders/outbound/${buyerTeamId}`).then(r => r.data),

    getMyOutboundOrders: () =>
        api.get<InterGroupOrder[]>('/api/inter-group-orders/outbound-personal').then(r => r.data),

    getInboundOrders: (sellerTeamId: string) =>
        api.get<InterGroupOrder[]>(`/api/inter-group-orders/inbound/${sellerTeamId}`).then(r => r.data),

    getOrder: (orderId: string) =>
        api.get<InterGroupOrder>(`/api/inter-group-orders/${orderId}`).then(r => r.data),

    placeOrder: (data: Partial<InterGroupOrder>) =>
        api.post<InterGroupOrder>('/api/inter-group-orders', data).then(r => r.data),

    acceptOrder: (orderId: string) =>
        api.post<InterGroupOrder>(`/api/inter-group-orders/${orderId}/accept`).then(r => r.data),

    rejectOrder: (orderId: string) =>
        api.post<InterGroupOrder>(`/api/inter-group-orders/${orderId}/reject`).then(r => r.data),

    cancelOrder: (orderId: string) =>
        api.post<InterGroupOrder>(`/api/inter-group-orders/${orderId}/cancel`).then(r => r.data),

    approveCancelOrder: (orderId: string) =>
        api.post<InterGroupOrder>(`/api/inter-group-orders/${orderId}/approve-cancel`).then(r => r.data),

    rejectCancelOrder: (orderId: string) =>
        api.post<InterGroupOrder>(`/api/inter-group-orders/${orderId}/reject-cancel`).then(r => r.data),

    shipOrder: (orderId: string) =>
        api.patch<InterGroupOrder>(`/api/inter-group-orders/${orderId}/ship`).then(r => r.data),

    deliverOrder: (orderId: string, payload?: { deliveryNote?: string }) =>
        api.patch<InterGroupOrder>(`/api/inter-group-orders/${orderId}/deliver`, payload).then(r => r.data),

    /** Người mua xác nhận đã nhận hàng + đánh giá sao */
    buyerConfirmDelivery: (orderId: string, payload: {
        deliveryStatus: 'ON_TIME' | 'LATE' | 'NOT_DELIVERED';
        rating: number;
        comment: string;
    }) =>
        api.post<InterGroupOrder>(`/api/inter-group-orders/${orderId}/buyer-confirm`, payload).then(r => r.data),

    markViewed: (orderIds: string[], role: 'BUYER' | 'SELLER') =>
        api.post('/api/inter-group-orders/mark-viewed', { orderIds, role }).then(r => r.data),
};


```
