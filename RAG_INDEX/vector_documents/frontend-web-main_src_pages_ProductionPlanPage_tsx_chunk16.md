# Knowledge Document: ProductionPlanPage.tsx (Chunk 17/22)

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
  "chunk_index": 16,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
                               cursor: savingTargetId === target.id ? 'not-allowed' : 'pointer',
                                                                opacity: savingTargetId === target.id ? 0.6 : 1
                                                            }}>
                                                                {savingTargetId === target.id ? 'Dang luu...' : 'Luu tien do'}
                                                            </button>
                                                        </div>
                                                    )}
                                                </div>

                                                {target.notes && (
                                                    <div style={{ marginTop: 8, fontSize: 12, color: 'var(--text-secondary)', fontStyle: 'italic' }}>Ghi chu: {target.notes}</div>
                                                )}
                                                {target.issues && (
                                                    <div style={{ marginTop: 6, fontSize: 12, color: '#ef4444', padding: '6px 10px', background: 'rgba(239,68,68,0.08)', borderRadius: 8 }}>
                                                        Van de: {target.issues}
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })}
                                </div>
                            )}
                        </div>
                    )}

                    {/* Tab: Attendance */}
                    {activeTab === 'attendance' && (
                        <div>
                            <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 16 }}>Cham cong</h2>
                            {!myAttendance ? (
                                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 28 }}>
                                    <div style={{ marginBottom: 20 }}>
                                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)', marginBottom: 8 }}>Chon ca lam viec</label>

```
