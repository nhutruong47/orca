# Knowledge Document: GroupDetailPage.tsx (Chunk 32/136)

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
  "chunk_index": 31,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
               <div style={{ fontSize: 14, color: '#24324a', fontWeight: 500, lineHeight: 1.65 }} className="markdown-body goal-roadmap-markdown">
                                        <ReactMarkdown remarkPlugins={[remarkGfm]}>{displayDesc}</ReactMarkdown>
                                    </div>
                                </div>
                                {aiData?.contingency && (
                                    <div>
                                        <div style={{ fontSize: 11, fontWeight: 800, color: '#64748b', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 8 }}>Phương án dự phòng</div>
                                        <div style={{ fontSize: 13, color: '#b42318', background: '#fff4f2', padding: '10px 12px', borderRadius: 10, border: '1px solid #ffd7d0', lineHeight: 1.55 }}>
                                            <ion-icon name="warning-outline" style={{ verticalAlign: 'middle', marginRight: 4 }}></ion-icon>
                                            {aiData.contingency}
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>
                    );
                })}
            </div>
            )}

            {/* ===== TASK TABLE ===== */}
            <div style={{ background: 'var(--bg-card)', borderRadius: 14, border: '1px solid var(--border)', overflow: 'hidden', marginBottom: 18 }}>
                <div style={{ padding: '16px 24px', borderBottom: '1px solid var(--border)' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
                        <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: 'var(--text-primary)' }}>
                            <ion-icon name="list-outline" style={{ verticalAlign: 'middle', marginRight: 6, color: '#d4a574' }}></ion-icon>
                            CÔNG VIỆC
                        </h3>
                        {isAdmin && (
                            <div style={{ display: 'flex', gap: 8 }}>
                                {latestGoal && latestGoal.chatLog && (
                                    <button onClick={() => {
                                        setActiveGoalTitle(latestGoal.title || '');

```
