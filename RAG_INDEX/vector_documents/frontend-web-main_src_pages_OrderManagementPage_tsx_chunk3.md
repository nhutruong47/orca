# Knowledge Document: OrderManagementPage.tsx (Chunk 4/23)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/OrderManagementPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
     if (!confirm('Xác nhận bắt đầu giao đơn hàng này?')) return;
        try {
            await interGroupOrderService.shipOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, status: 'SHIPPING' } : o));
        } catch (err) {
            alert('Có lỗi xảy ra.');
            console.error(err);
        }
    };

    const handleDeliver = async (orderId: string) => {
        if (!confirm('Xác nhận đã giao đơn hàng này đến nơi?')) return;
        try {
            await interGroupOrderService.deliverOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, status: 'DELIVERED' } : o));
        } catch (err) {
            alert('Có lỗi xảy ra.');
            console.error(err);
        }
    };

    const handleConfirmDelivery = async (orderId: string) => {
        if (!confirm('Xác nhận đã nhận hàng thành công?')) return;
        try {
            await interGroupOrderService.buyerConfirmDelivery(orderId, {
                deliveryStatus: 'ON_TIME',
                rating: 5,
                comment: 'Đã nhận hàng'
            });
            setOrders(orders.map(o => o.id === orderId ? { ...o, status: 'COMPLETED' } : o));
        } catch (err) {
            alert('Có lỗi xảy ra.');
            console.error(err);
        }
    };

    const handleApproveCancel = async (orderId: string) => {
        if (!confirm('Bạn có chắc chắn muốn đồng ý hủy đơn hàng này?')) return;
        try {
            await interGroupOrderService.approveCancelOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, status: 'CANCELED', cancelRequested: false, cancelledBy: 'BUYER' } : o));
        } catch (err) {
            alert('Có lỗi xảy ra.');
            console.error(err);
        }
    };

    const handleRejectCancel = async (orderId: string) => {
        if (!confirm('Từ chối yêu cầu hủy đơn này? Đơn hàng sẽ tiếp tục trạng thái bình thường.')) return;
        try {
            await interGroupOrderService.rejectCancelOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, cancelRequested: false } : o));
        } catch (err) {
            alert('Có lỗi xảy ra.');
            console.error(err);
        }
    };

    const handleManualOrderChange = (field: keyof typeof DEFAULT_MANUAL_ORDER_FORM, value: string | number) => {

```
