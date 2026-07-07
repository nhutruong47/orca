# Knowledge Document: AdminPage.tsx (Chunk 5/16)

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
  "chunk_index": 4,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx

        setOverview({ ...emptyOverview, ...overviewData });
        setAdminUsers(userData || []);
        setAdminTeams(teamData || []);
        setAdminPayments(paymentData || []);
      })
      .catch(() => {
        setAdminError('Không tải được thống kê thật từ hệ thống.');
      })
      .finally(() => setAdminLoading(false));
  }, [user?.role]);



  const revenueReport = useMemo(() => {
    const fromDate = parseDateInput(revenueFrom);
    const toDate = parseDateInput(revenueTo, true);
    const safeFrom = fromDate <= toDate ? fromDate : toDate;
    const safeTo = fromDate <= toDate ? toDate : fromDate;
    const rangePayments = adminPayments.filter(item => {
      const date = paymentDate(item);
      return Boolean(date && date >= safeFrom && date <= safeTo);
    });
    const paidPayments = rangePayments.filter(item => item.status === 'PAID');
    const total = paidPayments.reduce((sum, item) => sum + Number(item.amount), 0);
    const pending = rangePayments.filter(item => item.status === 'PENDING').reduce((sum, item) => sum + Number(item.amount), 0);
    
    const dailyMap = paidPayments.reduce<Record<string, { amount: number; time: number }>>((acc, item) => {
      const date = paymentDate(item);
      const dateKey = formatShortDate(date);
      const current = acc[dateKey] || { amount: 0, time: date?.getTime() || 0 };
      acc[dateKey] = { amount: current.amount + Number(item.amount), time: current.time };
      return acc;
    }, {});
    
    const timeline = Object.entries(dailyMap)
      .map(([date, data]) => ({ date, revenue: Math.round(data.amount / 1000000), time: data.time }))
      .sort((a, b) => a.time - b.time);
      
    const planMap = paidPayments.reduce<Record<string, number>>((acc, item) => {
      const planName = !item.planId || item.planId === 'free' ? 'Dùng thử' : item.planId === 'professional' ? 'Chuyên nghiệp' : item.planId === 'enterprise' ? 'Doanh nghiệp' : item.planId;
      acc[planName] = (acc[planName] || 0) + Number(item.amount);
      return acc;
    }, {});
    
    const revenueByPlan = Object.entries(planMap).map(([name, value]) => ({ name, value: Math.round(value / 1000000), amount: value })).sort((a, b) => b.amount - a.amount);
    
    const customerMap = paidPayments.reduce<Record<string, number>>((acc, item) => {
      const name = paymentCustomerName(item);

```
