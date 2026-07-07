# Knowledge Document: AdminPage.tsx (Chunk 6/16)

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
  "chunk_index": 5,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
planName] = (acc[planName] || 0) + Number(item.amount);
      return acc;
    }, {});
    
    const revenueByPlan = Object.entries(planMap).map(([name, value]) => ({ name, value: Math.round(value / 1000000), amount: value })).sort((a, b) => b.amount - a.amount);
    
    const customerMap = paidPayments.reduce<Record<string, number>>((acc, item) => {
      const name = paymentCustomerName(item);
      acc[name] = (acc[name] || 0) + Number(item.amount);
      return acc;
    }, {});
    
    const topCustomers = Object.entries(customerMap).map(([name, value]) => ({ name, value: Math.round(value / 1000000) })).sort((a, b) => b.value - a.value).slice(0, 5);

    return { total, pending, rangeInvoices: rangePayments, timeline, revenueByPlan, topCustomers };
  }, [adminPayments, revenueFrom, revenueTo]);

  const dashboardKpis: KpiItem[] = [
    { label: 'Tổng số doanh nghiệp', value: number(adminTeams.length), detail: `+${number(overview.newTeamsThisMonth)} tháng này`, icon: Building2, tone: 'blue', trend: 'up' },
    { label: 'Tổng số người dùng', value: number(adminUsers.length), detail: `+${number(overview.newUsersThisMonth)} tháng này`, icon: Users, tone: 'violet', trend: 'up' },
    { label: 'Doanh thu tháng này', value: money(overview.revenueThisMonth), detail: 'so với tháng trước', icon: DollarSign, tone: 'green', trend: 'up' },
    { label: 'Xưởng chờ duyệt', value: number(adminTeams.filter(t => t.verificationStatus === 'PENDING').length), detail: 'Cần xử lý', icon: AlertTriangle, tone: 'amber' },
  ];

  const systemTrendData = [
    { month: 'Jan', revenue: 120, companies: 45, users: 1200 },
    { month: 'Feb', revenue: 150, companies: 52, users: 1450 },
    { month: 'Mar', revenue: 180, companies: 61, users: 1680 },
    { month: 'Apr', revenue: 210, companies: 75, users: 1900 },
    { month: 'May', revenue: 250, companies: 88, users: 2200 },
    { month: 'Jun', revenue: 310, companies: 105, users: 2600 },
  ];

  const pendingRequests = adminTeams.filter(t => t.verificationStatus === 'PENDING');
  const approvedCompanies = adminTeams.filter(t => t.verificationStatus !== 'PENDING');

  const updateTeamVerification = async (teamId: string, nextStatus: 'APPROVED' | 'REJECTED') => {
    const rejectReason = nextStatus === 'REJECTED' ? window.prompt('Reject reason?') : '';
    if (nextStatus === 'REJECTED' && rejectReason === null) return;
    try {

```
