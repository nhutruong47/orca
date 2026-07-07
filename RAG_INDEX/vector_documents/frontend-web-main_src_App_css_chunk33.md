# Knowledge Document: App.css (Chunk 34/43)

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
  "chunk_index": 33,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
t [style*="color: rgb(26, 26, 26)"],
body.theme-dark .layout [style*="color: #1e293b"],
body.theme-dark .layout [style*="color:#1e293b"],
body.theme-dark .layout [style*="color: #111"],
body.theme-dark .layout [style*="color:#111"] {
  color: var(--shell-text) !important;
}

body.theme-dark .layout [style*="color: rgb(100, 116, 139)"],
body.theme-dark .layout [style*="color: rgb(107, 114, 128)"],
body.theme-dark .layout [style*="color: rgb(148, 163, 184)"],
body.theme-dark .layout [style*="color: #64748b"],
body.theme-dark .layout [style*="color:#64748b"],
body.theme-dark .layout [style*="color: #6b7280"],
body.theme-dark .layout [style*="color:#6b7280"],
body.theme-dark .layout [style*="color: #94a3b8"],
body.theme-dark .layout [style*="color:#94a3b8"] {
  color: var(--shell-text-soft) !important;
}

body.theme-dark .layout [style*="border: 1px solid rgb(226, 232, 240)"],
body.theme-dark .layout [style*="border-top: 1px solid rgb(226, 232, 240)"],
body.theme-dark .layout [style*="border-bottom: 1px solid rgb(226, 232, 240)"],
body.theme-dark .layout [style*="border: 1px solid #e2e8f0"],
body.theme-dark .layout [style*="border-top: 1px solid #e2e8f0"],
body.theme-dark .layout [style*="border-bottom: 1px solid #e2e8f0"] {
  border-color: var(--shell-border) !important;
}

/* Login page refinement */
.login-split {
  display: grid;
  grid-template-columns: minmax(0, 56%) minmax(600px, 44%);
  min-height: 100vh;
  background:
    linear-gradient(90deg, rgba(7, 10, 18, 0.76) 0%, rgba(7, 10, 18, 0.58) 48%, rgba(7, 10, 18, 0.7) 100%),
    url('https://images.pexels.com/photos/15851582/pexels-photo-15851582.jpeg?auto=compress&cs=tinysrgb&w=2400&q=85') center / cover no-repeat;
}

.login-hero {
  min-height: 100vh;
  align-items: center;
  padding: clamp(36px, 5vw, 72px);
}

.login-hero-img {
  display: none;
}

.login-hero-overlay {
  background:
    linear-gradient(90deg, rgba(7, 10, 18, 0.92) 0%, rgba(7, 10, 18, 0.62) 48%, rgba(7, 10, 18, 0.34) 100%),
    linear-gradient(180deg, rgba(7, 10, 18, 0.08) 0%, rgba(7, 10, 18, 0.72) 100%);
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


```
