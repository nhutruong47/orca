# Knowledge Document: CreateTaskPage.tsx (Chunk 38/66)

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
  "chunk_index": 37,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
ext-primary)' }}>Thông tin nhóm</h2>
                    </div>

                    <div style={{ marginBottom: 20 }}>
                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 8 }}>
                            Tên nhóm
                        </label>
                        <input
                            type="text"
                            value={team!.name}
                            readOnly
                            style={{
                                width: '100%', padding: '12px 14px', borderRadius: 10,
                                border: '1px solid var(--border)', background: 'var(--bg-primary)',
                                color: 'var(--text-secondary)', fontSize: 14, outline: 'none', cursor: 'not-allowed'
                            }}
                        />
                    </div>

                    <div style={{ marginBottom: 24 }}>
                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 8 }}>
                            Danh mục
                        </label>
                        <div ref={categoryMenuRef} style={{ position: 'relative' }}>
                            <button
                                type="button"
                                className="task-select-trigger"
                                aria-haspopup="listbox"
                                aria-expanded={categoryOpen}
                                onClick={() => setCategoryOpen(open => !open)}
                            >
                                {category}
                            </button>
                            <ion-icon name="chevron-down-outline" style={{ position: 'absolute', right: 14, top: '50%', transform: `translateY(-50%) rotate(${categoryOpen ? 180 : 0}deg)`, color: 'var(--text-secondary)', pointerEvents: 'none', transition: 'transform 0.2s' }}></ion-icon>
                            {categoryOpen && (
                                <ul className="task-select-menu" role="listbox">
                                    {categoryOptions.map(option => (
                                        <li key={option}>
                                            <button
                                                type="button"

```
