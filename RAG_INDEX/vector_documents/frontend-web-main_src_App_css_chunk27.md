# Knowledge Document: App.css (Chunk 28/43)

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
  "chunk_index": 27,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
kground: rgba(122, 79, 43, 0.1);
  border: 1px solid rgba(122, 79, 43, 0.2);
}

.icon-container.glow {
  box-shadow: var(--shadow-glow);
}

/* Hover Lift */
.hover-lift {
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.25s ease;
}

.hover-lift:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
  border-color: var(--border-focus);
}

/* Active Glow Text */
.text-glow-active {
  text-shadow: 0 0 10px rgba(212, 165, 116, 0.5);
  color: var(--accent-primary);
}

body.theme-light .text-glow-active {
  text-shadow: 0 0 10px rgba(122, 79, 43, 0.3);
}

/* Neon Text */
.text-neon {
  color: var(--accent-primary);
  text-shadow: 0 0 8px rgba(212, 165, 116, 0.4);
}

/* ============================================
   ORCA Unified App Shell
   Applies the homepage/marketplace visual language to all dashboard pages.
   ============================================ */
.layout {
  background: var(--shell-bg);
}

.layout-main {
  background: transparent;
}

.layout-content {
  padding: clamp(20px, 3vw, 36px);
  background: var(--shell-content-bg);
}

.sidebar {
  background: var(--shell-sidebar-bg);
  border-right: 1px solid var(--shell-border);
  box-shadow: 14px 0 42px rgba(0, 0, 0, 0.18);
}

.sidebar-logo {
  padding-bottom: 26px;
  border-bottom: 1px solid var(--shell-border);
}

.logo-icon {
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: var(--shell-accent-soft);
  box-shadow: inset 0 0 0 1px var(--shell-border-strong);
}

.logo-text {
  color: var(--shell-accent);
  background: none;
  -webkit-text-fill-color: currentColor;
  letter-spacing: 0.14em;
}

.nav-label {
  color: var(--shell-accent);
  opacity: 0.9;
}

.nav-item-wrap {
  display: contents;
}

.nav-divider {
  width: calc(100% - 46px);
  height: 1px;
  margin: 12px auto;
  border-radius: 999px;
  background: var(--shell-border);
  opacity: 1;
}

.nav-item {
  position: relative;
  min-height: 48px;
  border-radius: 8px;
  color: var(--shell-text-soft);
  font-weight: 700;
  border: 1px solid transparent;
  background: transparent;
  box-shadow: none;
}

.nav-item:not(.active) {
  opacity: 0.76;
}

.nav-item:hover {
  background: var(--shell-surface-hover);
  color: var(--shell-title);
  opacity: 1;
  transform: translateX(2px);
}

.nav-item.active {
  background:

```
