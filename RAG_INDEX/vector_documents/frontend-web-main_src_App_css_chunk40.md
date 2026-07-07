# Knowledge Document: App.css (Chunk 41/43)

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
  "chunk_index": 40,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
r(--border);
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
  margin: 0;
  font-size: 20px;
  font-weight: 700;
}

.fb-notification-options {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  cursor: pointer;
  border-radius: 50%;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.fb-notification-options:hover {
  background: var(--bg-input);
  color: var(--text-primary);
}

.fb-notification-tabs {
  display: flex;
  gap: 8px;
  padding: 0 16px 8px;
}

.fb-notification-tabs button {
  background: transparent;
  border: none;
  padding: 8px 12px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  cursor: pointer;
  transition: var(--transition);
}

.fb-notification-tabs button:hover {
  background: var(--bg-input);
}

.fb-notification-tabs button.active {
  background: rgba(45, 136, 255, 0.15);
  color: #3b82f6;
}

.fb-notification-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
}

.fb-notification-section span {
  font-size: 15px;
  font-weight: 600;
}

.fb-notification-section button {
  background: transparent;
  border: none;
  color: #3b82f6;
  font-size: 14px;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
}

.fb-notification-section button:hover {
  background: rgba(45, 136, 255, 0.1);
}

.fb-notification-list {
  max-height: 400px;
  overflow-y: auto;
  padding: 0 8px;
}

.fb-notification-item {
  display: flex;
  align-items: center;
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
  transition: var(--transition);
  position: relative;
  gap: 12px;
  margin-bottom: 2px;
}

.fb-notification-item:hover {
  background: var(--bg-input);
}

.fb-notification-item.unread {
  background: rgba(45, 136, 255, 0.05);
}

.fb-notif-avatar-wrapper {
  position: relative;
  flex-shrink: 0;
}

.fb-notif-avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  object-fit: cover;
}

.fb-notif-badge {

```
