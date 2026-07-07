# Knowledge Document: FactoryDashboardPage.tsx (Chunk 12/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 11,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
                                            {staff.orderTitle && ` · ${staff.orderTitle}`}
                                        </div>
                                    </div>
                                    <div style={{ textAlign: 'right' }}>
                                        <div style={{ fontWeight: 700, fontSize: 14, color: staff.workHours ? '#10b981' : 'var(--text-muted)' }}>
                                            {staff.workHours ? `${(staff.workHours as number).toFixed(1)}h` : 'Dang lam'}
                                        </div>
                                        <div style={{ fontSize: 11, color: staff.attendanceStatus === 'LATE' ? '#ef4444' : 'var(--text-muted)' }}>
                                            {staff.attendanceStatus === 'LATE' ? 'Di tre' : staff.attendanceStatus === 'MISSING_CHECKOUT' ? 'Chua check-out' : 'On time'}
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </div>

            {/* Section D: Stats */}
            {dashboard.stats && (
                <div style={{ marginBottom: 32 }}>
                    <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 12, color: 'var(--text-primary)' }}>Thong ke</h2>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 12 }}>
                        {[
                            { label: 'Da hoan thanh', value: dashboard.stats.completedOrders, color: '#10b981' },
                            { label: 'Dang san xuat', value: dashboard.stats.inProductionOrders, color: '#3b82f6' },
                            { label: 'Cho xu ly', value: dashboard.stats.pendingOrders, color: '#f59e0b' },
                            { label: 'Tong don', value: dashboard.stats.totalOrders, color: 'var(--text-secondary)' },
                        ].map(stat => (
                            <div key={stat.label} style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 12, padding: 16, textAlign: 'center' }}>
                                <div style={{ fontSize: 24, fontWeight: 800, color: stat.color }}>{stat.value}</div>

```
