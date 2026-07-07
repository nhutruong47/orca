# Knowledge Document: GroupDetailPage.tsx (Chunk 53/136)

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
  "chunk_index": 52,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
0 ? (
                            <tr><td colSpan={5} style={{ textAlign: 'center', padding: 40, color: '#94a3b8', fontSize: 13 }}>Kho hàng trống</td></tr>
                        ) : inventoryItems.map(item => {
                            const isUpdating = updatingInvId === item.id;
                            let statusColor = '#16a34a'; let statusBg = '#dcfce7'; let statusLabel = 'Còn hàng';
                            if (item.status === 'OUT_OF_STOCK') { statusColor = '#dc2626'; statusBg = '#fee2e2'; statusLabel = 'Hết hàng'; }
                            else if (item.status === 'LOW_STOCK') { statusColor = '#d97706'; statusBg = '#fef3c7'; statusLabel = 'Sắp hết'; }

                            return (
                                <tr key={item.id} style={{ borderBottom: '1px solid #f1f5f9' }}>
                                    <td style={{ padding: '12px 16px' }}>
                                        <div style={{ fontWeight: 600, fontSize: 14, color: '#1e293b' }}>{item.name}</div>
                                        <div style={{ fontSize: 11, color: '#94a3b8', marginTop: 2 }}>Mức báo hết: &lt;= {item.lowStockThreshold} {item.unit}</div>
                                    </td>
                                    <td style={{ padding: '12px 16px' }}>
                                        <span style={{ background: statusBg, color: statusColor, padding: '4px 10px', borderRadius: 8, fontSize: 11, fontWeight: 700, display: 'inline-flex', alignItems: 'center', gap: 4 }}>
                                            <div style={{ width: 6, height: 6, borderRadius: '50%', background: statusColor }}></div> {statusLabel}
                                        </span>
                                    </td>
                                    <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 30px', gap: 6, alignItems: 'baseline', width: '100%', maxWidth: 120, margin: '0 auto' }}>
                                            <div style={{ textAlign: 'right', fontWeight: 700, fontSize: 15, color: '#3b82f6', letterSpacing: '0.5px' }}>
                                                {Number(item.quantity).toLocaleString('vi-VN')}
                                            </div>

```
