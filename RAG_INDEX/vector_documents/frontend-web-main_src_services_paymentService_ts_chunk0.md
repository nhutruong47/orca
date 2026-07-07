# Knowledge Document: paymentService.ts (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/services/paymentService.ts",
  "language": "ts",
  "module": "services",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```ts
import api from './api';

export interface CreateVnpayPaymentResponse {
    paymentUrl: string;
    txnRef: string;
    planId: string;
    planName: string;
    amount: number;
}

export interface MockTransferResponse {
    status: string;
    txnRef: string;
    planId: string;
    planName: string;
    amount: number;
    message: string;
    paymentMethod?: PaymentMethod;
}

export interface CreatePayosPaymentResponse {
    checkoutUrl: string;
    txnRef: string;
    planId: string;
    planName: string;
    amount: number;
}

export type PaymentMethod = 'MB_BANK' | 'VNPAY' | 'PAYOS';

export interface VirtualQrPaymentResponse {
    status: string;
    txnRef: string;
    planId: string;
    planName: string;
    amount: number;
    message: string;
    paymentMethod: PaymentMethod;
    paymentMethodName: string;
    qrPayload: string;
    qrCodeUrl?: string;
    deeplink?: string;
    payUrl?: string;
    expiresAt: string;
}

export const paymentService = {
    async createVnpayPayment(planId: string): Promise<CreateVnpayPaymentResponse> {
        const response = await api.post<CreateVnpayPaymentResponse>('/api/payments/vnpay/create', { planId });
        return response.data;
    },

    async createPayosPayment(planId: string): Promise<CreatePayosPaymentResponse> {
        const response = await api.post<CreatePayosPaymentResponse>('/api/payments/payos/create', { planId });
        return response.data;
    },

    async createMockTransfer(planId: string, method: PaymentMethod = 'VNPAY'): Promise<MockTransferResponse> {
        const response = await api.post<MockTransferResponse>('/api/payments/mock/transfer', { planId, method });
        return response.data;
    },

    async createVirtualQrPayment(planId: string, method: PaymentMethod): Promise<VirtualQrPaymentResponse> {
        const response = await api.post<VirtualQrPaymentResponse>('/api/payments/virtual-qr/create', { planId, method });
        return response.data;
    },

    async confirmVirtualQrPayment(txnRef: string): Promise<MockTransferResponse> {
        const response = await api.post<MockTransferResponse>('/api/payments/virtual-qr/confirm', { txnRef });
        return response.data;
    },
};

```
