# Knowledge Document: MarketplacePage.tsx (Chunk 54/70)

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
  "chunk_index": 53,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                     <div className="mp-detail-actions">
                                <button disabled={selectedFactory.ownerId === user?.id} onClick={() => openChat(selectedFactory)}>Trao đổi</button>
                                <button disabled={selectedFactory.ownerId === user?.id} onClick={() => { const factory = selectedFactory; setSelectedFactory(null); handleOrderClick(factory); }}>
                                    {selectedFactory.ownerId === user?.id ? 'Xưởng của bạn' : 'Gửi yêu cầu'}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {showChatModal && chatTarget && (
                <div className="fb-chat-popup">
                    <div className="fb-chat-header" onClick={() => setShowChatModal(false)}>
                        <div className="fb-chat-header-info">
                            <img src={chatTarget.factoryImageUrl || chatTarget.factoryImages?.[0] || fallbackFactoryImages[getFactoryImageSeed(chatTarget) % fallbackFactoryImages.length]} alt="avatar" />
                            <div className="fb-chat-header-text">
                                <h4>{chatTarget.name}</h4>
                                <span style={{ color: '#10b981' }}>Đang hoạt động</span>
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <button className="fb-chat-action-btn" onClick={(e) => { e.stopPropagation(); alert('Tính năng gọi thoại đang được phát triển'); }}>
                                <span className="material-symbols-outlined" style={{fontSize: 20}}>call</span>
                            </button>
                            <button className="fb-chat-action-btn" onClick={(e) => { e.stopPropagation(); alert('Tính năng gọi video đang được phát triển'); }}>
                                <span className="material-symbols-outlined" style={{fontSize: 20}}>videocam</span>
                            </button>
                            <button className="fb-chat-close" onClick={(e) => { e.stopPropagation(); setShowChatModal(false); }}>
                                <span className="material-symbols-outlined" style={{fontSize: 20}}>close</span>

```
