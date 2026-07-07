# Knowledge Document: OrderManagementPage.tsx (Chunk 18/23)

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
  "chunk_index": 17,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                                       {new Date(order.deadline).toLocaleDateString('vi-VN')}
                                    </td>
                                    <td style={{ padding: '12px' }}>
                                        {getStatusBadge(order)}
                                    </td>
                                    <td style={{ padding: '12px', textAlign: 'right' }}>
                                        <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'wrap' }} onClick={e => e.stopPropagation()}>
                                            {/* Inbound PENDING: Accept/Reject */}
                                            {activeTab === 'inbound' && (order.status === 'PENDING' || order.status === 'RFQ_CREATED') && !order.cancelRequested && (
                                                <>
                                                    <button className="btn btn-secondary" onClick={() => handleReject(order.id)} style={{ padding: '4px 8px', fontSize: '0.8rem' }}>Từ chối</button>
                                                    <button className="btn btn-primary" onClick={() => handleAccept(order.id)} style={{ padding: '4px 8px', fontSize: '0.8rem' }}>Chấp nhận</button>
                                                </>
                                            )}
                                            {/* Inbound ACCEPTED: Mark as Shipping */}
                                            {activeTab === 'inbound' && (order.status === 'ACCEPTED' || order.status === 'CONFIRMED') && !order.cancelRequested && (
                                                <button className="btn btn-primary" onClick={() => handleShip(order.id)} style={{ padding: '4px 8px', fontSize: '0.8rem' }}><ion-icon name="car-outline" style={{ fontSize: '13px', verticalAlign: 'middle', marginRight: 2 }}></ion-icon> Giao hàng</button>
                                            )}
                                            {/* Inbound SHIPPING: Mark as Delivered */}
                                            {activeTab === 'inbound' && order.status === 'SHIPPING' && !order.cancelRequested && (

```
