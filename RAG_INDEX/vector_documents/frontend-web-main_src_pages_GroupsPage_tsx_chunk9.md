# Knowledge Document: GroupsPage.tsx (Chunk 10/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 9,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
 </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: 10, marginBottom: 18 }}>
              <button type="button" className="btn btn-secondary" onClick={() => navigate(`/groups/${managedTeam.id}`)}>
                <ion-icon name="open-outline" style={{ fontSize: 16 }}></ion-icon>
                Vao chi tiet
              </button>
              <button type="button" className="btn btn-secondary" onClick={() => navigator.clipboard?.writeText(managedTeam.inviteCode || '')} disabled={!managedTeam.inviteCode}>
                <ion-icon name="copy-outline" style={{ fontSize: 16 }}></ion-icon>
                Copy ma moi
              </button>
              <button type="button" className="btn btn-secondary" onClick={() => navigate(`/groups/${managedTeam.id}`)}>
                <ion-icon name="people-outline" style={{ fontSize: 16 }}></ion-icon>
                Thanh vien
              </button>
            </div>

            <form onSubmit={handleUpdateTeam} className="auth-form">
              {error && (
                <div className="form-error">
                  <ion-icon name="alert-circle-outline"></ion-icon>
                  {error}
                </div>
              )}

              <div className="form-group">
                <label className="form-label">Ten nhom</label>
                <input
                  className="form-input"
                  style={{ paddingLeft: 14 }}
                  value={editName}
                  onChange={event => setEditName(event.target.value)}
                  placeholder="Ten nhom"
                  autoFocus
                />
              </div>

              <div className="form-group">
                <label className="form-label">Mo ta</label>
                <textarea
                  className="form-input form-textarea"
                  style={{ paddingLeft: 14 }}
                  value={editDescription}
                  onChange={event => setEditDescription(event.target.value)}
                  placeholder="Mo ta ngan ve nhom"
                />
              </div>

              <div className="modal-actions" style={{ justifyContent: 'space-between', gap: 12 }}>

```
