# Knowledge Document: GroupDetailPage.tsx (Chunk 82/136)

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
  "chunk_index": 81,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                     <h2 style={{ margin: '0 0 24px', fontSize: 20 }}>Nhập hàng hóa mới</h2>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
                            <div>
                                <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Tên hàng hóa <span style={{ color: '#dc2626' }}>*</span></label>
                                <input value={invName} onChange={e => setInvName(e.target.value)} placeholder="Ví dụ: Cà phê hạt loại A..." style={{ width: '100%', padding: '12px 16px', borderRadius: 10, border: '1px solid var(--border, #cbd5e1)', fontSize: 15, outline: 'none', background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} autoFocus />
                            </div>
                            <div style={{ display: 'flex', gap: 16 }}>
                                <div style={{ flex: 1 }}>
                                    <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Số lượng <span style={{ color: '#dc2626' }}>*</span></label>
                                    <input type="text" value={invQty} onChange={e => { const val = e.target.value.replace(/\./g, ''); if (!isNaN(Number(val))) setInvQty(val === '' ? '' : Number(val).toLocaleString('de-DE')); }} placeholder="0" style={{ width: '100%', padding: '12px 16px', borderRadius: 10, border: '1px solid var(--border, #cbd5e1)', fontSize: 15, outline: 'none', background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                                </div>
                                <div style={{ flex: 1 }}>
                                    <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Đơn vị</label>
                                    <input value={invUnit} onChange={e => setInvUnit(e.target.value)} placeholder="VD: kg, hộp..." style={{ width: '100%', padding: '12px 16px', borderRadius: 10, border: '1px solid var(--border, #cbd5e1)', fontSize: 15, outline: 'none', background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                                </div>
                            </div>
                            <div>

```
