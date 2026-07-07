# Knowledge Document: HomePage.css (Chunk 30/34)

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
  "chunk_index": 29,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
gallery__track {
    top: 12%;
    gap: 14px;
    padding-inline: 18px;
  }

  .coffee-interface-card {
    width: 82vw;
  }

  .coffee-interface-card__caption strong {
    font-size: clamp(1.35rem, 8vw, 2.2rem);
  }

  .coffee-stat-card,
  .coffee-role-card,
  .coffee-ai-card,
  .coffee-pricing-card {
    min-height: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  html.luxury-home-page,
  body.luxury-home-page,
  body.luxury-home-page #root {
    scroll-behavior: auto;
  }

  *,
  *::before,
  *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }

  .coffee-hero__image,
  .coffee-hero__content {
    transform: none !important;
  }
}

/* XTRA coffee inspired top navigation */
.coffee-nav {
  position: fixed;
  inset: 0 0 auto;
  z-index: 60;
  display: block;
  min-height: 0;
  padding: 0;
  color: #fffaf0;
  background: transparent;
  border: 0;
  border-radius: 0;
  box-shadow: none;
  backdrop-filter: none;
  transform: translateY(0);
}

.coffee-nav button,
.coffee-nav a {
  font: inherit;
  color: inherit;
  border: 0;
  text-decoration: none;
}

.coffee-nav__inner {
  min-height: 92px;
  display: grid;
  grid-template-columns: minmax(176px, 20vw) minmax(0, 1fr) auto;
  align-items: stretch;
  padding: 0 clamp(20px, 6vw, 128px);
  background: rgba(10, 7, 5, 0.26);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-top: 0;
  backdrop-filter: blur(10px);
}

.coffee-nav__brand {
  justify-self: start;
  align-self: center;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
  color: #fff;
  background: transparent;
  cursor: pointer;
  text-shadow: 0 6px 22px rgba(0, 0, 0, 0.45);
}

.coffee-nav__brand svg {
  flex: 0 0 auto;
  color: #a46d3f;
  fill: rgba(164, 109, 63, 0.26);
}

.coffee-nav__brand img {
  width: 82px;
  height: 52px;
  flex: 0 0 auto;
  display: block;
  object-fit: contain;
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.45));
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

```
