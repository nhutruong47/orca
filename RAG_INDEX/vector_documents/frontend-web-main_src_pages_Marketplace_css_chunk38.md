# Knowledge Document: Marketplace.css (Chunk 39/44)

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
  "chunk_index": 38,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
}

.mp-cpc-image:hover img {
    transform: scale(1.04);
}

.mp-cpc-info h3 {
    margin: 0 0 8px;
    color: #fff;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.05em;
    font-family: 'Montserrat', sans-serif;
}

.mp-cpc-info p {
    margin: 0 0 14px;
    color: #a79d94;
    font-style: italic;
    font-size: 13px;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.mp-cpc-info strong {
    font-family: 'Montserrat', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: #ffd9bd;
}

@media (max-width: 1180px) {
    .mp-clean-product-card {
        flex: 0 0 240px;
    }
}


/* ============================================
   FACEBOOK MESSENGER POPUP
   ============================================ */
.fb-chat-popup {
  position: fixed;
  bottom: 0;
  right: 80px;
  width: 340px;
  height: 450px;
  background: var(--bg-card);
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
  z-index: 9999;
  border: 1px solid var(--border);
  border-bottom: none;
}

.fb-chat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
  background: rgba(255, 255, 255, 0.03);
}

.fb-chat-header-info {
  display: flex;
  align-items: center;
  gap: 8px;
}

.fb-chat-header-info img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.fb-chat-header-text h4 {
  margin: 0;
  font-size: 14px;
  color: var(--text-primary);
}

.fb-chat-header-text span {
  font-size: 11px;
  color: #10b981;
}

.fb-chat-close {
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


```
