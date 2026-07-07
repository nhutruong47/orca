# Knowledge Document: GroupDetailPage.tsx (Chunk 30/136)

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
  "chunk_index": 29,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                   <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                                <div style={{ flex: 1, height: 6, background: 'var(--bg-secondary)', borderRadius: 999, overflow: 'hidden' }}>
                                                    <div style={{ height: '100%', width: `${progressPct}%`, background: status.color, borderRadius: 999 }} />
                                                </div>
                                                <span style={{ color: status.color, fontSize: 12, fontWeight: 800, minWidth: 34 }}>{progressPct}%</span>
                                            </div>
                                        </td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>
            </div>
            )}

            {/* ===== GOAL STRATEGIC OVERVIEW (LEGACY AI TEXT) ===== */}
            {false && isAdmin && latestGoal && (
            <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: 14, marginBottom: 18 }}>
                {[latestGoal].map(g => {
                    let aiData: any = null;
                    if (g.aiParsedData) {
                        try {
                            aiData = JSON.parse(g.aiParsedData);
                        } catch (e) {
                            console.error("Failed to parse AI data", e);
                        }
                    }

                    const displayTitle = g.title || aiData?.mainGoal || 'Kế hoạch công việc';
                    const displayDesc = g.outputTarget || g.rawInstruction || aiData?.description || 'Nhiệm vụ đã được phân bổ cho các thành viên trong nhóm.';
                    const displayPhase = aiData?.phase || 'CHÍNH THỨC';

                    return (
                        <div key={g.id} style={{ background: '#fff', borderRadius: 14, border: '1px solid #e2e8f0', overflow: 'hidden', boxShadow: '0 10px 26px rgba(15,23,42,0.06)' }}>
                            <div style={{ padding: '16px 20px', color: '#1e293b', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 16, borderBottom: '1px solid #edf2f7', background: 'linear-gradient(180deg, #fffaf3, #fff)' }}>

```
