# Knowledge Document: HomePage.css (Chunk 18/34)

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
  "chunk_index": 17,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
2, 0.4);
}

.coffee-ai-section {
  background:
    linear-gradient(135deg, rgba(185, 135, 86, 0.14), transparent 48%),
    #1f140d;
  color: var(--cream);
  scroll-margin-top: 80px;
}

.coffee-ai-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 28px;
  align-items: center;
  margin-bottom: clamp(28px, 5vw, 54px);
}

.coffee-ai-hero h2 {
  max-width: 880px;
  margin: 0;
  color: var(--cream);
  font-size: clamp(2.7rem, 6vw, 5.4rem);
  line-height: 1;
}

.coffee-ai-hero p {
  max-width: 720px;
  margin: 20px 0 0;
  color: rgba(247, 234, 217, 0.72);
  line-height: 1.85;
}

.coffee-ai-orb {
  position: relative;
  width: clamp(110px, 13vw, 170px);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  color: var(--cream);
  background:
    radial-gradient(circle at 32% 24%, rgba(247, 234, 217, 0.28), transparent 34%),
    linear-gradient(135deg, rgba(185, 135, 86, 0.46), rgba(255, 255, 255, 0.08));
  border: 1px solid rgba(247, 234, 217, 0.14);
  border-radius: 999px;
  box-shadow: 0 30px 90px rgba(0, 0, 0, 0.24);
}

.coffee-ai-orb svg:last-child {
  position: absolute;
  right: 24%;
  top: 22%;
  color: var(--caramel);
}

.coffee-ai-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: clamp(14px, 2vw, 22px);
}

.coffee-ai-card {
  min-height: 270px;
  padding: 26px;
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(247, 234, 217, 0.1);
}

.coffee-ai-card h3 {
  color: var(--cream);
}

.coffee-ai-card p {
  color: rgba(247, 234, 217, 0.7);
}

.coffee-pricing {
  background: #fbf6ed;
  scroll-margin-top: 80px;
}

.coffee-pricing .upgrade-grid {
  width: min(1120px, 100%);
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  align-items: stretch;
}

.coffee-pricing .plan-card {
  position: relative;
  min-height: 585px;
  padding: clamp(34px, 4vw, 48px) 32px 30px;
  display: flex;
  flex-direction: column;
  color: #15100d;
  background: rgba(255, 253, 249, 0.82);
  border: 1px solid rgba(76, 57, 38, 0.1);
  border-radius: 8px;
  box-shadow: 0 20px 54px rgba(75, 47, 32, 0.08);
  transform: translateY(0);
  transition: transform 220ms ease, box-shadow 220ms ease, border-color 220ms ease;
}

.coffee-pricing .plan-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 28px 68px rgba(75, 47, 32, 0.12);
}


```
