# Knowledge Document: HomePage.css (Chunk 16/34)

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
  "chunk_index": 15,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
x, 31vw, 360px)) scale(0.74) rotateY(-8deg);
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
  box-shadow: 0 24px 64px rgba(75, 47, 32, 0.1);
  transition-property: opacity, transform, box-shadow, border-color, background-color;
}

.coffee-role-card {
  min-height: 250px;
  padding: 28px;
}

.coffee-role-card svg,
.coffee-ai-card svg {
  color: var(--caramel);
}

.coffee-role-card h3,
.coffee-ai-card h3 {
  margin: 24px 0 12px;
  color: var(--espresso);
  font-size: clamp(1.35rem, 2.2vw, 1.85rem);
  line-height: 1.18;
}

.coffee-role-card p,
.coffee-ai-card p {
  color: var(--muted);
  line-height: 1.75;
}

.coffee-role-card.is-visible:hover,
.coffee-ai-card.is-visible:hover {
  transform: translateY(-6px);
  border-color: rgba(75, 47, 32, 0.26);
  background: rgba(255, 255, 255, 0.72);
  box-shadow: 0 34px 82px rgba(75, 47, 32, 0.16);
}

.coffee-dashboard-section {
  overflow: hidden;
  background:
    radial-gradient(circle at 20% 8%, rgba(185, 135, 86, 0.22), transparent 32%),
    linear-gradient(180deg, #f3e5d1 0%, #fbf6ed 100%);
  scroll-margin-top: 80px;
}

.coffee-dashboard-curved {
  position: relative;
  width: 100%;
  min-height: 760px;
  overflow: hidden;
  background-color: #0c0b0a;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 80px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.coffee-curved-heading {
  text-align: center;
  z-index: 10;
  position: relative;
  margin-bottom: 20px;
}

.coffee-curved-heading .coffee-kicker {
  display: block;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #d7b184;
  margin-bottom: 12px;
  font-weight: 600;
}

.coffee-curved-heading h2 {
  font-size: 32px;
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
  margin: 0 auto;
  font-weight: 500;
  max-width: 900px;
  line-height: 1.4;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.8) !important;
}

.coffee-curved-wheel-container {
  position: absolute;
  top: 220px;
  left: 50%;
  transform: translateX(-50%);
  width: 5500px;
  height: 5500px;
  pointer-events: none;
}

```
