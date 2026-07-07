# Knowledge Document: MarketplacePage.tsx (Chunk 25/70)

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
  "chunk_index": 24,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.06)', borderRadius: 10}}>
                            {editingReviewId === review.id ? (
                                <div style={{display: 'flex', flexDirection: 'column', gap: 12}}>
                                    <div style={{display: 'flex', gap: 6}}>
                                        {[1, 2, 3, 4, 5].map(star => (
                                            <button key={star} onClick={() => setEditReviewRating(star)} style={{background: 'transparent', border: 'none', color: star <= editReviewRating ? '#f59e0b' : '#6b7280', fontSize: 24, cursor: 'pointer'}}>★</button>
                                        ))}
                                    </div>
                                    <select value={editReviewStatus} onChange={event => setEditReviewStatus(event.target.value as typeof editReviewStatus)} style={{padding: '10px 12px', borderRadius: 8, border: '1px solid var(--border)', background: 'var(--bg-input)', color: 'var(--text-primary)'}}>
                                        <option value="ON_TIME">Giao đúng hẹn</option>
                                        <option value="LATE">Giao trễ</option>
                                        <option value="NOT_DELIVERED">Chưa nhận hàng</option>
                                    </select>
                                    <textarea value={editReviewComment} onChange={event => setEditReviewComment(event.target.value)} rows={3} style={{padding: '10px 12px', borderRadius: 8, border: '1px solid var(--border)', background: 'var(--bg-input)', color: 'var(--text-primary)', resize: 'vertical'}} />
                                    <div style={{display: 'flex', gap: 8, justifyContent: 'flex-end'}}>
                                        <button onClick={cancelEditReview} style={{padding: '8px 12px', borderRadius: 8, border: '1px solid var(--border)', background: 'transparent', color: 'var(--text-primary)', cursor: 'pointer'}}>Hủy</button>
                                        <button onClick={() => handleUpdateReview(factory.id, review.id)} style={{padding: '8px 12px', borderRadius: 8, border: 'none', background: '#10b981', color: '#fff', fontWeight: 700, cursor: 'pointer'}}>Lưu đánh giá</button>
                                    </div>
                                </div>
                            ) : (

```
