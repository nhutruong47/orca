# Knowledge Document: Marketplace.css (Chunk 40/44)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/Marketplace.css",
  "language": "css",
  "module": "pages",
  "business_domain": "factory",
  "tags": [
    "factory",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 39,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
ustify-content: center;
}

.fb-chat-close:hover {
  background: var(--bg-input);
}

.fb-chat-body {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: var(--bg-primary);
}

.fb-msg-row {
  display: flex;
  flex-direction: column;
}

.fb-msg-row.received {
  align-items: flex-start;
}

.fb-msg-row.sent {
  align-items: flex-end;
}

.fb-msg-bubble {
  max-width: 75%;
  padding: 8px 12px;
  border-radius: 18px;
  font-size: 14px;
  line-height: 1.4;
  word-wrap: break-word;
}

.fb-msg-row.received .fb-msg-bubble {
  background: var(--bg-input);
  color: var(--text-primary);
}

.fb-msg-row.sent .fb-msg-bubble {
  background: #d4a574;
  color: #1a1a1a;
}

.fb-chat-footer {
  padding: 12px;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--bg-card);
}

.fb-chat-input {
  flex: 1;
  background: var(--bg-input);
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  color: var(--text-primary);
  outline: none;
  font-size: 14px;
}

.fb-chat-input::placeholder {
  color: var(--text-muted);
}

.fb-chat-send {
  background: transparent;
  border: none;
  color: #d4a574;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

.fb-chat-send:disabled {
  color: var(--text-muted);
  cursor: not-allowed;
}

.fb-chat-send:not(:disabled):hover {
  color: #b58550;
}

.fb-chat-action-btn {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 4px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fb-chat-action-btn:hover {
  background: var(--bg-input);
  color: #d4a574;
}

/* GSAP Motion & Linear UI additions */
.mp-spotlight-search {
    background: rgba(255,255,255,0.03);
    border: 1px solid var(--mp-outline);
    border-radius: 12px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.2);
    backdrop-filter: blur(16px);
    transition: all 0.3s ease;
}

.mp-spotlight-search:focus-within {
    border-color: var(--mp-primary);
    box-shadow: 0 4px 32px rgba(245, 158, 11, 0.15);
}

.mp-market-card {
    background: var(--mp-surface);
    border: 1px solid var(--mp-outline);
    border-radius: 16px;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    overflow: hidden;

```
