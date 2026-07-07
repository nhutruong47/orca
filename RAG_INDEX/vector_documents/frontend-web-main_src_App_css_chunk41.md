# Knowledge Document: App.css (Chunk 42/43)

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
  "chunk_index": 41,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ar(--transition);
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
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--bg-card);
}

.fb-notif-content {
  flex: 1;
  min-width: 0;
}

.fb-notif-content p {
  margin: 0;
  font-size: 14px;
  line-height: 1.4;
  color: var(--text-primary);
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.fb-notif-content strong {
  font-weight: 600;
}

.fb-notif-time {
  font-size: 13px;
  color: #3b82f6;
  margin-top: 4px;
  display: block;
}

.fb-notification-item.read .fb-notif-time {
  color: var(--text-muted);
}

.fb-notif-unread-dot {
  width: 10px;
  height: 10px;
  background-color: #3b82f6;
  border-radius: 50%;
  flex-shrink: 0;
  margin-left: 8px;
}

.fb-notification-footer {
  padding: 12px 16px;
  text-align: center;
  border-top: 1px solid var(--border);
}

.fb-notification-footer button {
  width: 100%;
  padding: 8px;
  background: var(--bg-input);
  border: none;
  border-radius: 6px;
  color: var(--text-primary);
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: var(--transition);
}

.fb-notification-footer button:hover {
  background: rgba(255, 255, 255, 0.15);
}

/* FIX: Ensure dropdown has a solid background so elements behind it don't show through */
.fb-notification-dropdown {
  background: var(--bg-primary) !important;
}

/* ============================================
   FACEBOOK MESSENGER STYLE
   ============================================ */
.topbar-messenger {
  position: relative;
  display: flex;
  align-items: center;
}

.online-indicator {
  position: absolute;
  bottom: 0px;
  right: 0px;
  width: 14px;
  height: 14px;
  background-color: #10b981;
  border-radius: 50%;
  border: 2px solid var(--bg-primary);
}

.msg-item {
  align-items: center;
}

.msg-group-name {
  margin: 0;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-primary);
}

```
