# Knowledge Document: MarketplacePage.tsx (Chunk 39/70)

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
  "chunk_index": 38,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                  <h3>Chưa có xưởng đối tác</h3>
                            <p>Đăng xưởng của bạn để bắt đầu nhận yêu cầu gia công và hiển thị trong mạng lưới ORCA.</p>
                            <button className="mp-publish-btn" onClick={openPublishModal}>Đăng xưởng ngay</button>
                        </div>
                    ) : (
                        <div className="mp-factory-grid">
                            {featuredFactories.map((factory) => {
                                const isOwnFactory = factory.ownerId === user?.id;
                                const image = getFactoryCardImage(factory);
                                return (
                                    <article key={factory.id} className="mp-factory-card" style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
                                        <div className="mp-factory-image">
                                            <img
                                                src={image}
                                                alt={`Ảnh xưởng ${factory.name}`}
                                                referrerPolicy="no-referrer"
                                                onError={handleFactoryImageError}
                                            />
                                            <span className="mp-card-ribbon">{t[factory.statusBadgeMock?.replace(' ', '_') || ''] || factory.statusBadgeMock}</span>
                                        </div>
                                        <div className="mp-factory-card-body" style={{padding: '16px 20px', display: 'flex', flexDirection: 'column', flexGrow: 1}}>
                                            <div className="mp-fcard-header">
                                                <h3>{factory.name} {factory.verifiedFactory && <span className="material-symbols-outlined verified-icon" title={t.verifiedFactory} style={{fontSize: 16, color: '#10b981'}}>verified</span>}</h3>
                                                <span className="mp-fcard-location"><span className="material-symbols-outlined" style={{fontSize: 14}}>location_on</span> {t[factory.region || ''] || factory.region || t.vietnam}</span>
                                            </div>

```
