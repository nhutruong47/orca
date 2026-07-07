# Knowledge Document: SettingsPage.tsx (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security

## Source Code Chunk
```tsx

                        <div>
                            <span>Vai trò</span>
                            <strong className="settings-dot-role">{displayRole}</strong>
                        </div>
                    </div>
                    <div className="settings-verification">
                        <img src="/coffee-hero.png" alt="Roastery verification" />
                        <div>
                            <h3>Xác thực Roastery</h3>
                            <p>Chứng chỉ chuyên gia đã được xác minh vào tháng 12, 2025.</p>
                        </div>
                    </div>
                </section>

                <aside className="settings-side-stack">
                    <section className="settings-security-card">
                        <div className="settings-side-head">
                            <h2>Bảo mật</h2>
                            <span className="material-symbols-outlined">shield</span>
                        </div>
                        <button type="button" className="settings-security-row">
                            <span className="material-symbols-outlined">key</span>
                            <span>
                                <strong>Mật khẩu</strong>
                                <small>Cập nhật 3 tháng trước</small>
                            </span>
                            <span className="material-symbols-outlined">chevron_right</span>
                        </button>
                        <button type="button" className="settings-security-row">
                            <span className="material-symbols-outlined">phonelink_lock</span>
                            <span>
                                <strong>Xác thực 2 lớp (2FA)</strong>
                                <small>Đang bật</small>
                            </span>
                            <span className="material-symbols-outlined">chevron_right</span>
                        </button>
                        <button type="button" className="settings-outline-btn">Đăng xuất tất cả thiết bị</button>
                    </section>

                    <section className="settings-plan-card">
                        <span>Gói dịch vụ</span>
                        <h2>Roastery Enterprise</h2>
                        <div className="settings-plan-meter">
                            <div>

```
