# Knowledge Document: DashboardPage.tsx (Chunk 8/9)

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
  "chunk_index": 7,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
 ORCA.'}</p>
                                        </div>
                                        <dl>
                                            <div>
                                                <dt>Thành viên</dt>
                                                <dd>{team.memberCount}</dd>
                                            </div>
                                            <div>
                                                <dt>Ngày tạo</dt>
                                                <dd>{formatDate(team.createdAt)}</dd>
                                            </div>
                                        </dl>
                                    </div>
                                </article>
                                );
                            })}
                        </div>
                    ) : (
                        <div className="dashboard-empty">
                            <Factory size={34} />
                            <h3>Chưa có nhóm xưởng</h3>
                            <p>Tạo nhóm đầu tiên để bắt đầu quản lý nhân sự, quy trình và công việc sản xuất.</p>
                            <button onClick={() => navigate('/groups')} type="button">Tạo nhóm</button>
                        </div>
                    )}
                </section>

                <section className="dashboard-panel dashboard-tasks-panel">
                    <div className="dashboard-section-head">
                        <div>
                            <span>Công việc</span>
                            <h2>Việc gần đây</h2>
                        </div>
                        <button onClick={() => goToTeamFeature('/create-task')} type="button">
                            Tạo công việc
                            <ArrowRight size={16} />
                        </button>
                    </div>

                    <div className="dashboard-task-list">
                        {recentTasks.length > 0 ? recentTasks.map(task => (
                            <article className="dashboard-task-row" key={task.id}>
                                <div className="dashboard-task-mark">
                                    {task.status === 'COMPLETED' ? <CheckCircle2 size={18} /> : <Clock3 size={18} />}
                                </div>
                                <div className="dashboard-task-copy">

```
