# Knowledge Document: GroupDetailPage.tsx (Chunk 70/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 69,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
arginBottom: 6 }}>Chào mừng bạn đến với đoạn chat</div>
                                    <div style={{ fontSize: 14 }}>Chọn một cuộc trò chuyện bên trái để bắt đầu nhắn tin</div>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* ===== MODALS (preserved) ===== */}
            {/* Video Call Modal */}
            {showVideoCall && (
                <div style={{ position: 'fixed', inset: 0, background: '#111827', zIndex: 9999, display: 'flex', flexDirection: 'column' }}>
                    {/* Header */}
                    <div style={{ padding: '24px', display: 'flex', justifyContent: 'space-between', color: '#fff' }}>
                        <h2 style={{ margin: 0, fontWeight: 500, fontSize: 18 }}>Cuộc gọi nhóm {team?.name}</h2>
                        <button onClick={() => setShowVideoCall(false)} style={{ background: 'none', border: 'none', color: '#fff', fontSize: 28, cursor: 'pointer', display: 'flex' }}><ion-icon name="expand"></ion-icon></button>
                    </div>

                    {/* Main Content */}
                    <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
                        <div style={{ width: 160, height: 160, borderRadius: '50%', background: '#374151', display: 'flex', alignItems: 'center', justifyContent: 'center', border: '4px solid #4b5563' }}>
                            <ion-icon name="person" style={{ fontSize: 80, color: '#9ca3af' }}></ion-icon>
                        </div>
                        <div style={{ position: 'absolute', bottom: 40, color: '#fff', fontSize: 20, fontWeight: 500 }}>Đang gọi...</div>
                    </div>

                    {/* Controls */}
                    <div style={{ padding: '32px', display: 'flex', justifyContent: 'center', gap: 24, background: 'linear-gradient(transparent, rgba(0,0,0,0.8))' }}>
                        <button style={{ width: 64, height: 64, borderRadius: '50%', background: '#374151', border: 'none', color: '#fff', fontSize: 24, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><ion-icon name="mic-outline"></ion-icon></button>

```
