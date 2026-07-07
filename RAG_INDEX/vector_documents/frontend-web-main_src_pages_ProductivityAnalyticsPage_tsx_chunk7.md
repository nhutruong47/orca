# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 8/12)

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
  "chunk_index": 7,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 10, fontSize: 13 }} />
                                <Legend />
                                <Line type="monotone" dataKey="Muc tieu (kg)" stroke="#94a3b8" strokeWidth={2} dot={false} />
                                <Line type="monotone" dataKey="Thuc te (kg)" stroke="#10b981" strokeWidth={2} dot={false} />
                            </LineChart>
                        </ResponsiveContainer>
                    </SectionCard>
                </div>
            )}

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginBottom: 20 }}>
                {/* Hieu suat theo cong doan */}
                <SectionCard title="Hieu suat theo Cong doan">
                    {stageData.length > 0 ? (
                        <ResponsiveContainer width="100%" height={200}>
                            <BarChart data={stageData} margin={{ top: 5, right: 10, bottom: 5, left: 0 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
                                <XAxis dataKey="name" tick={{ fontSize: 12 }} />
                                <YAxis tick={{ fontSize: 11 }} />
                                <Tooltip contentStyle={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 10, fontSize: 13 }} />
                                <Legend />
                                <Bar dataKey="Muc tieu" fill="#e5e7eb" />
                                <Bar dataKey="Thuc te" fill="#10b981" />
                            </BarChart>
                        </ResponsiveContainer>
                    ) : (
                        <div style={{ textAlign: 'center', padding: 40, color: 'var(--text-muted)', fontSize: 13 }}>Chua co du lieu</div>
                    )}
                </SectionCard>

                {/* Thong ke don hang */}
                <SectionCard title="Thong ke Don hang">
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 0 }}>
                        {[
                            { label: 'Da hoan thanh', value: os.completed || 0, color: '#10b981' },
                            { label: 'Dang san xuat', value: os.inProduction || 0, color: '#3b82f6' },

```
