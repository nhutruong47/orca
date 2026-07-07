# Knowledge Document: GroupDetailPage.tsx (Chunk 76/136)

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
  "chunk_index": 75,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
{showLabelModal && selectedMemberForLabels && (
                <div className="modal-overlay" onClick={() => setShowLabelModal(false)} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(4px)', zIndex: 1000 }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 400, background: '#fff', color: '#1a1a1a', borderRadius: 16, padding: '24px' }}>
                        <h2 style={{ margin: '0 0 8px', color: '#1e293b', fontSize: 18 }}>Phân vai trò</h2>
                        <p style={{ fontSize: 13, color: '#64748b', marginBottom: 20 }}>
                            Gán vai trò cho <b>{selectedMemberForLabels.fullName || selectedMemberForLabels.username}</b>. Bạn có thể chọn từ danh sách hoặc tự nhập ở dưới.
                        </p>
                        
                        {teamRoles.length > 0 && (
                            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginBottom: 16 }}>
                                {teamRoles.map(role => {
                                    const currentRoles = editingLabels.split(',').map(r => r.trim()).filter(r => r);
                                    const isSelected = currentRoles.includes(role);
                                    return (
                                        <button 
                                            key={role}
                                            onClick={() => {
                                                if (isSelected) {
                                                    setEditingLabels(currentRoles.filter(r => r !== role).join(', '));
                                                } else {
                                                    setEditingLabels([...currentRoles, role].join(', '));
                                                }
                                            }}
                                            style={{ 
                                                padding: '6px 12px', 
                                                borderRadius: 12, 
                                                border: isSelected ? '1px solid #d4a574' : '1px solid #e2e8f0', 
                                                background: isSelected ? '#fff7ed' : '#f8fafc', 
                                                color: isSelected ? '#d97706' : '#64748b', 

```
