# Knowledge Document: HomePage.css (Chunk 23/34)

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
  "chunk_index": 22,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
y: 0;
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
    transform: translateX(calc(-50% + 50vw));
  }
}

@keyframes coffeeInterfaceZoom {
  from {
    transform: scale(1.04);
  }

  to {
    transform: scale(1.1);
  }
}

@keyframes coffeeRailPulse {
  0%,
  100% {
    opacity: 0.35;
    transform: scaleX(0.24);
  }

  45% {
    opacity: 1;
    transform: scaleX(1);
  }
}

@keyframes studioGridDrift {
  from {
    background-position: 0 0;
  }

  to {
    background-position: 56px 56px;
  }
}

@keyframes studioPulse {
  0%,
  100% {
    opacity: 0.58;
    transform: translateX(-50%) scale(0.96);
  }

  50% {
    opacity: 0.86;
    transform: translateX(-50%) scale(1.08);
  }
}

@keyframes studioMainFloat {
  0%,
  100% {
    transform: rotateX(0deg) rotateY(0deg) translate3d(0, 0, 0);
  }

  50% {
    transform: rotateX(1.5deg) rotateY(-2.5deg) translate3d(0, -12px, 0);
  }
}

@keyframes studioFloatCard {
  0%,
  100% {
    transform: rotateX(0deg) rotateY(-8deg) translate3d(0, 0, 38px);
  }

  50% {
    transform: rotateX(2deg) rotateY(-3deg) translate3d(-10px, 16px, 70px);
  }
}

@keyframes studioChipFloat {
  0%,
  100% {
    transform: translate3d(0, 0, 0);
  }

  50% {
    transform: translate3d(0, -10px, 0);
  }
}

/* Readability pass: stronger contrast for dark cinematic sections and sticky nav. */
.coffee-home {
  --readable-cream: #fffaf0;
  --readable-gold: #ffd166;
  --readable-brown: #412D15;
  --readable-brown-soft: #6f4b22;
}

.coffee-nav {
  min-height: 48px;
  padding: 0;
  color: var(--readable-cream);
  background: transparent;
  border: 0;
  border-radius: 0;
  box-shadow: none;
  backdrop-filter: none;
  transform: translateY(0);
  opacity: 1;
  transition:
    transform 260ms ease,
    opacity 220ms ease,
    background-color 220ms ease,
    border-color 220ms ease,
    box-shadow 220ms ease,
    padding 220ms ease,
    border-radius 220ms ease;
}

.coffee-nav__brand {
  color: #ffffff;
  font-size: clamp(1.02rem, 1.4vw, 1.2rem);
  text-shadow:
    0 0 14px rgba(255, 209, 102, 0.44),

```
