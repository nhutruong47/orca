# Knowledge Document: ProfilePage.tsx (Chunk 9/11)

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
  "chunk_index": 8,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
ecurity-label">Mật khẩu</span>
                            <span className="security-value">Được bảo vệ bằng mã hóa chuẩn công nghiệp BCrypt</span>
                        </div>
                    </div>
                    <div className="security-item">
                        <span className="security-icon"><ion-icon name="finger-print-outline" style={{ fontSize: '16px' }}></ion-icon></span>
                        <div>
                            <span className="security-label">Phiên đăng nhập</span>
                            <span className="security-value">Xác thực bằng thẻ JWT bảo mật cao</span>
                        </div>
                    </div>
                </div>

                <div className="profile-security-actions">
                    <button
                        type="button"
                        className="secondary-button"
                        onClick={() => {
                            setPasswordMode('change');
                            setFeedback(null);
                        }}
                    >
                        <ion-icon name="key-outline"></ion-icon>
                        Đổi mật khẩu
                    </button>
                    <button
                        type="button"
                        className="secondary-button"
                        onClick={() => {
                            setPasswordMode('reset');
                            setPasswordForm(current => ({ ...current, username: user?.username || '' }));
                            setFeedback(null);
                        }}
                    >
                        <ion-icon name="refresh-outline"></ion-icon>
                        Đặt lại mật khẩu
                    </button>
                </div>

                {passwordMode && (
                    <div className="profile-password-panel">
                        <div className="profile-password-heading">
                            <div>
                                <h3>{passwordMode === 'change' ? 'Đổi mật khẩu' : 'Đặt lại mật khẩu'}</h3>
                                <p>
                                    {passwordMode === 'change'
                                        ? 'Nhập mật khẩu hiện tại để xác nhận thay đổi.'
                                        : 'Xác nhận tên đăng nhập của tài khoản đang đăng nhập.'}

```
