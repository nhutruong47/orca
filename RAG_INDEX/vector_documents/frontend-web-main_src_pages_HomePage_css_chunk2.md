# Knowledge Document: HomePage.css (Chunk 3/34)

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
  "chunk_index": 2,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
eroTitle 1200ms cubic-bezier(0.16, 1, 0.3, 1) 220ms forwards,
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
  text-transform: uppercase;
}

.coffee-hero h1 {
  position: relative;
  margin: 0 auto;
  max-width: 1040px;
  color: #fff5e8;
  font-family: var(--display-font);
  font-size: clamp(5.8rem, 16vw, 15.8rem);
  font-weight: 800;
  line-height: 0.82;
  letter-spacing: 0;
  text-shadow:
    0 18px 58px rgba(0, 0, 0, 0.52),
    0 0 28px rgba(255, 245, 232, 0.16),
    0 0 72px rgba(215, 177, 132, 0.18);
}

.coffee-hero h1::after {
  content: "ORCA";
  position: absolute;
  inset: 0;
  color: transparent;
  background: linear-gradient(105deg, transparent 30%, rgba(255, 255, 255, 0.72) 48%, transparent 66%);
  background-size: 240% 100%;
  background-clip: text;
  -webkit-background-clip: text;
  pointer-events: none;
  opacity: 0;
  animation: coffeeHeroShine 4200ms ease-in-out 1700ms infinite;
}

.coffee-hero p {
  max-width: 720px;
  margin: 34px auto 0;
  color: rgba(255, 245, 232, 0.88);
  font-size: clamp(1.08rem, 1.9vw, 1.55rem);
  font-weight: 600;
  line-height: 1.75;
  text-shadow: 0 10px 34px rgba(0, 0, 0, 0.46);
}

.coffee-hero__actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 38px;
}

.coffee-button {
  min-height: 48px;
  padding: 0 22px;
  border: 1px solid transparent;
  border-radius: 8px;
  font: inherit;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: transform 240ms ease, background 240ms ease, border-color 240ms ease;
}

.coffee-button:hover {
  transform: translateY(-2px);
}

.coffee-button--light {
  color: var(--espresso);
  background: var(--cream);
}

.coffee-button--ghost {
  color: var(--cream);
  background: rgba(247, 234, 217, 0.08);
  border-color: rgba(247, 234, 217, 0.28);
}

.coffee-button--dark {
  color: var(--cream);
  background: var(--espresso);
}

.coffee-scroll-cue {
  position: absolute;
  left: 50%;
  bottom: 24px;
  z-index: 3;
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;

```
