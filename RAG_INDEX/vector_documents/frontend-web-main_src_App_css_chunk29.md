# Knowledge Document: App.css (Chunk 30/43)

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
  "chunk_index": 29,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
lumn;
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
  box-shadow: 0 18px 44px rgba(0, 0, 0, 0.22);
  color: var(--shell-text);
}

.sidebar-user-menu-item {
  min-height: 42px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 6px;
  color: var(--shell-text-soft);
  border: 0;
  border-radius: 8px;
  background: transparent;
  font-size: 15px;
  font-weight: 520;
  text-decoration: none;
  transition: background 0.18s ease, color 0.18s ease;
}

.sidebar-user-menu-item:hover,
.sidebar-user-menu-item.active {
  color: var(--shell-title);
  background: var(--shell-surface-hover);
}

.sidebar-user-menu-head {
  min-height: 50px;
  display: flex;
  align-items: center;
  gap: 10px;
  padding-bottom: 14px;
  margin-bottom: 6px;
  border-bottom: 1px solid var(--shell-border);
}

.sidebar-user-menu-head .sidebar-user-info,
.sidebar-user .sidebar-user-info {
  min-width: 0;
}

.sidebar-user-plan {
  display: inline-block;
  margin-top: 4px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  line-height: 1.2;
}

.sidebar-user-menu .nav-icon {
  width: 22px;
  min-width: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--shell-text-soft);
}

.sidebar-user-menu-item.separated {
  margin-top: 10px;
  padding-top: 12px;
  border-top: 1px solid var(--shell-border);
  border-radius: 0;
}

.sidebar-menu-chevron,
.sidebar-menu-head-chevron {
  margin-left: auto;
  color: var(--shell-text-soft);
  font-size: 18px;
}

.sidebar-user-menu-button {
  width: 100%;
  font-family: inherit;
  cursor: pointer;
  text-align: left;
}

.sidebar-avatar-initials {
  background: var(--shell-avatar-bg);
  color: var(--shell-avatar-text);
  font-size: 12px;
  font-weight: 750;
  letter-spacing: 0;
}

.sidebar-avatar,
.topbar-avatar,
.profile-avatar-large {
  background: var(--shell-avatar-bg);
  color: var(--shell-avatar-text);
}

.sidebar-user-wrap .sidebar-avatar.sidebar-avatar-initials {
  background: var(--shell-avatar-bg);

```
