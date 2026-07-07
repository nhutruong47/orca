# Knowledge Document: OrderManagementPage.tsx (Chunk 5/23)

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
  "chunk_index": 4,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
    try {
            await interGroupOrderService.rejectCancelOrder(orderId);
            setOrders(orders.map(o => o.id === orderId ? { ...o, cancelRequested: false } : o));
        } catch (err) {
            alert('Có lỗi xảy ra.');
            console.error(err);
        }
    };

    const handleManualOrderChange = (field: keyof typeof DEFAULT_MANUAL_ORDER_FORM, value: string | number) => {
        setManualOrderForm(prev => ({ ...prev, [field]: value }));
    };

    const handleCreateManualInboundOrder = async (event: React.FormEvent) => {
        event.preventDefault();
        if (!selectedTeam || selectedTeam === PERSONAL_BUYER) {
            setManualCreateError('Vui lòng chọn xưởng nhận đơn trước khi tạo.');
            return;
        }
        if (!manualOrderForm.title.trim()) {
            setManualCreateError('Vui lòng nhập tên đơn hàng.');
            return;
        }
        if (!manualOrderForm.customerName.trim()) {
            setManualCreateError('Vui lòng nhập tên khách/xưởng đặt.');
            return;
        }

        setManualCreateLoading(true);
        setManualCreateError('');
        try {
            const descriptionParts = [
                manualOrderForm.description.trim(),
                manualOrderForm.customerName.trim() ? `Khách/xưởng đặt: ${manualOrderForm.customerName.trim()}` : '',
                manualOrderForm.deliveryNote.trim() ? `Ghi chú: ${manualOrderForm.deliveryNote.trim()}` : '',
            ].filter(Boolean);

            const created = await interGroupOrderService.placeOrder({
                sellerTeamId: selectedTeam,
                title: manualOrderForm.title.trim(),
                description: descriptionParts.join('\n'),
                quantity: Number(manualOrderForm.quantity) || 1,
                deadline: manualOrderForm.deadline,
                contactPhone: manualOrderForm.contactPhone.trim() || undefined,
                deliveryAddress: manualOrderForm.deliveryAddress.trim() || undefined,
                deliveryNote: manualOrderForm.deliveryNote.trim() || undefined,
            });

            setOrders(prev => [created, ...prev]);
            setActiveTab('inbound');
            setShowManualOrderForm(false);
            setManualOrderForm(DEFAULT_MANUAL_ORDER_FORM);
        } catch (err: any) {

```
