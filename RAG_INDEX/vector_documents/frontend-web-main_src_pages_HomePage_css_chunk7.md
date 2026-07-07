# Knowledge Document: HomePage.css (Chunk 8/34)

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
  "chunk_index": 7,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
amp(1rem, 1.6vw, 1.3rem);
  line-height: 1.1;
}

.studio-signal-card {
  position: absolute;
  z-index: 3;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 13px 15px;
  color: var(--walnut);
  background: rgba(255, 248, 237, 0.76);
  border: 1px solid rgba(185, 135, 86, 0.34);
  border-radius: 8px;
  box-shadow: 0 18px 56px rgba(80, 48, 25, 0.18), 0 0 42px rgba(185, 135, 86, 0.14);
  backdrop-filter: blur(18px);
}

.studio-signal-card svg {
  color: var(--caramel);
}

.studio-signal-card span {
  color: rgba(64, 43, 30, 0.72);
}

.studio-signal-card--top {
  left: clamp(18px, 5vw, 72px);
  top: 3%;
  animation: studioChipFloat 5.8s ease-in-out infinite;
}

.studio-signal-card--bottom {
  right: clamp(18px, 6vw, 92px);
  bottom: 9%;
  animation: studioChipFloat 6.4s ease-in-out 0.8s infinite;
}

.production-studio__copy {
  position: relative;
  z-index: 2;
}

.coffee-story--production.production-studio .coffee-kicker {
  color: #a16635;
  text-shadow: 0 0 24px rgba(224, 164, 102, 0.26);
}

.coffee-story--production.production-studio .production-studio__copy h2 {
  color: #1f140d;
  font-size: clamp(3.2rem, 6.4vw, 6.7rem);
  text-shadow:
    0 18px 58px rgba(80, 48, 25, 0.16),
    0 0 42px rgba(224, 164, 102, 0.18);
}

.coffee-story--production.production-studio .production-studio__copy p {
  color: rgba(64, 43, 30, 0.74);
  font-size: clamp(1rem, 1.35vw, 1.16rem);
}

.coffee-story--production.production-studio .production-studio__workflow div {
  opacity: 0;
  color: var(--walnut);
  background: rgba(255, 250, 242, 0.72);
  border-color: rgba(185, 135, 86, 0.24);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.62), 0 18px 52px rgba(80, 48, 25, 0.12);
  transform: translateX(34px);
  backdrop-filter: blur(18px);
}

.coffee-story--production.production-studio .production-studio__copy.is-visible .production-studio__workflow div {
  opacity: 1;
  transform: translateX(0);
}

.coffee-story--production.production-studio .production-studio__workflow strong {
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

```
