# Knowledge Document: MarketplacePage.tsx (Chunk 56/70)

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
  "chunk_index": 55,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
      />
                        <button className="fb-chat-send" onClick={() => { if(chatDraft.trim()) handleSaveChatDraft(); }} disabled={!chatDraft.trim()}>
                            <span className="material-symbols-outlined" style={{fontSize: 24}}>send</span>
                        </button>
                    </div>
                </div>
            )}

            {showOrderModal && (
                <div className="mp-modal-overlay" onClick={() => setShowOrderModal(false)}>
                    <div className="mp-modal" onClick={event => event.stopPropagation()}>
                        <div className="mp-modal-header">
                            <h2>{selectedSeller ? 'Gửi yêu cầu' : 'Đăng Yêu Cầu Tìm Xưởng'}</h2>
                            <button className="mp-modal-close" onClick={() => setShowOrderModal(false)}>×</button>
                        </div>
                        {selectedSeller && <div className="mp-modal-seller">Xưởng nhận RFQ: <strong>{selectedSeller.name}</strong></div>}
                        <form onSubmit={handleSubmitOrder}>

                            <div className="mp-form-group">
                                <label>Tiêu đề RFQ</label>
                                <input value={rfqTitle} onChange={event => setRfqTitle(event.target.value)} placeholder="VD: Báo giá gia công 2 tấn Arabica" required />
                            </div>
                            <div className="mp-form-row">
                                <div className="mp-form-group">
                                    <label>Dịch vụ yêu cầu (Service Required)</label>
                                    <select value={rfqRequestType} onChange={event => setRfqRequestType(event.target.value)} required>
                                        {RFQ_SERVICE_OPTIONS.map(option => (
                                            <option key={option.value} value={option.value}>{option.label}</option>
                                        ))}
                                    </select>
                                </div>
                                <div className="mp-form-group">
                                    <label>Loại sản phẩm (Product Type)</label>
                                    <select value={rfqProductName} onChange={event => setRfqProductName(event.target.value)} required>

```
