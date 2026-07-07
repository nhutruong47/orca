# Knowledge Document: MarketplacePage.tsx (Chunk 22/70)

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
  "chunk_index": 21,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
irm('Xóa đánh giá này? Điểm sao của xưởng sẽ được cập nhật lại.')) return;
        try {
            await reviewService.remove(reviewId);
            await loadFactoryReviews(factoryId);
        } catch (err: any) {
            alert(err?.response?.data?.error || 'Không thể xóa đánh giá.');
        }
    };

    const renderMetric = (label: string, value?: string | number | React.ReactNode) => (
        <div className="mp-capacity-metric">
            <span>{label}</span>
            <strong>{displayText(value)}</strong>
        </div>
    );

    const renderVerification = (factory: MarketplaceFactory) => {
        const badges = [
            { label: 'Xưởng đã xác minh', active: factory.verifiedFactory },
            { label: 'Doanh nghiệp đã xác minh', active: factory.verifiedBusiness },
            { label: 'Địa chỉ đã xác minh', active: factory.verifiedAddress },
            { label: 'Chứng nhận đã xác minh', active: factory.verifiedCertification },
        ];
        const hasAny = badges.some(badge => badge.active);
        if (!hasAny) return <p className="mp-empty-inline">Chưa xác minh</p>;
        return (
            <div className="mp-verification-list">
                {badges.map(badge => (
                    <span className={badge.active ? 'verified' : ''} key={badge.label}>
                        <span className="material-symbols-outlined">{badge.active ? 'verified' : 'radio_button_unchecked'}</span>
                        {badge.label}
                    </span>
                ))}
            </div>
        );
    };

    const renderReviewsTab = (factory: MarketplaceFactory) => {
        const summary = factoryReviewsSummary[factory.id] || {};
        const avgRating = summary.avgRating || 0;
        const reviewCount = summary.reviewCount || 0;
        const onTimeRate = summary.onTimeRate || 0;
        const completed = summary.completedOrders || 0;
        const late = summary.lateOrders || 0;
        const starCounts = summary.starCounts || {};
        const reviews = factoryReviews[factory.id] || [];

        if (reviewsLoading && reviews.length === 0) {
            return (
                <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '16px'}}>
                    <div style={{ textAlign: 'center', padding: '40px 20px', color: 'var(--text-muted)' }}>

```
