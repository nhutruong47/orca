# Knowledge Document: HomePage.css (Chunk 7/34)

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
  "chunk_index": 6,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
t 34%);
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
  position: relative;
  z-index: 1;
  min-height: clamp(540px, 64vw, 760px);
  perspective: 1200px;
}

.studio-video-card {
  position: absolute;
  overflow: hidden;
  color: var(--cream);
  background: rgba(42, 27, 18, 0.82);
  border: 1px solid rgba(185, 135, 86, 0.42);
  border-radius: 8px;
  box-shadow:
    0 34px 96px rgba(80, 48, 25, 0.28),
    0 0 72px rgba(185, 135, 86, 0.18);
  transform-style: preserve-3d;
}

.studio-video-card--main {
  left: 0;
  top: 12%;
  width: min(82%, 760px);
  height: clamp(360px, 40vw, 540px);
  animation: studioMainFloat 7.5s ease-in-out infinite;
}

.studio-video-card--float {
  right: 0;
  top: 2%;
  width: min(44%, 410px);
  height: clamp(210px, 23vw, 330px);
  animation: studioFloatCard 6.8s ease-in-out infinite;
}

.studio-video-card video {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  filter: saturate(1.08) contrast(1.04) brightness(0.98);
}

.studio-video-card__shade {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(180deg, rgba(42, 27, 18, 0.02) 34%, rgba(31, 20, 13, 0.7) 100%),
    linear-gradient(110deg, rgba(224, 164, 102, 0.22), transparent 44%);
  pointer-events: none;
}

.studio-video-card__meta {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 18px;
  z-index: 2;
  display: grid;
  gap: 6px;
}

.studio-video-card__meta span,
.studio-signal-card span {
  color: rgba(255, 245, 232, 0.78);
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.studio-video-card__meta strong {
  color: #ffffff;
  font-size: clamp(1rem, 1.6vw, 1.3rem);
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

```
