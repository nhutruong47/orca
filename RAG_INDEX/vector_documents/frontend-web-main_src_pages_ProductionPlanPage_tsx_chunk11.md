# Knowledge Document: ProductionPlanPage.tsx (Chunk 12/22)

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
  "chunk_index": 11,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
,92,246,0.06)', border: '1px solid rgba(139,92,246,0.2)', borderRadius: 10, padding: 14 }}>
                                            <div style={{ fontSize: 12, fontWeight: 700, color: '#8b5cf6', marginBottom: 8 }}>AI De xuat</div>
                                            <pre style={{ fontSize: 12, color: 'var(--text-secondary)', whiteSpace: 'pre-wrap', margin: 0, fontFamily: 'inherit' }}>
                                                {selectedPlan.aiRecommendations}
                                            </pre>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    )}

                    {/* Tab: Daily Target */}
                    {activeTab === 'daily' && (
                        <div>
                            <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 16 }}>Muc tieu theo ngay</h2>
                            {dailyTargets.length === 0 ? (
                                <div style={{ textAlign: 'center', padding: 40, background: 'var(--bg-card)', borderRadius: 14, border: '1px solid var(--border)', color: 'var(--text-muted)' }}>
                                    Tao ke hoach AI truoc de xem muc tieu ngay
                                </div>
                            ) : (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                                    {dailyTargets.map(target => {
                                        const isToday = target.targetDate === new Date().toISOString().split('T')[0];
                                        const stage = (selectedOrder?.productType as string) || 'RANG';
                                        const unit = unitForStage(stage);
                                        const edit = target.id ? targetEdits[target.id] : undefined;
                                        const targetQty = edit?.target ?? (target.targetQuantity || target.targetRoastKg || 0);
                                        const actualQty = edit?.actual ?? (target.actualQuantity || target.actualRoastKg || 0);
                                        const cappedActual = Math.min(actualQty, targetQty);

```
