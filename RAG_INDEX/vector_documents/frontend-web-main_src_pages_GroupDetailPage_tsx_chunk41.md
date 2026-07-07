# Knowledge Document: GroupDetailPage.tsx (Chunk 42/136)

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
  "chunk_index": 41,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
8, border: '1px solid var(--border)', fontSize: 12, color: 'var(--text-secondary)', background: 'var(--bg-input)', width: 90 }} title="Đơn vị (kg, gói, hộp, chai, tem, mẫu, đơn...)" />
                                                    </div>
                                                </div>
                                            ) : (
                                                <>
                                                    {t.taskCode && <div style={{ fontSize: 10, color: 'var(--accent-primary)', fontWeight: 800, letterSpacing: '0.08em', marginBottom: 2 }}>{t.taskCode}</div>}
                                                    <div style={{ fontWeight: 600, fontSize: 14, color: 'var(--text-primary)' }}>{t.title}</div>
                                                    {t.description && <div style={{ fontSize: 12, color: 'var(--text-secondary)', marginTop: 2 }}>{t.description}</div>}
                                                    <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap', marginTop: 4 }}>
                                                        {t.productionStage && <span style={{ fontSize: 11, color: 'var(--text-secondary)', background: 'var(--bg-secondary)', borderRadius: 6, padding: '2px 6px' }}>{t.productionStage}</span>}
                                                        {t.dependencyTaskTitles && t.dependencyTaskTitles.length > 0 && <span style={{ fontSize: 11, color: '#dc2626', background: 'rgba(220, 38, 38, 0.1)', borderRadius: 6, padding: '2px 6px' }}>Depends on: {t.dependencyTaskTitles.join(', ')}</span>}
                                                        {(t.dueTime || t.deadline) && <span style={{ fontSize: 11, color: '#f59e0b' }}><ion-icon name="time-outline" style={{ fontSize: 11 }}></ion-icon> Hạn: {new Date(t.dueTime || t.deadline).toLocaleDateString('vi')}</span>}
                                                    </div>
                                                </>
                                            )}
                                        </td>
                                        <td style={{ padding: '12px 16px', minWidth: 200 }}>
                                            {(() => {
                                                const target = Number(t.outputTarget ?? t.workload ?? 0);

```
