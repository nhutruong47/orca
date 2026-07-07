# Knowledge Document: App.css (Chunk 40/43)

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
  "chunk_index": 39,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ht: 16px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--bg-card);
}

.notification-dropdown {
  position: absolute;
  top: 48px;
  right: -10px;
  width: 320px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  z-index: 100;
  overflow: hidden;
  animation: dropDownEnter 0.2s ease-out;
}

@keyframes dropDownEnter {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.notification-header {
  padding: 14px 16px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-secondary);
}

.notification-header h3 {
  margin: 0;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
}

.notification-list {
  max-height: 350px;
  overflow-y: auto;
}

.notification-item {
  padding: 14px 16px;
  border-bottom: 1px solid var(--border);
  transition: var(--transition);
  cursor: pointer;
}

.notification-item:hover {
  background: var(--bg-input);
}

.notification-item.unread {
  background: rgba(212, 165, 116, 0.05);
  border-left: 3px solid var(--accent-primary);
}

.notification-content h4 {
  margin: 0 0 4px 0;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
}

.notification-content p {
  margin: 0 0 8px 0;
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.4;
}

.notification-time {
  font-size: 11px;
  color: var(--text-muted);
}

/* FIX: Ensure topbar is always above page content so notification dropdown is clickable and not covered */
.topbar {
  position: relative !important;
  z-index: 9999 !important;
}

/* ============================================
   FACEBOOK STYLE NOTIFICATIONS (Dark Mode adapted)
   ============================================ */
.fb-notification-dropdown {
  position: absolute;
  top: 48px;
  right: -10px;
  width: 360px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4);
  z-index: 10000;
  display: flex;
  flex-direction: column;
  animation: dropDownEnter 0.2s ease-out;
  color: var(--text-primary);
  font-family: inherit;
}

.fb-notification-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 16px 8px;
}

.fb-notification-header h3 {

```
