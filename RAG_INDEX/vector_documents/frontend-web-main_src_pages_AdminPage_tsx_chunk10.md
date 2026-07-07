# Knowledge Document: AdminPage.tsx (Chunk 11/16)

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
  "chunk_index": 10,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
                  <thead><tr><th>Công ty</th><th>Mã Workspace</th><th>Chủ sở hữu</th><th>Thành viên</th><th>Trạng thái</th><th>Thao tác</th></tr></thead>
                  <tbody>
                    {approvedCompanies.filter(c => c.name.toLowerCase().includes(query.toLowerCase())).map(item => (
                      <tr key={item.id}>
                        <td><strong>{item.name}</strong></td>
                        <td><code style={{background:'rgba(255,255,255,0.1)', color: 'inherit', padding:'4px 8px', borderRadius:'6px', fontSize:'12px', fontWeight: 600, letterSpacing: '0.5px'}}>{item.id.slice(0,8)}</code></td>
                        <td>{item.ownerName || '-'}</td>
                        <td>{item.memberCount} users</td>
                        <td><StatusBadge value="Active" /></td>
                        <td>
                          <div className="admin-row-actions">
                            <button className="btn-icon" title="Xem" onClick={handleNotImplemented}><FileText size={16}/></button>
                            <button className="btn-icon danger" title="Đình chỉ" onClick={handleNotImplemented}><Lock size={16}/></button>
                          </div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>
          )}

          {active === 'users' && (
            <section className="admin-card">
              <div className="admin-card-head">
                <div><h3>Người dùng nền tảng</h3><p>Quản lý tất cả tài khoản đã đăng ký trên hệ thống.</p></div>
              </div>
              <div className="admin-toolbar">
                <div className="admin-search-input"><Search size={16}/><input value={query} onChange={e=>{setQuery(e.target.value); setUserPage(1);}} placeholder="Tìm kiếm tên, email..." /></div>
                <select className="admin-select" value={status} onChange={e=>{setStatus(e.target.value); setUserPage(1);}}>
                  <option value="All">Tất cả vai trò</option>
                  <option value="ADMIN">Quản trị viên</option>
                  <option value="FACTORY_OWNER">Chủ xưởng</option>
                  <option value="MEMBER">Thành viên</option>
                </select>
              </div>
              <div className="admin-table-wrap">

```
