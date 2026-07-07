# Knowledge Document: DashboardPage.tsx (Chunk 5/9)

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
  "chunk_index": 4,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
trong>
                    <p>{isOverachieving ? `Sản lượng đạt ${totalActual}/${totalTarget}, vượt mức kế hoạch đề ra.` : isOverloaded ? `Đã hết ngày nhưng còn ${activeTasks.length} task chưa xong.` : activeTasks.length > 0 ? `${activeTasks.length} task chưa hoàn thành.` : 'Bạn có thể tạo thêm kế hoạch hoặc kiểm tra nhóm xưởng.'}</p>
                    <div className="dashboard-progress-track">
                        <span style={{ width: `${progress}%`, background: isOverachieving ? 'var(--success)' : isOverloaded ? 'var(--danger)' : undefined }} />
                    </div>
                    <small style={{ color: isOverachieving ? 'var(--success)' : isOverloaded ? 'var(--danger)' : undefined }}>{progress}% hoàn thành</small>
                </div>
            </section>

            <section className="dashboard-quick-actions" aria-label="Lối tắt chức năng">
                {quickActions.map(action => {
                    const Icon = action.icon;
                    return (
                        <button key={action.label} type="button" onClick={action.onClick}>
                            <span className="dashboard-quick-icon">
                                <Icon size={18} />
                            </span>
                            <span>
                                <strong>{action.label}</strong>
                                <small>{action.caption}</small>
                            </span>
                        </button>
                    );
                })}
            </section>

            <section className="dashboard-stat-grid" aria-label="Tổng quan nhanh">
                {stats.map(stat => {
                    const Icon = stat.icon;
                    return (
                        <article className={`dashboard-stat-card ${stat.tone}`} key={stat.label}>
                            <div className="dashboard-stat-icon">
                                <Icon size={19} />
                            </div>
                            <div>
                                <span>{stat.label}</span>
                                <strong>{stat.value}</strong>
                                <p>{stat.caption}</p>
                            </div>
                        </article>
                    );
                })}
            </section>

            <div className="dashboard-workspace-grid">

```
