# Knowledge Document: GroupsPage.tsx (Chunk 9/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
orm-group">
                <label className="form-label">Ma moi nhom</label>
                <input
                  className="form-input"
                  style={{ paddingLeft: 14, textTransform: 'uppercase', letterSpacing: 2 }}
                  value={inviteCode}
                  onChange={event => setInviteCode(event.target.value.toUpperCase())}
                  placeholder="VD: ABC123"
                  maxLength={6}
                  autoFocus
                />
              </div>

              <p style={{ margin: '10px 0 0', color: 'var(--text-secondary)', fontSize: 13 }}>
                Nhap ma moi 6 ky tu do chu nhom cung cap de tham gia nhom xuong.
              </p>

              <div className="modal-actions">
                <button type="button" className="btn btn-secondary" onClick={closeJoinModal} disabled={saving}>
                  Hủy
                </button>
                <button type="submit" className="btn btn-primary" disabled={saving || !inviteCode.trim()}>
                  {saving ? 'Dang tham gia...' : 'Tham gia'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {managedTeam && (
        <div className="modal-overlay" onClick={closeManageModal}>
          <div className="modal" onClick={event => event.stopPropagation()} style={{ maxWidth: 560 }}>
            <div className="modal-header" style={{ padding: 0, paddingBottom: 16, marginBottom: 18 }}>
              <div>
                <h2>Quan ly nhom</h2>
                <p style={{ margin: '4px 0 0', color: 'var(--text-secondary)', fontSize: 13 }}>{managedTeam.name}</p>
              </div>
              <button type="button" className="modal-close" onClick={closeManageModal} aria-label="Dong">
                <ion-icon name="close-outline"></ion-icon>
              </button>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: 10, marginBottom: 18 }}>
              <button type="button" className="btn btn-secondary" onClick={() => navigate(`/groups/${managedTeam.id}`)}>
                <ion-icon name="open-outline" style={{ fontSize: 16 }}></ion-icon>
                Vao chi tiet
              </button>

```
