# Knowledge Document: ProductionCalendarPage.tsx (Chunk 2/12)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionCalendarPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
split('T')[0]);
    };
    const nextWeek = () => {
        const d = new Date(new Date(weekStart).getTime() + 14 * 86400000);
        setWeekStart(d.toISOString().split('T')[0]);
    };
    const thisWeek = () => {
        const d = new Date();
        d.setDate(today.getDate() - today.getDay() + 1);
        setWeekStart(d.toISOString().split('T')[0]);
    };

    const formatWeekRange = () => {
        const start = new Date(weekStart);
        const end = new Date(new Date(weekStart).getTime() + 13 * 86400000);
        const fmt = (d: Date) => d.toLocaleDateString('vi-VN', { day: '2-digit', month: '2-digit' });
        return `${fmt(start)} - ${fmt(end)}`;
    };

    const dayName = (d: Date) => ['CN', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'][d.getDay()];
    const isWeekend = (d: Date) => d.getDay() === 0 || d.getDay() === 6;
    const isToday = (d: Date) => {
        const t = new Date();
        return d.toDateString() === t.toDateString();
    };

    return (
        <div style={{ padding: 24, margin: '0 auto' }}>
            {/* Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                    <button onClick={() => navigate(`/groups/${teamId}`)} style={{
                        background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                        width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                        color: 'var(--text-secondary)', fontSize: 18,
                    }}>
                        <ion-icon name="chevron-back-outline" />
                    </button>
                    <div>
                        <h1 style={{ fontSize: 22, fontWeight: 800, color: 'var(--text-primary)', marginBottom: 4 }}>Lich San Xuat</h1>
                        <p style={{ color: 'var(--text-secondary)', fontSize: 13 }}>{formatWeekRange()}</p>
                    </div>
                </div>
                <div style={{ display: 'flex', gap: 8 }}>
                    <button onClick={prevWeek} style={{
                        padding: '8px 16px', borderRadius: 10, border: '1px solid var(--border)',

```
