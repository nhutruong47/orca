# Knowledge Document: DashboardPage.tsx (Chunk 7/9)

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
  "chunk_index": 6,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
event.key === ' ') {
                                            event.preventDefault();
                                            openTeamWorkspace(team.id);
                                        }
                                    }}
                                    aria-label={`Mở nơi làm việc của nhóm ${team.name}`}
                                    style={{ position: 'relative' }}
                                >
                                    <img src={teamImages[index % teamImages.length]} alt={team.name} />
                                    <div className="dashboard-team-body">
                                        <div>
                                            <h3 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                                {team.name}
                                                <span
                                                    style={{
                                                        display: 'inline-block',
                                                        width: 10,
                                                        height: 10,
                                                        borderRadius: '50%',
                                                        backgroundColor: isAllCompleted ? '#10b981' : '#ef4444',
                                                        boxShadow: `0 0 8px ${isAllCompleted ? 'rgba(16, 185, 129, 0.4)' : 'rgba(239, 68, 68, 0.4)'}`,
                                                        flexShrink: 0
                                                    }}
                                                    title={isAllCompleted ? 'Tất cả công việc đã hoàn thành' : 'Có công việc chưa hoàn thành'}
                                                />
                                            </h3>
                                            <p>{team.description || team.specialty || 'Nhóm xưởng đang được quản lý trên ORCA.'}</p>
                                        </div>
                                        <dl>
                                            <div>
                                                <dt>Thành viên</dt>
                                                <dd>{team.memberCount}</dd>
                                            </div>
                                            <div>

```
