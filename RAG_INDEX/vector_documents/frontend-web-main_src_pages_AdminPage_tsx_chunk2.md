# Knowledge Document: AdminPage.tsx (Chunk 3/16)

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
  "chunk_index": 2,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
000, period: 'Tháng', users: 500, orders: 99999, batches: 99999, workshops: 50, ai: 500000, features: ['Kế hoạch dài hạn', 'Dự báo nhu cầu', 'Mô phỏng kịch bản', 'Quản lý nhiều xưởng'] }
];

function KpiCard({ item }: { item: KpiItem }) {
  const Icon = item.icon;
  return (
    <article className={`admin-kpi admin-kpi-${item.tone}`}>
      <div className="admin-kpi-icon"><Icon size={22} /></div>
      <div className="admin-kpi-content">
        <span>{item.label}</span>
        <strong>{item.value}</strong>
        <small className={item.trend === 'up' ? 'positive' : item.trend === 'down' ? 'negative' : ''}>{item.detail}</small>
      </div>
    </article>
  );
}

function MiniMetric({ label, value, icon: Icon }: { label: string; value: string; icon: React.ElementType }) {
  return (
    <article className="admin-mini-metric">
      <Icon size={18} />
      <div>
        <span>{label}</span>
        <strong>{value}</strong>
      </div>
    </article>
  );
}

function ChartPanel({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="admin-card admin-chart-card">
      <div className="admin-card-head">
        <h3>{title}</h3>
        <button type="button" className="btn-icon"><MoreHorizontal size={16} /></button>
      </div>
      <div className="admin-chart">{children}</div>
    </section>
  );
}

function StatusBadge({ value }: { value: string }) {
  const lower = value.toLowerCase().replaceAll(' ', '-');
  let type = 'neutral';
  
  if (['active', 'paid', 'approved', 'published', 'completed', 'success'].includes(lower)) type = 'success';
  if (['pending', 'trial', 'processing'].includes(lower)) type = 'warning';
  if (['locked', 'failed', 'rejected', 'suspended', 'canceled', 'rejected_order'].includes(lower)) type = 'danger';
  if (['admin', 'professional', 'enterprise', 'factory_owner'].includes(lower)) type = 'info';

  const labels: Record<string, string> = {
    Active: 'Đang hoạt động', Trial: 'Dùng thử', Locked: 'Đã khóa',
    APPROVED: 'Đã duyệt', PENDING: 'Chờ duyệt', REJECTED: 'Từ chối',
    Suspended: 'Tạm đình chỉ',
    PAID: 'Đã thanh toán', FAILED: 'Thất bại', REFUNDED: 'Hoàn tiền',
    Published: 'Công khai', Private: 'Nội bộ',
    ADMIN: 'Admin Nền Tảng', MEMBER: 'Thành viên', FACTORY_OWNER: 'Chủ xưởng',
    free: 'Miễn phí', professional: 'Chuyên nghiệp', enterprise: 'Doanh nghiệp',

```
