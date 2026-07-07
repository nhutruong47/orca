# Knowledge Document: SettingsPage.tsx (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security

## Source Code Chunk
```tsx
                   <button type="button" className="settings-outline-btn">Đăng xuất tất cả thiết bị</button>
                    </section>

                    <section className="settings-plan-card">
                        <span>Gói dịch vụ</span>
                        <h2>Roastery Enterprise</h2>
                        <div className="settings-plan-meter">
                            <div>
                                <span>Dung lượng hồ sơ rang</span>
                                <strong>85%</strong>
                            </div>
                            <progress value="85" max="100" />
                        </div>
                        <button type="button">Nâng cấp gói</button>
                    </section>
                </aside>
            </div>

            <section className="settings-device-card">
                <div>
                    <span className="settings-pill">Thiết bị</span>
                    <h2>Thiết bị đăng nhập</h2>
                </div>
                <div className="settings-device-list">
                    <article>
                        <span className="material-symbols-outlined">desktop_windows</span>
                        <div>
                            <strong>Windows Workstation</strong>
                            <small>Đang hoạt động · Việt Nam</small>
                        </div>
                    </article>
                    <article>
                        <span className="material-symbols-outlined">smartphone</span>
                        <div>
                            <strong>Mobile Roastery App</strong>
                            <small>Đăng nhập gần đây</small>
                        </div>
                    </article>
                </div>
            </section>

            <section className="settings-device-card settings-theme-card">
                <div>
                    <span className="settings-pill">Giao diện</span>
                    <h2>Chế độ hiển thị</h2>
                    <p>{theme === 'dark' ? 'Đang dùng giao diện tối' : 'Đang dùng giao diện sáng'}</p>
                </div>
                <button className={`theme-toggle-btn ${theme}`} onClick={toggleTheme}>
                    <span className="toggle-icon">
                        {theme === 'dark'

```
