# Knowledge Document: ProfilePage.tsx (Chunk 10/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProfilePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 9,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
 <div>
                                <h3>{passwordMode === 'change' ? 'Đổi mật khẩu' : 'Đặt lại mật khẩu'}</h3>
                                <p>
                                    {passwordMode === 'change'
                                        ? 'Nhập mật khẩu hiện tại để xác nhận thay đổi.'
                                        : 'Xác nhận tên đăng nhập của tài khoản đang đăng nhập.'}
                                </p>
                            </div>
                            <button type="button" className="profile-password-close" onClick={closePasswordForm}>
                                <ion-icon name="close-outline"></ion-icon>
                            </button>
                        </div>

                        <div className="profile-password-grid">
                            {passwordMode === 'change' ? (
                                <label>
                                    <span>Mật khẩu hiện tại</span>
                                    <input
                                        type="password"
                                        value={passwordForm.currentPassword}
                                        onChange={event => setPasswordForm(current => ({ ...current, currentPassword: event.target.value }))}
                                        autoComplete="current-password"
                                    />
                                </label>
                            ) : (
                                <label>
                                    <span>Xác nhận tên đăng nhập</span>
                                    <input
                                        type="text"
                                        value={passwordForm.username}
                                        onChange={event => setPasswordForm(current => ({ ...current, username: event.target.value }))}
                                        autoComplete="username"
                                    />
                                </label>
                            )}
                            <label>
                                <span>Mật khẩu mới</span>
                                <input
                                    type="password"
                                    value={passwordForm.newPassword}

```
