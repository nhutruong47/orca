# Knowledge Document: Sidebar.tsx (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, workspace, admin, payment

## Source Code Chunk
```tsx
    if (path === '/marketplace') {
            return location.pathname.startsWith('/marketplace')
                || location.pathname === '/dat-hang'
                || location.pathname === '/thi-truong-dat-hang';
        }
        return location.pathname.startsWith(path);
    };
    const userMenuActive = accountMenuItems.some((item) => location.pathname.startsWith(item.path));

    return (
        <aside className="sidebar">
            <div className="sidebar-logo">
                <img className="app-logo-mark sidebar-brand-logo" src={orcaLogo} alt="ORCA" />
            </div>

            <nav className="sidebar-nav">
                <div className="nav-label">DANH MỤC</div>
                {navItems.map((item) => {
                    const active = isNavActive(item.path);
                    return (
                        <div className="nav-item-wrap" key={item.path}>
                            <NavLink to={item.path} className={() => `nav-item ${active ? 'active' : ''}`}>
                                <span className="nav-icon"><ion-icon name={item.icon} style={{ fontSize: '18px' }}></ion-icon></span>
                                <span className="nav-text">{item.label}</span>
                                {!!item.badge && item.badge > 0 && (
                                    <span className="nav-badge" style={{
                                        marginLeft: 'auto',
                                        background: 'linear-gradient(135deg, #ef4444, #dc2626)',
                                        color: '#fff',
                                        fontSize: '11px',
                                        fontWeight: 800,
                                        padding: '3px 8px',
                                        borderRadius: '12px',
                                        lineHeight: 1,
                                        boxShadow: '0 2px 8px rgba(239, 68, 68, 0.4)',
                                        minWidth: '20px',
                                        textAlign: 'center'
                                    }}>
                                        {item.badge}
                                    </span>
                                )}
                            </NavLink>
                            {item.afterDivider && <div className="nav-divider" role="separator" />}

```
