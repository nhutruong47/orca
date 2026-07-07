# Knowledge Document: LoginPage.tsx (Chunk 5/8)

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
  "chunk_index": 4,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, authorization

## Source Code Chunk
```tsx
         </div>
                        <div className="login-brands-dots">
                            {COFFEE_BRANDS.map((_, i) => (
                                <span key={i} className={`dot ${i === activeBrand ? 'active' : ''}`}
                                    onClick={() => setActiveBrand(i)} />
                            ))}
                        </div>
                    </div>

                    <div className="login-hero-stats">
                        <div className="login-hero-stat">
                            <span className="stat-value">500+</span>
                            <span className="stat-label">Xưởng sử dụng</span>
                        </div>
                        <div className="login-hero-stat">
                            <span className="stat-value">10K+</span>
                            <span className="stat-label">Đơn hàng/tháng</span>
                        </div>
                        <div className="login-hero-stat">
                            <span className="stat-value">99.9%</span>
                            <span className="stat-label">Uptime</span>
                        </div>
                    </div>
                </div>
            </div>

            {/* RIGHT — Login form */}
            <div className="login-form-side">
                <div className="login-form-container">
                    <div className="login-form-header">
                        <div className="login-logo-row">
                            <img src={orcaLogo} alt="ORCA" className="login-brand-full-logo" />
                        </div>
                        <h2 className="login-form-title">Chào mừng trở lại!</h2>
                        <p className="login-form-subtitle">Đăng nhập để quản lý xưởng cà phê của bạn</p>
                    </div>

                    <form onSubmit={handleSubmit} className="login-form">
                        <div className="login-field">
                            <label>Tài khoản</label>
                            <div className="login-input-wrap">
                                <svg className="login-input-icon" viewBox="0 0 20 20" fill="currentColor" width="18" height="18">
                                    <path d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" />
                                </svg>
                                <input

```
