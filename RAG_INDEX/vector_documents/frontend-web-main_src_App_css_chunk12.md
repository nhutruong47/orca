# Knowledge Document: App.css (Chunk 13/43)

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
  "chunk_index": 12,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ebar-avatar-initials {
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
  text-overflow: ellipsis;
  letter-spacing: 0.2px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.role-badge {
  font-size: 11px;
  font-weight: 500;
  padding: 2px 0;
}

.role-badge.manager {
  color: var(--warning);
}

.role-badge.member {
  color: var(--accent-primary);
}

.role-badge.large {
  font-size: 14px;
  padding: 6px 16px;
  border-radius: 20px;
  display: inline-block;
}

.role-badge.large.manager {
  background: rgba(210, 153, 34, 0.15);
  border: 1px solid rgba(210, 153, 34, 0.3);
}

.role-badge.large.member {
  background: rgba(212, 156, 87, 0.12);
  color: var(--accent-primary);
  box-shadow: 0 1px 4px rgba(212, 156, 87, 0.1);
}
/* Topbar - Responsive */
.topbar {
  height: var(--topbar-height);
  min-height: var(--topbar-height);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 clamp(12px, 2vw, 32px);
  background: var(--bg-card);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
  gap: clamp(8px, 2vw, 16px);
}

.topbar-greeting {
  font-size: clamp(12px, 2vw, 14px);
  font-weight: 400;
  color: var(--text-secondary);
}

.topbar-username {
  color: var(--text-primary);
  font-weight: 600;
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.topbar-avatar {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: var(--accent-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  transition: var(--transition);
}

.topbar-avatar ion-icon {
  font-size: 22px;
}

.topbar-avatar:hover {
  transform: scale(1.05);
  box-shadow: 0 0 12px rgba(88, 166, 255, 0.3);
}

.topbar-logout {
  padding: 7px 14px;
  border: 1px solid var(--danger);
  border-radius: 8px;
  background: transparent;
  color: var(--danger);
  font-size: 12px;
  font-weight: 600;
  font-family: var(--font);
  cursor: pointer;
  transition: var(--transition);
}

```
