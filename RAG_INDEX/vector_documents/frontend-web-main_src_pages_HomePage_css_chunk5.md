# Knowledge Document: HomePage.css (Chunk 6/34)

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
  "chunk_index": 5,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
caramel);
  font-size: 0.78rem;
  letter-spacing: 0.12em;
}

.coffee-problem-row svg {
  color: var(--caramel);
}

.coffee-problem-row p {
  margin: 0;
  color: rgba(247, 234, 217, 0.74);
  line-height: 1.72;
}

.coffee-stat-card.is-visible:hover,
.coffee-pricing-card.is-visible:hover {
  transform: translateY(-6px);
  border-color: rgba(75, 47, 32, 0.26);
  background: rgba(255, 255, 255, 0.72);
  box-shadow: 0 34px 82px rgba(75, 47, 32, 0.16);
}

.coffee-story {
  display: grid;
  grid-template-columns: minmax(0, 0.95fr) minmax(320px, 0.85fr);
  gap: clamp(32px, 7vw, 96px);
  align-items: center;
  min-height: 92svh;
  background: linear-gradient(180deg, #f6ead8 0%, #fbf6ed 100%);
  scroll-margin-top: 80px;
}

.coffee-story--production {
  background: linear-gradient(180deg, #fbf6ed 0%, #f3e5d1 100%);
}

.coffee-story--production.production-studio {
  position: relative;
  grid-template-columns: minmax(0, 1.05fr) minmax(360px, 0.95fr);
  gap: clamp(34px, 6vw, 86px);
  min-height: 100svh;
  overflow: hidden;
  color: var(--espresso);
  background:
    radial-gradient(circle at 50% 0%, rgba(224, 164, 102, 0.46), transparent 34%),
    radial-gradient(circle at 88% 34%, rgba(126, 89, 57, 0.2), transparent 30%),
    linear-gradient(180deg, #fff8ed 0%, #f8ead7 52%, #eed7bc 100%);
  isolation: isolate;
}

.production-studio::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -2;
  background-image: radial-gradient(circle, rgba(126, 89, 57, 0.28) 1px, transparent 1.6px);
  background-size: 28px 28px;
  mask-image: linear-gradient(180deg, rgba(0, 0, 0, 0.9), transparent 88%);
  opacity: 0.36;
  animation: studioGridDrift 18s linear infinite;
}

.production-studio::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(90deg, rgba(255, 248, 237, 0.82), transparent 30%, transparent 72%, rgba(255, 248, 237, 0.62)),
    radial-gradient(circle at 50% 44%, rgba(185, 135, 86, 0.22), transparent 34%);
  pointer-events: none;
}

.production-studio__glow {
  position: absolute;
  left: 50%;
  top: 12%;
  width: min(680px, 62vw);
  height: min(680px, 62vw);
  background: radial-gradient(circle, rgba(224, 164, 102, 0.46), transparent 68%);
  filter: blur(28px);
  transform: translateX(-50%);
  opacity: 0.72;
  animation: studioPulse 6.2s ease-in-out infinite;
}

.production-studio__media {

```
