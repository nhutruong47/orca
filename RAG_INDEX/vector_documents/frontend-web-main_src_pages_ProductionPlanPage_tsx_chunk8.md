# Knowledge Document: ProductionPlanPage.tsx (Chunk 9/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
lan(plan); loadPlanTargets(plan.id!); }}
                                            style={{
                                                padding: 16, background: 'var(--bg-card)', border: `2px solid ${selectedPlan?.id === plan.id ? '#8b5cf6' : 'var(--border)'}`,
                                                borderRadius: 14, cursor: 'pointer'
                                            }}>
                                            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 10 }}>
                                                <span style={{ fontSize: 12, fontWeight: 700, color: '#8b5cf6' }}>{plan.planCode}</span>
                                                <span style={{ fontSize: 11, fontWeight: 600, padding: '2px 8px', borderRadius: 4, background: plan.status === 'APPROVED' ? '#10b98120' : '#8b5cf620', color: plan.status === 'APPROVED' ? '#10b981' : '#8b5cf6' }}>
                                                    {STATUS_LABELS[plan.status] || plan.status}
                                                </span>
                                            </div>
                                            {plan.dailyTargets && (
                                                <div style={{ fontSize: 12, color: 'var(--text-muted)', marginBottom: 6 }}>
                                                    {plan.dailyTargets.length} ngay ke hoach
                                                </div>
                                            )}
                                            <div style={{ fontSize: 13, color: 'var(--text-secondary)' }}>
                                                Muc tieu ngay: <strong style={{ color: 'var(--text-primary)' }}>{(plan.dailyTargetKg || 0).toLocaleString()} kg</strong>
                                            </div>
                                            <div style={{ fontSize: 13, color: 'var(--text-secondary)' }}>
                                                Ngay lam viec: <strong style={{ color: 'var(--text-primary)' }}>{plan.totalWorkingDays}</strong>
                                            </div>
                                            {plan.riskFactors && (
                                                <div style={{ marginTop: 8, fontSize: 12, color: '#f59e0b', padding: '6px 10px', background: 'rgba(245,158,11,0.1)', borderRadius: 8 }}>

```
