# Knowledge Document: HomePage.css (Chunk 32/34)

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
  "chunk_index": 31,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
s: 6px;
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
  color: #24140d;
  background: #fff7ea;
  border-color: #fff7ea;
}

.coffee-nav.coffee-nav--scrolled,
.coffee-nav.coffee-nav--hidden {
  padding: 0;
  background: transparent;
  border: 0;
  box-shadow: none;
  backdrop-filter: none;
}

.coffee-nav.coffee-nav--scrolled .coffee-nav__brand,
.coffee-nav.coffee-nav--scrolled .coffee-nav__links button {
  color: inherit;
  text-shadow: 0 5px 18px rgba(0, 0, 0, 0.7);
}

.coffee-nav.coffee-nav--hidden {
  opacity: 0;
  pointer-events: none;
  transform: translateY(-100%);
}

@media (max-width: 1180px) {
  .coffee-nav__inner {
    grid-template-columns: auto minmax(0, 1fr);
    min-height: 86px;
    padding-inline: 20px;
  }

  .coffee-nav__auth {
    justify-self: end;
  }

  .coffee-nav__links {
    justify-content: flex-start;
  }
}

@media (max-width: 860px) {
  .coffee-nav__inner {
    grid-template-columns: 1fr auto;
    gap: 0;
    min-height: 118px;
    padding: 10px 14px 0;
  }

  .coffee-nav__brand {
    justify-self: start;
    min-height: 46px;
  }

  .coffee-nav__links {
    justify-self: stretch;
    justify-content: flex-start;
    grid-column: 1 / -1;
  }

  .coffee-nav__links .coffee-nav__item {
    min-width: 112px;
    min-height: 66px;
    padding-inline: 12px;
    gap: 0;
  }

  .coffee-hero {
    padding-top: 160px;
  }
}

@media (max-width: 520px) {
  .coffee-nav__auth {
    gap: 8px;
  }

  .coffee-nav__auth button {
    min-height: 38px;
    padding-inline: 10px;
    font-size: 0.84rem;
  }

  .coffee-nav__brand svg {
    width: 30px;
    height: 30px;
  }

  .coffee-nav__brand img {
    width: 64px;
    height: 42px;
  }

  .coffee-nav__brand strong {
    font-size: 1rem;
  }

  .coffee-nav__links .coffee-nav__item {
    min-width: 104px;
  }
}

.coffee-contact-footer {
  position: relative;
  min-height: 500px;
  padding: clamp(70px, 8vw, 104px) clamp(20px, 7vw, 120px);
  color: #fff7ea;
  background:
    linear-gradient(90deg, rgba(5, 5, 5, 0.88), rgba(6, 4, 3, 0.72)),

```
