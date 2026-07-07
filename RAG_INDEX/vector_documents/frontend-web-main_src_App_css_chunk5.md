# Knowledge Document: App.css (Chunk 6/43)

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
  "chunk_index": 5,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
t-align: center;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid var(--border);
}

.auth-footer p {
  color: var(--text-secondary);
  font-size: 14px;
}

.auth-link {
  color: var(--accent-primary);
  font-weight: 600;
  transition: var(--transition);
}

.auth-link:hover {
  color: var(--text-accent);
  text-decoration: underline;
}

/* Split Layout - Responsive */
.login-split {
  display: flex;
  min-height: 100vh;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background: var(--bg-primary);
}

/* --- HERO SIDE --- */
.login-hero {
  flex: 1.2;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
}

.login-hero-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.35) saturate(1.2);
}

.login-hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top,
      rgba(10, 14, 23, 0.95) 0%,
      rgba(10, 14, 23, 0.7) 40%,
      rgba(10, 14, 23, 0.3) 100%);
  z-index: 1;
}

.login-hero-content {
  position: relative;
  z-index: 2;
  padding: clamp(24px, 4vw, 48px);
  width: 100%;
  animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.login-hero-badge {
  display: inline-block;
  padding: 6px 16px;
  background: rgba(139, 94, 60, 0.3);
  border: 1px solid rgba(139, 94, 60, 0.5);
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  color: #d4a574;
  letter-spacing: 1px;
  margin-bottom: 16px;
}

.login-hero-title {
  font-size: clamp(24px, 6vw, 36px);
  font-weight: 800;
  line-height: 1.2;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.login-hero-highlight {
  background: linear-gradient(135deg, #d4a574, #8b5e3c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  display: inline-block;
}

.login-hero-desc {
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.6;
  max-width: 480px;
  margin-bottom: 24px;
}

/* Coffee Brands Carousel */
.login-brands {
  margin-bottom: 24px;
}

.login-brands-label {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 12px;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.login-brands-list {
  display: flex;
  gap: 10px;
  overflow: hidden;

```
