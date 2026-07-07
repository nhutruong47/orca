# Knowledge Document: AdminPage.tsx (Chunk 9/16)

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
  "chunk_index": 8,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
i dùng & Công ty">
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={systemTrendData}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
                      <XAxis dataKey="month" axisLine={false} tickLine={false} />
                      <YAxis axisLine={false} tickLine={false} yAxisId="left" />
                      <YAxis axisLine={false} tickLine={false} yAxisId="right" orientation="right" />
                      <Tooltip />
                      <Line yAxisId="left" type="monotone" dataKey="users" stroke="#3b82f6" strokeWidth={3} dot={false} />
                      <Line yAxisId="right" type="monotone" dataKey="companies" stroke="#8b5cf6" strokeWidth={3} dot={false} />
                    </LineChart>
                  </ResponsiveContainer>
                </ChartPanel>
              </section>
            </>
          )}

          {active === 'workspace_requests' && (
            <section className="admin-card">
              <div className="admin-card-head">
                <div><h3>Yêu cầu chờ duyệt</h3><p>Xem xét và xác minh đăng ký công ty mới.</p></div>
              </div>
              <div className="admin-table-wrap">
                <table className="admin-table">
                  <thead><tr><th>Tên công ty</th><th>Chủ sở hữu</th><th>Thông tin kinh doanh</th><th>Ngày đăng ký</th><th>Trạng thái</th><th>Thao tác</th></tr></thead>
                  <tbody>
                    {pendingRequests.length === 0 ? (
                      <tr><td colSpan={6} style={{textAlign:'center', padding:'32px', color:'#6b7280'}}>Không có yêu cầu chờ duyệt.</td></tr>
                    ) : pendingRequests.map(item => (
                      <tr key={item.id}>
                        <td><strong>{item.name}</strong></td>
                        <td>{item.ownerName || '-'}</td>
                        <td>
                          <div style={{fontSize:'12px', color:'#6b7280'}}>
                            <div>GPKD: {item.businessLicense || '-'}</div>
                            <div>Địa chỉ: {item.businessAddress || '-'}</div>
                          </div>
                        </td>
                        <td>{item.createdAt ? formatShortDate(item.createdAt) : '-'}</td>

```
