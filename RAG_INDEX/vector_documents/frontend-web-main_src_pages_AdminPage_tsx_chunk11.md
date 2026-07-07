# Knowledge Document: AdminPage.tsx (Chunk 12/16)

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
  "chunk_index": 11,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
{e=>{setStatus(e.target.value); setUserPage(1);}}>
                  <option value="All">Tất cả vai trò</option>
                  <option value="ADMIN">Quản trị viên</option>
                  <option value="FACTORY_OWNER">Chủ xưởng</option>
                  <option value="MEMBER">Thành viên</option>
                </select>
              </div>
              <div className="admin-table-wrap">
                <table className="admin-table">
                  <thead><tr><th>Người dùng</th><th>Email</th><th>Vai trò</th><th>Trạng thái</th><th>Ngày tạo</th><th>Thao tác</th></tr></thead>
                  <tbody>
                    {(() => {
                      const filteredUsers = adminUsers.filter(u => `${u.fullName} ${u.email}`.toLowerCase().includes(query.toLowerCase()) && (status === 'All' || u.role === status));
                      const paginatedUsers = filteredUsers.slice((userPage - 1) * 10, userPage * 10);
                      return paginatedUsers.map(item => (
                        <tr key={item.id}>
                          <td><div className="admin-user-cell"><div className="admin-user-avatar">{(item.fullName || item.username || '?').charAt(0)}</div><strong>{item.fullName || item.username}</strong></div></td>
                          <td>{item.email}</td>
                          <td><StatusBadge value={item.role} /></td>
                          <td><StatusBadge value="Active" /></td>
                          <td>{item.createdAt ? formatShortDate(item.createdAt) : '-'}</td>
                          <td>
                            <div className="admin-row-actions">
                              <button className="btn-icon" title="Cấp lại mật khẩu" onClick={handleNotImplemented}><RotateCcw size={16}/></button>
                              <button className="btn-icon danger" title="Khóa tài khoản" onClick={handleNotImplemented}><Lock size={16}/></button>
                            </div>
                          </td>
                        </tr>
                      ));
                    })()}
                  </tbody>
                </table>
              </div>
              {(() => {
                const filteredUsers = adminUsers.filter(u => `${u.fullName} ${u.email}`.toLowerCase().includes(query.toLowerCase()) && (status === 'All' || u.role === status));

```
