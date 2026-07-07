# Knowledge Document: App.css (Chunk 11/43)

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
  "chunk_index": 10,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
der-bottom: 1px solid var(--border);
  margin-bottom: clamp(12px, 2vw, 20px);
}

.logo-icon {
  font-size: clamp(20px, 4vw, 28px);
  filter: drop-shadow(0 0 10px rgba(212, 165, 116, 0.5));
}

.logo-text {
  font-size: clamp(16px, 3.5vw, 22px);
  font-weight: 800;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: 2px;
}

.app-logo-mark {
  width: 72px;
  height: 60px;
  object-fit: contain;
  flex-shrink: 0;
  filter: drop-shadow(0 8px 14px rgba(0, 0, 0, 0.28));
}

/* Combined logo (whale + ORCA text in one image) */
.sidebar-brand-logo {
  height: 64px;
  width: auto;
  max-width: 180px;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 2px 8px rgba(180, 120, 40, 0.4));
}

.login-brand-full-logo {
  height: 80px;
  width: auto;
  max-width: 220px;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 4px 12px rgba(180, 120, 40, 0.45));
  margin-bottom: 4px;
}

.auth-brand-full-logo {
  height: 100px;
  width: auto;
  max-width: 200px;
  object-fit: contain;
  display: block;
  margin: 0 auto 8px;
  filter: drop-shadow(0 4px 14px rgba(180, 120, 40, 0.5));
  animation: logoFloat 3s ease-in-out infinite;
}

.coffee-nav__brand-img {
  height: 72px;
  width: auto;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 4px 12px rgba(180, 120, 40, 0.55)) drop-shadow(0 8px 20px rgba(0, 0, 0, 0.4));
}


.sidebar-nav {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.nav-label {
  font-size: 10px;
  font-weight: 700;
  color: var(--shell-accent);
  letter-spacing: 2px;
  padding: 0 14px;
  margin-bottom: 8px;
  text-transform: uppercase;
  opacity: 0.85;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 14px;
  border-radius: 10px;
  color: var(--text-secondary);
  font-size: 14px;
  font-weight: 600;
  transition: var(--transition);
  position: relative;
  border: 1px solid transparent;
  background: transparent;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.nav-item:hover {
  background: var(--bg-card-hover);
  color: var(--text-primary);
  transform: translateX(2px);
  border-color: var(--border);
}

.nav-item:hover {
  background: var(--bg-input);
  color: var(--text-primary);
  transform: translateX(4px);

```
