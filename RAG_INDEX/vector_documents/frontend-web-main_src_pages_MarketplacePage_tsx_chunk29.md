# Knowledge Document: MarketplacePage.tsx (Chunk 30/70)

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
  "chunk_index": 29,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
Ngày cấp: {cert.issueDate} • Hết hạn: {cert.expDate}</span>
                                    </div>
                                    <span style={{color: '#10b981', display: 'flex', alignItems: 'center', gap: '4px', fontSize: '13px', fontWeight: 600}}>
                                        <span className="material-symbols-outlined" style={{fontSize: '16px'}}>verified</span> {cert.status}
                                    </span>
                                </div>
                            ))}
                        </div>
                    </div>
                );
            case 'reviews':
                return renderReviewsTab(factory);
                return (
                    <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '16px'}}>
                        {(() => {
                            const summary = factoryReviewsSummary[factory.id] || {};
                            const avgRating = summary.avgRating || 0;
                            const reviewCount = summary.reviewCount || 0;
                            const onTimeRate = summary.onTimeRate || 0;
                            const completed = summary.completedOrders || 0;
                            const late = summary.lateOrders || 0;
                            if (reviewCount === 0) {
                                return (
                                    <div style={{ textAlign: 'center', padding: '40px 20px', color: 'var(--text-muted)' }}>
                                        <div style={{ fontSize: 40, marginBottom: 12 }}>Chưa có đánh giá</div>
                                        <p>Chưa có đơn hàng nào được hoàn thành với xưởng này.</p>
                                    </div>
                                );
                            }
                            return (
                                <>
                                    <div style={{display: 'flex', alignItems: 'center', gap: '24px', padding: '24px', background: 'rgba(255,255,255,0.03)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.05)'}}>
                                        <div style={{textAlign: 'center'}}>
                                            <div style={{fontSize: '36px', fontWeight: 700, color: '#f59e0b'}}>{avgRating > 0 ? avgRating.toFixed(1) : '—'}</div>

```
