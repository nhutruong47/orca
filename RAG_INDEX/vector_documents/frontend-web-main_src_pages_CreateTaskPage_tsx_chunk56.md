# Knowledge Document: CreateTaskPage.tsx (Chunk 57/66)

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
  "chunk_index": 56,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                                          </div>
                                        </div>
                                        <button
                                            onClick={() => removeTask(idx)}
                                            aria-label="Xóa task"
                                            title="Xóa task"
                                            style={{
                                                width: 34,
                                                height: 34,
                                                borderRadius: '50%',
                                                background: 'rgba(239, 68, 68, 0.1)',
                                                border: '1px solid #fecdd3',
                                                color: '#e11d48',
                                                cursor: 'pointer',
                                                fontSize: 20,
                                                display: 'grid',
                                                placeItems: 'center',
                                                flexShrink: 0
                                            }}
                                        >
                                            <ion-icon name="close-circle-outline"></ion-icon>
                                        </button>
                                    </div>

                                    <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0, 1.45fr) minmax(260px, 0.8fr)', gap: 16, alignItems: 'stretch' }}>
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, minWidth: 0 }}>
                                            <label style={{ fontSize: 12, fontWeight: 850, color: 'var(--text-secondary)' }}>Mô tả chi tiết</label>
                                            <textarea
                                                value={task.description || ''}
                                                onChange={e => updateTaskDescription(idx, e.target.value)}
                                                rows={4}
                                                style={{
                                                    width: '100%',
                                                    minHeight: 112,

```
