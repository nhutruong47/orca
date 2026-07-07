# Knowledge Document: OrderManagementPage.tsx (Chunk 16/23)

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
  "chunk_index": 15,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
 className="goals-table" style={{ width: '100%', borderCollapse: 'collapse' }}>
                        <thead>
                            <tr>
                                <th style={{ textAlign: 'left', padding: '12px' }}>Đơn hàng</th>
                                <th style={{ textAlign: 'left', padding: '12px' }}>{activeTab === 'outbound' ? 'Nhà cung cấp (Bán)' : 'Người đặt (Mua)'}</th>
                                {activeTab === 'inbound' && <th style={{ textAlign: 'center', padding: '12px' }}>Uy tín</th>}
                                <th style={{ textAlign: 'center', padding: '12px' }}>Số lượng</th>
                                <th style={{ textAlign: 'left', padding: '12px' }}>Hạn chót</th>
                                <th style={{ textAlign: 'left', padding: '12px' }}>Trạng thái</th>
                                <th style={{ textAlign: 'right', padding: '12px' }}>Thao tác</th>
                            </tr>
                        </thead>
                        <tbody>
                            {orders.map(order => (
                                <>
                                <tr key={order.id} style={{ borderBottom: expandedOrderId === order.id ? 'none' : '1px solid var(--border-color)', cursor: 'pointer' }} onClick={() => setExpandedOrderId(expandedOrderId === order.id ? null : order.id)}>
                                    <td style={{ padding: '12px' }}>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                            <ion-icon name={expandedOrderId === order.id ? 'chevron-down-outline' : 'chevron-forward-outline'} style={{ fontSize: '14px', color: 'var(--text-secondary)', flexShrink: 0 }}></ion-icon>
                                            <div>
                                                <strong>{order.title}</strong>
                                                <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '4px' }}>
                                                    {order.description}
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                    <td style={{ padding: '12px' }}>

```
