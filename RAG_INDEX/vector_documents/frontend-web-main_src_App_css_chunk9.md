# Knowledge Document: App.css (Chunk 10/43)

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
  "chunk_index": 9,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ointer;
  transition: all 0.2s;
  font-family: var(--font);
}

.login-demo-btn:hover {
  background: rgba(212, 165, 116, 0.1);
  border-color: rgba(212, 165, 116, 0.2);
}

.login-demo-btn .demo-user {
  font-size: 13px;
  font-weight: 600;
  color: #fff;
}

.login-demo-btn .demo-role {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.4);
  margin-left: auto;
}

/* Login Footer */
.login-footer {
  text-align: center;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.login-footer p {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
}

.login-link {
  color: #d4a574;
  font-weight: 600;
  transition: all 0.2s;
}

.login-link:hover {
  color: #e8c09a;
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 1024px) {
  .login-hero {
    display: none;
  }

  .login-form-side {
    flex: 1;
  }
}


/* ============================================
   Layout - Full Height Container */
.layout {
  display: flex;
  min-height: 100vh;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background: var(--bg-primary);
}

.layout-main {
  flex: 1;
  min-width: 0;
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: var(--bg-primary);
}

.layout-content {
  flex: 1;
  min-width: 0;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  padding: clamp(16px, 3vw, 32px);
}

.page-container {
  width: 100%;
  margin: 0 auto;
}

/* Sidebar - Responsive */
.sidebar {
  width: var(--sidebar-width);
  min-width: var(--sidebar-width);
  background: var(--bg-secondary);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  padding: clamp(12px, 2vw, 20px) clamp(8px, 1.5vw, 14px);
  overflow-y: auto;
  height: 100%;
  max-height: 100vh;
}

/* Logo and Text - Responsive */
.sidebar-logo {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(8px, 1.5vw, 16px) clamp(8px, 2vw, 14px) clamp(16px, 3vw, 28px);
  border-bottom: 1px solid var(--border);
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

```
