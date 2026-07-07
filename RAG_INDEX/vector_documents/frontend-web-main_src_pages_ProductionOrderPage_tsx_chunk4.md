# Knowledge Document: ProductionOrderPage.tsx (Chunk 5/19)

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
  "chunk_index": 4,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
ce.updateOrder(editingOrderId, payload);
            } else {
                await productionService.createOrder(teamId, payload);
            }
            setEditingOrderId(null);
            setForm(createDefaultForm());
            setActiveTab('list');
            loadOrders();
        } catch (e: any) {
            const message = e.response?.data?.error || e.message || 'Loi luu don hang';
            if (message.toLowerCase().includes('ngay giao') || message.toLowerCase().includes('delivery')) {
                setFieldErrorAndFocus('customerDeliveryDate', message);
            } else {
                setError(message);
            }
        } finally {
            setSaving(false);
        }
    };

    const handleDelete = async (order: ProductionOrder) => {
        if (!confirm(`Xoa don san xuat "${order.title}"? Hanh dong nay se xoa ke hoach san xuat lien quan neu co.`)) return;
        setSaving(true);
        try {
            await productionService.deleteOrder(order.id);
            if (editingOrderId === order.id) {
                cancelForm();
            }
            await loadOrders();
        } catch (e: any) {
            setError(e.response?.data?.error || e.message || 'Loi xoa don hang');
        } finally {
            setSaving(false);
        }
    };

    const getStatusColor = (status: string) =>
        STATUS_OPTIONS.find(s => s.value === status)?.color || '#94a3b8';

    const getStatusLabel = (status: string) =>
        STATUS_OPTIONS.find(s => s.value === status)?.label || status;

    const inputRequired = calculateInput();

    return (
        <div style={{ padding: 24, margin: '0 auto' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                    <button onClick={() => navigate(`/groups/${teamId}`)} style={{
                        background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                        width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                        color: 'var(--text-secondary)', fontSize: 18, flexShrink: 0
                    }} title="Quay lại nhóm">
                        <ion-icon name="chevron-back-outline" />

```
