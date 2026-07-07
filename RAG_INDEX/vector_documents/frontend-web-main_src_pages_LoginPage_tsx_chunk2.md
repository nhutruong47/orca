# Knowledge Document: LoginPage.tsx (Chunk 3/8)

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
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, authorization

## Source Code Chunk
```tsx
          localStorage.setItem('orca_remember_password', password.trim());
            } else {
                localStorage.removeItem('orca_remember_username');
                localStorage.removeItem('orca_remember_password');
            }
            navigate(returnUrl, { replace: true });
        } catch (err: unknown) {
            if (err && typeof err === 'object' && 'response' in err) {
                const axiosErr = err as { response?: { data?: { error?: string } } };
                setError(axiosErr.response?.data?.error || 'Đăng nhập thất bại!');
            } else {
                setError('Không thể kết nối đến server!');
            }
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="login-split">
            {/* LEFT — Hero side with coffee brands */}
            <div className="login-hero">
                <div className="login-hero-overlay" />
                <img src="/coffee-hero.png" alt="Coffee Workshop" className="login-hero-img" />

                <div className="login-hero-content">
                    <div className="login-hero-badge">ORCA Coffee Platform</div>
                    <h1 className="login-hero-title">
                        Nền tảng quản lý<br />
                        <span className="login-hero-highlight">xưởng cà phê</span><br />
                        thông minh
                    </h1>
                    <p className="login-hero-desc">
                        Tích hợp AI để tối ưu quy trình sản xuất, quản lý nguyên liệu,
                        theo dõi đơn hàng và phân công công việc tự động.
                    </p>

                    {/* Famous coffee brands carousel */}
                    <div className="login-brands">
                        <p className="login-brands-label">Đối tác & Xưởng cà phê nổi bật</p>
                        <div className="login-brands-list">
                            {COFFEE_BRANDS.map((brand, i) => {
                                const logo = COFFEE_BRAND_LOGOS[i];
                                return (
                                    <div
                                        key={brand.name}
                                        className={`login-brand-card ${i === activeBrand ? 'active' : ''}`}
                                        onClick={() => setActiveBrand(i)}

```
