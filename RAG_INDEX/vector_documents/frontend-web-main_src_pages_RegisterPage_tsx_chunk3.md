# Knowledge Document: RegisterPage.tsx (Chunk 4/5)

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
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard

## Source Code Chunk
```tsx
v>
                    </div>

                    <div className="form-group">
                        <label className="form-label">Xác nhận mật khẩu</label>
                        <div className="input-container">
                            <span className="input-icon"><ion-icon name="shield-checkmark-outline" style={{ fontSize: '16px' }}></ion-icon></span>
                            <input
                                id="register-confirm-password"
                                type={showConfirmPassword ? 'text' : 'password'}
                                className="form-input"
                                placeholder="Nhập lại mật khẩu"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                autoComplete="new-password"
                            />
                            <button
                                type="button"
                                className="password-toggle-btn"
                                onClick={() => setShowConfirmPassword(prev => !prev)}
                                aria-label={showConfirmPassword ? 'Ẩn mật khẩu xác nhận' : 'Hiện mật khẩu xác nhận'}
                                title={showConfirmPassword ? 'Ẩn mật khẩu xác nhận' : 'Hiện mật khẩu xác nhận'}
                            >
                                <ion-icon name={showConfirmPassword ? 'eye-off-outline' : 'eye-outline'}></ion-icon>
                            </button>
                        </div>
                    </div>

                    <label className="remember-row">
                        <input
                            type="checkbox"
                            checked={rememberMe}
                            onChange={e => setRememberMe(e.target.checked)}
                        />
                        <span>Ghi nhớ tài khoản</span>
                    </label>

                    {error && (
                        <div className="form-error">
                            <ion-icon name="alert-circle-outline" style={{ fontSize: '16px', verticalAlign: 'middle', marginRight: 4 }}></ion-icon> {error}
                        </div>
                    )}

                    <button
                        id="register-submit"
                        type="submit"

```
