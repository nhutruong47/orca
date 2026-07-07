# Knowledge Document: HomePage.css (Chunk 31/34)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/HomePage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 30,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
px 16px rgba(0, 0, 0, 0.45));
}

.coffee-reserve__logo {
  width: 74px;
  height: 46px;
  display: block;
  object-fit: contain;
  margin: 0 auto 14px;
  filter: drop-shadow(0 12px 24px rgba(0, 0, 0, 0.42));
}

.coffee-office-logo {
  width: 25px;
  height: 18px;
  display: block;
  object-fit: contain;
}

.coffee-nav__brand strong {
  display: block;
  font-size: clamp(1.08rem, 1.55vw, 1.48rem);
  font-weight: 950;
  letter-spacing: 0.01em;
}

.coffee-nav__links {
  justify-self: center;
  align-self: stretch;
  display: flex;
  align-items: stretch;
  justify-content: center;
  gap: 0;
  min-width: 0;
  overflow-x: auto;
  scrollbar-width: none;
}

.coffee-nav__links::-webkit-scrollbar {
  display: none;
}

.coffee-nav__links .coffee-nav__item {
  min-width: clamp(112px, 8.2vw, 148px);
  padding: 0 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0;
  color: rgba(255, 255, 255, 0.66);
  background: transparent;
  border-radius: 0;
  cursor: pointer;
  text-shadow: 0 5px 18px rgba(0, 0, 0, 0.7);
  transition: color 180ms ease, background 180ms ease;
}

.coffee-nav__links .coffee-nav__item:hover {
  color: #fff7ea;
  background: rgba(115, 72, 42, 0.32);
  transform: none;
}

.coffee-nav__links .coffee-nav__item--active {
  color: #fff8ed;
  background: linear-gradient(180deg, rgba(128, 77, 43, 0.88), rgba(160, 94, 47, 0.88));
}

.coffee-nav__item span {
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(1.08rem, 1.45vw, 1.32rem);
  font-weight: 800;
  letter-spacing: 0;
  text-transform: none;
  white-space: nowrap;
}

.coffee-nav__auth {
  justify-self: end;
  align-self: center;
  display: flex;
  align-items: center;
  gap: 12px;
}

.coffee-nav__auth button {
  min-height: 44px;
  padding: 0 18px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #fff7ea;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 6px;
  font-size: 0.98rem;
  font-weight: 800;
  white-space: nowrap;
  cursor: pointer;
  transition: color 180ms ease, background 180ms ease, border-color 180ms ease, transform 180ms ease;
}

.coffee-nav__auth button:hover {
  color: #fff;
  background: rgba(164, 109, 63, 0.28);
  border-color: rgba(255, 255, 255, 0.24);
  transform: translateY(-1px);
}

.coffee-nav__auth button:last-child {

```
