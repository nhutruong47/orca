# Knowledge Document: CreateTaskPage.tsx (Chunk 41/66)

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
  "chunk_index": 40,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
| '')) hash = (hash * 31 + c.charCodeAt(0)) % colors.length;
                                    const bgColor = colors[hash];
                                    return (
                                        <div key={m.userId} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '10px 12px', background: 'var(--bg-primary)', borderRadius: 10, border: '1px solid var(--border)' }}>
                                            <div style={{ width: 32, height: 32, borderRadius: '50%', background: bgColor, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 12, fontWeight: 700, flexShrink: 0 }}>
                                                {initials}
                                            </div>
                                            <div style={{ flex: 1, minWidth: 0 }}>
                                                <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                                    {m.fullName || m.username}
                                                </div>
                                                <div style={{ display: 'flex', gap: 4, flexWrap: 'wrap', marginTop: 4 }}>
                                                    {m.jobLabels && m.jobLabels.length > 0 ? (
                                                        m.jobLabels.map((label: string, idx: number) => (
                                                            <span key={idx} style={{ background: 'rgba(212, 165, 116, 0.12)', color: 'var(--accent-primary)', padding: '2px 8px', borderRadius: 12, fontSize: 10, fontWeight: 700 }}>
                                                                {label}
                                                            </span>
                                                        ))
                                                    ) : (
                                                        <span style={{ fontSize: 10, color: 'var(--text-muted)', fontStyle: 'italic' }}>Chưa gán nhãn</span>
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                    );

```
