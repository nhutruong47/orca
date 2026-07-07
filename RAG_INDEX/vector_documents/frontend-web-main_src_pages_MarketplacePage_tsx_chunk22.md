# Knowledge Document: MarketplacePage.tsx (Chunk 23/70)

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
  "chunk_index": 22,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
 starCounts = summary.starCounts || {};
        const reviews = factoryReviews[factory.id] || [];

        if (reviewsLoading && reviews.length === 0) {
            return (
                <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '16px'}}>
                    <div style={{ textAlign: 'center', padding: '40px 20px', color: 'var(--text-muted)' }}>
                        <div className="btn-spinner" style={{ margin: '0 auto 12px' }} />
                        <p>Đang tải đánh giá...</p>
                    </div>
                </div>
            );
        }

        if (reviewCount === 0) {
            return (
                <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '16px'}}>
                    <div style={{ textAlign: 'center', padding: '40px 20px', color: 'var(--text-muted)' }}>
                        <div style={{ fontSize: 40, marginBottom: 12 }}>Chưa có đánh giá</div>
                        <p>Chưa có đơn hàng nào được hoàn thành với xưởng này.</p>
                    </div>
                </div>
            );
        }

        return (
            <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '16px'}}>
                <div style={{display: 'flex', alignItems: 'stretch', gap: '24px', padding: '24px', background: 'rgba(255,255,255,0.03)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.05)', flexWrap: 'wrap'}}>
                    <div style={{textAlign: 'center', minWidth: 120}}>
                        <div style={{fontSize: '36px', fontWeight: 700, color: '#f59e0b'}}>{avgRating > 0 ? avgRating.toFixed(1) : '-'}</div>
                        <div style={{color: '#f59e0b', margin: '4px 0', letterSpacing: '2px'}}>{avgRating > 0 ? '★'.repeat(Math.round(avgRating)) + '☆'.repeat(5 - Math.round(avgRating)) : '-'}</div>
                        <div style={{fontSize: '13px', color: '#a79d94'}}>{reviewCount} đánh giá</div>
                    </div>
                    <div style={{flex: 1, minWidth: 240}}>
                        {[5, 4, 3, 2, 1].map(star => {
                            const count = Number(starCounts[star as keyof typeof starCounts] || 0);
                            const pct = reviewCount > 0 ? Math.round((count / reviewCount) * 100) : 0;

```
