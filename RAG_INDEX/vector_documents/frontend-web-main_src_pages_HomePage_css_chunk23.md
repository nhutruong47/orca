# Knowledge Document: HomePage.css (Chunk 24/34)

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
  "chunk_index": 23,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
er: none;
  transform: translateY(0);
  opacity: 1;
  transition:
    transform 260ms ease,
    opacity 220ms ease,
    background-color 220ms ease,
    border-color 220ms ease,
    box-shadow 220ms ease,
    padding 220ms ease,
    border-radius 220ms ease;
}

.coffee-nav__brand {
  color: #ffffff;
  font-size: clamp(1.02rem, 1.4vw, 1.2rem);
  text-shadow:
    0 0 14px rgba(255, 209, 102, 0.44),
    0 2px 12px rgba(0, 0, 0, 0.6);
}

.coffee-nav__links {
  gap: clamp(12px, 2.3vw, 26px);
}

.coffee-nav__links button {
  min-height: 32px;
  padding: 0 4px;
  color: #fff7d8;
  background: transparent;
  border: 0;
  border-radius: 0;
  font-size: clamp(0.78rem, 0.98vw, 0.96rem);
  font-weight: 900;
  letter-spacing: 0.12em;
  text-shadow:
    0 0 12px rgba(255, 209, 102, 0.34),
    0 2px 10px rgba(0, 0, 0, 0.74);
  transition: color 220ms ease, background 220ms ease, border-color 220ms ease, transform 220ms ease;
}

.coffee-nav__links button:hover {
  color: #fffaf0;
  background: transparent;
  box-shadow: none;
  text-shadow:
    0 0 14px rgba(255, 209, 102, 0.42),
    0 2px 10px rgba(0, 0, 0, 0.74);
  transform: translateY(-1px);
}

.coffee-nav.coffee-nav--scrolled {
  min-height: 48px;
  padding: 0;
  color: var(--readable-brown);
  background: transparent;
  border: 0;
  border-radius: 0;
  box-shadow: none;
  backdrop-filter: none;
}

.coffee-nav.coffee-nav--scrolled .coffee-nav__brand {
  color: var(--readable-brown);
  text-shadow: none;
}

.coffee-nav.coffee-nav--scrolled .coffee-nav__links button {
  color: #2c1b11;
  background: transparent;
  border: 0;
  text-shadow: none;
}

.coffee-nav.coffee-nav--scrolled .coffee-nav__links button:hover {
  color: #6f4b22;
  background: transparent;
  box-shadow: none;
  text-shadow: none;
}

.coffee-nav.coffee-nav--hidden {
  opacity: 0;
  pointer-events: none;
  transform: translateY(calc(-100% - 32px));
}

.coffee-hero__veil {
  background:
    linear-gradient(90deg, rgba(4, 13, 12, 0.84) 0%, rgba(24, 14, 8, 0.62) 48%, rgba(8, 20, 18, 0.38) 100%),
    linear-gradient(180deg, rgba(4, 13, 12, 0.24) 0%, rgba(11, 8, 5, 0.5) 72%, #f6ead8 100%);
}

.coffee-hero h1,
.coffee-hero__content h1 {
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
  text-shadow:
    0 14px 44px rgba(0, 0, 0, 0.72),
    0 0 30px rgba(255, 255, 255, 0.24),
    0 0 84px rgba(255, 209, 102, 0.24) !important;
}


```
