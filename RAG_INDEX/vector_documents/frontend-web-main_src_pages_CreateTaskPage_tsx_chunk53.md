# Knowledge Document: CreateTaskPage.tsx (Chunk 54/66)

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
  "chunk_index": 53,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
n style={{ fontSize: 20, color: '#f59e0b' }}><ion-icon name="clipboard-outline"></ion-icon></span>
                        <div style={{ flex: 1 }}>
                            <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: 'var(--text-primary)' }}>Công việc đã chuẩn hóa</h3>
                            <p style={{ margin: '4px 0 0', fontSize: 12, color: 'var(--text-secondary)' }}>
                                AI đã gợi ý người phụ trách cho {assignedCount}/{totalTasks} task dựa trên job labels.
                            </p>
                        </div>
                        <div style={{
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: 6,
                            padding: '7px 12px',
                            borderRadius: 999,
                            background: assignedCount > 0 ? '#ecfdf5' : '#f8fafc',
                            color: assignedCount > 0 ? '#047857' : '#64748b',
                            border: `1px solid ${assignedCount > 0 ? '#a7f3d0' : '#e2e8f0'}`,
                            fontSize: 12,
                            fontWeight: 800
                        }}>
                            <ion-icon name="person-add-outline"></ion-icon>
                            {assignedCount > 0 ? `${assignedCount} gợi ý` : 'Chưa gán'}
                        </div>
                    </div>

                    {/* Title Input */}
                    <div style={{ marginBottom: 24 }}>
                        <label style={{ display: 'block', fontSize: 13, fontWeight: 700, color: 'var(--text-secondary)', marginBottom: 8 }}>Tên công việc</label>
                        <input
                            type="text"
                            value={editedResult.title || ''}
                            onChange={e => updateField('title', e.target.value)}
                            style={{
                                width: '100%', padding: '14px 18px', borderRadius: '12px',
                                border: '1px solid var(--border)', background: 'var(--bg-card)',
                                color: 'var(--text-primary)', fontSize: 15, fontWeight: 500, outline: 'none',
                                transition: 'border-color 0.2s'
                            }}
                        />

```
