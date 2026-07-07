# Knowledge Document: GroupDetailPage.tsx (Chunk 99/136)

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
  "chunk_index": 98,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
y: 'flex', alignItems: 'center' }}>
                                                                <span style={{ position: 'absolute', right: 8, fontSize: 10, fontWeight: 800, color: '#fff' }}>{count} task</span>
                                                            </div>
                                                        </div>
                                                    );
                                                });
                                            })()}
                                        </div>
                                    </div>
                                </div>
                                </>
                            );
                        })()}

                        {/* Footer buttons */}
                        <div style={{ marginTop: 12, borderTop: '1px solid var(--border, #334155)', paddingTop: 20, textAlign: 'right' }}>
                            <button onClick={() => setShowStatsModal(false)} style={{ background: '#d4a574', color: '#fff', border: 'none', padding: '12px 36px', borderRadius: 12, fontWeight: 700, cursor: 'pointer', fontSize: 14, boxShadow: '0 4px 12px rgba(212,165,116,0.2)', transition: 'all 0.2s' }}>Đóng báo cáo</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Schedule Modal */}
            {showScheduleModal && (
                <div className="modal-overlay" onClick={() => setShowScheduleModal(false)} style={{ background: 'rgba(10, 10, 12, 0.85)', backdropFilter: 'blur(10px)', zIndex: 10000, position: 'fixed', inset: 0, display: 'grid', placeItems: 'center', transition: 'all 0.3s ease' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 1250, width: '92%', background: '#121214', color: '#ffffff', borderRadius: 20, padding: '24px', border: '1px solid #232328', maxHeight: '92vh', overflowY: 'auto', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.6)', display: 'flex', flexDirection: 'column', gap: '20px', fontFamily: "'Inter', sans-serif" }}>
                        {/* Header */}
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #232328', paddingBottom: 16 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>

```
