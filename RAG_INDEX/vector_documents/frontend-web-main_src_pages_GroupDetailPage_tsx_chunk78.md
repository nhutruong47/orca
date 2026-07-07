# Knowledge Document: GroupDetailPage.tsx (Chunk 79/136)

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
  "chunk_index": 78,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
or: '#94a3b8', textAlign: 'center', padding: '10px 0' }}>Chưa có vai trò nào</div>
                            ) : (
                                teamRoles.map(role => (
                                    <div key={role} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 14px', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: 8 }}>
                                        <span style={{ fontSize: 14, fontWeight: 600, color: '#1e293b' }}>{role}</span>
                                        <button onClick={async () => {
                                            const updatedRoles = teamRoles.filter(r => r !== role);
                                            setTeamRoles(updatedRoles);
                                            const newMetadata = JSON.stringify({ ...JSON.parse(team?.metadata || '{}'), roles: updatedRoles });
                                            try {
                                                await teamService.update(team!.id, { metadata: newMetadata });
                                                setTeam(prev => prev ? { ...prev, metadata: newMetadata } : prev);
                                            } catch (e) { console.error(e); }
                                        }} style={{ background: 'transparent', border: 'none', color: '#ef4444', cursor: 'pointer', display: 'flex', alignItems: 'center', padding: 4 }}>
                                            <ion-icon name="trash-outline" style={{ fontSize: 16 }}></ion-icon>
                                        </button>
                                    </div>
                                ))
                            )}
                        </div>
                        
                        <div style={{ display: 'flex', gap: 8 }}>
                            <input
                                value={newRoleName}
                                onChange={e => setNewRoleName(e.target.value)}
                                placeholder="Nhập tên vai trò mới..."
                                style={{ flex: 1, padding: '10px 14px', borderRadius: 10, border: '1px solid #cbd5e1', fontSize: 14, outline: 'none' }}
                                onKeyDown={e => {
                                    if (e.key === 'Enter' && newRoleName.trim()) {

```
