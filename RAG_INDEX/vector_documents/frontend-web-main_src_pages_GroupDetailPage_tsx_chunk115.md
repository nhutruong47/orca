# Knowledge Document: GroupDetailPage.tsx (Chunk 116/136)

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
  "chunk_index": 115,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
style={{ fontSize: 11, fontWeight: 700, color: '#f59e0b' }}>{formatted}</div>
                                                                        <div style={{ fontSize: 9, color: '#8e8e93', textTransform: 'uppercase', marginTop: 1 }}>Hạn chót</div>
                                                                    </div>
                                                                </div>
                                                            );
                                                        })}
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    </div>

                                </div>
                            );
                        })()}

                        {/* Footer buttons */}
                        <div style={{ marginTop: 12, borderTop: '1px solid #232328', paddingTop: 16, display: 'flex', justifyContent: 'flex-end' }}>
                            <button onClick={() => setShowScheduleModal(false)} style={{ background: 'rgba(255, 255, 255, 0.08)', color: '#ffffff', border: 'none', padding: '10px 32px', borderRadius: 10, fontWeight: 600, cursor: 'pointer', fontSize: 13, transition: 'background 0.2s' }} onMouseEnter={e => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.15)'} onMouseLeave={e => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.08)'}>Đóng</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Modal Lịch sử vào ra ca */}
            {showAttendanceHistory && (
                <div className="modal-overlay" onClick={() => setShowAttendanceHistory(false)} style={{ background: 'rgba(10, 10, 12, 0.85)', backdropFilter: 'blur(10px)', zIndex: 10000, position: 'fixed', inset: 0, display: 'grid', placeItems: 'center' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 900, minWidth: 'min(90vw, 750px)', width: '100%', background: '#121214', color: '#ffffff', borderRadius: 20, padding: '32px', border: '1px solid #232328', maxHeight: '80vh', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '24px' }}>

```
