# Knowledge Document: RegisterPage.tsx (Chunk 5/5)

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
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard

## Source Code Chunk
```tsx
             {error && (
                        <div className="form-error">
                            <ion-icon name="alert-circle-outline" style={{ fontSize: '16px', verticalAlign: 'middle', marginRight: 4 }}></ion-icon> {error}
                        </div>
                    )}

                    <button
                        id="register-submit"
                        type="submit"
                        className={`btn btn-primary ${isLoading ? 'btn-loading' : ''}`}
                        disabled={isLoading}
                    >
                        {isLoading ? (
                            <>
                                <span className="btn-spinner" />
                                Đang đăng ký...
                            </>
                        ) : (
                            'Đăng ký'
                        )}
                    </button>
                </form>

                <div className="auth-footer">
                    <p>
                        Đã có tài khoản?{' '}
                        <Link to={`/login${returnUrl !== '/dashboard' ? `?returnUrl=${encodeURIComponent(returnUrl)}` : ''}`} className="auth-link">
                            Đăng nhập
                        </Link>
                    </p>
                </div>
            </div>
        </div>
    );
}

```
