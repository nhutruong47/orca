# Knowledge Document: AdminPage.tsx (Chunk 16/16)

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
  "chunk_index": 15,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
API</td><td>2 ngày trước</td><td><button className="admin-button admin-button-secondary" style={{padding:'4px 12px'}}><Download size={14}/> PDF</button></td></tr>
                  </tbody>
                </table>
              </div>
            </section>
          )}

          {active === 'logs' && (
            <section className="admin-card">
              <div className="admin-card-head">
                <div><h3>Nhật ký hệ thống</h3><p>Theo dõi hoạt động và bảo mật của nền tảng.</p></div>
                <div className="admin-toolbar" style={{margin:0}}>
                  <select className="admin-select"><option>Tất cả sự kiện</option><option>Đăng nhập</option><option>Thanh toán</option><option>Bảo mật</option></select>
                </div>
              </div>
              <div className="admin-table-wrap">
                <table className="admin-table">
                  <thead><tr><th>Thời gian</th><th>Loại sự kiện</th><th>Người thực hiện</th><th>Địa chỉ IP</th><th>Trạng thái</th></tr></thead>
                  <tbody>
                    <tr><td>{formatShortDate(new Date())} {formatTime(new Date().toISOString())}</td><td><strong>Đăng nhập Admin</strong></td><td>john.admin</td><td>192.168.1.1</td><td><StatusBadge value="SUCCESS" /></td></tr>
                    <tr><td>{formatShortDate(new Date())} {formatTime(new Date(Date.now() - 3600000).toISOString())}</td><td><strong>Hoàn tiền</strong></td><td>system</td><td>-</td><td><StatusBadge value="SUCCESS" /></td></tr>
                    <tr><td>{formatShortDate(new Date())} {formatTime(new Date(Date.now() - 7200000).toISOString())}</td><td><strong>Đăng nhập thất bại</strong></td><td>unknown</td><td>10.0.0.45</td><td><StatusBadge value="FAILED" /></td></tr>
                  </tbody>
                </table>
              </div>
            </section>
          )}

        </div>
      </main>
    </div>
  );
}

```
