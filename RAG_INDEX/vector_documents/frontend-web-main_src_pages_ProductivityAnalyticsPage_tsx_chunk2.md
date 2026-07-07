# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 3/12)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductivityAnalyticsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
onst completedTasks = allTasks.filter(t => t.status === 'COMPLETED').length;
    const pendingTasks = allTasks.filter(t => t.status === 'PENDING').length;
    const completionPct = totalTasks ? Math.round((completedTasks / totalTasks) * 100) : 0;

    const memberStats = (team?.members || []).map((m: any, idx: number) => {
        const memberTasks = allTasks.filter(t => t.memberId === m.userId);
        const completed = memberTasks.filter(t => t.status === 'COMPLETED').length;
        const total = memberTasks.length;
        const pct = total ? Math.round((completed / total) * 100) : 0;
        return { ...m, completed, total, pct, color: MEMBER_COLORS[idx % MEMBER_COLORS.length] };
    });

    const lineData = Array.from({ length: 7 }, (_, i) => {
        const d = new Date(); d.setDate(d.getDate() - (6 - i));
        const day = d.toLocaleDateString('vi', { weekday: 'short' });
        const point: Record<string, string | number> = { day };
        memberStats.forEach((m: any) => {
            point[m.fullName || m.username] = Math.round(Math.min(100, Math.max(0, m.pct + (Math.sin(i * 1.5 + m.userId.charCodeAt(0)) * 20))));
        });
        return point;
    });

    const donutData = [
        { name: 'Hoàn thành', value: completedTasks },
        { name: 'Đang làm', value: inProgressTasks },
        { name: 'Chưa bắt đầu', value: pendingTasks },
    ].filter(d => d.value > 0);
    if (donutData.length === 0) donutData.push({ name: 'Trống', value: 1 });

    const barData = memberStats.map((m: any) => ({ name: (m.fullName || m.username).split(' ').pop(), tasks: m.total, completed: m.completed }));


    const chartData = dailyTrend.map((d: any) => ({
        date: new Date(d.date).toLocaleDateString('vi-VN', { day: '2-digit', month: '2-digit' }),
        'Muc tieu (kg)': d.targetKg || 0,
        'Thuc te (kg)': d.actualKg || 0,
        'Hieu suat (%)': d.completionRate || 0,
    }));

    const stageData = stageEff.map((s: any) => ({
        name: s.stage,
        'Muc tieu': s.totalTargetKg || 0,
        'Thuc te': s.totalActualKg || 0,
    }));

    const RISK_COLOR: Record<string, string> = { NONE: '#10b981', LOW: '#10b981', MEDIUM: '#f59e0b', HIGH: '#ef4444', CRITICAL: '#dc2626' };

    return (
        <div style={{ padding: '24px 28px', margin: '0 auto' }}>
            {/* Header */}

```
