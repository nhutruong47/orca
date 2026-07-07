# Knowledge Document: AdminPage.tsx (Chunk 2/16)

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
  "chunk_index": 1,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
em = {
  label: string;
  value: string;
  detail: string;
  icon: React.ElementType;
  tone: KpiTone;
  trend?: 'up' | 'down';
};

const emptyOverview: AdminOverview = {
  totalUsers: 0,
  adminUsers: 0,
  memberUsers: 0,
  newUsersThisMonth: 0,
  newUsersPreviousMonth: 0,
  totalTeams: 0,
  publishedTeams: 0,
  newTeamsThisMonth: 0,
  newTeamsPreviousMonth: 0,
  totalGoals: 0,
  activeGoals: 0,
  totalTasks: 0,
  completedTasks: 0,
  overdueTasks: 0,
  totalOrders: 0,
  activeOrders: 0,
  totalProductionOrders: 0,
  activeProductionOrders: 0,
  overdueProductionOrders: 0,
  totalBatches: 0,
  activeBatches: 0,
  completedBatches: 0,
  paidPayments: 0,
  totalPayments: 0,
  revenueThisMonth: 0,
  revenuePreviousMonth: 0,
  revenueThisYear: 0,
  revenuePreviousYear: 0,
  revenueTotal: 0,
  orderStatusCounts: {},
  productionOrderStatusCounts: {},
  batchStatusCounts: {},
  taskStatusCounts: {},
  recentUsers: [],
  recentTeams: [],
};

const getDate = (value: string | null | undefined) => {
  if (!value) return null;
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? null : date;
};

const paymentDate = (payment: AdminPayment) => getDate(payment.paidAt || payment.createdAt);

const formatShortDate = (value: Date | string | null | undefined) => {
  const date = value instanceof Date ? value : getDate(value);
  return date ? date.toLocaleDateString('vi-VN') : '-';
};

const formatTime = (value: string | null | undefined) => {
  const date = getDate(value);
  return date ? date.toLocaleTimeString('vi-VN') : '-';
};

const paymentCustomerName = (payment: AdminPayment) =>
  payment.fullName || payment.username || payment.email || 'Không rõ người dùng';

const initialPlans = [
  { name: 'Chuyên nghiệp', price: 129000, period: 'Tháng', users: 30, orders: 1000, batches: 5000, workshops: 5, ai: 40000, features: ['Cảnh báo công việc', 'Cảnh báo nguyên liệu', 'Phân tích hiệu suất', 'Phát hiện điểm nghẽn'] },
  { name: 'Doanh nghiệp', price: 249000, period: 'Tháng', users: 500, orders: 99999, batches: 99999, workshops: 50, ai: 500000, features: ['Kế hoạch dài hạn', 'Dự báo nhu cầu', 'Mô phỏng kịch bản', 'Quản lý nhiều xưởng'] }
];

function KpiCard({ item }: { item: KpiItem }) {
  const Icon = item.icon;
  return (
    <article className={`admin-kpi admin-kpi-${item.tone}`}>
      <div className="admin-kpi-icon"><Icon size={22} /></div>

```
