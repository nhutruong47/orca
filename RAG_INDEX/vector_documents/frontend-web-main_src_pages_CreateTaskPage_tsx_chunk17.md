# Knowledge Document: CreateTaskPage.tsx (Chunk 18/66)

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
  "chunk_index": 17,
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
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                            {draftMessages.length === 0 ? (
                                <p style={{ color: '#94a3b8', fontSize: 14, textAlign: 'center', marginTop: 40 }}>Chưa có bản nháp nào.</p>
                            ) : (
                                draftMessages.map(msg => (
                                    <div key={msg.id} style={{ border: '1px solid #e2e8f0', borderRadius: 12, padding: 16, cursor: 'pointer', background: selectedHistoryId === msg.id ? '#f8fafc' : '#fff' }} onClick={() => setSelectedHistoryId(selectedHistoryId === msg.id ? null : msg.id)}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
                                            <div style={{ fontSize: 14, fontWeight: 700, color: '#1e293b' }}>{msg.result?.title || 'Mục tiêu không tên'}</div>
                                            <span style={{
                                                fontSize: 11,
                                                padding: '2px 8px',
                                                borderRadius: 12,
                                                background: msg.isConfirmed ? '#dcfce7' : msg.isCancelled ? '#fee2e2' : msg.isArchived ? '#ede9fe' : '#dbeafe',
                                                color: msg.isConfirmed ? '#166534' : msg.isCancelled ? '#991b1b' : msg.isArchived ? '#6d28d9' : '#1d4ed8',
                                                fontWeight: 600
                                            }}>
                                                {msg.isConfirmed ? 'Đã xác nhận' : msg.isCancelled ? 'Đã hủy' : msg.isArchived ? 'Bản trước' : 'Hiện tại'}
                                            </span>
                                        </div>
                                        <div style={{ fontSize: 12, color: '#64748b', marginBottom: 12 }}>{new Date(msg.timestamp).toLocaleString()}</div>
                                        <div style={{ fontSize: 12, color: '#64748b', marginBottom: 8 }}>
                                            {msg.result?.tasks?.length || 0} công việc
                                        </div>

```
