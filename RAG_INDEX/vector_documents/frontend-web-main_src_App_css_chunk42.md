# Knowledge Document: App.css (Chunk 43/43)

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
  "chunk_index": 42,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
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

.msg-group-name.unread-text {
  font-weight: 700;
}

.msg-preview {
  display: flex;
  align-items: center;
  margin-top: 4px;
  max-width: 100%;
}

.msg-preview-text {
  font-size: 13px;
  color: var(--text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 180px;
}

.msg-preview-text.unread-text {
  color: var(--text-primary);
  font-weight: 600;
}

.msg-preview-time {
  font-size: 13px;
  color: var(--text-muted);
  white-space: nowrap;
}

.msg-unread-badge-icon {
  background-color: #f85149;
  color: white;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: auto;
  align-self: center;
}

```
