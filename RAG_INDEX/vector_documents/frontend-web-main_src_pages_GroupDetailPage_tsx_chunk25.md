# Knowledge Document: GroupDetailPage.tsx (Chunk 26/136)

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
  "chunk_index": 25,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                       )}

                            <div style={{ height: 6, background: '#f1f5f9', borderRadius: 3, overflow: 'hidden', marginBottom: 6 }}>
                                <div style={{ height: '100%', background: m.pct === 100 ? '#16a34a' : m.pct > 0 ? '#f59e0b' : '#e2e8f0', borderRadius: 3, width: `${m.pct}%`, transition: 'width 0.4s' }} />
                            </div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 12 }}>
                                <div style={{ fontSize: 11, color: '#94a3b8' }}>{m.completed}/{m.total} công việc</div>
                                {m.userId !== user?.id && (
                                    <button
                                        onClick={() => {
                                            setChatTab('dm');
                                            setDmUserId(m.userId);
                                            setShowChat(true);
                                        }}
                                        style={{
                                            background: '#f9f1e3', color: '#d4a574', border: 'none',
                                            borderRadius: 8, padding: '4px 10px', fontSize: 11,
                                            fontWeight: 700, cursor: 'pointer', display: 'flex',
                                            alignItems: 'center', gap: 4
                                        }}
                                    >
                                        <ion-icon name="chatbubble-ellipses-outline"></ion-icon> Nhắn tin
                                    </button>
                                )}
                            </div>
                        </div>
                    );
                })}
            </div>
            </>
            )}

            {/* ===== DB ROADMAP: same source as task table ===== */}
            {isAdmin && latestGoal && (
            <div style={{ background: 'var(--bg-card)', borderRadius: 14, border: '1px solid var(--border)', overflow: 'hidden', marginBottom: 18, boxShadow: '0 10px 26px rgba(0,0,0,0.06)' }}>

```
