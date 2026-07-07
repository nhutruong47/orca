# Knowledge Document: MarketplacePage.tsx (Chunk 26/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 25,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
er'}}>Hủy</button>
                                        <button onClick={() => handleUpdateReview(factory.id, review.id)} style={{padding: '8px 12px', borderRadius: 8, border: 'none', background: '#10b981', color: '#fff', fontWeight: 700, cursor: 'pointer'}}>Lưu đánh giá</button>
                                    </div>
                                </div>
                            ) : (
                                <>
                                    <div style={{display: 'flex', justifyContent: 'space-between', gap: 12, flexWrap: 'wrap'}}>
                                        <div>
                                            <strong style={{color: '#ece8e1'}}>{review.buyerTeamName || review.buyerUserName || 'Người đặt hàng'}</strong>
                                            <div style={{fontSize: 12, color: '#a79d94', marginTop: 4}}>
                                                {deliveryResultLabel(review.deliveryResult)} - {new Date(review.createdAt).toLocaleDateString('vi-VN')}
                                            </div>
                                        </div>
                                        <div style={{color: '#f59e0b', letterSpacing: 1}}>{'★'.repeat(review.rating)}{'☆'.repeat(5 - review.rating)}</div>
                                    </div>
                                    {review.comment && <p style={{margin: '12px 0 0', color: '#cfc7bf', lineHeight: 1.6}}>{review.comment}</p>}
                                    {canManageReview(review) && (
                                        <div style={{display: 'flex', gap: 8, marginTop: 12}}>
                                            <button onClick={() => startEditReview(review)} style={{padding: '6px 10px', borderRadius: 8, border: '1px solid rgba(245,158,11,0.35)', background: 'rgba(245,158,11,0.08)', color: '#fbbf24', cursor: 'pointer'}}>Sửa</button>
                                            <button onClick={() => handleDeleteReview(factory.id, review.id)} style={{padding: '6px 10px', borderRadius: 8, border: '1px solid rgba(239,68,68,0.35)', background: 'rgba(239,68,68,0.08)', color: '#fca5a5', cursor: 'pointer'}}>Xóa</button>
                                        </div>
                                    )}
                                </>
                            )}
                        </div>
                    ))}

```
