# Knowledge Document: CreateTaskPage.tsx (Chunk 53/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 52,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
sk => task.suggestedAssignee || task.assignee).length;
    const totalTasks = editedResult.tasks?.length || 0;
    const memberName = (member: TeamMemberInfo) => member.fullName || member.username || 'Thành viên';

    return (
        <div style={{
            width: '100%',
            background: 'var(--bg-card)',
            borderRadius: '24px',
            border: '1px solid var(--border)',
            boxShadow: '0 10px 40px rgba(0,0,0,0.08)',
            overflow: 'hidden',
            marginBottom: 16,
            animation: 'slideUp 0.4s ease-out'
        }}>
            {/* Header Area */}
            <div style={{ padding: '24px 32px', borderBottom: '1px solid var(--border)', position: 'relative' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 8 }}>
                    <h2 style={{ margin: 0, fontSize: 24, fontWeight: 800, color: 'var(--text-primary)' }}>Xem trước công việc</h2>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 6, background: 'rgba(212, 165, 116, 0.12)', color: 'var(--accent-primary)', padding: '4px 12px', borderRadius: '20px', fontSize: 11, fontWeight: 700 }}>
                        <ion-icon name="checkmark-done-outline"></ion-icon> AI ĐÃ XỬ LÝ
                    </div>
                </div>
                <p style={{ margin: 0, fontSize: 14, color: 'var(--text-secondary)' }}>Xem lại chi tiết công việc và phân bổ nhân sự trước khi xác nhận.</p>
            </div>

            <div style={{ padding: '32px' }}>
                {/* Standardization Card */}
                <div style={{ background: 'var(--bg-secondary)', borderRadius: '16px', border: '1px solid var(--border)', padding: '24px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 20 }}>
                        <span style={{ fontSize: 20, color: '#f59e0b' }}><ion-icon name="clipboard-outline"></ion-icon></span>
                        <div style={{ flex: 1 }}>
                            <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: 'var(--text-primary)' }}>Công việc đã chuẩn hóa</h3>
                            <p style={{ margin: '4px 0 0', fontSize: 12, color: 'var(--text-secondary)' }}>

```
