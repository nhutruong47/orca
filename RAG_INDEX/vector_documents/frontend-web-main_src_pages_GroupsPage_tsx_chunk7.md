# Knowledge Document: GroupsPage.tsx (Chunk 8/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 7,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
              value={name}
                  onChange={event => setName(event.target.value)}
                  placeholder="VD: Xưởng rang Đà Lạt"
                  autoFocus
                />
              </div>

              <div className="form-group">
                <label className="form-label">Mô tả</label>
                <textarea
                  className="form-input form-textarea"
                  style={{ paddingLeft: 14 }}
                  value={description}
                  onChange={event => setDescription(event.target.value)}
                  placeholder="Mô tả ngắn về xưởng, năng lực hoặc khu vực..."
                />
              </div>

              <div className="modal-actions">
                <button type="button" className="btn btn-secondary" onClick={closeCreateModal} disabled={saving}>
                  Hủy
                </button>
                <button type="submit" className="btn btn-primary" disabled={saving}>
                  {saving ? 'Đang tạo...' : 'Tạo nhóm'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {showJoinModal && (
        <div className="modal-overlay" onClick={closeJoinModal}>
          <div className="modal" onClick={event => event.stopPropagation()} style={{ maxWidth: 460 }}>
            <div className="modal-header" style={{ padding: 0, paddingBottom: 16, marginBottom: 18 }}>
              <h2>Tham gia nhóm xưởng</h2>
              <button type="button" className="modal-close" onClick={closeJoinModal} aria-label="Đóng">
                <ion-icon name="close-outline"></ion-icon>
              </button>
            </div>

            <form onSubmit={handleJoinGroup} className="auth-form">
              {error && (
                <div className="form-error">
                  <ion-icon name="alert-circle-outline"></ion-icon>
                  {error}
                </div>
              )}

              <div className="form-group">
                <label className="form-label">Ma moi nhom</label>
                <input
                  className="form-input"
                  style={{ paddingLeft: 14, textTransform: 'uppercase', letterSpacing: 2 }}
                  value={inviteCode}
                  onChange={event => setInviteCode(event.target.value.toUpperCase())}
                  placeholder="VD: ABC123"

```
