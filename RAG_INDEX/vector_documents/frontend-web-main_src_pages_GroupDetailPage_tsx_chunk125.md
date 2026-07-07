# Knowledge Document: GroupDetailPage.tsx (Chunk 126/136)

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
  "chunk_index": 125,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
nth Selector & Content */}
            {showSalary && (
                <div style={{ borderTop: '1px solid #e2e8f0' }}>
                    <div style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: '#f8fafc' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                            <button
                                onClick={() => {
                                    const [y, m] = selectedMonth.split('-').map(Number);
                                    const prev = new Date(y, m - 2);
                                    setSelectedMonth(`${prev.getFullYear()}-${String(prev.getMonth() + 1).padStart(2, '0')}`);
                                }}
                                style={{ width: 32, height: 32, borderRadius: 8, border: '1px solid #e2e8f0', background: '#fff', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                            >
                                <svg width="16" height="16" fill="none" stroke="#64748b" strokeWidth="2"><path d="M15 18l-6-6 6-6"/></svg>
                            </button>
                            <select
                                value={selectedMonth}
                                onChange={e => setSelectedMonth(e.target.value)}
                                style={{
                                    padding: '6px 12px', borderRadius: 8, border: '1px solid #e2e8f0',
                                    background: '#fff', fontSize: 13, fontWeight: 600, color: '#1e293b',
                                    cursor: 'pointer', outline: 'none'
                                }}
                            >
                                {Array.from({ length: 12 }, (_, i) => {
                                    const d = new Date();
                                    d.setMonth(d.getMonth() - i);
                                    const val = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
                                    return <option key={val} value={val} style={{ color: '#000' }}>{d.toLocaleDateString('vi-VN', { month: 'long', year: 'numeric' })}</option>;
                                })}
                            </select>
                            <button
                                onClick={() => {

```
