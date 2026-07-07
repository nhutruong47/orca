# Knowledge Document: GroupDetailPage.tsx (Chunk 15/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 14,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
 // Cập nhật state ui cho team member
            setTeam(prev => {
                if (!prev) return prev;
                return {
                    ...prev,
                    members: prev.members?.map(m => m.userId === selectedMemberForLabels.userId ? { ...m, jobLabels: updatedLabels } : m)
                };
            });
            setShowLabelModal(false);
        } catch (e: any) {
            alert(e?.response?.data?.error || 'Lỗi khi lưu nhãn dán');
        } finally {
            setLoading(false);
        }
    };

    const handleAddInventory = async () => {
        if (!id || !invName.trim() || !invQty) return;
        setLoading(true);
        try {
            await inventoryService.create({
                teamId: id,
                name: invName,
                quantity: Number(invQty.replace(/\./g, '')),
                unit: invUnit || 'Cái',
                lowStockThreshold: Number(invThreshold) || 10
            });
            const items = await inventoryService.getByTeam(id);
            setanys(items);
            setInvName(''); setInvQty(''); setInvUnit(''); setInvThreshold(''); setShowAddInventory(false);
        } catch (e: any) { alert(e?.response?.data?.error || 'Lỗi thêm hàng'); } finally { setLoading(false); }
    };

    const handleUpdateInvQty = async (invId: string) => {
        if (!id || !updateInvQty) return;
        setLoading(true);
        try {
            await inventoryService.updateQuantity(invId, Number(updateInvQty.replace(/\./g, '')));
            const items = await inventoryService.getByTeam(id);
            setanys(items);
            setUpdatingInvId(null); setUpdateInvQty('');
        } catch (e: any) { alert(e?.response?.data?.error || 'Lỗi cập nhật số lượng'); } finally { setLoading(false); }
    };

    const handleDeleteInventory = async (invId: string) => {
        if (!confirm('Xóa mặt hàng này khỏi kho?')) return;
        try {
            await inventoryService.delete(invId);
            const items = await inventoryService.getByTeam(id!);
            setanys(items);
        } catch (e: any) { alert(e?.response?.data?.error || 'Lỗi xóa hàng'); }
    };

    if (!team) return (
        <div className="page-container" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 300 }}>
            <div style={{ textAlign: 'center', opacity: 0.5 }}>

```
