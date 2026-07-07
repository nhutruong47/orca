# Knowledge Document: OrderManagementPage.tsx (Chunk 10/23)

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
  "chunk_index": 9,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
công cho xưởng đang chọn.
                            </p>
                        </div>
                        <button
                            className="btn btn-primary"
                            onClick={() => {
                                setShowManualOrderForm(true);
                                setManualCreateError('');
                            }}
                        >
                            <ion-icon name="add-circle-outline" style={{ fontSize: 16 }}></ion-icon>
                            Tạo đơn hàng thủ công
                        </button>
                    </div>
                </div>
            )}

            {showManualOrderForm && (
                <div style={{
                    position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.75)',
                    backdropFilter: 'blur(8px)', zIndex: 10000,
                    display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px'
                }}>
                    <div style={{
                        background: 'var(--bg-card)', borderRadius: 24, padding: '40px',
                        maxWidth: 1000, width: '100%', boxShadow: '0 24px 80px rgba(0,0,0,0.5)',
                        maxHeight: '90vh', overflowY: 'auto', position: 'relative'
                    }}>
                        <button
                            type="button"
                            onClick={() => setShowManualOrderForm(false)}
                            style={{ position: 'absolute', top: 24, right: 32, background: 'transparent', border: 'none', fontSize: 32, color: 'var(--text-secondary)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', width: 40, height: 40, borderRadius: '50%', transition: 'all 0.2s' }}
                            onMouseEnter={e => e.currentTarget.style.background = 'rgba(255,255,255,0.1)'}
                            onMouseLeave={e => e.currentTarget.style.background = 'transparent'}
                        >
                            &times;
                        </button>
                        
                        <div style={{ marginBottom: 32 }}>
                            <h2 style={{ margin: 0, fontSize: 28, color: 'var(--text-primary)', fontWeight: 800 }}>Đơn xưởng khác đặt</h2>

```
