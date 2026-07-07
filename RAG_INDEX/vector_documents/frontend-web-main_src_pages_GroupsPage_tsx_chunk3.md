# Knowledge Document: GroupsPage.tsx (Chunk 4/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
className="btn btn-secondary" onClick={loadGroups} disabled={loading}>
              <ion-icon name="refresh-outline" style={{ fontSize: 16 }}></ion-icon>
              {loading ? 'Đang tải...' : 'Làm mới'}
            </button>
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
      </header>

      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 16, marginBottom: 20 }}>
        <div className="glass-panel premium-card" style={{ padding: 18 }}>
          <div style={{ fontSize: 12, color: 'var(--text-secondary)' }}>Tổng nhóm</div>
          <div style={{ fontSize: 24, fontWeight: 800 }}>{groups.length}</div>
        </div>
        <div className="glass-panel premium-card" style={{ padding: 18 }}>
          <div style={{ fontSize: 12, color: 'var(--text-secondary)' }}>Thành viên</div>
          <div style={{ fontSize: 24, fontWeight: 800 }}>{totalMembers}</div>
        </div>
        <div className="glass-panel premium-card" style={{ padding: 18 }}>
          <div style={{ fontSize: 12, color: 'var(--text-secondary)' }}>Đang lên Marketplace</div>
          <div style={{ fontSize: 24, fontWeight: 800 }}>{publishedCount}</div>
        </div>
      </section>

      {error && !showCreateModal && (
        <div className="form-error" style={{ marginBottom: 16 }}>
          <ion-icon name="alert-circle-outline"></ion-icon>
          {error}
        </div>
      )}

      {loading ? (
        <div className="empty-state glass-panel" style={{ padding: '64px 20px' }}>
          <div className="btn-spinner" />
          <p>Đang tải danh sách nhóm...</p>
        </div>
      ) : groups.length === 0 ? (
        <div className="empty-state glass-panel" style={{ padding: '72px 20px', borderStyle: 'dashed' }}>
          <div className="empty-icon">
            <span className="icon-container glow" style={{ width: 64, height: 64, fontSize: 36 }}>

```
