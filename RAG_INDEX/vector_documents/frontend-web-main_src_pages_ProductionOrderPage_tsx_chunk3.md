# Knowledge Document: ProductionOrderPage.tsx (Chunk 4/19)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionOrderPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
veryDate: customerDeliveryDateRef,
        };
        window.setTimeout(() => {
            refs[field]?.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
            refs[field]?.current?.focus({ preventScroll: true });
        }, 0);
    };

    const setFieldErrorAndFocus = (field: string, message: string) => {
        setFieldErrors({ [field]: message });
        setError('');
        focusField(field);
    };

    const isSameOrBefore = (value: string, compareTo: string) => {
        return new Date(`${value}T00:00:00`).getTime() <= new Date(`${compareTo}T00:00:00`).getTime();
    };

    const calculateInput = () => {
        const target = parseFloat(form.outputTarget as any) || 0;
        const yield_ = parseFloat(form.expectedYield as any) || 1;
        if (target > 0 && yield_ > 0) {
            return Math.ceil((target / yield_) * 100) / 100;
        }
        return 0;
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setFieldErrors({});
        setSaving(true);
        try {
            const payload: any = { ...form };
            if (!payload.productionStartDate) payload.productionStartDate = undefined;
            if (!payload.confirmDate) payload.confirmDate = undefined;
            if (!payload.customerDeliveryDate) {
                setFieldErrorAndFocus('customerDeliveryDate', 'Vui lòng chọn ngày giao hàng cho khách.');
                setSaving(false);
                return;
            }
            if (payload.productionStartDate && isSameOrBefore(payload.customerDeliveryDate, payload.productionStartDate)) {
                setFieldErrorAndFocus('customerDeliveryDate', 'Ngày giao hàng phải sau ngày bắt đầu sản xuất.');
                setSaving(false);
                return;
            }
            if (editingOrderId) {
                await productionService.updateOrder(editingOrderId, payload);
            } else {
                await productionService.createOrder(teamId, payload);
            }
            setEditingOrderId(null);
            setForm(createDefaultForm());
            setActiveTab('list');
            loadOrders();
        } catch (e: any) {
            const message = e.response?.data?.error || e.message || 'Loi luu don hang';

```
