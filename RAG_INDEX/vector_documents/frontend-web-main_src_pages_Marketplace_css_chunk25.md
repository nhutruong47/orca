# Knowledge Document: Marketplace.css (Chunk 26/44)

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
  "chunk_index": 25,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
g: 16px;
    background: var(--mp-surface-high);
}

.mp-verification-list {
    display: grid;
    gap: 8px;
}

.mp-verification-list span {
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--mp-muted);
    font-weight: 700;
}

.mp-verification-list .verified {
    color: var(--mp-success);
}

.mp-review-list {
    display: grid;
    gap: 12px;
}

.mp-review-list article {
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 14px;
    background: var(--mp-surface-high);
}

/* === Dark Roastery Marketplace === */
.mp-body.mp-manufacturing-market {
    --mp-bg: #111415;
    --mp-surface: #202325;
    --mp-surface-low: #171a1b;
    --mp-surface-high: #282b2d;
    --mp-outline: rgba(255, 255, 255, 0.08);
    --mp-outline-strong: rgba(255, 216, 188, 0.2);
    --mp-text: #f4eee8;
    --mp-heading: #fff7ef;
    --mp-muted: #a79d94;
    --mp-primary: #ffd9bd;
    --mp-primary-strong: #ffb579;
    --mp-success: #64d98a;
    background: var(--mp-bg);
    color: var(--mp-text);
}

.mp-manufacturing-market .sidebar {
    background: #191c1d;
    border-right-color: rgba(255, 255, 255, 0.07);
    box-shadow: none;
}

.mp-manufacturing-market .sidebar-logo {
    border-bottom-color: rgba(255, 255, 255, 0.07);
}

.mp-manufacturing-market .nav-label {
    color: #b8a08c;
}

.mp-manufacturing-market .nav-item {
    color: #b9aea5;
}

.mp-manufacturing-market .nav-item:hover,
.mp-manufacturing-market .nav-item.active {
    color: #ffe2c8;
    background: rgba(255, 181, 121, 0.12);
    border-color: rgba(255, 181, 121, 0.56);
}

.mp-manufacturing-market .mp-topbar {
    height: 58px;
    background: rgba(17, 20, 21, 0.94);
    border-bottom-color: rgba(255, 255, 255, 0.07);
}

.mp-manufacturing-market .mp-top-search {
    width: min(430px, 100%);
}

.mp-manufacturing-market .mp-top-search input {
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 8px;
    background: #26292b;
    color: #e8ded6;
}

.mp-manufacturing-market .mp-top-search input::placeholder {
    color: #8b837d;
}

.mp-manufacturing-market .mp-top-actions button {
    color: #d6bba5;
}

.mp-manufacturing-market .mp-user-avatar {
    border-color: rgba(255, 181, 121, 0.28);
    background: #24211f;
    color: #ffd8b7;
}

.mp-manufacturing-market .mp-main {
    --mp-page-max: min(1600px, calc(100vw - var(--sidebar-width) - 96px));

```
