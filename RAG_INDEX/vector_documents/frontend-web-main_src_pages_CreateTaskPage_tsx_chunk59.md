# Knowledge Document: CreateTaskPage.tsx (Chunk 60/66)

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
  "chunk_index": 59,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                            flexShrink: 0
                                                }}>
                                                    <ion-icon name={task.suggestedAssignee || task.assignee ? 'person-circle-outline' : 'alert-circle-outline'}></ion-icon>
                                                </span>
                                                <div style={{ minWidth: 0 }}>
                                                    <div style={{
                                                        fontSize: 11,
                                                        lineHeight: 1.2,
                                                        color: task.suggestedAssignee || task.assignee ? '#047857' : '#92400e',
                                                        fontWeight: 900,
                                                        textTransform: 'uppercase'
                                                    }}>
                                                        Người phụ trách
                                                    </div>
                                                    <div style={{
                                                        marginTop: 2,
                                                        fontSize: 15,
                                                        color: 'var(--text-primary)',
                                                        fontWeight: 900,
                                                        overflow: 'hidden',
                                                        textOverflow: 'ellipsis',
                                                        whiteSpace: 'nowrap'
                                                    }}>
                                                        {task.suggestedAssignee || task.assignee || 'Chưa chọn'}
                                                    </div>
                                                </div>
                                            </div>

                                            <div>
                                                <label style={{ display: 'block', marginBottom: 6, fontSize: 12, color: 'var(--text-secondary)', fontWeight: 850 }}>Chọn member</label>
                                                <select
                                                    value={task.suggestedAssigneeId || ''}

```
