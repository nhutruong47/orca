# Knowledge Document: OrderManagementPage.tsx (Chunk 17/23)

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
  "chunk_index": 16,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
'0.85rem', color: 'var(--text-secondary)', marginTop: '4px' }}>
                                                    {order.description}
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                    <td style={{ padding: '12px' }}>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                            <span className="group-icon" style={{ fontSize: '1rem', padding: '4px' }}><ion-icon name="business-outline" style={{ fontSize: '16px' }}></ion-icon></span>
                                            {activeTab === 'outbound' ? order.sellerTeamName : (order.buyerTeamName || order.buyerUserName || 'Khách thuê gia công')}
                                        </div>
                                    </td>
                                    {activeTab === 'inbound' && (
                                        <td style={{ padding: '12px', textAlign: 'center' }}>
                                            <span className={`status-badge ${(order.buyerTrustScore ?? 100) >= 80 ? 'status-completed' : (order.buyerTrustScore ?? 100) >= 50 ? 'status-pending' : 'status-rejected'}`}>
                                                {(order.buyerTrustScore ?? 100) >= 80 ? 'Tốt' : (order.buyerTrustScore ?? 100) >= 50 ? 'TB' : 'Yếu'} {order.buyerTrustScore ?? 100}%
                                            </span>
                                        </td>
                                    )}
                                    <td style={{ padding: '12px', textAlign: 'center', fontWeight: 'bold' }}>
                                        {order.quantity}
                                    </td>
                                    <td style={{ padding: '12px', color: 'var(--text-secondary)' }}>
                                        {new Date(order.deadline).toLocaleDateString('vi-VN')}
                                    </td>
                                    <td style={{ padding: '12px' }}>
                                        {getStatusBadge(order)}
                                    </td>
                                    <td style={{ padding: '12px', textAlign: 'right' }}>

```
