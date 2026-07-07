# Knowledge Document: MarketplacePage.tsx (Chunk 18/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 17,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
eryFrom('');
        setDeliveryTo('');
        setDeliveryFailureAction('RETRY_LATER');
        setDeliveryNote('');
        setShowOrderModal(true);
    };

    const handleSubmitOrder = async (event: React.FormEvent) => {
        event.preventDefault();
        if (!rfqTitle.trim() || !rfqProductName.trim()) return;
        if (rfqQuantity <= 0) {
            alert('Số lượng phải lớn hơn 0.');
            return;
        }
        if (rfqDeadline && new Date(rfqDeadline) <= new Date()) {
            alert('Deadline mong muốn phải là ngày trong tương lai.');
            return;
        }

        try {
            setSubmitting(true);
            const detailLines = [
                `Dịch vụ yêu cầu: ${rfqRequestType}`,
                `Loại sản phẩm: ${rfqProductName}`,
                `Số lượng: ${rfqQuantity} ${rfqUnit}`,
                rfqQuality ? `Mức rang: ${rfqQuality}` : '',
                rfqPackaging ? `Quy cách đóng gói: ${rfqPackaging}` : '',
                rfqBudget ? `Ngân sách dự kiến: ${rfqBudget}` : '',
                rfqNote ? `Ghi chú: ${rfqNote}` : '',
            ].filter(Boolean).join('\n');

            setShowOrderModal(false);
            setShowAiMatching(true);
            setAiMatchingProgress(0);

            const interval = setInterval(() => {
                setAiMatchingProgress(prev => {
                    if (prev >= 100) {
                        clearInterval(interval);
                        return 100;
                    }
                    return prev + 15;
                });
            }, 300);

            setTimeout(async () => {
                try {
                    if (selectedSeller) {
                        const dto: Partial<InterGroupOrder> = {
                            ...(buyerTeamId ? { buyerTeamId } : {}),
                            sellerTeamId: selectedSeller.id,
                            title: rfqTitle,
                            description: detailLines,
                            quantity: rfqQuantity,
                            deadline: rfqDeadline,
                            contactPhone: deliveryPhone || undefined,
                            contactPhoneAlt: deliveryPhoneAlt || undefined,
                            deliveryAddress: deliveryAddress || undefined,
                            preferredDeliveryFrom: deliveryFrom || undefined,

```
