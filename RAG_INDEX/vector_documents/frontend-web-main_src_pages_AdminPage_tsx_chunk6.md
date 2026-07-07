# Knowledge Document: AdminPage.tsx (Chunk 7/16)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/AdminPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "report",
    "dashboard",
    "admin",
    "workspace",
    "production",
    "factory",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 6,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
r(t => t.verificationStatus === 'PENDING');
  const approvedCompanies = adminTeams.filter(t => t.verificationStatus !== 'PENDING');

  const updateTeamVerification = async (teamId: string, nextStatus: 'APPROVED' | 'REJECTED') => {
    const rejectReason = nextStatus === 'REJECTED' ? window.prompt('Reject reason?') : '';
    if (nextStatus === 'REJECTED' && rejectReason === null) return;
    try {
      const updated = await adminService.updateTeamVerification(teamId, nextStatus, rejectReason || '');
      setAdminTeams(current => current.map(item => item.id === teamId ? { ...item, ...updated } : item));
    } catch { window.alert('Error updating status.'); }
  };

  const handleCreateUser = async () => {
    const username = window.prompt("Username:");
    if (!username) return;
    try {
      const created = await adminService.createUser({ username, email: '', fullName: '', role: 'MEMBER' });
      setAdminUsers(current => [created, ...current]);
    } catch { window.alert("Error creating user."); }
  };

  if (user?.role !== 'ADMIN') {
    return (
      <div className="admin-access">
        <ShieldCheck size={40} />
        <h1>Từ chối truy cập</h1>
        <p>Bạn cần quyền Quản trị viên để xem bảng điều khiển này.</p>
      </div>
    );
  }

  if (adminLoading) {
    return (
      <div className="admin-access">
        <Activity size={40} />
        <h1>Đang tải thống kê nền tảng</h1>
        <p>Đang kết nối tới cơ sở dữ liệu bảo mật...</p>
      </div>
    );
  }

  if (adminError) {
    return (
      <div className="admin-access">
        <AlertTriangle size={40} />
        <h1>Lỗi tải bảng điều khiển</h1>
        <p>{adminError}</p>
      </div>
    );
  }

  return (
    <div className="admin-app">
      <main className="admin-main">
        <div className="admin-main-inner">
          <header className="admin-hero">
            <div>
              <h1>{sidebarModules.find(m => m.id === active)?.label || 'Dashboard'}</h1>
              <p>Quản lý cấu hình nền tảng, theo dõi hoạt động và hỗ trợ khách hàng của bạn.</p>
            </div>
            <div className="admin-hero-actions">
              {active === 'users' && <button className="admin-button admin-button-primary" onClick={handleCreateUser}><Plus size={16} /> Thêm người dùng</button>}

```
