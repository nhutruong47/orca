# Knowledge Document: GroupDetailPage.tsx (Chunk 56/136)

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
  "chunk_index": 55,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
,
                        display: 'flex', flexDirection: 'column',
                        borderRight: '1px solid var(--border, #e4e6eb)',
                        background: 'var(--bg-secondary, #fff)',
                        overflow: 'hidden',
                        transition: 'width 0.3s ease'
                    }}>
                        {/* Sidebar header — chỉ 1 nút đóng (X) gọn */}
                        <div style={{ padding: '14px 16px', borderBottom: '1px solid var(--border, #e4e6eb)', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexShrink: 0 }}>
                            <h3 style={{ margin: 0, fontSize: 22, fontWeight: 800, color: 'var(--text-primary, #050505)', letterSpacing: '-0.5px' }}>Đoạn chat</h3>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                <button onClick={() => setShowChat(false)} aria-label="Đóng" style={{ width: 36, height: 36, borderRadius: '50%', background: 'var(--bg-input, #e4e6eb)', border: 'none', color: 'var(--text-primary, #050505)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }} title="Đóng chat"
                                    onMouseEnter={e => { e.currentTarget.style.background = 'var(--danger, #f02849)'; e.currentTarget.style.color = '#fff'; }} onMouseLeave={e => { e.currentTarget.style.background = 'var(--bg-input, #e4e6eb)'; e.currentTarget.style.color = 'var(--text-primary, #050505)'; }}>
                                    <ion-icon name="close" style={{ fontSize: 22 }}></ion-icon>
                                </button>
                            </div>
                        </div>

                        {/* Search box */}
                        <div style={{ padding: '8px 12px', flexShrink: 0 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: 'var(--bg-input, #f0f2f5)', borderRadius: 20, padding: '8px 12px' }}>
                                <ion-icon name="search-outline" style={{ color: 'var(--text-secondary, #65676b)', fontSize: 16 }}></ion-icon>
                                <input placeholder="Tìm kiếm nhân viên" style={{ flex: 1, background: 'transparent', border: 'none', outline: 'none', fontSize: 14, color: 'var(--text-primary, #050505)' }} />

```
