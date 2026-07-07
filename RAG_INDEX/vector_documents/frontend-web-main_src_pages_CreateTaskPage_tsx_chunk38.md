# Knowledge Document: CreateTaskPage.tsx (Chunk 39/66)

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
  "chunk_index": 38,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
transform 0.2s' }}></ion-icon>
                            {categoryOpen && (
                                <ul className="task-select-menu" role="listbox">
                                    {categoryOptions.map(option => (
                                        <li key={option}>
                                            <button
                                                type="button"
                                                className={`task-select-option ${category === option ? 'active' : ''}`}
                                                role="option"
                                                aria-selected={category === option}
                                                onClick={() => {
                                                    setCategory(option);
                                                    setCategoryOpen(false);
                                                }}
                                            >
                                                {option}
                                            </button>
                                        </li>
                                    ))}
                                </ul>
                            )}
                        </div>
                    </div>

                    <div>
                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 8 }}>
                            Mức ưu tiên
                        </label>
                        <div style={{ display: 'flex', borderRadius: 10, border: '1px solid var(--border)', overflow: 'hidden' }}>
                            {['Thấp', 'Trung bình', 'Cao'].map((level) => (
                                <button
                                    key={level}
                                    onClick={() => setPriority(level)}
                                    style={{
                                        flex: 1, padding: '10px 0', fontSize: 13, fontWeight: 600,
                                        border: 'none', borderRight: level !== 'Cao' ? '1px solid var(--border)' : 'none',
                                        background: priority === level ? '#d4a574' : 'transparent',
                                        color: priority === level ? '#ffffff' : 'var(--text-secondary)',

```
