# Knowledge Document: HomePage.css (Chunk 1/34)

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
  "chunk_index": 0,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
html.luxury-home-page,
body.luxury-home-page,
body.luxury-home-page #root {
  height: auto;
  min-height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  scroll-behavior: smooth;
}

body.luxury-home-page {
  background: #17100b;
}

.coffee-home {
  --espresso: #17100b;
  --espresso-2: #2a1b12;
  --walnut: #4b2f20;
  --caramel: #b98756;
  --cream: #f7ead9;
  --linen: #fbf6ed;
  --sage: #7b8464;
  --ink: #201710;
  --muted: rgba(64, 43, 30, 0.68);
  --display-font: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
  min-height: 100vh;
  overflow: clip;
  background:
    linear-gradient(180deg, #17100b 0, #f6ead8 100svh, #fbf6ed 100%);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.coffee-nav {
  position: fixed;
  inset: 24px clamp(18px, 5vw, 72px) auto;
  z-index: 30;
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 28px;
  min-height: 32px;
  padding: 0;
  color: var(--cream);
  background: transparent;
  border: 0;
  border-radius: 0;
  backdrop-filter: none;
}

.coffee-nav button {
  font: inherit;
  color: inherit;
  border: 0;
  background: transparent;
  cursor: pointer;
}

.coffee-nav__brand {
  justify-self: start;
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: 0.32em;
}

.coffee-nav__links {
  justify-self: end;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: clamp(18px, 3vw, 34px);
}

.coffee-nav__links button {
  color: rgba(247, 234, 217, 0.78);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  transition: color 220ms ease;
}

.coffee-nav__links button:hover {
  color: #fff8ef;
}

.coffee-hero {
  position: relative;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: 140px clamp(20px, 7vw, 96px) 76px;
  isolation: isolate;
  color: var(--cream);
  text-align: center;
}

.coffee-hero__image,
.coffee-hero__veil,
.coffee-hero__steam {
  position: absolute;
  inset: 0;
}

.coffee-hero__image {
  z-index: -3;
  overflow: hidden;
  background: linear-gradient(135deg, #3a2417, #120b07);
  transform:
    translate3d(0, var(--coffee-hero-y, 0px), 0)
    scale(var(--coffee-hero-scale, 1.05));
  transform-origin: center;
  filter: saturate(1.02) contrast(1.04);

```
