# Knowledge Document: GroupsPage.tsx (Chunk 6/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
0 0', color: 'var(--text-secondary)', minHeight: 42 }}>
                        {group.description || 'Chưa có mô tả.'}
                      </p>
                    </div>
                    <span className="badge badge-info" style={{ whiteSpace: 'nowrap' }}>
                      {group.memberCount || group.members?.length || 0} thành viên
                    </span>
                  </div>

                  <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap', marginTop: 16 }}>
                    <button type="button" className="btn btn-primary" onClick={() => navigate(`/groups/${group.id}`)}>
                      <ion-icon name="open-outline" style={{ fontSize: 16 }}></ion-icon>
                      Vào nhóm
                    </button>
                    <button type="button" className="btn btn-secondary" onClick={() => openManageModal(group)}>
                      <ion-icon name="settings-outline" style={{ fontSize: 16 }}></ion-icon>
                      Quản lý
                    </button>
                  </div>
                </article>
              ))}
            </div>
          </section>

          <section>
            <h2 className="section-title" style={{ fontSize: 18, marginBottom: 12 }}>Tất cả nhóm</h2>
            <div className="glass-panel table-container" style={{ overflowX: 'auto' }}>
              <table className="data-table" style={{ width: '100%', borderCollapse: 'collapse' }}>
                <thead>
                  <tr>
                    <th>Tên</th>
                    <th>Mô tả</th>
                    <th>Thành viên</th>
                    <th>Marketplace</th>
                    <th style={{ textAlign: 'right' }}>Thao tác</th>
                  </tr>
                </thead>
                <tbody>
                  {groups.map(group => (
                    <tr key={group.id}>
                      <td className="td-name">{group.name}</td>
                      <td className="td-desc">{group.description || 'Chưa có mô tả'}</td>
                      <td>{group.memberCount || group.members?.length || 0}</td>
                      <td>
                        <span className={`badge ${group.isPublished ? 'badge-success' : 'badge-info'}`}>
                          {group.isPublished ? 'Đang hiển thị' : 'Chưa đăng'}
                        </span>
                      </td>
                      <td>

```
