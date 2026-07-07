# Knowledge Document: CreateTaskPage.tsx (Chunk 62/66)

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
  "chunk_index": 61,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
               ))}
                                                </select>
                                            </div>

                                            <div style={{
                                                padding: 10,
                                                borderRadius: 12,
                                                background: 'rgba(255,255,255,0.72)',
                                                fontSize: 12,
                                                lineHeight: 1.45,
                                                color: task.suggestedAssignee || task.assignee ? '#065f46' : '#92400e'
                                            }}>
                                                <strong style={{ display: 'block', marginBottom: 3 }}>Lý do</strong>
                                                {task.suggestedReason || (task.suggestedAssignee || task.assignee
                                                    ? 'Phù hợp với nhãn công việc của task này.'
                                                    : 'AI không tìm thấy thành viên có nhãn phù hợp. Bạn có thể chọn thủ công ở đây.')}
                                            </div>

                                            {(task.suggestedAssignee || task.assignee) && (
                                                <button
                                                    type="button"
                                                    onClick={() => clearTaskAssignee(idx)}
                                                    style={{
                                                        alignSelf: 'flex-start',
                                                        border: '1px solid #bbf7d0',
                                                        background: 'var(--bg-card)',
                                                        color: '#047857',
                                                        borderRadius: 9,
                                                        padding: '7px 10px',
                                                        fontSize: 12,
                                                        fontWeight: 850,
                                                        cursor: 'pointer'
                                                    }}
                                                >

```
