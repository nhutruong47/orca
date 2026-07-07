# Knowledge Document: OrderManagementPage.tsx (Chunk 19/23)

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
  "chunk_index": 18,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
 }}><ion-icon name="car-outline" style={{ fontSize: '13px', verticalAlign: 'middle', marginRight: 2 }}></ion-icon> Giao hàng</button>
                                            )}
                                            {/* Inbound SHIPPING: Mark as Delivered */}
                                            {activeTab === 'inbound' && order.status === 'SHIPPING' && !order.cancelRequested && (
                                                <button className="btn btn-primary" onClick={() => handleDeliver(order.id)} style={{ padding: '4px 8px', fontSize: '0.8rem' }}><ion-icon name="cube-outline" style={{ fontSize: '13px', verticalAlign: 'middle', marginRight: 2 }}></ion-icon> Đã giao hàng</button>
                                            )}
                                            {/* Outbound DELIVERED: Confirm Delivery */}
                                            {activeTab === 'outbound' && order.status === 'DELIVERED' && !order.cancelRequested && (
                                                <button className="btn btn-primary" onClick={() => handleConfirmDelivery(order.id)} style={{ padding: '4px 8px', fontSize: '0.8rem' }}><ion-icon name="checkmark-done-outline" style={{ fontSize: '13px', verticalAlign: 'middle', marginRight: 2 }}></ion-icon> Xác nhận đã nhận hàng</button>
                                            )}
                                            {/* Inbound CANCEL_REQUESTED: Approve/Reject Cancel */}
                                            {activeTab === 'inbound' && order.cancelRequested && (
                                                <>
                                                    <button className="btn btn-secondary" onClick={() => handleRejectCancel(order.id)} style={{ padding: '4px 8px', fontSize: '0.8rem' }}>Từ chối hủy</button>
                                                    <button className="btn btn-primary" style={{ padding: '4px 8px', fontSize: '0.8rem', background: '#d32f2f' }} onClick={() => handleApproveCancel(order.id)}>Đồng ý hủy</button>
                                                </>
                                            )}
                                            {/* Both: Cancel (PENDING or ACCEPTED) */}

```
