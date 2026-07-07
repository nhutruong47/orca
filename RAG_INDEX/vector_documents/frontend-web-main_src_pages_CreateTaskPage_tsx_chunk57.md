# Knowledge Document: CreateTaskPage.tsx (Chunk 58/66)

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
  "chunk_index": 57,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
             value={task.description || ''}
                                                onChange={e => updateTaskDescription(idx, e.target.value)}
                                                rows={4}
                                                style={{
                                                    width: '100%',
                                                    minHeight: 112,
                                                    padding: '13px 14px',
                                                    borderRadius: 14,
                                                    border: '1px solid #cbd5e1',
                                                    background: 'var(--bg-input)',
                                                    color: 'var(--text-primary)',
                                                    fontSize: 14,
                                                    lineHeight: 1.55,
                                                    resize: 'vertical',
                                                    outline: 'none',
                                                    fontFamily: 'inherit'
                                                }}
                                            />
                                            <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
                                                <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, padding: '5px 9px', borderRadius: 999, background: 'var(--bg-secondary)', color: 'var(--text-secondary)', fontSize: 12, fontWeight: 750 }}>
                                                    <ion-icon name="barbell-outline"></ion-icon>
                                                    Workload: {task.workload || 1}
                                                </span>
                                                <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, padding: '5px 9px', borderRadius: 999, background: 'rgba(249, 115, 22, 0.1)', color: 'var(--warning)', fontSize: 12, fontWeight: 750 }}>
                                                    <ion-icon name="flag-outline"></ion-icon>
                                                    Priority: {task.priority || 2}
                                                </span>
                                            </div>

```
