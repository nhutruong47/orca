# Knowledge Document: GroupDetailPage.tsx (Chunk 43/136)

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
  "chunk_index": 42,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
>
                                                </>
                                            )}
                                        </td>
                                        <td style={{ padding: '12px 16px', minWidth: 200 }}>
                                            {(() => {
                                                const target = Number(t.outputTarget ?? t.workload ?? 0);
                                                const actual = Number(t.actualOutput ?? 0);
                                                const unit = t.unit && t.unit.trim() ? t.unit : inferUnitFromText(`${t.title || ''} ${t.description || ''}`, t.productionStage);
                                                const pct = target > 0 ? Math.min(100, Math.round((actual / target) * 100)) : (t.completionPercentage || 0);
                                                const PROGRESS_COLOR = '#d4a574';
                                                const clampActual = (val: number) => Math.max(0, target > 0 ? Math.min(val, target) : val);
                                                const persistActual = (val: number) => {
                                                    taskService.update(t.id, { actualOutput: val })
                                                        .then((updatedTask) => {
                                                            if (updatedTask && updatedTask.id) {
                                                                setAllTasks(prev => prev.map(tk => tk.id === updatedTask.id ? updatedTask : tk));
                                                            }
                                                            if (id) { goalService.getByTeam(id).then(setGoals); }
                                                        })
                                                        .catch((err: any) => setError(err?.response?.data?.error || 'Khong the cap nhat'));
                                                };
                                                return (
                                                    <div>
                                                        <div style={{ display: 'flex', alignItems: 'center', flexWrap: 'wrap', gap: 6, fontSize: 12 }}>
                                                            <span style={{ color: 'var(--text-secondary)' }}>Số lượng hiện tại:</span>

```
