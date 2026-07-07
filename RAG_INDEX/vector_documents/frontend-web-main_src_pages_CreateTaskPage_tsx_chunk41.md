# Knowledge Document: CreateTaskPage.tsx (Chunk 42/66)

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
  "chunk_index": 41,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                                                    <span style={{ fontSize: 10, color: 'var(--text-muted)', fontStyle: 'italic' }}>Chưa gán nhãn</span>
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                            <p style={{ fontSize: 11, color: 'var(--text-muted)', marginTop: 10, lineHeight: 1.5 }}>
                                <ion-icon name="information-circle-outline" style={{ fontSize: 12, verticalAlign: 'middle' }}></ion-icon>{' '}
                                AI sẽ tự động phân công dựa trên nhãn dán công việc.
                            </p>
                        </div>
                    )}
                </div>

                {/* Right Panel: AI Chat interface */}
                <div style={{
                    background: 'var(--bg-card)',
                    borderRadius: 16,
                    border: '1px solid var(--border)',
                    boxShadow: '0 4px 24px rgba(0,0,0,0.04)',
                    display: 'flex', flexDirection: 'column',
                    height: 'clamp(560px, calc(100vh - 220px), 680px)',
                    minHeight: 0,
                    overflow: 'hidden'
                }}>
                    {/* Header */}
                    <div style={{ padding: '16px 24px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-card)' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                            <div style={{ width: 40, height: 40, borderRadius: '50%', background: '#d4a574', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: 20 }}>
                                <ion-icon name="sparkles"></ion-icon>
                            </div>
                            <div>
                                <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: 'var(--text-primary)' }}>AI Xử Lý Công Việc</h3>
                                <p style={{ margin: 0, fontSize: 13, color: 'var(--text-secondary)' }}>Mô tả mục tiêu một cách tự nhiên</p>

```
