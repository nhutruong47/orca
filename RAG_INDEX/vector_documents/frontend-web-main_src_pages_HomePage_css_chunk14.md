# Knowledge Document: HomePage.css (Chunk 15/34)

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
  "chunk_index": 14,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
;
}

.coffee-feature-slide {
  position: absolute;
  width: clamp(230px, 31vw, 430px);
  overflow: hidden;
  color: var(--cream);
  background: var(--espresso);
  border: 1px solid rgba(75, 47, 32, 0.16);
  border-radius: 8px;
  box-shadow: 0 28px 80px rgba(75, 47, 32, 0.16);
  isolation: isolate;
  transition: transform 780ms cubic-bezier(0.22, 1, 0.36, 1), opacity 640ms ease, filter 640ms ease;
  animation: featureDrift 780ms cubic-bezier(0.22, 1, 0.36, 1);
}

.coffee-feature-slide::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  background: linear-gradient(180deg, rgba(23, 16, 11, 0.02) 32%, rgba(23, 16, 11, 0.82) 100%);
  pointer-events: none;
}

.coffee-feature-slide img {
  width: 100%;
  height: clamp(280px, 38vw, 500px);
  display: block;
  object-fit: cover;
}

.coffee-feature-slide div {
  position: absolute;
  left: 22px;
  right: 22px;
  bottom: 20px;
  z-index: 2;
}

.coffee-feature-slide h3 {
  margin: 0 0 8px;
  font-family: var(--display-font);
  font-size: clamp(1.35rem, 2.2vw, 2rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: 0;
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
  text-shadow: 0 2px 8px rgba(0,0,0,0.8);
}

.coffee-feature-slide p {
  margin: 0;
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
  line-height: 1.6;
  text-shadow: 0 1px 4px rgba(0,0,0,0.8);
  opacity: 0.9;
}

.coffee-feature-slide--left {
  opacity: 0.58;
  filter: saturate(0.84) brightness(0.82);
  transform: translateX(clamp(-360px, -31vw, -260px)) scale(0.74) rotateY(8deg);
  z-index: 1;
}

.coffee-feature-slide--center {
  opacity: 1;
  filter: saturate(1.04) brightness(1);
  transform: translateX(0) scale(1.05);
  z-index: 3;
}

.coffee-feature-slide--center img {
  animation: featureCenterZoom 3.2s ease-in-out both;
}

.coffee-feature-slide--right {
  opacity: 0.58;
  filter: saturate(0.84) brightness(0.82);
  transform: translateX(clamp(260px, 31vw, 360px)) scale(0.74) rotateY(-8deg);
  z-index: 1;
}

.coffee-roles {
  background: #fbf6ed;
  scroll-margin-top: 80px;
}

.coffee-role-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: clamp(16px, 2.3vw, 26px);
}

.coffee-role-card,
.coffee-ai-card {
  border: 1px solid rgba(75, 47, 32, 0.14);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.56);

```
