# Knowledge Document: CreateTaskPage.tsx (Chunk 63/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 62,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx

                                                        padding: '7px 10px',
                                                        fontSize: 12,
                                                        fontWeight: 850,
                                                        cursor: 'pointer'
                                                    }}
                                                >
                                                    Bỏ gợi ý
                                                </button>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            ))}
                            <button
                                onClick={addTask}
                                style={{
                                    alignSelf: 'flex-start', background: '#f5f3ff', border: '1px solid #ddd6fe',
                                    color: '#7c3aed', padding: '8px 16px', borderRadius: '10px',
                                    fontSize: 12, fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6
                                }}
                            >
                                <ion-icon name="add-outline"></ion-icon> Thêm mục
                            </button>
                        </div>
                    </div>

                    {/* Deadline & Priority Row */}
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24 }}>
                        <div>
                            <label style={{ display: 'block', fontSize: 13, fontWeight: 700, color: 'var(--text-secondary)', marginBottom: 8 }}>Hạn chót</label>
                            <input
                                type="text"
                                value={editedResult.deadline || ''}
                                onChange={e => updateField('deadline', e.target.value)}
                                style={{
                                    width: '100%', padding: '12px 16px', borderRadius: '12px',
                                    border: '1px solid var(--border)', background: 'var(--bg-card)',
                                    color: 'var(--text-primary)', fontSize: 14, outline: 'none'
                                }}

```
