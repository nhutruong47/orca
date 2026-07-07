# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 6/12)

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
  "chunk_index": 5,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
                                ))}
                                </LineChart>
                            </ResponsiveContainer>
                        </SectionCard>
                    </div>

                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: 16, marginBottom: 20 }}>
                        <SectionCard title="Tiến độ nhóm">
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8, marginTop: -20 }}>
                                <span></span>
                                <span style={{ fontSize: 22, fontWeight: 800, color: '#16a34a' }}>{completionPct}%</span>
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
                                <ResponsiveContainer width={140} height={140}>
                                    <PieChart>
                                        <Pie data={donutData} innerRadius={40} outerRadius={65} dataKey="value" paddingAngle={2} startAngle={90} endAngle={-270}>
                                            {donutData.map((_, i) => <Cell key={i} fill={DONUT_COLORS[i % DONUT_COLORS.length]} />)}
                                        </Pie>
                                    </PieChart>
                                </ResponsiveContainer>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                                    {donutData.map((d, i) => (
                                        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 13 }}>
                                            <div style={{ width: 10, height: 10, borderRadius: 3, background: DONUT_COLORS[i % DONUT_COLORS.length] }} />
                                            <span style={{ color: '#475569' }}>{d.name}: <b>{d.value}</b></span>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </SectionCard>

                        <SectionCard title="So sánh thành viên">
                            <ResponsiveContainer width="100%" height={140}>

```
