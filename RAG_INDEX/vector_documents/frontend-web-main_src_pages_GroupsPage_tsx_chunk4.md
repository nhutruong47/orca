# Knowledge Document: GroupsPage.tsx (Chunk 5/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 4,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
ing: '64px 20px' }}>
          <div className="btn-spinner" />
          <p>Đang tải danh sách nhóm...</p>
        </div>
      ) : groups.length === 0 ? (
        <div className="empty-state glass-panel" style={{ padding: '72px 20px', borderStyle: 'dashed' }}>
          <div className="empty-icon">
            <span className="icon-container glow" style={{ width: 64, height: 64, fontSize: 36 }}>
              <ion-icon name="business-outline"></ion-icon>
            </span>
          </div>
          <h2 style={{ margin: '0 0 8px' }}>Chưa có nhóm xưởng</h2>
          <p>Tạo nhóm mới hoặc nhập mã mời để tham gia nhóm xưởng có sẵn.</p>
          <div style={{ display: 'flex', justifyContent: 'center', gap: 10, flexWrap: 'wrap' }}>
            <button type="button" className="btn btn-secondary" onClick={openJoinModal}>
              <ion-icon name="enter-outline" style={{ fontSize: 16 }}></ion-icon>
              Tham gia nhóm
            </button>
            <button type="button" className="btn btn-primary" onClick={openCreateModal}>
              <ion-icon name="add-circle-outline" style={{ fontSize: 16 }}></ion-icon>
              Tạo nhóm mới
            </button>
          </div>
        </div>
      ) : (
        <>
          <section style={{ marginBottom: 20 }}>
            <h2 className="section-title" style={{ fontSize: 18, marginBottom: 12 }}>Nhóm của bạn</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 16 }}>
              {groups.map(group => (
                <article key={group.id} className="premium-card glass-panel" style={{ padding: 18 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', gap: 14, alignItems: 'flex-start' }}>
                    <div style={{ minWidth: 0 }}>
                      <h3 style={{ margin: 0, color: 'var(--text-primary)' }}>{group.name}</h3>
                      <p style={{ margin: '8px 0 0', color: 'var(--text-secondary)', minHeight: 42 }}>
                        {group.description || 'Chưa có mô tả.'}
                      </p>
                    </div>
                    <span className="badge badge-info" style={{ whiteSpace: 'nowrap' }}>
                      {group.memberCount || group.members?.length || 0} thành viên
                    </span>
                  </div>


```
