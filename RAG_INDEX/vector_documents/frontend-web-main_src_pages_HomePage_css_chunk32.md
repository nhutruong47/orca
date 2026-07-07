# Knowledge Document: HomePage.css (Chunk 33/34)

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
  "chunk_index": 32,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
g {
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
    url('/coffee-hero.png') center / cover no-repeat;
  overflow: hidden;
  scroll-margin-top: 80px;
}

.coffee-contact-footer__veil {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 78% 18%, rgba(164, 109, 63, 0.18), transparent 28%),
    rgba(0, 0, 0, 0.32);
  backdrop-filter: blur(3px);
  pointer-events: none;
}

.coffee-contact-footer__inner {
  position: relative;
  z-index: 1;
  width: min(1280px, 100%);
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.orca-footer-content {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr 1.1fr;
  gap: 50px;
  align-items: start;
}

.orca-footer-info {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.orca-footer-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.orca-footer-logo {
  height: 48px;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 2px 8px rgba(180, 120, 40, 0.4));
}

.orca-footer-name {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: 2px;
  background: linear-gradient(135deg, #d7b184 0%, #b48551 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.orca-footer-tagline {
  font-size: 18px;
  color: rgba(255, 250, 240, 0.85);
  margin: 0 0 16px;
  font-weight: 500;
}

.orca-footer-details {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.orca-footer-details li {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  font-size: 16px;
  color: rgba(255, 250, 240, 0.9);
  line-height: 1.5;
}

.footer-icon {
  color: #d7b184;
  flex-shrink: 0;
  margin-top: 2px;
}

.orca-footer-details strong {
  display: block;
  font-weight: 700;
  color: #fff;
  margin-bottom: 4px;
}

.orca-footer-details p {
  margin: 0;
  color: rgba(255, 250, 240, 0.7);
}

.orca-footer-links {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.footer-heading {
  font-size: 22px;
  font-weight: 700;
  color: #ffffff !important;

```
