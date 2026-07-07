# Knowledge Document: CreateTaskPage.tsx (Chunk 40/66)

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
  "chunk_index": 39,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
             flex: 1, padding: '10px 0', fontSize: 13, fontWeight: 600,
                                        border: 'none', borderRight: level !== 'Cao' ? '1px solid var(--border)' : 'none',
                                        background: priority === level ? '#d4a574' : 'transparent',
                                        color: priority === level ? '#ffffff' : 'var(--text-secondary)',
                                        cursor: 'pointer', transition: 'all 0.2s'
                                    }}
                                >
                                    {level}
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Team Members with Job Labels */}
                    {team!.members && team!.members!.length > 0 && (
                        <div style={{ marginTop: 24, borderTop: '1px solid var(--border)', paddingTop: 20 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
                                <ion-icon name="people-outline" style={{ color: '#d4a574', fontSize: 18 }}></ion-icon>
                                <span style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-primary)' }}>Thành viên nhóm ({team!.members!.length})</span>
                            </div>
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                                {team!.members!.map((m: any) => {
                                    const initials = (m.fullName || m.username || '?').split(' ').map((w: string) => w[0]).join('').slice(0, 2).toUpperCase();
                                    const colors = ['#d4a574', '#8b5cf6', '#ec4899', '#f43f5e', '#f59e0b', '#10b981', '#06b6d4', '#3b82f6'];
                                    let hash = 0;
                                    for (const c of (m.username || '')) hash = (hash * 31 + c.charCodeAt(0)) % colors.length;
                                    const bgColor = colors[hash];
                                    return (
                                        <div key={m.userId} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '10px 12px', background: 'var(--bg-primary)', borderRadius: 10, border: '1px solid var(--border)' }}>

```
