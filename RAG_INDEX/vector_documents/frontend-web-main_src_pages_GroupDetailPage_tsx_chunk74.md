# Knowledge Document: GroupDetailPage.tsx (Chunk 75/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 74,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
"checkbox" checked={isPublished} onChange={e => setIsPublished(e.target.checked)} style={{ width: 16, height: 16 }} />
                            <label style={{ fontSize: 14, fontWeight: 600 }}>Công khai trên Marketplace</label>
                        </div>
                        {isPublished && (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                <input value={adRegion} onChange={e => setAdRegion(e.target.value)} placeholder="Khu vực" style={{ padding: '10px 14px', borderRadius: 8, border: '1px solid #e2e8f0', fontSize: 14 }} />
                                <input value={adSpecialty} onChange={e => setAdSpecialty(e.target.value)} placeholder="Chuyên môn" style={{ padding: '10px 14px', borderRadius: 8, border: '1px solid #e2e8f0', fontSize: 14 }} />
                                <input value={adCapacity} onChange={e => setAdCapacity(e.target.value)} placeholder="Năng suất" style={{ padding: '10px 14px', borderRadius: 8, border: '1px solid #e2e8f0', fontSize: 14 }} />
                            </div>
                        )}
                        <div style={{ display: 'flex', gap: 8, justifyContent: 'flex-end', marginTop: 20 }}>
                            <button onClick={() => setShowAdSettings(false)} style={{ padding: '10px 20px', borderRadius: 8, border: '1px solid #e2e8f0', background: '#fff', color: '#64748b', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Thoát</button>
                            <button onClick={handleSaveAdSettings} disabled={loading} style={{ padding: '10px 20px', borderRadius: 8, border: 'none', background: '#d4a574', color: '#fff', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>{loading ? 'Đang lưu...' : 'Lưu'}</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Job Labels Modal */}
            {showLabelModal && selectedMemberForLabels && (
                <div className="modal-overlay" onClick={() => setShowLabelModal(false)} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(4px)', zIndex: 1000 }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 400, background: '#fff', color: '#1a1a1a', borderRadius: 16, padding: '24px' }}>

```
