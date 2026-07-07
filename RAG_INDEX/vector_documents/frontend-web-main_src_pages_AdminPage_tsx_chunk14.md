# Knowledge Document: AdminPage.tsx (Chunk 15/16)

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
  "chunk_index": 14,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
em => (
                        <tr key={item.id}>
                          <td><code style={{fontSize:12}}>{item.txnRef}</code></td>
                          <td><strong>{paymentCustomerName(item)}</strong></td>
                          <td>{item.planId}</td>
                          <td>{money(Number(item.amount))}</td>
                          <td>{formatShortDate(paymentDate(item))}</td>
                          <td><StatusBadge value={String(item.status)} /></td>
                          <td><button className="admin-button admin-button-secondary" style={{padding:'4px 8px', fontSize:12}}>Biên lai</button></td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </section>
            </>
          )}

          {active === 'reports' && (
            <section className="admin-card">
              <div className="admin-card-head">
                <div><h3>Xuất dữ liệu & Báo cáo</h3><p>Tạo các báo cáo phân tích hiệu suất của nền tảng.</p></div>
              </div>
              <div className="admin-table-wrap">
                <table className="admin-table">
                  <thead><tr><th>Loại báo cáo</th><th>Mô tả</th><th>Tạo lần cuối</th><th>Thao tác</th></tr></thead>
                  <tbody>
                    <tr><td><strong>Báo cáo doanh thu</strong></td><td>Thống kê doanh thu thanh toán SaaS hàng tháng</td><td>Hôm nay, 10:30 AM</td><td><button className="admin-button admin-button-secondary" style={{padding:'4px 12px'}}><Download size={14}/> CSV</button></td></tr>
                    <tr><td><strong>Tăng trưởng công ty</strong></td><td>Lượt đăng ký công ty mới và tỷ lệ rời bỏ</td><td>Hôm qua, 14:00 PM</td><td><button className="admin-button admin-button-secondary" style={{padding:'4px 12px'}}><Download size={14}/> Excel</button></td></tr>
                    <tr><td><strong>Mức độ sử dụng</strong></td><td>Sử dụng bộ nhớ, điểm AI và yêu cầu API</td><td>2 ngày trước</td><td><button className="admin-button admin-button-secondary" style={{padding:'4px 12px'}}><Download size={14}/> PDF</button></td></tr>
                  </tbody>
                </table>
              </div>
            </section>
          )}

          {active === 'logs' && (
            <section className="admin-card">
              <div className="admin-card-head">

```
