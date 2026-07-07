# Knowledge Document: App.css (Chunk 29/43)

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
  "chunk_index": 28,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
lative;
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
    linear-gradient(90deg, rgba(212, 165, 116, 0.24), rgba(212, 165, 116, 0.08)),
    var(--shell-surface-hover);
  border-color: var(--shell-border-strong);
  color: var(--shell-title);
  box-shadow:
    inset 4px 0 0 var(--shell-accent),
    0 12px 26px rgba(0, 0, 0, 0.16);
  opacity: 1;
  text-shadow: none;
  transform: translateX(3px);
}

.nav-item.active::before {
  content: '';
  position: absolute;
  right: 12px;
  top: 50%;
  display: block;
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: var(--shell-accent-line);
  box-shadow: 0 0 14px rgba(245, 158, 11, 0.65);
  transform: translateY(-50%);
}

.nav-icon {
  color: inherit;
}

.sidebar-user {
  width: 100%;
  border-top: 1px solid var(--shell-border);
  background: var(--shell-surface-soft);
  border-radius: 10px;
}

.sidebar-user-wrap {
  position: relative;
  margin-top: auto;
}

.sidebar-user-wrap .sidebar-user {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 64px;
  padding: 10px 14px;
  margin-top: 0;
  border: 1px solid var(--shell-border);
  background: var(--shell-surface-soft);
  color: var(--shell-text);
  cursor: pointer;
  text-align: left;
  box-shadow: none;
  transition: background 0.18s ease, border-color 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease;
}

.sidebar-user-wrap .sidebar-user:hover,
.sidebar-user-wrap .sidebar-user.active {
  background: var(--shell-surface-hover);
  border-color: var(--shell-border-strong);
  box-shadow: none;
}

.sidebar-user-wrap .sidebar-user-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sidebar-user-menu {
  position: absolute;
  left: 0;
  right: auto;
  bottom: calc(100% + 10px);
  z-index: 20;
  display: grid;
  gap: 6px;
  width: min(312px, calc(100vw - 24px));
  padding: 18px 20px 14px;
  background: var(--shell-surface);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid var(--shell-border);
  border-radius: 8px;

```
