# Knowledge Document: CreateTaskPage.tsx (Chunk 56/66)

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
  "chunk_index": 55,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                                 display: 'inline-flex',
                                                alignItems: 'center',
                                                justifyContent: 'center',
                                                background: '#ede9fe',
                                                color: '#6d28d9',
                                                fontSize: 13,
                                                fontWeight: 800
                                            }}>{idx + 1}</span>
                                            <div style={{ minWidth: 0 }}>
                                                <div style={{ fontSize: 12, color: '#7c3aed', fontWeight: 900, textTransform: 'uppercase' }}>Task draft</div>
                                                <input
                                                    type="text"
                                                    value={task.title || ''}
                                                    onChange={e => updateTaskTitle(idx, e.target.value)}
                                                    style={{
                                                        width: '100%',
                                                        minWidth: 0,
                                                        marginTop: 3,
                                                        padding: 0,
                                                        border: 0,
                                                        background: 'transparent',
                                                        color: 'var(--text-primary)',
                                                        fontSize: 17,
                                                        fontWeight: 850,
                                                        outline: 'none'
                                                    }}
                                                />
                                            </div>
                                        </div>
                                        <button
                                            onClick={() => removeTask(idx)}
                                            aria-label="Xóa task"
                                            title="Xóa task"
                                            style={{

```
