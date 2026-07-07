# Knowledge Document: LoginPage.tsx (Chunk 7/8)

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
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, authorization

## Source Code Chunk
```tsx
                          type="button"
                                    className="password-toggle-btn login-password-toggle"
                                    onClick={() => setShowPassword(prev => !prev)}
                                    aria-label={showPassword ? 'Ẩn mật khẩu' : 'Hiện mật khẩu'}
                                    title={showPassword ? 'Ẩn mật khẩu' : 'Hiện mật khẩu'}
                                >
                                    <ion-icon name={showPassword ? 'eye-off-outline' : 'eye-outline'}></ion-icon>
                                </button>
                            </div>
                        </div>

                        <label className="remember-row login-remember-row">
                            <input
                                type="checkbox"
                                checked={rememberMe}
                                onChange={e => setRememberMe(e.target.checked)}
                            />
                            <span>Ghi nhớ tài khoản</span>
                        </label>

                        {error && (
                            <div className="login-error">
                                <svg viewBox="0 0 20 20" fill="currentColor" width="16" height="16">
                                    <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                                </svg>
                                {error}
                            </div>
                        )}

                        <button
                            id="login-submit"
                            type="submit"
                            className={`login-btn-primary ${isLoading ? 'loading' : ''}`}
                            disabled={isLoading}
                        >
                            {isLoading ? (
                                <><span className="login-spinner" /> Đang đăng nhập...</>
                            ) : (
                                'Đăng nhập'
                            )}
                        </button>
                    </form>

                    <div className="login-divider"><span>hoặc</span></div>

                    <button
                        id="google-login"
                        className="login-btn-google"

```
