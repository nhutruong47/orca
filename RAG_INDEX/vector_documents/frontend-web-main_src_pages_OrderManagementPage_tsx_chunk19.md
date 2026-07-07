# Knowledge Document: OrderManagementPage.tsx (Chunk 20/23)

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
  "chunk_index": 19,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                                      <button className="btn btn-primary" style={{ padding: '4px 8px', fontSize: '0.8rem', background: '#d32f2f' }} onClick={() => handleApproveCancel(order.id)}>Đồng ý hủy</button>
                                                </>
                                            )}
                                            {/* Both: Cancel (PENDING or ACCEPTED) */}
                                            {(order.status === 'PENDING' || order.status === 'RFQ_CREATED' || order.status === 'ACCEPTED' || order.status === 'CONFIRMED') && !order.cancelRequested && (
                                                <button className="btn btn-secondary" onClick={() => handleCancel(order.id)} style={{ padding: '4px 8px', fontSize: '0.8rem' }}><ion-icon name="ban-outline" style={{ fontSize: '13px', verticalAlign: 'middle', marginRight: 2 }}></ion-icon> {activeTab === 'outbound' ? 'Hủy / Xin hủy' : 'Hủy'}</button>
                                            )}
                                            {/* Show canceller */}
                                            {order.status === 'CANCELED' && order.cancelledBy && (
                                                <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Bởi: {order.cancelledBy === 'BUYER' ? 'Bên mua' : 'Bên bán'}</span>
                                            )}
                                        </div>
                                    </td>
                                </tr>
                                {/* Expandable delivery detail row */}
                                {expandedOrderId === order.id && (
                                    <tr key={`${order.id}-detail`} style={{ borderBottom: '1px solid var(--border-color)' }}>
                                        <td colSpan={activeTab === 'inbound' ? 7 : 6} style={{ padding: '0 12px 16px 40px' }}>
                                            <div style={{
                                                background: 'rgba(255,255,255,0.03)',
                                                border: '1px solid var(--border-color)',
                                                borderRadius: 8,
                                                padding: '16px 20px',
                                                marginTop: 4,
                                            }}>

```
