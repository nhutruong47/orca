# Knowledge Document: Sidebar.tsx (Chunk 3/7)

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
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, workspace, admin, payment

## Source Code Chunk
```tsx
   { path: '/admin?section=workspace_requests', label: 'Yêu cầu mở xưởng', icon: 'person-add-outline' },
        { path: '/admin?section=companies', label: 'Quản lý doanh nghiệp', icon: 'business-outline' },
        { path: '/admin?section=users', label: 'Quản lý người dùng', icon: 'people-outline' },
        { path: '/admin?section=subscriptions', label: 'Gói dịch vụ', icon: 'receipt-outline' },
        { path: '/admin?section=payments', label: 'Thanh toán & doanh thu', icon: 'card-outline' },
        { path: '/admin?section=reports', label: 'Báo cáo thống kê', icon: 'document-text-outline' },
        { path: '/admin?section=logs', label: 'Nhật ký hệ thống', icon: 'shield-checkmark-outline' },
    ];

    const navItems = user?.role === 'ADMIN' ? adminNavItems : [
        { path: '/dashboard', label: 'Tổng quan', icon: 'grid-outline' },
        { path: '/groups', label: 'Nhóm xưởng', icon: 'people-outline', afterDivider: true },
        { path: '/marketplace', label: 'Thị trường', icon: 'storefront-outline' },
        { path: '/orders', label: 'Đơn hàng', icon: 'cube-outline', badge: pendingOrderCount },
    ];

    const accountMenuItems = [
        { path: '/upgrade', label: 'Nâng cấp gói', icon: 'sparkles-outline' },
        { path: '/settings', label: 'Cá nhân hóa', icon: 'color-palette-outline' },
        { path: '/profile', label: 'Hồ sơ', icon: 'person-circle-outline' },
        { path: '/settings', label: 'Cài đặt', icon: 'settings-outline' },
        { path: '/settings', label: 'Trợ giúp', icon: 'help-buoy-outline', separated: true, hasChevron: true },
    ];

    const isNavActive = (path: string) => {
        if (path.startsWith('/admin')) {
            const section = new URLSearchParams(path.split('?')[1] || '').get('section') || 'overview';
            const currentSection = new URLSearchParams(location.search).get('section') || 'overview';
            return location.pathname === '/admin' && section === currentSection;
        }
        if (path === '/marketplace') {
            return location.pathname.startsWith('/marketplace')
                || location.pathname === '/dat-hang'
                || location.pathname === '/thi-truong-dat-hang';
        }
        return location.pathname.startsWith(path);
    };
    const userMenuActive = accountMenuItems.some((item) => location.pathname.startsWith(item.path));

    return (

```
