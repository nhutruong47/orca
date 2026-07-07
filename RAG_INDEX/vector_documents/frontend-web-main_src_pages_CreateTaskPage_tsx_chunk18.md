# Knowledge Document: CreateTaskPage.tsx (Chunk 19/66)

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
  "chunk_index": 18,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
div>
                                        <div style={{ fontSize: 12, color: '#64748b', marginBottom: 12 }}>{new Date(msg.timestamp).toLocaleString()}</div>
                                        <div style={{ fontSize: 12, color: '#64748b', marginBottom: 8 }}>
                                            {msg.result?.tasks?.length || 0} công việc
                                        </div>
                                        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                                            {(msg.result?.tasks || []).map((task, index) => (
                                                <span
                                                    key={`${msg.id}-task-${index}`}
                                                    style={{
                                                        padding: '4px 8px',
                                                        borderRadius: 999,
                                                        background: '#f1f5f9',
                                                        color: '#475569',
                                                        fontSize: 11,
                                                        lineHeight: 1.2
                                                    }}
                                                >
                                                    {index + 1}. {task.title || task.description}
                                                </span>
                                            ))}
                                        </div>

                                        {selectedHistoryId === msg.id && (
                                            <div style={{ borderTop: '1px solid #e2e8f0', paddingTop: 12, marginTop: 4 }}>
                                                <div style={{ fontSize: 12, color: '#475569', marginBottom: 12 }}>
                                                    <strong>Mô tả:</strong> {msg.result?.description || msg.content}
                                                </div>
                                                {msg.isArchived || msg.isConfirmed || msg.isCancelled ? (

```
