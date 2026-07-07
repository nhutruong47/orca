# Knowledge Document: LoginPage.tsx (Chunk 4/8)

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
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, authorization

## Source Code Chunk
```tsx
d, i) => {
                                const logo = COFFEE_BRAND_LOGOS[i];
                                return (
                                    <div
                                        key={brand.name}
                                        className={`login-brand-card ${i === activeBrand ? 'active' : ''}`}
                                        onClick={() => setActiveBrand(i)}
                                    >
                                        <span className={`login-brand-logo login-brand-logo--${logo.key}`}>
                                            <img
                                                src={logo.src}
                                                alt={`${brand.name} logo`}
                                                loading="lazy"
                                                onError={(event) => {
                                                    event.currentTarget.style.display = 'none';
                                                    event.currentTarget.parentElement?.classList.add('login-brand-logo--fallback');
                                                }}
                                            />
                                            <span className="login-brand-logo-fallback">
                                                <strong>{logo.top}</strong>
                                                <small>{logo.bottom}</small>
                                            </span>
                                        </span>
                                        <div>
                                            <div className="login-brand-name">{brand.name}</div>
                                            <div className="login-brand-desc">{brand.desc}</div>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                        <div className="login-brands-dots">
                            {COFFEE_BRANDS.map((_, i) => (
                                <span key={i} className={`dot ${i === activeBrand ? 'active' : ''}`}
                                    onClick={() => setActiveBrand(i)} />
                            ))}
                        </div>
                    </div>


```
