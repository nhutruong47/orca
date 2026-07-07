# Knowledge Document: COMPONENT_STANDARDIZATION.md (Chunk 3/4)

## Metadata
```json
{
  "file_path": "COMPONENT_STANDARDIZATION.md",
  "language": "md",
  "module": "orca",
  "business_domain": "production",
  "tags": [
    "production",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: production, chat

## Source Code Chunk
```md
  </h1>
    <p className="page-subtitle">Page description text</p>
  </div>
  <div className="page-header-actions">
    <button className="btn btn-primary">Action</button>
  </div>
</div>
```

---

## 6. Feedback

### 6.1 Empty State

```tsx
<div className="empty-state">
  <ion-icon name="folder-open"></ion-icon>
  <h3 className="empty-state-title">No data</h3>
  <p>Description of empty state</p>
  <button className="btn btn-primary">Create</button>
</div>
```

### 6.2 Loading Spinner

```tsx
<div className="loading-screen">
  <div className="loading-spinner"></div>
  <p>Loading...</p>
</div>
```

### 6.3 Modal

```tsx
<div className="modal-overlay" onClick={onClose}>
  <div className="modal" onClick={e => e.stopPropagation()}>
    <div className="modal-header">
      <h2>Modal Title</h2>
      <button className="modal-close-btn" onClick={onClose}>
        <ion-icon name="close"></ion-icon>
      </button>
    </div>
    <div className="modal-body">
      Modal content
    </div>
    <div className="modal-footer">
      <button className="btn btn-secondary">Cancel</button>
      <button className="btn btn-primary">Confirm</button>
    </div>
  </div>
</div>
```

---

## 7. Chat Components

### 7.1 Message Bubble

```tsx
// Outgoing message
<div className="chat-message own">
  <div className="chat-bubble">
    Message text
  </div>
</div>

// Incoming message
<div className="chat-message incoming">
  <div className="chat-bubble">
    Message text
  </div>
</div>
```

### 7.2 Chat Input

```tsx
<div className="chat-input-floating">
  <input className="chat-input" placeholder="Type a message..." />
  <button className="chat-send-btn">
    <ion-icon name="send"></ion-icon>
  </button>
</div>
```

---

## 8. Utility Classes

### 8.1 Text Colors

```html
<span class="text-primary">Primary</span>
<span class="text-secondary">Secondary</span>
<span class="text-muted">Muted</span>
<span class="text-success">Success</span>
<span class="text-warning">Warning</span>
<span class="text-danger">Danger</span>
<span class="text-link">Link</span>
```

### 8.2 Animation Helpers

```html
<div class="fade-in">Fade In</div>
<div class="scale-in">Scale In</div>
<div class="rise-in">Rise In</div>
```

---

## 9. Icon Usage

### 9.1 Icon Sizes

- Small: 16px (inside small buttons, badges)
- Default: 18-20px (navigation, lists)
- Medium: 22-24px (cards, headers)

```
