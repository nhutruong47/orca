# Knowledge Document: HomePage.css (Chunk 28/34)

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
  "chunk_index": 27,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css

  .coffee-problem-panel {
    grid-template-columns: 1fr;
  }

  .coffee-dashboard-shot {
    grid-template-columns: 1fr;
  }

  .coffee-dashboard-sidebar {
    display: none;
  }

  .coffee-dashboard-board {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .coffee-interface-gallery {
    min-height: clamp(380px, 76vw, 560px);
    margin-inline: -20px;
  }

  .coffee-interface-card {
    width: clamp(260px, 72vw, 520px);
  }

  .coffee-story {
    min-height: auto;
  }

  .coffee-story__copy {
    max-width: 760px;
  }

  .coffee-story--production.production-studio {
    grid-template-columns: 1fr;
    padding-top: 112px;
  }

  .production-studio__media {
    min-height: clamp(420px, 86vw, 620px);
    order: 2;
  }

  .production-studio__copy {
    order: 1;
  }

  .studio-video-card--main {
    width: 76%;
    height: clamp(300px, 52vw, 440px);
  }

  .studio-video-card--float {
    width: 42%;
    height: clamp(180px, 30vw, 260px);
  }

  .coffee-product__image {
    aspect-ratio: 16 / 10;
  }

  .coffee-workshop-card p {
    min-height: auto;
  }

  .coffee-feature-slide {
    width: clamp(210px, 42vw, 360px);
  }

  .coffee-feature-slide--left {
    transform: translateX(-32vw) scale(0.72);
  }

  .coffee-feature-slide--right {
    transform: translateX(32vw) scale(0.72);
  }
}

@media (max-width: 640px) {
  .coffee-nav {
    inset: 18px 18px auto;
  }

  .coffee-nav__links {
    justify-self: start;
    gap: 10px 16px;
  }

  .coffee-nav__links button {
    font-size: 0.76rem;
  }

  .coffee-hero {
    min-height: 100svh;
    padding: 120px 18px 70px;
  }

  .coffee-hero__veil {
    background:
      linear-gradient(90deg, rgba(19, 12, 7, 0.86), rgba(19, 12, 7, 0.44)),
      linear-gradient(180deg, rgba(19, 12, 7, 0.18) 0%, rgba(19, 12, 7, 0.44) 72%, #f6ead8 100%);
  }

  .coffee-hero h1 {
    font-size: clamp(4.4rem, 22vw, 6.8rem);
  }

  .production-studio__copy h2 {
    font-size: clamp(2.8rem, 13vw, 4.9rem);
  }

  .production-studio__media {
    min-height: 390px;
  }

  .studio-video-card--main {
    top: 12%;
    width: 88%;
    height: 280px;
  }

  .studio-video-card--float {
    top: 0;
    width: 54%;
    height: 170px;
  }

  .studio-signal-card--top {
    left: 8px;
    top: 2%;
  }

  .studio-signal-card--bottom {
    right: 8px;
    bottom: 2%;
  }

  .coffee-hero p {
    max-width: 34rem;

```
