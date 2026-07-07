# Knowledge Document: CreateTaskPage.tsx (Chunk 61/66)

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
  "chunk_index": 60,
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

                                            <div>
                                                <label style={{ display: 'block', marginBottom: 6, fontSize: 12, color: 'var(--text-secondary)', fontWeight: 850 }}>Chọn member</label>
                                                <select
                                                    value={task.suggestedAssigneeId || ''}
                                                    onChange={e => updateTaskAssignee(idx, e.target.value)}
                                                    style={{
                                                        width: '100%',
                                                        minHeight: 42,
                                                        padding: '0 12px',
                                                        borderRadius: 12,
                                                        border: '1px solid #cbd5e1',
                                                        background: 'var(--bg-card)',
                                                        color: 'var(--text-primary)',
                                                        fontSize: 14,
                                                        fontWeight: 700,
                                                        outline: 'none'
                                                    }}
                                                >
                                                    <option value="">Chưa gán</option>
                                                    {members.map(member => (
                                                        <option key={member.userId} value={member.userId}>
                                                            {memberName(member)}{member.jobLabels?.length ? ` - ${member.jobLabels.join(', ')}` : ''}
                                                        </option>
                                                    ))}
                                                </select>
                                            </div>

                                            <div style={{
                                                padding: 10,
                                                borderRadius: 12,
                                                background: 'rgba(255,255,255,0.72)',

```
