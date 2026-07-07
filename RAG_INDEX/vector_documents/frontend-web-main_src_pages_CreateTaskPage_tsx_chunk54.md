# Knowledge Document: CreateTaskPage.tsx (Chunk 55/66)

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
  "chunk_index": 54,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
            width: '100%', padding: '14px 18px', borderRadius: '12px',
                                border: '1px solid var(--border)', background: 'var(--bg-card)',
                                color: 'var(--text-primary)', fontSize: 15, fontWeight: 500, outline: 'none',
                                transition: 'border-color 0.2s'
                            }}
                        />
                    </div>

                    {/* Task List (Mô tả chi tiết) */}
                    <div style={{ marginBottom: 24 }}>
                        <label style={{ display: 'block', fontSize: 13, fontWeight: 700, color: 'var(--text-secondary)', marginBottom: 8 }}>Chi tiết mô tả</label>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                            {editedResult.tasks?.map((task, idx) => (
                                <div key={idx} style={{
                                    display: 'flex',
                                    flexDirection: 'column',
                                    gap: 16,
                                    padding: 18,
                                    borderRadius: 18,
                                    border: '1px solid #dbe3ef',
                                    background: 'var(--bg-card)',
                                    boxShadow: '0 8px 24px rgba(15, 23, 42, 0.06)'
                                }}>
                                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 12 }}>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 10, minWidth: 0 }}>
                                            <span style={{
                                                width: 30,
                                                height: 30,
                                                borderRadius: '50%',
                                                display: 'inline-flex',
                                                alignItems: 'center',
                                                justifyContent: 'center',
                                                background: '#ede9fe',
                                                color: '#6d28d9',
                                                fontSize: 13,

```
