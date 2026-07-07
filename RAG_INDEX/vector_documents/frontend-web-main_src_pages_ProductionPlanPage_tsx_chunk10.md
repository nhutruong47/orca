# Knowledge Document: ProductionPlanPage.tsx (Chunk 11/22)

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
  "chunk_index": 10,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
                    </button>
                                        )}
                                    </div>

                                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 16, marginBottom: 20 }}>
                                        {[
                                            ['Ngay lam viec', selectedPlan.totalWorkingDays + ' ngay'],
                                            ['Muc tieu/ngay', `${(selectedPlan.dailyTargetKg || 0).toLocaleString()} kg`],
                                            ['Tong rang', `${(selectedPlan.totalRoastKg || 0).toLocaleString()} kg`],
                                            ['Tong QC', `${(selectedPlan.totalQcKg || 0).toLocaleString()} kg`],
                                            ['Tong dong goi', `${(selectedPlan.totalPackagedKg || 0).toLocaleString()} kg`],
                                            ['Tong goi', selectedPlan.totalPackages + ' goi'],
                                            ['Nguyen lieu can', `${(selectedPlan.totalInputKg || 0).toLocaleString()} kg`],
                                            ['Rui ro', selectedPlan.riskFactors || 'Khong co'],
                                        ].map(([label, value]) => (
                                            <div key={label as string} style={{ background: 'var(--bg-input)', borderRadius: 10, padding: '12px 14px' }}>
                                                <div style={{ fontSize: 11, color: 'var(--text-muted)', marginBottom: 4 }}>{label}</div>
                                                <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-primary)' }}>{value}</div>
                                            </div>
                                        ))}
                                    </div>

                                    {selectedPlan.aiRecommendations && (
                                        <div style={{ background: 'rgba(139,92,246,0.06)', border: '1px solid rgba(139,92,246,0.2)', borderRadius: 10, padding: 14 }}>
                                            <div style={{ fontSize: 12, fontWeight: 700, color: '#8b5cf6', marginBottom: 8 }}>AI De xuat</div>
                                            <pre style={{ fontSize: 12, color: 'var(--text-secondary)', whiteSpace: 'pre-wrap', margin: 0, fontFamily: 'inherit' }}>

```
