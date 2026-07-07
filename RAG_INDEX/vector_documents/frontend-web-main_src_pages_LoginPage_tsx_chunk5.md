# Knowledge Document: LoginPage.tsx (Chunk 6/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/LoginPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "authorization"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, authorization

## Source Code Chunk
```tsx
   <label>Tài khoản</label>
                            <div className="login-input-wrap">
                                <svg className="login-input-icon" viewBox="0 0 20 20" fill="currentColor" width="18" height="18">
                                    <path d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" />
                                </svg>
                                <input
                                    id="login-username"
                                    type="text"
                                    placeholder="Nhập tên đăng nhập"
                                    value={username}
                                    onChange={e => setUsername(e.target.value)}
                                    autoComplete="username"
                                />
                            </div>
                        </div>

                        <div className="login-field">
                            <label>Mật khẩu</label>
                            <div className="login-input-wrap">
                                <svg className="login-input-icon" viewBox="0 0 20 20" fill="currentColor" width="18" height="18">
                                    <path fillRule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clipRule="evenodd" />
                                </svg>
                                <input
                                    id="login-password"
                                    type={showPassword ? 'text' : 'password'}
                                    className="password-input"
                                    placeholder="Nhập mật khẩu"
                                    value={password}
                                    onChange={e => setPassword(e.target.value)}
                                    autoComplete="current-password"
                                />
                                <button
                                    type="button"
                                    className="password-toggle-btn login-password-toggle"
                                    onClick={() => setShowPassword(prev => !prev)}
                                    aria-label={showPassword ? 'Ẩn mật khẩu' : 'Hiện mật khẩu'}
                                    title={showPassword ? 'Ẩn mật khẩu' : 'Hiện mật khẩu'}

```
