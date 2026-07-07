# Knowledge Document: Layout.tsx (Chunk 7/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Layout.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "notification",
  "tags": [
    "notification",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
                                       <p>
                                                        <strong>Hệ thống</strong> {notif.message}
                                                    </p>
                                                    <span className="fb-notif-time">{new Date(notif.createdAt).toLocaleDateString('vi-VN')}</span>
                                                </div>
                                                {!notif.read && <div className="fb-notif-unread-dot"></div>}
                                            </div>
                                        ))}
                                    </div>
                                    <div className="fb-notification-footer">
                                        <button>Xem thông báo trước đó</button>
                                    </div>
                                </div>
                            )}
                        </div>

                        <div className="topbar-avatar" onClick={() => navigate('/profile')} title="Hồ sơ nhân viên" style={{ cursor: 'pointer', backgroundImage: `url(${user?.avatar || defaultAvatar})`, backgroundSize: 'cover', backgroundPosition: 'center', color: 'transparent' }}>
                        </div>
                        <button className="topbar-logout" onClick={logout}>
                            Đăng xuất
                        </button>
                    </div>
                </header>

                {/* Page content */}
                <main className="layout-content">
                    <Outlet />
                </main>
            </div>

            {showUpgradeModal && (
                <div className="modal-overlay">
                    <div className="modal-content upgrade-required-modal">
                        <div style={{ color: '#7c3aed', marginBottom: '16px' }}>
                            <Sparkles size={48} style={{ margin: '0 auto' }} />
                        </div>
                        <h3 style={{ marginBottom: '12px' }}>Nâng cấp để tiếp tục</h3>
                        <p style={{ color: '#64748b', marginBottom: '24px', fontSize: '15px' }}>
                            Chọn gói phù hợp để tiếp tục sử dụng trợ lý AI ORCA.
                        </p>
                        <div className="upgrade-required-actions">
                            <button

```
