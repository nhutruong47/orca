# Knowledge Document: ProductionPlanPage.tsx (Chunk 10/22)

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
  "chunk_index": 9,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
Ngay lam viec: <strong style={{ color: 'var(--text-primary)' }}>{plan.totalWorkingDays}</strong>
                                            </div>
                                            {plan.riskFactors && (
                                                <div style={{ marginTop: 8, fontSize: 12, color: '#f59e0b', padding: '6px 10px', background: 'rgba(245,158,11,0.1)', borderRadius: 8 }}>
                                                    ⚠️ {plan.riskFactors}
                                                </div>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            )}

                            {/* Selected Plan Details */}
                            {selectedPlan && (
                                <div style={{ marginTop: 20, background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 20 }}>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
                                        <h3 style={{ fontSize: 15, fontWeight: 700 }}>Chi tiet ke hoach: {selectedPlan.planCode}</h3>
                                        {selectedPlan.status === 'DRAFT' && (
                                            <button onClick={handleApprovePlan} disabled={approving} style={{
                                                padding: '8px 20px', borderRadius: 10, border: 'none',
                                                background: 'linear-gradient(135deg, #10b981, #059669)',
                                                color: '#fff', fontSize: 13, fontWeight: 700, cursor: approving ? 'not-allowed' : 'pointer'
                                            }}>
                                                {approving ? 'Dang duyet...' : 'Duyet ke hoach'}
                                            </button>
                                        )}
                                    </div>

                                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 16, marginBottom: 20 }}>
                                        {[
                                            ['Ngay lam viec', selectedPlan.totalWorkingDays + ' ngay'],

```
