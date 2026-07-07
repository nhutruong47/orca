# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 7/12)

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
  "chunk_index": 6,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
={{ color: '#475569' }}>{d.name}: <b>{d.value}</b></span>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </SectionCard>

                        <SectionCard title="So sánh thành viên">
                            <ResponsiveContainer width="100%" height={140}>
                                <BarChart data={barData} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                                    <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                                    <XAxis dataKey="name" tick={{ fontSize: 11, fill: '#94a3b8' }} />
                                    <YAxis tick={{ fontSize: 11, fill: '#94a3b8' }} />
                                    <Tooltip />
                                    <Bar dataKey="completed" fill="#d4a574" radius={[4, 4, 0, 0]} name="Hoàn thành" />
                                    <Bar dataKey="tasks" fill="#e2e8f0" radius={[4, 4, 0, 0]} name="Tổng" />
                                </BarChart>
                            </ResponsiveContainer>
                        </SectionCard>
                    </div>
                </>
            )}

            {/* Bieu do xu huong */}

            {chartData.length > 0 && (
                <div style={{ marginBottom: 20 }}>
                    <SectionCard title="Xu huong San Xuat">
                        <ResponsiveContainer width="100%" height={220}>
                            <LineChart data={chartData} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
                                <XAxis dataKey="date" tick={{ fontSize: 11, fill: 'var(--text-muted)' }} />
                                <YAxis tick={{ fontSize: 11, fill: 'var(--text-muted)' }} />
                                <Tooltip contentStyle={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 10, fontSize: 13 }} />
                                <Legend />
                                <Line type="monotone" dataKey="Muc tieu (kg)" stroke="#94a3b8" strokeWidth={2} dot={false} />
                                <Line type="monotone" dataKey="Thuc te (kg)" stroke="#10b981" strokeWidth={2} dot={false} />

```
