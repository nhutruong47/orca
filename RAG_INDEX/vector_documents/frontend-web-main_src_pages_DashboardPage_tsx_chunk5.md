# Knowledge Document: DashboardPage.tsx (Chunk 6/9)

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
  "chunk_index": 5,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
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
                <section className="dashboard-panel dashboard-teams-panel">
                    <div className="dashboard-section-head">
                        <div>
                            <span>Không gian làm việc</span>
                            <h2>Nhóm đang vận hành</h2>
                        </div>
                        <button onClick={() => navigate('/groups')} type="button">
                            Xem tất cả
                            <ArrowRight size={16} />
                        </button>
                    </div>

                    {teams.length > 0 ? (
                        <div className="dashboard-team-list">
                            {teams.slice(0, 3).map((team, index) => {
                                const goals = teamGoals[team.id] || [];
                                const totalGoals = goals.length;
                                const completedGoals = goals.filter(g => g.status === 'COMPLETED').length;
                                const isAllCompleted = totalGoals === 0 || totalGoals === completedGoals;

                                return (
                                <article
                                    className="dashboard-team-card"
                                    key={team.id}
                                    role="button"
                                    tabIndex={0}
                                    onClick={() => openTeamWorkspace(team.id)}
                                    onKeyDown={(event) => {
                                        if (event.key === 'Enter' || event.key === ' ') {
                                            event.preventDefault();
                                            openTeamWorkspace(team.id);
                                        }
                                    }}
                                    aria-label={`Mở nơi làm việc của nhóm ${team.name}`}
                                    style={{ position: 'relative' }}

```
