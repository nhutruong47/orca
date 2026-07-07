# Knowledge Document: Sidebar.tsx (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, workspace, admin, payment

## Source Code Chunk
```tsx
           minWidth: '20px',
                                        textAlign: 'center'
                                    }}>
                                        {item.badge}
                                    </span>
                                )}
                            </NavLink>
                            {item.afterDivider && <div className="nav-divider" role="separator" />}
                        </div>
                    );
                })}
            </nav>

            {user && (
                <div className="sidebar-user-wrap">
                    {userMenuOpen && (
                        <div className="sidebar-user-menu">
                            <div className="sidebar-user-menu-head">
                                <div className="sidebar-avatar sidebar-avatar-initials" style={{ backgroundImage: `url(${user?.avatar || defaultAvatar})`, backgroundSize: 'cover', backgroundPosition: 'center', color: 'transparent' }}></div>
                                <div className="sidebar-user-info">
                                    <span className="sidebar-username">{displayName}</span>
                                    <span className="sidebar-user-plan">{displayPlan}</span>
                                </div>
                                <ion-icon name="chevron-forward-outline" className="sidebar-menu-head-chevron"></ion-icon>
                            </div>
                            {accountMenuItems.map((item) => (
                                <NavLink
                                    key={`${item.path}-${item.label}`}
                                    to={item.path}
                                    className={`sidebar-user-menu-item ${item.separated ? 'separated' : ''} ${location.pathname.startsWith(item.path) ? 'active' : ''}`}
                                    onClick={() => setUserMenuOpen(false)}
                                >
                                    <span className="nav-icon">
                                        <ion-icon name={item.icon} style={{ fontSize: '18px' }}></ion-icon>
                                    </span>
                                    <span>{item.label}</span>
                                    {item.hasChevron && <ion-icon name="chevron-forward-outline" className="sidebar-menu-chevron"></ion-icon>}
                                </NavLink>

```
