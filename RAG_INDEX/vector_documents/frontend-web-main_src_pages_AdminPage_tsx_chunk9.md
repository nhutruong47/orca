# Knowledge Document: AdminPage.tsx (Chunk 10/16)

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
  "chunk_index": 9,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
              <td>
                          <div style={{fontSize:'12px', color:'#6b7280'}}>
                            <div>GPKD: {item.businessLicense || '-'}</div>
                            <div>Địa chỉ: {item.businessAddress || '-'}</div>
                          </div>
                        </td>
                        <td>{item.createdAt ? formatShortDate(item.createdAt) : '-'}</td>
                        <td><StatusBadge value={item.verificationStatus || 'PENDING'} /></td>
                        <td>
                          <div className="admin-row-actions">
                            <button className="admin-button admin-button-primary" onClick={() => updateTeamVerification(item.id, 'APPROVED')} style={{padding:'4px 10px', fontSize:'12px'}}>Duyệt</button>
                            <button className="admin-button admin-button-secondary" onClick={() => updateTeamVerification(item.id, 'REJECTED')} style={{padding:'4px 10px', fontSize:'12px'}}>Từ chối</button>
                          </div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>
          )}

          {active === 'companies' && (
            <section className="admin-card">
              <div className="admin-card-head">
                <div><h3>Công ty đã duyệt</h3><p>Quản lý tất cả các tổ chức đang hoạt động trên nền tảng.</p></div>
              </div>
              <div className="admin-toolbar">
                <div className="admin-search-input"><Search size={16}/><input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Tìm kiếm công ty..." /></div>
              </div>
              <div className="admin-table-wrap">
                <table className="admin-table">
                  <thead><tr><th>Công ty</th><th>Mã Workspace</th><th>Chủ sở hữu</th><th>Thành viên</th><th>Trạng thái</th><th>Thao tác</th></tr></thead>
                  <tbody>
                    {approvedCompanies.filter(c => c.name.toLowerCase().includes(query.toLowerCase())).map(item => (
                      <tr key={item.id}>
                        <td><strong>{item.name}</strong></td>

```
