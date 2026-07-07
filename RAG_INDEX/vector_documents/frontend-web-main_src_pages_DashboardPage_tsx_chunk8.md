# Knowledge Document: DashboardPage.tsx (Chunk 9/9)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "workspace",
  "tags": [
    "workspace",
    "factory",
    "dashboard",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
Tasks.map(task => (
                            <article className="dashboard-task-row" key={task.id}>
                                <div className="dashboard-task-mark">
                                    {task.status === 'COMPLETED' ? <CheckCircle2 size={18} /> : <Clock3 size={18} />}
                                </div>
                                <div className="dashboard-task-copy">
                                    <h3>{task.title}</h3>
                                    <p>{task.description || task.goalTitle || 'Không có mô tả.'}</p>
                                </div>
                                <span className={`dashboard-task-status ${task.status.toLowerCase().replaceAll('_', '-')}`}>
                                    {statusText(task.status)}
                                </span>
                            </article>
                        )) : (
                            <div className="dashboard-empty dashboard-empty-compact">
                                <ClipboardList size={34} />
                                <h3>Chưa có công việc mới</h3>
                                <p>Khi có task được giao, danh sách sẽ hiện ở đây.</p>
                            </div>
                        )}
                    </div>
                </section>
            </div>
        </div>
    );
}

```
