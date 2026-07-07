# Knowledge Document: AdminPage.tsx (Chunk 8/16)

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
  "chunk_index": 7,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
>{sidebarModules.find(m => m.id === active)?.label || 'Dashboard'}</h1>
              <p>Quản lý cấu hình nền tảng, theo dõi hoạt động và hỗ trợ khách hàng của bạn.</p>
            </div>
            <div className="admin-hero-actions">
              {active === 'users' && <button className="admin-button admin-button-primary" onClick={handleCreateUser}><Plus size={16} /> Thêm người dùng</button>}
              {active === 'overview' && <button className="admin-button admin-button-secondary"><Download size={16} /> Xuất dữ liệu</button>}
            </div>
          </header>

          {active === 'overview' && (
            <>
              <section className="admin-kpi-grid">
                {dashboardKpis.map(item => <KpiCard key={item.label} item={item} />)}
              </section>
              <section className="admin-grid-2">
                <ChartPanel title="Tăng trưởng doanh thu (Hàng tháng)">
                  <ResponsiveContainer width="100%" height="100%">
                    <AreaChart data={systemTrendData}>
                      <defs>
                        <linearGradient id="revFill" x1="0" y1="0" x2="0" y2="1">
                          <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                          <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                        </linearGradient>
                      </defs>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
                      <XAxis dataKey="month" axisLine={false} tickLine={false} />
                      <YAxis axisLine={false} tickLine={false} />
                      <Tooltip />
                      <Area type="monotone" dataKey="revenue" stroke="#10b981" strokeWidth={3} fillOpacity={1} fill="url(#revFill)" />
                    </AreaChart>
                  </ResponsiveContainer>
                </ChartPanel>
                <ChartPanel title="Người dùng & Công ty">
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={systemTrendData}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
                      <XAxis dataKey="month" axisLine={false} tickLine={false} />
                      <YAxis axisLine={false} tickLine={false} yAxisId="left" />

```
