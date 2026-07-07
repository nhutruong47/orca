# Knowledge Document: ProductionPlanPage.tsx (Chunk 7/22)

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
  "chunk_index": 6,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
ntWeight: 600 }}>
                                    Con lai: {(selectedOrder.remainingQuantity || 0).toLocaleString()} kg
                                </div>
                            </div>
                        </div>
                        {selectedOrder.progressPercent !== undefined && selectedOrder.progressPercent > 0 && (
                            <div style={{ marginTop: 16 }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginBottom: 4 }}>
                                    <span style={{ color: 'var(--text-secondary)' }}>Tien do</span>
                                    <span style={{ fontWeight: 700, color: '#10b981' }}>{selectedOrder.progressPercent.toFixed(0)}%</span>
                                </div>
                                <div style={{ background: 'var(--bg-input)', borderRadius: 6, height: 8 }}>
                                    <div style={{ width: `${selectedOrder.progressPercent}%`, height: '100%', background: '#10b981', borderRadius: 6 }} />
                                </div>
                            </div>
                        )}
                    </div>

                    {/* Tabs */}
                    <div style={{ display: 'flex', gap: 4, marginBottom: 20, background: 'var(--bg-input)', borderRadius: 10, padding: 4, width: 'fit-content' }}>
                        {[['overview', 'Tong quan'], ['daily', 'Muc tieu ngay'], ['attendance', 'Cham cong']].map(([tab, label]) => (
                            <button key={tab} onClick={() => setActiveTab(tab as any)} style={{
                                padding: '8px 20px', borderRadius: 8, border: 'none', cursor: 'pointer', fontSize: 13, fontWeight: 600,
                                background: activeTab === tab ? '#fff' : 'transparent',
                                color: activeTab === tab ? 'var(--text-primary)' : 'var(--text-secondary)',
                                boxShadow: activeTab === tab ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'
                            }}>{label}</button>
                        ))}
                    </div>

                    {/* Tab: Overview */}
                    {activeTab === 'overview' && (
                        <div>

```
