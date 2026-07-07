# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 5/12)

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
  "chunk_index": 4,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
             padding: '8px 16px', borderRadius: 10, border: 'none',
                    background: 'linear-gradient(135deg, #10b981, #059669)', color: '#fff',
                    fontSize: 13, fontWeight: 700, cursor: 'pointer'
                }}>Tai lai</button>
            </div>

            {/* KPI */}
            <div style={{ display: 'flex', gap: 12, marginBottom: 20, flexWrap: 'wrap' }}>
                <MetricPill label="Tong don" value={os.total || 0} color="#8b5cf6" />
                <MetricPill label="Dang san xuat" value={os.inProduction || 0} color="#f59e0b" />
                <MetricPill label="Co nguy co" value={os.atRisk || 0} color="#ef4444" />
                <MetricPill label="Nang suat TB" value={(data?.overallProductivity || 0).toFixed(2)} unit=" kg/gio" color="#10b981" />
            </div>

            
            {/* ===== TASK STATS ===== */}
            {totalTasks > 0 && (
                <>
                    <div style={{ marginBottom: 20 }}>
                        <SectionCard title="Hiệu suất nhân viên trong tuần">
                            <ResponsiveContainer width="100%" height={220}>
                                <LineChart data={lineData} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                                    <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                                    <XAxis dataKey="day" tick={{ fontSize: 12, fill: '#94a3b8' }} />
                                    <YAxis tick={{ fontSize: 12, fill: '#94a3b8' }} domain={[0, 100]} tickFormatter={v => `${v}%`} />
                                    <Tooltip formatter={(v: any) => `${v}%`} />
                                    <Legend />
                                    {memberStats.map((m: any) => (
                                        <Line key={m.userId} type="monotone" dataKey={m.fullName || m.username} stroke={m.color} strokeWidth={2.5} dot={{ r: 3 }} activeDot={{ r: 5 }} />
                                    ))}
                                </LineChart>
                            </ResponsiveContainer>
                        </SectionCard>
                    </div>

                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: 16, marginBottom: 20 }}>
                        <SectionCard title="Tiến độ nhóm">

```
