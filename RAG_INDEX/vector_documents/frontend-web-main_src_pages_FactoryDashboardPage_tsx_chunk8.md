# Knowledge Document: FactoryDashboardPage.tsx (Chunk 9/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
              <span style={{ color: 'var(--text-secondary)', fontSize: 13 }}>Con lai</span>
                                        <span style={{ fontWeight: 700, fontSize: 15, color: '#ef4444' }}>{Math.max(0, (todayTarget.targetQuantityKg || 0) - (todayTarget.totalActualKg || 0)).toLocaleString('vi-VN')} kg</span>
                                    </div>
                                </div>
                            </div>
                            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
                                <thead>
                                    <tr style={{ borderBottom: '1px solid var(--border)' }}>
                                        <th style={{ textAlign: 'left', padding: '8px 0', color: 'var(--text-muted)', fontWeight: 600 }}>Cong doan</th>
                                        <th style={{ textAlign: 'right', padding: '8px 0', color: 'var(--text-muted)', fontWeight: 600 }}>Muc tieu</th>
                                        <th style={{ textAlign: 'right', padding: '8px 0', color: 'var(--text-muted)', fontWeight: 600 }}>Thuc te</th>
                                        <th style={{ textAlign: 'right', padding: '8px 0', color: 'var(--text-muted)', fontWeight: 600 }}>Chenh lech</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {[
                                        { key: 'targetRoastKg', actual: 'actualRoastKg', label: 'Rang' },
                                        { key: 'targetQcKg', actual: 'actualQcKg', label: 'QC' },
                                        { key: 'targetPackagedKg', actual: 'actualPackagedKg', label: 'Dong goi' },
                                    ].map(row => {
                                        const target = todayTarget[row.key] || 0;
                                        const actual = todayTarget[row.actual] || 0;
                                        const diff = actual - target;
                                        return (
                                            <tr key={row.key} style={{ borderBottom: '1px solid var(--border)' }}>
                                                <td style={{ padding: '10px 0', fontWeight: 600 }}>{row.label}</td>

```
