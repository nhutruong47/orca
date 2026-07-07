# Knowledge Document: RegisterPage.tsx (Chunk 3/5)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/RegisterPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "dashboard",
  "tags": [
    "dashboard"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard

## Source Code Chunk
```tsx
</ion-icon></span>
                            <input
                                id="register-username"
                                type="text"
                                className="form-input"
                                placeholder="Nhập tên đăng nhập"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                autoComplete="username"
                            />
                        </div>
                    </div>

                    <div className="form-group">
                        <label className="form-label">Mật khẩu</label>
                        <div className="input-container">
                            <span className="input-icon"><ion-icon name="lock-closed-outline" style={{ fontSize: '16px' }}></ion-icon></span>
                            <input
                                id="register-password"
                                type={showPassword ? 'text' : 'password'}
                                className="form-input password-input"
                                placeholder="Ít nhất 6 ký tự"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                autoComplete="new-password"
                            />
                            <button
                                type="button"
                                className="password-toggle-btn"
                                onClick={() => setShowPassword(prev => !prev)}
                                aria-label={showPassword ? 'Ẩn mật khẩu' : 'Hiện mật khẩu'}
                                title={showPassword ? 'Ẩn mật khẩu' : 'Hiện mật khẩu'}
                            >
                                <ion-icon name={showPassword ? 'eye-off-outline' : 'eye-outline'}></ion-icon>
                            </button>
                        </div>
                    </div>

                    <div className="form-group">
                        <label className="form-label">Xác nhận mật khẩu</label>
                        <div className="input-container">
                            <span className="input-icon"><ion-icon name="shield-checkmark-outline" style={{ fontSize: '16px' }}></ion-icon></span>
                            <input

```
