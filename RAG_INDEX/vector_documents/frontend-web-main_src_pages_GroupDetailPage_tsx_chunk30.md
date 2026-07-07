# Knowledge Document: GroupDetailPage.tsx (Chunk 31/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 30,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
e={{ background: '#fff', borderRadius: 14, border: '1px solid #e2e8f0', overflow: 'hidden', boxShadow: '0 10px 26px rgba(15,23,42,0.06)' }}>
                            <div style={{ padding: '16px 20px', color: '#1e293b', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 16, borderBottom: '1px solid #edf2f7', background: 'linear-gradient(180deg, #fffaf3, #fff)' }}>
                                <div style={{ display: 'flex', alignItems: 'flex-start', gap: 12, minWidth: 0 }}>
                                    <span style={{ width: 36, height: 36, borderRadius: 10, background: '#f3dfc6', color: '#8a5a2d', display: 'grid', placeItems: 'center', flexShrink: 0 }}>
                                        <ion-icon name="flag-outline" style={{ fontSize: 18 }}></ion-icon>
                                    </span>
                                    <div style={{ minWidth: 0 }}>
                                        <div style={{ fontSize: 11, color: '#9a6b3b', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 4 }}>Mục tiêu sản xuất</div>
                                        <h3 style={{ margin: 0, fontSize: 17, fontWeight: 800, color: '#172033', lineHeight: 1.35 }}>{displayTitle}</h3>
                                    </div>
                                </div>
                                <span style={{ background: '#f3dfc6', color: '#6b4321', padding: '5px 10px', borderRadius: 8, fontSize: 11, fontWeight: 800, whiteSpace: 'nowrap' }}>{displayPhase}</span>
                            </div>
                            <div style={{ padding: 20 }}>
                                <div style={{ marginBottom: aiData?.contingency ? 16 : 0 }}>
                                    <div style={{ fontSize: 11, fontWeight: 800, color: '#64748b', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 10 }}>Kế hoạch hiện tại</div>
                                    <div style={{ fontSize: 14, color: '#24324a', fontWeight: 500, lineHeight: 1.65 }} className="markdown-body goal-roadmap-markdown">
                                        <ReactMarkdown remarkPlugins={[remarkGfm]}>{displayDesc}</ReactMarkdown>
                                    </div>
                                </div>
                                {aiData?.contingency && (

```
