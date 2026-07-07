# Knowledge Document: MarketplacePage.tsx (Chunk 24/70)

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
  "chunk_index": 23,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
'13px', color: '#a79d94'}}>{reviewCount} đánh giá</div>
                    </div>
                    <div style={{flex: 1, minWidth: 240}}>
                        {[5, 4, 3, 2, 1].map(star => {
                            const count = Number(starCounts[star as keyof typeof starCounts] || 0);
                            const pct = reviewCount > 0 ? Math.round((count / reviewCount) * 100) : 0;
                            return (
                                <div key={star} style={{display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '8px'}}>
                                    <span style={{fontSize: '12px', color: '#f59e0b', width: '44px'}}>{star} sao</span>
                                    <div style={{flex: 1, height: '8px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', overflow: 'hidden'}}>
                                        <div style={{height: '100%', background: '#f59e0b', width: `${pct}%`, transition: 'width 0.3s'}} />
                                    </div>
                                    <span style={{fontSize: '12px', color: '#a79d94', width: '56px', textAlign: 'right'}}>{count} ({pct}%)</span>
                                </div>
                            );
                        })}
                        <div style={{display: 'flex', gap: 16, marginTop: 10, flexWrap: 'wrap'}}>
                            <span style={{fontSize: 12, color: '#a79d94'}}>Đúng hẹn {Math.round(onTimeRate)}%</span>
                            <span style={{fontSize: 12, color: '#a79d94'}}>{completed} đơn hoàn thành</span>
                            <span style={{fontSize: 12, color: '#a79d94'}}>{late} đơn trễ</span>
                        </div>
                    </div>
                </div>

                <div style={{display: 'flex', flexDirection: 'column', gap: 12}}>
                    {reviews.map(review => (
                        <div key={review.id} style={{padding: 16, background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.06)', borderRadius: 10}}>
                            {editingReviewId === review.id ? (
                                <div style={{display: 'flex', flexDirection: 'column', gap: 12}}>
                                    <div style={{display: 'flex', gap: 6}}>
                                        {[1, 2, 3, 4, 5].map(star => (

```
