# Knowledge Document: HomePage.css (Chunk 9/34)

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
  "chunk_index": 8,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
ction-studio .production-studio__workflow strong {
  color: #fff8ed;
  background: linear-gradient(135deg, #1f140d, #7e5939);
  box-shadow: 0 0 24px rgba(185, 135, 86, 0.24);
}

.coffee-story--solution {
  background: linear-gradient(180deg, #fbf6ed 0%, #f7ead8 100%);
}

.coffee-story__media {
  position: relative;
  min-height: clamp(420px, 62vw, 680px);
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 34px 90px rgba(80, 48, 25, 0.18);
  transform: translate3d(0, var(--coffee-story-y, 0px), 0) scale(0.995);
  will-change: transform;
}

.coffee-story__media img,
.coffee-cinema__panel img,
.coffee-product__image img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
}

.coffee-story__media video {
  width: 100%;
  height: 100%;
  min-height: inherit;
  display: block;
  object-fit: cover;
  transform: scale(var(--coffee-story-scale, 1.02));
  transform-origin: center;
  filter: saturate(1.02) contrast(1.04);
}

.coffee-story__media--video::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(180deg, rgba(23, 16, 11, 0.02) 45%, rgba(23, 16, 11, 0.48) 100%),
    linear-gradient(90deg, rgba(23, 16, 11, 0.16), transparent 52%);
  pointer-events: none;
}

.coffee-video-badge {
  position: absolute;
  left: 18px;
  bottom: 18px;
  z-index: 2;
  padding: 9px 12px;
  color: var(--cream);
  background: rgba(42, 27, 18, 0.7);
  border: 1px solid rgba(247, 234, 217, 0.18);
  border-radius: 4px;
  font-size: 0.66rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  backdrop-filter: blur(12px);
}

.coffee-story__media img {
  transform: scale(var(--coffee-story-scale, 1.02));
  transform-origin: center;
  transition: transform 900ms cubic-bezier(0.22, 1, 0.36, 1);
  will-change: transform;
}

.coffee-story__copy h2,
.coffee-section-heading h2,
.coffee-cinema h2,
.coffee-reserve h2 {
  margin: 0;
  color: var(--espresso);
  font-family: var(--display-font);
  font-size: clamp(2.7rem, 6vw, 5.6rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: 0;
}

.coffee-story__copy p,
.coffee-cinema p,
.coffee-reserve p {
  max-width: 620px;
  margin: 24px 0 0;
  color: var(--muted);
  font-size: 1rem;
  line-height: 1.9;
}

.coffee-story__metrics {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 34px;
}

.coffee-story__metrics div {

```
