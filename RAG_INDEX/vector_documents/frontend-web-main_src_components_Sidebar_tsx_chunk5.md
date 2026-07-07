# Knowledge Document: Sidebar.tsx (Chunk 6/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Sidebar.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "report",
    "dashboard",
    "workspace",
    "admin",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, workspace, admin, payment

## Source Code Chunk
```tsx
                                        <ion-icon name={item.icon} style={{ fontSize: '18px' }}></ion-icon>
                                    </span>
                                    <span>{item.label}</span>
                                    {item.hasChevron && <ion-icon name="chevron-forward-outline" className="sidebar-menu-chevron"></ion-icon>}
                                </NavLink>
                            ))}
                            <button
                                type="button"
                                className="sidebar-user-menu-item sidebar-user-menu-button"
                                onClick={() => {
                                    setUserMenuOpen(false);
                                    logout();
                                }}
                            >
                                <span className="nav-icon"><ion-icon name="log-out-outline" style={{ fontSize: '18px' }}></ion-icon></span>
                                <span>Đăng xuất</span>
                            </button>
                        </div>
                    )}

                    <button
                        type="button"
                        className={`sidebar-user ${userMenuOpen || userMenuActive ? 'active' : ''}`}
                        onClick={() => setUserMenuOpen((open) => !open)}
                        aria-expanded={userMenuOpen}
                    >
                        <div className="sidebar-avatar sidebar-avatar-initials" style={{ backgroundImage: `url(${user?.avatar || defaultAvatar})`, backgroundSize: 'cover', backgroundPosition: 'center', color: 'transparent' }}></div>
                        <div className="sidebar-user-info">
                            <span className="sidebar-username">{displayName}</span>
                            <span 
                                className="sidebar-user-plan"
                                style={{
                                    background: planStyle.bg,
                                    color: planStyle.text,
                                    padding: planStyle.bg === 'transparent' ? '2px 0' : '2px 10px',
                                    borderRadius: '12px',
                                    fontSize: '10px',
                                    fontWeight: 800,
                                    textTransform: 'uppercase',

```
