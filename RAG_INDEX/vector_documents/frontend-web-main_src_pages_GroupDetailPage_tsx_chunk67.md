# Knowledge Document: GroupDetailPage.tsx (Chunk 68/136)

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
  "chunk_index": 67,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                             <div style={{ padding: '12px 16px', borderTop: '1px solid var(--border, #e4e6eb)', background: 'var(--bg-card, #fff)', display: 'flex', alignItems: 'center', gap: 8 }}>
                                    <input type="file" ref={fileInputRef} style={{ display: 'none' }} onChange={e => { if(e.target.files && e.target.files[0]) setChatAttachment(e.target.files[0]) }} />
                                    <button onClick={() => alert('Tính năng gửi ảnh đang được phát triển')} style={{ width: 40, height: 40, borderRadius: '50%', background: 'transparent', border: 'none', color: '#d4a574', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }} title="Gửi ảnh"
                                        onMouseEnter={e => e.currentTarget.style.background = 'var(--bg-input, #f0f2f5)'} onMouseLeave={e => e.currentTarget.style.background = 'transparent'}>
                                        <ion-icon name="image" style={{ fontSize: 24 }}></ion-icon>
                                    </button>
                                    <button onClick={() => fileInputRef.current?.click()} style={{ width: 40, height: 40, borderRadius: '50%', background: 'transparent', border: 'none', color: '#d4a574', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }} title="Đính kèm file"
                                        onMouseEnter={e => e.currentTarget.style.background = 'var(--bg-input, #f0f2f5)'} onMouseLeave={e => e.currentTarget.style.background = 'transparent'}>
                                        <ion-icon name="attach" style={{ fontSize: 24 }}></ion-icon>
                                    </button>
                                    <div style={{ flex: 1, minWidth: 0, background: 'var(--bg-input, #f0f2f5)', borderRadius: 20, padding: '8px 14px', display: 'flex', alignItems: 'center', gap: 8 }}>
                                        <input value={chatInput} onChange={e => setChatInput(e.target.value)} onKeyDown={e => e.key === 'Enter' && handleSendChat()} placeholder={chatTab === 'dm' ? "Aa" : "Aa, nhắn cho nhóm..."} style={{ width: '100%', background: 'transparent', border: 'none', outline: 'none', fontSize: 14, color: 'var(--text-primary, #050505)' }} />
                                    </div>

```
