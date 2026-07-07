# Knowledge Document: ProductionPlanPage.tsx (Chunk 8/22)

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
  "chunk_index": 7,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
or: activeTab === tab ? 'var(--text-primary)' : 'var(--text-secondary)',
                                boxShadow: activeTab === tab ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'
                            }}>{label}</button>
                        ))}
                    </div>

                    {/* Tab: Overview */}
                    {activeTab === 'overview' && (
                        <div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
                                <h2 style={{ fontSize: 16, fontWeight: 700 }}>Ke hoach AI</h2>
                                <button onClick={handleGeneratePlan} disabled={generating} style={{
                                    padding: '8px 18px', borderRadius: 10, border: 'none',
                                    background: generating ? 'var(--bg-input)' : 'linear-gradient(135deg, #8b5cf6, #7c3aed)',
                                    color: '#fff', fontSize: 13, fontWeight: 700, cursor: generating ? 'not-allowed' : 'pointer'
                                }}>
                                    {generating ? 'Dang tao...' : 'Tao ke hoach AI'}
                                </button>
                            </div>

                            {plans.length === 0 ? (
                                <div style={{ textAlign: 'center', padding: 40, background: 'var(--bg-card)', borderRadius: 14, border: '1px solid var(--border)', color: 'var(--text-muted)' }}>
                                    Chua co ke hoach nao. Nhan "Tao ke hoach AI" de bat dau.
                                </div>
                            ) : (
                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: 12 }}>
                                    {plans.map(plan => (
                                        <div key={plan.id} onClick={() => { setSelectedPlan(plan); loadPlanTargets(plan.id!); }}
                                            style={{
                                                padding: 16, background: 'var(--bg-card)', border: `2px solid ${selectedPlan?.id === plan.id ? '#8b5cf6' : 'var(--border)'}`,
                                                borderRadius: 14, cursor: 'pointer'
                                            }}>

```
