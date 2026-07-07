# Knowledge Document: HomePage.css (Chunk 22/34)

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
  "chunk_index": 21,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
 0.66);
  font-size: 0.92rem;
  font-weight: 650;
  line-height: 1.6;
}

.coffee-support-card strong {
  margin-top: auto;
  color: #0f766e;
  font-size: 0.94rem;
  font-weight: 850;
}

@keyframes featureDrift {
  from {
    opacity: 0;
    transform: translateX(42vw) scale(0.7);
  }
}

@keyframes featureCenterZoom {
  from {
    transform: scale(1.02);
  }

  to {
    transform: scale(1.12);
  }
}

@keyframes coffeeHeroReveal {
  from {
    opacity: 0;
    filter: blur(10px);
    transform: translate3d(0, 28px, 0) scale(0.985);
  }

  to {
    opacity: 1;
    filter: blur(0);
    transform: translate3d(0, 0, 0) scale(1);
  }
}

@keyframes coffeeHeroTitle {
  0% {
    opacity: 0;
    filter: blur(18px);
    transform: translate3d(0, 34px, 0) scale(0.9);
    letter-spacing: 0.08em;
  }

  58% {
    opacity: 1;
    filter: blur(0);
    transform: translate3d(0, -4px, 0) scale(1.035);
    letter-spacing: 0.015em;
  }

  100% {
    opacity: 1;
    filter: blur(0);
    transform: translate3d(0, 0, 0) scale(1);
    letter-spacing: 0;
  }
}

@keyframes coffeeHeroGlow {
  0%,
  100% {
    text-shadow:
      0 18px 58px rgba(0, 0, 0, 0.52),
      0 0 28px rgba(255, 245, 232, 0.16),
      0 0 72px rgba(215, 177, 132, 0.18);
  }

  45% {
    text-shadow:
      0 20px 64px rgba(0, 0, 0, 0.56),
      0 0 42px rgba(255, 245, 232, 0.24),
      0 0 110px rgba(215, 177, 132, 0.28);
  }
}

@keyframes coffeeHeroShine {
  0%,
  38% {
    opacity: 0;
    background-position: 140% 0;
  }

  48% {
    opacity: 0.72;
  }

  68% {
    opacity: 0;
    background-position: -60% 0;
  }

  100% {
    opacity: 0;
    background-position: -60% 0;
  }
}

.coffee-story__metrics div {
  transition: transform 280ms ease, border-color 280ms ease, background-color 280ms ease;
}

.coffee-story__metrics div:hover {
  transform: translateY(-3px);
  border-color: rgba(75, 47, 32, 0.28);
  background: rgba(255, 255, 255, 0.5);
}

@keyframes coffeeSteam {
  0% {
    opacity: 0;
    transform: translate3d(0, 40px, 0) scale(0.75);
  }

  28% {
    opacity: 0.42;
  }

  100% {
    opacity: 0;
    transform: translate3d(-24px, -130px, 0) scale(1.18);
  }
}

@keyframes coffeeCue {
  0%,
  100% {
    transform: translate(-50%, 0);
  }

  50% {
    transform: translate(-50%, 8px);
  }
}

@keyframes coffeeInterfaceSlide {
  from {
    transform: translateX(0);
  }

  to {

```
