# Knowledge Document: OrderManagementPage.tsx (Chunk 3/23)

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
  "chunk_index": 2,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
              const outb = (selectedTeam === PERSONAL_BUYER || selectedTeam === '')
                    ? await interGroupOrderService.getMyOutboundOrders()
                    : await interGroupOrderService.getOutboundOrders(selectedTeam);
                setUnreadOutboundCount(outb.filter(o => o.buyerViewed === false).length);
            } catch (err) {}
        };
        fetchUnreadCounts();
    }, [selectedTeam, orders, user]);

    const handleAccept = async (orderId: string) => {
        if (!confirm('Chấp nhận đơn hàng này? Một mục tiêu (Goal) mới sẽ được tạo tự động trong xưởng của bạn.')) return;
        try {
            await interGroupOrderService.acceptOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, status: 'ACCEPTED' } : o));
            alert('Đã chấp nhận đơn hàng và tạo Mục tiêu thành công!');
        } catch (err: any) {
            console.error(err);
            alert('Có lỗi xảy ra khi chấp nhận đơn: ' + (err.response?.data?.error || err.message));
        }
    };

    const handleReject = async (orderId: string) => {
        if (!confirm('Từ chối đơn hàng này?')) return;
        try {
            await interGroupOrderService.rejectOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, status: 'REJECTED' } : o));
        } catch (err) {
            alert('Có lỗi xảy ra khi từ chối đơn.');
            console.error(err);
        }
    };

    const handleCancel = async (orderId: string) => {
        if (!confirm('Hủy đơn hàng này? Điều này sẽ ảnh hưởng đến độ uy tín của bạn.')) return;
        try {
            await interGroupOrderService.cancelOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, status: 'CANCELED' } : o));
        } catch (err) {
            alert('Có lỗi xảy ra khi hủy đơn.');
            console.error(err);
        }
    };

    const handleShip = async (orderId: string) => {
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

```
