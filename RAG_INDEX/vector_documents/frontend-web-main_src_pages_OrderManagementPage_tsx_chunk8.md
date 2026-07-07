# Knowledge Document: OrderManagementPage.tsx (Chunk 9/23)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/OrderManagementPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
'20px', display: 'inline-block', padding: 4 }}>
                <div className="tabs-header" style={{ gap: 8 }}>
                    <button
                        className={`tab-btn ${activeTab === 'outbound' ? 'active' : ''}`}
                        onClick={() => setActiveTab('outbound')}
                        style={{ display: 'flex', alignItems: 'center', gap: 4 }}
                    >
                        <ion-icon name="arrow-up-outline" style={{ fontSize: '15px' }}></ion-icon> Đơn đã đi đặt (Mua)
                        {unreadOutboundCount > 0 && <span className="nav-badge" style={{ background: '#E53935', color: '#fff', fontSize: '0.75rem', padding: '2px 6px', borderRadius: '10px', marginLeft: 4 }}>{unreadOutboundCount}</span>}
                    </button>
                    <button
                        className={`tab-btn ${activeTab === 'inbound' ? 'active' : ''}`}
                        onClick={() => {
                            setActiveTab('inbound');
                        }}
                        style={{ display: 'flex', alignItems: 'center', gap: 4 }}
                    >
                        <ion-icon name="arrow-down-outline" style={{ fontSize: '15px' }}></ion-icon> Đơn xưởng khác đặt (Bán/Gia công)
                    </button>
                </div>
            </div>

            {activeTab === 'inbound' && (
                <div className="glass-panel" style={{ padding: '16px 20px', marginBottom: 20, border: '1px solid rgba(217, 156, 95, 0.28)' }}>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 12, flexWrap: 'wrap' }}>
                        <div>
                            <h2 style={{ margin: 0, fontSize: 20, color: 'var(--text-primary)' }}>Đơn xưởng khác đặt</h2>
                            <p style={{ margin: '4px 0 0', color: 'var(--text-secondary)', fontSize: 13 }}>
                                Quản lý đơn bán/gia công cho xưởng đang chọn.
                            </p>
                        </div>
                        <button
                            className="btn btn-primary"
                            onClick={() => {
                                setShowManualOrderForm(true);
                                setManualCreateError('');
                            }}
                        >

```
