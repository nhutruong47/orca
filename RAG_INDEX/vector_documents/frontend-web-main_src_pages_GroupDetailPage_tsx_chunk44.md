# Knowledge Document: GroupDetailPage.tsx (Chunk 45/136)

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
  "chunk_index": 44,
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
                                                            {isAdmin ? (
                                                                <input
                                                                    type="number"
                                                                    min={0}
                                                                    defaultValue={target || ''}
                                                                    placeholder={String(target || '')}
                                                                    onBlur={async e => {
                                                                        const value = e.currentTarget.value;
                                                                        try {
                                                                            setError('');
                                                                            const updatedTask = await taskService.update(t.id, { outputTarget: value === '' ? undefined : Number(value) });
                                                                            if (updatedTask && updatedTask.id) {
                                                                                setAllTasks(prev => prev.map(tk => tk.id === updatedTask.id ? updatedTask : tk));
                                                                            }
                                                                            if (id) { const g = await goalService.getByTeam(id); setGoals(g); }
                                                                        } catch (err: any) {
                                                                            setError(err?.response?.data?.error || 'Không thể cập nhật mục tiêu');
                                                                        }
                                                                    }}
                                                                    onKeyDown={(e) => { if (e.key === 'Enter') e.currentTarget.blur(); }}
                                                                    style={{ width: 72, padding: '6px 8px', borderRadius: 7, border: '1px solid #cbd5e1', fontSize: 14, fontWeight: 800, color: '#0f172a', textAlign: 'right', background: '#fff' }}
                                                                />

```
