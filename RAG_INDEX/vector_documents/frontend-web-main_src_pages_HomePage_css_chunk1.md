# Knowledge Document: HomePage.css (Chunk 2/34)

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
  "chunk_index": 1,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
 center;
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
  will-change: transform;
}

.coffee-hero__image video {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  filter: saturate(0.92) contrast(1.04);
}

.coffee-hero__veil {
  z-index: -2;
  background:
    linear-gradient(90deg, rgba(19, 12, 7, 0.88) 0%, rgba(19, 12, 7, 0.56) 44%, rgba(19, 12, 7, 0.28) 100%),
    linear-gradient(180deg, rgba(19, 12, 7, 0.18) 0%, rgba(19, 12, 7, 0.36) 72%, #f6ead8 100%);
}

.coffee-hero__steam {
  z-index: -1;
  pointer-events: none;
  overflow: hidden;
}

.coffee-hero__steam span {
  position: absolute;
  right: clamp(19%, 30vw, 37%);
  bottom: clamp(34%, 42vw, 56%);
  width: 74px;
  height: 180px;
  border-radius: 999px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.34), rgba(255, 255, 255, 0));
  filter: blur(18px);
  opacity: 0;
  animation: coffeeSteam 4.8s ease-in-out infinite;
}

.coffee-hero__steam span:nth-child(2) {
  right: clamp(23%, 35vw, 43%);
  animation-delay: 1.1s;
  transform: scale(0.82);
}

.coffee-hero__steam span:nth-child(3) {
  right: clamp(15%, 26vw, 31%);
  animation-delay: 2.2s;
  transform: scale(0.68);
}

.coffee-hero__content {
  width: min(1040px, 100%);
  max-width: 1040px;
  justify-self: center;
  transform:
    translate3d(0, var(--coffee-copy-y, 0px), 0)
    scale(var(--coffee-copy-scale, 1));
  will-change: transform;
}

.coffee-hero__content > * {
  opacity: 0;
  animation: coffeeHeroReveal 900ms cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

.coffee-hero__content .coffee-kicker {
  animation-delay: 120ms;
}

.coffee-hero__content h1 {
  animation:
    coffeeHeroTitle 1200ms cubic-bezier(0.16, 1, 0.3, 1) 220ms forwards,
    coffeeHeroGlow 4600ms ease-in-out 1400ms infinite;
}

.coffee-hero__content p {
  animation-delay: 420ms;
}

.coffee-hero__actions {
  animation-delay: 560ms;
}

.coffee-kicker {
  display: inline-block;
  margin-bottom: 22px;
  color: #d7b184;
  font-size: clamp(0.76rem, 1vw, 0.95rem);
  font-weight: 800;
  letter-spacing: 0.28em;

```
