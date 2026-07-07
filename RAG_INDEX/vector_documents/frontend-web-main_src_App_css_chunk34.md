# Knowledge Document: App.css (Chunk 35/43)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/App.css",
  "language": "css",
  "module": "src",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "admin",
    "inventory",
    "security",
    "notification"
  ],
  "logical_type": "Generic",
  "chunk_index": 34,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
near-gradient(180deg, rgba(7, 10, 18, 0.08) 0%, rgba(7, 10, 18, 0.72) 100%);
}

.login-hero-content {
  width: min(880px, 100%);
  padding: 0;
  margin-top: auto;
}

.login-hero-badge {
  margin-bottom: 18px;
  padding: 8px 16px;
  color: #f4c389;
  background: rgba(185, 122, 62, 0.14);
  border-color: rgba(244, 195, 137, 0.34);
  border-radius: 999px;
  font-size: 0.74rem;
  font-weight: 850;
}

.login-hero-title {
  max-width: 760px;
  margin: 0 0 18px;
  color: #fffaf2;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: clamp(2.3rem, 4.1vw, 4.35rem);
  line-height: 1.04;
  letter-spacing: 0;
  text-shadow: 0 20px 60px rgba(0, 0, 0, 0.55);
}

.login-hero-desc {
  max-width: 620px;
  margin-bottom: 32px;
  color: rgba(255, 247, 236, 0.82);
  font-size: clamp(0.98rem, 1.2vw, 1.12rem);
  font-weight: 600;
}

.login-brands {
  width: min(1080px, 100%);
  margin: 0 0 34px;
}

.login-brands-label {
  margin-bottom: 14px;
  color: rgba(255, 247, 236, 0.72);
  font-size: 0.78rem;
  font-weight: 750;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.login-brands-list {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  overflow: visible;
}

.login-brand-card {
  min-width: 0;
  min-height: 78px;
  padding: 12px 14px;
  gap: 14px;
  background: rgba(12, 18, 33, 0.66);
  border: 1px solid rgba(255, 255, 255, 0.11);
  border-radius: 8px;
  opacity: 0.82;
  transform: none;
  backdrop-filter: blur(14px);
}

.login-brand-card.active,
.login-brand-card:hover {
  background: rgba(185, 122, 62, 0.18);
  border-color: rgba(244, 195, 137, 0.48);
  opacity: 1;
  box-shadow: 0 16px 42px rgba(0, 0, 0, 0.24);
}

.login-brand-logo {
  width: 96px;
  min-width: 96px;
  height: 46px;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 0;
  color: #fff;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.14), rgba(255, 255, 255, 0.04));
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 6px;
  line-height: 1;
  text-align: center;
}

.login-brand-logo img {
  max-width: 82px;
  max-height: 34px;
  display: block;
  object-fit: contain;
}

.login-brand-logo-fallback {
  display: none;
}

.login-brand-logo--fallback .login-brand-logo-fallback {
  display: block;
}

.login-brand-logo strong {
  display: block;
  font-size: 0.78rem;

```
