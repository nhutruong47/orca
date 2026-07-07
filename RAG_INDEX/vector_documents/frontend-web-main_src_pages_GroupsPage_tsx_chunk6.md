# Knowledge Document: GroupsPage.tsx (Chunk 7/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 6,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
'Chưa có mô tả'}</td>
                      <td>{group.memberCount || group.members?.length || 0}</td>
                      <td>
                        <span className={`badge ${group.isPublished ? 'badge-success' : 'badge-info'}`}>
                          {group.isPublished ? 'Đang hiển thị' : 'Chưa đăng'}
                        </span>
                      </td>
                      <td>
                        <div className="td-actions" style={{ justifyContent: 'flex-end' }}>
                          <button type="button" className="btn btn-secondary" onClick={() => navigate(`/groups/${group.id}`)}>
                            Chi tiết
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        </>
      )}

      {showCreateModal && (
        <div className="modal-overlay" onClick={closeCreateModal}>
          <div className="modal" onClick={event => event.stopPropagation()} style={{ maxWidth: 520 }}>
            <div className="modal-header" style={{ padding: 0, paddingBottom: 16, marginBottom: 18 }}>
              <h2>Tạo nhóm xưởng mới</h2>
              <button type="button" className="modal-close" onClick={closeCreateModal} aria-label="Đóng">
                <ion-icon name="close-outline"></ion-icon>
              </button>
            </div>

            <form onSubmit={handleCreateGroup} className="auth-form">
              {error && (
                <div className="form-error">
                  <ion-icon name="alert-circle-outline"></ion-icon>
                  {error}
                </div>
              )}

              <div className="form-group">
                <label className="form-label">Tên nhóm *</label>
                <input
                  className="form-input"
                  style={{ paddingLeft: 14 }}
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

```
