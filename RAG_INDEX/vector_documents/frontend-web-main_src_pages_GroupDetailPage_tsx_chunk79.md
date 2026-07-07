# Knowledge Document: GroupDetailPage.tsx (Chunk 80/136)

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
  "chunk_index": 79,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
Change={e => setNewRoleName(e.target.value)}
                                placeholder="Nhập tên vai trò mới..."
                                style={{ flex: 1, padding: '10px 14px', borderRadius: 10, border: '1px solid #cbd5e1', fontSize: 14, outline: 'none' }}
                                onKeyDown={e => {
                                    if (e.key === 'Enter' && newRoleName.trim()) {
                                        const r = newRoleName.trim();
                                        if (!teamRoles.includes(r)) {
                                            const updatedRoles = [...teamRoles, r];
                                            setTeamRoles(updatedRoles);
                                            setNewRoleName('');
                                            const newMetadata = JSON.stringify({ ...JSON.parse(team?.metadata || '{}'), roles: updatedRoles });
                                            teamService.update(team!.id, { metadata: newMetadata }).then(() => {
                                                setTeam(prev => prev ? { ...prev, metadata: newMetadata } : prev);
                                            }).catch(console.error);
                                        }
                                    }
                                }}
                            />
                            <button onClick={async () => {
                                const r = newRoleName.trim();
                                if (r && !teamRoles.includes(r)) {
                                    const updatedRoles = [...teamRoles, r];
                                    setTeamRoles(updatedRoles);
                                    setNewRoleName('');
                                    const newMetadata = JSON.stringify({ ...JSON.parse(team?.metadata || '{}'), roles: updatedRoles });
                                    try {
                                        await teamService.update(team!.id, { metadata: newMetadata });
                                        setTeam(prev => prev ? { ...prev, metadata: newMetadata } : prev);
                                    } catch (e) { console.error(e); }
                                }
                            }} style={{ background: '#d4a574', color: '#fff', border: 'none', borderRadius: 10, padding: '0 16px', fontWeight: 600, cursor: 'pointer' }}>

```
