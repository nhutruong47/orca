# Knowledge Document: DashboardPage.tsx (Chunk 4/9)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "workspace",
  "tags": [
    "workspace",
    "factory",
    "dashboard",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
k) => sum + (task.actualOutput || 0), 0);
    const isOverachieving = totalTarget > 0 && totalActual > totalTarget;

    if (loading) {
        return (
            <div className="dashboard-page dashboard-loading">
                <div className="btn-spinner" />
                <p>Đang tải dashboard...</p>
            </div>
        );
    }

    return (
        <div className="dashboard-page">
            <section className="dashboard-command">
                <div className="dashboard-command-main">
                    <span className="dashboard-eyebrow">Tổng quan vận hành</span>
                    <h1>Xin chào, {displayName}</h1>
                    <p>Theo dõi nhóm xưởng, tiến độ và việc cần xử lý trong ngày từ một màn hình gọn hơn.</p>
                    <div className="dashboard-command-actions">
                        <button className="dashboard-primary-action" onClick={() => navigate('/groups')} type="button">
                            <Plus size={18} />
                            Mở nhóm xưởng
                        </button>
                        <button onClick={() => goToTeamFeature('/create-task')} type="button">
                            <ClipboardList size={18} />
                            Tạo công việc
                        </button>
                    </div>
                </div>

                <div className={`dashboard-ops-card ${isOverachieving ? 'overachieving' : isOverloaded ? 'overloaded' : ''}`} aria-label="Trạng thái vận hành">
                    <div className="dashboard-ops-head">
                        <Activity size={18} />
                        <span>Nhịp vận hành</span>
                    </div>
                    <strong>{isOverachieving ? 'Phát triển vượt mong đợi' : isOverloaded ? 'Quá tải công việc' : activeTasks.length > 0 ? 'Đang có việc cần bám' : 'Không có việc quá tải'}</strong>
                    <p>{isOverachieving ? `Sản lượng đạt ${totalActual}/${totalTarget}, vượt mức kế hoạch đề ra.` : isOverloaded ? `Đã hết ngày nhưng còn ${activeTasks.length} task chưa xong.` : activeTasks.length > 0 ? `${activeTasks.length} task chưa hoàn thành.` : 'Bạn có thể tạo thêm kế hoạch hoặc kiểm tra nhóm xưởng.'}</p>
                    <div className="dashboard-progress-track">

```
