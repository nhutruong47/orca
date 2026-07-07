# Knowledge Document: CreateTaskPage.tsx (Chunk 37/66)

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
  "chunk_index": 36,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
px) {
                    .main-content-layout {
                        grid-template-columns: 1fr;
                    }
                }
            `}</style>

            {/* Navigation Header */}
            <div style={{ width: '100%', maxWidth: 1440, marginBottom: 32 }}>
                <button
                    onClick={() => navigate(`/groups/${teamId}`)}
                    style={{
                        background: 'none', border: 'none', color: '#d4a574',
                        fontSize: 14, fontWeight: 600, display: 'flex', alignItems: 'center', gap: 6,
                        cursor: 'pointer', padding: 0, marginBottom: 16
                    }}
                >
                    <ion-icon name="arrow-back-outline"></ion-icon> Quay lại tổng quan
                </button>
                <h1 style={{ margin: 0, fontSize: 32, fontWeight: 800, color: 'var(--text-primary)' }}>
                    Tạo công việc mới
                </h1>
                <p style={{ margin: '8px 0 0', color: 'var(--text-secondary)', fontSize: 15 }}>
                    Mô tả nhiệm vụ cần thực hiện, AI sẽ phân tích và chuẩn hóa thành task có cấu trúc.
                </p>
            </div>

            {/* Split Layout */}
            <div className="main-content-layout">

                {/* Left Panel: Group Info Form */}
                <div style={{
                    background: 'var(--bg-card)',
                    borderRadius: 16,
                    border: '1px solid var(--border)',
                    padding: 24,
                    boxShadow: '0 4px 24px rgba(0,0,0,0.04)'
                }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 24 }}>
                        <span style={{ color: '#ec4899', fontSize: 20 }}><ion-icon name="business-outline"></ion-icon></span>
                        <h2 style={{ margin: 0, fontSize: 18, fontWeight: 700, color: 'var(--text-primary)' }}>Thông tin nhóm</h2>
                    </div>

                    <div style={{ marginBottom: 20 }}>
                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 8 }}>
                            Tên nhóm
                        </label>
                        <input
                            type="text"

```
