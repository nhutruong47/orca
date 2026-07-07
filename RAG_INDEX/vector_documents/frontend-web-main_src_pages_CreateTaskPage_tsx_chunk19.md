# Knowledge Document: CreateTaskPage.tsx (Chunk 20/66)

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
  "chunk_index": 19,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
 4 }}>
                                                <div style={{ fontSize: 12, color: '#475569', marginBottom: 12 }}>
                                                    <strong>Mô tả:</strong> {msg.result?.description || msg.content}
                                                </div>
                                                {msg.isArchived || msg.isConfirmed || msg.isCancelled ? (
                                                    <button onClick={(e) => { e.stopPropagation(); handleRevertDraft(msg.result!); }} style={{ width: '100%', padding: '8px', background: '#d4a574', color: '#fff', border: 'none', borderRadius: 8, fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>
                                                        Tạo lại từ bản này
                                                    </button>
                                                ) : (
                                                    <div style={{ width: '100%', padding: '8px', background: '#dbeafe', color: '#1d4ed8', borderRadius: 8, fontSize: 13, fontWeight: 600, textAlign: 'center' }}>
                                                        Đây là bản đang sử dụng
                                                    </div>
                                                )}
                                            </div>
                                        )}
                                    </div>
                                ))
                            )}
                        </div>
                    </div>
                </div>
            )}

            <header className="task-gpt-topbar">
                <button className="task-gpt-action" type="button" onClick={() => navigate(`/groups/${teamId}`)}>
                    <ion-icon name="chevron-back-outline"></ion-icon>
                    ORCA
                </button>
                <div className="task-gpt-actions">
                    <button className="task-gpt-action" type="button" onClick={() => setShowHistory(true)}>
                        <ion-icon name="time-outline"></ion-icon>
                        Lịch sử
                    </button>

                    <button className="task-gpt-action" type="button" onClick={() => setShowTokens(prev => !prev)}>
                        <ion-icon name="ellipsis-horizontal"></ion-icon>
                    </button>

```
