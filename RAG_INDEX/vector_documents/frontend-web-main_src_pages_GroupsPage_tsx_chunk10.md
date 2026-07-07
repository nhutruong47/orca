# Knowledge Document: GroupsPage.tsx (Chunk 11/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 10,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
       className="form-input form-textarea"
                  style={{ paddingLeft: 14 }}
                  value={editDescription}
                  onChange={event => setEditDescription(event.target.value)}
                  placeholder="Mo ta ngan ve nhom"
                />
              </div>

              <div className="modal-actions" style={{ justifyContent: 'space-between', gap: 12 }}>
                <button type="button" className="btn btn-secondary" onClick={handleDeleteManagedTeam} disabled={saving} style={{ color: '#dc2626', borderColor: '#fecaca', background: '#fff7f7' }}>
                  <ion-icon name="trash-outline" style={{ fontSize: 16 }}></ion-icon>
                  Xoa nhom
                </button>
                <div style={{ display: 'flex', gap: 8 }}>
                  <button type="button" className="btn btn-secondary" onClick={closeManageModal} disabled={saving}>
                    Huy
                  </button>
                  <button type="submit" className="btn btn-primary" disabled={saving || !editName.trim()}>
                    {saving ? 'Dang luu...' : 'Luu thay doi'}
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

```
