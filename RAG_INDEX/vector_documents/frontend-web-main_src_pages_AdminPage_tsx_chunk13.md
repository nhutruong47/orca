# Knowledge Document: AdminPage.tsx (Chunk 14/16)

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
  "chunk_index": 13,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
Weight: 500, color: 'var(--text-secondary)'}}>/ {item.period}</span></div>
                    <div className="admin-plan-limits">
                      <div className="admin-plan-limit-item"><span>Tối đa người dùng</span><strong>{number(item.users)}</strong></div>
                      <div className="admin-plan-limit-item"><span>Tối đa đơn hàng</span><strong>{number(item.orders)}</strong></div>
                      <div className="admin-plan-limit-item"><span>Số xưởng con</span><strong>{item.workshops}</strong></div>
                      <div className="admin-plan-limit-item"><span>Điểm AI</span><strong>{number(item.ai)}</strong></div>
                    </div>
                    <div className="admin-row-actions" style={{marginTop: 20}}>
                      <button className="admin-button admin-button-secondary" style={{width:'100%'}} onClick={handleNotImplemented}>Chỉnh sửa</button>
                    </div>
                  </article>
                ))}
              </section>
            </>
          )}

          {active === 'payments' && (
            <>
              <section className="admin-mini-grid">
                <MiniMetric label="Tổng doanh thu" value={money(revenueReport.total)} icon={DollarSign} />
                <MiniMetric label="Đang chờ xử lý" value={money(revenueReport.pending)} icon={AlertTriangle} />
              </section>
              <section className="admin-card">
                <div className="admin-card-head">
                  <div><h3>Lịch sử giao dịch</h3><p>Xem tất cả các thanh toán trên toàn hệ thống.</p></div>
                </div>
                <div className="admin-table-wrap">
                  <table className="admin-table">
                    <thead><tr><th>Mã GD</th><th>Công ty/Người dùng</th><th>Gói</th><th>Số tiền</th><th>Ngày tháng</th><th>Trạng thái</th><th>Thao tác</th></tr></thead>
                    <tbody>
                      {revenueReport.rangeInvoices.slice(0,10).map(item => (
                        <tr key={item.id}>
                          <td><code style={{fontSize:12}}>{item.txnRef}</code></td>
                          <td><strong>{paymentCustomerName(item)}</strong></td>
                          <td>{item.planId}</td>
                          <td>{money(Number(item.amount))}</td>
                          <td>{formatShortDate(paymentDate(item))}</td>

```
