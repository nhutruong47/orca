# Knowledge Document: SettingsPage.tsx (Chunk 4/4)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/SettingsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security

## Source Code Chunk
```tsx
<span className="settings-pill">Giao diện</span>
                    <h2>Chế độ hiển thị</h2>
                    <p>{theme === 'dark' ? 'Đang dùng giao diện tối' : 'Đang dùng giao diện sáng'}</p>
                </div>
                <button className={`theme-toggle-btn ${theme}`} onClick={toggleTheme}>
                    <span className="toggle-icon">
                        {theme === 'dark'
                            ? <ion-icon name="moon-outline" style={{ fontSize: '14px' }}></ion-icon>
                            : <ion-icon name="sunny-outline" style={{ fontSize: '14px' }}></ion-icon>}
                    </span>
                    <span className="toggle-knob" />
                </button>
            </section>
        </div>
    );
}

```
