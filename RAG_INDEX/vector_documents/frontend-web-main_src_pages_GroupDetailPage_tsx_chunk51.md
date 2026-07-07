# Knowledge Document: GroupDetailPage.tsx (Chunk 52/136)

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
  "chunk_index": 51,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
amId={id!}
                />
            )}

            {/* ===== BẢNG KHO HÀNG (INVENTORY) ===== */}
            <div style={{ background: '#fff', borderRadius: 14, border: '1px solid #e2e8f0', overflow: 'hidden', marginBottom: 18 }}>
                <div style={{ padding: '16px 24px', borderBottom: '1px solid #e2e8f0', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h3 style={{ margin: 0, fontSize: 15, fontWeight: 700, color: '#1e293b' }}><ion-icon name="cube-outline" style={{ fontSize: 18, verticalAlign: 'middle', marginRight: 6, color: '#d4a574' }}></ion-icon> KHO HÀNG ({inventoryItems.length})</h3>
                    {isAdmin && (
                        <button onClick={() => setShowAddInventory(!showAddInventory)} style={{ background: '#d4a574', color: '#fff', border: 'none', borderRadius: 8, padding: '6px 14px', fontSize: 12, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}>
                            <ion-icon name="add"></ion-icon> Nhập kho
                        </button>
                    )}
                </div>



                {/* Table */}
                <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                    <thead>
                        <tr style={{ background: 'transparent' }}>
                            {['Tên mặt hàng', 'Tình trạng', 'Số lượng', 'Cập nhật', ''].map((h, i) => (
                                <th key={i} style={{ padding: '10px 16px', textAlign: h === 'Số lượng' ? 'center' : 'left', fontSize: 11, fontWeight: 700, color: h === 'Số lượng' ? '#d4a574' : '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.05em', borderBottom: '1px solid var(--border, #e2e8f0)' }}>{h}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {inventoryItems.length === 0 ? (
                            <tr><td colSpan={5} style={{ textAlign: 'center', padding: 40, color: '#94a3b8', fontSize: 13 }}>Kho hàng trống</td></tr>
                        ) : inventoryItems.map(item => {
                            const isUpdating = updatingInvId === item.id;
                            let statusColor = '#16a34a'; let statusBg = '#dcfce7'; let statusLabel = 'Còn hàng';

```
