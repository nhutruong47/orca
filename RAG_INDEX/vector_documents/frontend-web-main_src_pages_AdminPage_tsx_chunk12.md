# Knowledge Document: AdminPage.tsx (Chunk 13/16)

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
  "chunk_index": 12,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
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
                const totalPages = Math.max(1, Math.ceil(filteredUsers.length / 10));
                return (
                  <div className="admin-pagination">
                    <span>Đang hiển thị {filteredUsers.length} bản ghi</span>
                    <div className="admin-pagination-buttons">
                      <button disabled={userPage <= 1} onClick={() => setUserPage(p => Math.max(1, p - 1))}>&lt;</button>
                      <button className="active">{userPage} / {totalPages}</button>
                      <button disabled={userPage >= totalPages} onClick={() => setUserPage(p => Math.min(totalPages, p + 1))}>&gt;</button>
                    </div>
                  </div>
                );
              })()}
            </section>
          )}

          {active === 'subscriptions' && (
            <>
              <div className="admin-hero" style={{marginBottom: 16}}>
                <div><h3>Gói dịch vụ</h3><p>Quản lý các mức giá, giới hạn và tính năng.</p></div>
                <button className="admin-button admin-button-primary" onClick={handleNotImplemented}><Plus size={16} /> Tạo gói mới</button>
              </div>
              <section className="admin-plan-grid">
                {plans.map(item => (
                  <article className="admin-plan" key={item.name}>
                    <h4>{item.name}</h4>
                    <div className="price">{item.price ? money(item.price) : 'Liên hệ'} <span style={{fontSize: 14, fontWeight: 500, color: 'var(--text-secondary)'}}>/ {item.period}</span></div>
                    <div className="admin-plan-limits">
                      <div className="admin-plan-limit-item"><span>Tối đa người dùng</span><strong>{number(item.users)}</strong></div>
                      <div className="admin-plan-limit-item"><span>Tối đa đơn hàng</span><strong>{number(item.orders)}</strong></div>

```
