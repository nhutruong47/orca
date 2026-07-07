# Knowledge Document: App.css (Chunk 12/43)

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
  "chunk_index": 11,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ransition);
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
  box-shadow: var(--shadow-sm);
}

.nav-item.active {
  background: linear-gradient(90deg, rgba(212, 165, 116, 0.18) 0%, rgba(212, 165, 116, 0.06) 100%);
  color: var(--accent-primary);
  font-weight: 700;
  border-color: rgba(212, 165, 116, 0.35);
  box-shadow: 0 2px 12px rgba(212, 165, 116, 0.22);
}

.nav-item.active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 28px;
  background: var(--accent-gradient);
  border-radius: 0 4px 4px 0;
  box-shadow: 0 2px 10px rgba(212, 165, 116, 0.5);
}

.nav-icon {
  font-size: 17px;
  width: 24px;
  text-align: center;
}

.admin-menu-logo {
  width: 22px;
  height: 18px;
  display: block;
  object-fit: contain;
}

/* Sidebar User */
.sidebar-user {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 14px;
  border-top: 1px solid rgba(48, 54, 61, 0.5);
  margin-top: 12px;
  border-radius: 10px;
  transition: var(--transition);
}

.sidebar-user:hover {
  background: var(--bg-input);
}

.sidebar-avatar {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: var(--accent-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 15px;
  flex-shrink: 0;
  box-shadow: 0 2px 10px rgba(212, 165, 116, 0.3);
}

.sidebar-avatar-logo {
  width: 34px;
  height: 30px;
  display: block;
  object-fit: contain;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.28));
}

.sidebar-user-info {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  gap: 4px;
}

.sidebar-avatar-initials {
  background: var(--shell-avatar-bg);
  color: var(--shell-avatar-text);
  font-size: 12px;
  font-weight: 750;
  letter-spacing: 0;
  border: 2px solid var(--shell-border-strong);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  flex-shrink: 0;
}

.sidebar-username {
  font-size: 14px;
  font-weight: 700;
  color: var(--shell-title);
  white-space: nowrap;
  overflow: hidden;

```
