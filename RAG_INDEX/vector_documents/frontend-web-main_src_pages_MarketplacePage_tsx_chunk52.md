# Knowledge Document: MarketplacePage.tsx (Chunk 53/70)

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
  "chunk_index": 52,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
le-image">
                                    <img
                                        src={getFactoryCardImage(selectedFactory)}
                                        alt={`Ảnh xưởng ${selectedFactory.name}`}
                                        onError={handleFactoryImageError}
                                    />
                                </div>
                            )}
                            <h2>{selectedFactory.name}</h2>
                            <p>{displayText(selectedFactory.region)}</p>
                            <div className="mp-profile-side-metrics">
                                {renderMetric('Độ tin cậy', selectedFactory.totalOrders ? displayPercent(getTrustScore(selectedFactory)) : undefined)}
                                {renderMetric('Công suất', selectedFactory.monthlyCapacity)}
                                {renderMetric('Loại hình', selectedFactory.factoryType)}
                            </div>
                            {renderVerification(selectedFactory)}
                        </aside>
                        <div className="mp-detail-content">
                            <div className="mp-profile-tabs">
                                {(['overview', 'capabilities', 'equipment', 'certificates', 'reviews', 'portfolio', 'rfq'] as FactoryProfileTab[]).map(tab => (
                                    <button
                                        key={tab}
                                        className={activeProfileTab === tab ? 'active' : ''}
                                        onClick={() => setActiveProfileTab(tab)}
                                    >
                                        {profileTabLabels[tab]}
                                    </button>
                                ))}
                            </div>
                            {renderProfileTab(selectedFactory)}
                            <div className="mp-detail-actions">
                                <button disabled={selectedFactory.ownerId === user?.id} onClick={() => openChat(selectedFactory)}>Trao đổi</button>
                                <button disabled={selectedFactory.ownerId === user?.id} onClick={() => { const factory = selectedFactory; setSelectedFactory(null); handleOrderClick(factory); }}>

```
