# Knowledge Document: ProductionOrderPage.tsx (Chunk 3/19)

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
  "chunk_index": 2,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
));
    };

    const startCreate = () => {
        setEditingOrderId(null);
        setForm(createDefaultForm());
        setError('');
        setFieldErrors({});
        setActiveTab('create');
    };

    const startEdit = (order: ProductionOrder) => {
        setEditingOrderId(order.id);
        setForm({
            title: order.title || '',
            description: order.description || '',
            customerName: order.customerName || '',
            productType: order.productType || 'Robusta',
            processType: order.processType || 'Rang nguyen hat',
            roastLevel: order.roastLevel || 'Medium',
            packageSize: order.packageSize || '1kg',
            totalPackages: order.totalPackages || 0,
            outputTarget: order.outputTarget || 0,
            expectedYield: order.expectedYield || 0.85,
            expectedLoss: order.expectedLoss || 0,
            unit: order.unit || 'kg',
            orderDate: toDateInput(order.orderDate) || new Date().toISOString().split('T')[0],
            confirmDate: toDateInput(order.confirmDate),
            productionStartDate: toDateInput(order.productionStartDate) || new Date().toISOString().split('T')[0],
            customerDeliveryDate: toDateInput(order.customerDeliveryDate),
            safetyBufferDays: order.safetyBufferDays ?? 2,
            recipientName: order.recipientName || '',
            recipientPhone: order.recipientPhone || '',
            shippingNote: order.shippingNote || '',
        });
        setError('');
        setFieldErrors({});
        setActiveTab('create');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    const cancelForm = () => {
        setEditingOrderId(null);
        setForm(createDefaultForm());
        setError('');
        setFieldErrors({});
        setActiveTab('list');
    };

    const focusField = (field: string) => {
        const refs: Record<string, React.RefObject<HTMLInputElement | null>> = {
            customerDeliveryDate: customerDeliveryDateRef,
        };
        window.setTimeout(() => {
            refs[field]?.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
            refs[field]?.current?.focus({ preventScroll: true });
        }, 0);
    };

    const setFieldErrorAndFocus = (field: string, message: string) => {
        setFieldErrors({ [field]: message });
        setError('');

```
