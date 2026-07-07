# Knowledge Document: RegisterPage.tsx (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard

## Source Code Chunk
```tsx
  return;
        }

        if (password.length < 6) {
            setError('Mật khẩu phải có ít nhất 6 ký tự!');
            return;
        }

        if (password !== confirmPassword) {
            setError('Mật khẩu xác nhận không khớp!');
            return;
        }

        setIsLoading(true);
        try {
            await register({ username, password });
            if (rememberMe) {
                localStorage.setItem('orca_remember_username', username.trim());
            } else {
                localStorage.removeItem('orca_remember_username');
            }
            navigate(returnUrl);
        } catch (err: unknown) {
            if (err && typeof err === 'object' && 'response' in err) {
                const axiosErr = err as { response?: { data?: { error?: string } } };
                setError(friendlyRegisterError(axiosErr.response?.data?.error));
            } else {
                setError('Không thể kết nối đến server!');
            }
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="auth-container">
            <div className="auth-bg-shapes">
                <div className="shape shape-1" />
                <div className="shape shape-2" />
                <div className="shape shape-3" />
            </div>

            <div className="auth-card">
                <div className="auth-logo">
                    <img className="auth-brand-full-logo" src={orcaLogo} alt="ORCA" />
                    <p className="auth-subtitle">Tạo tài khoản mới</p>
                </div>

                <form onSubmit={handleSubmit} className="auth-form">
                    <div className="form-group">
                        <label className="form-label">Tài khoản</label>
                        <div className="input-container">
                            <span className="input-icon"><ion-icon name="person-outline" style={{ fontSize: '16px' }}></ion-icon></span>
                            <input
                                id="register-username"
                                type="text"
                                className="form-input"
                                placeholder="Nhập tên đăng nhập"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}

```
