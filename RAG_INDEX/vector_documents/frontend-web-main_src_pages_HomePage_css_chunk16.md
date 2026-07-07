# Knowledge Document: HomePage.css (Chunk 17/34)

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
  "chunk_index": 16,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
size: 32px;
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

.coffee-curved-wheel {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  pointer-events: auto;
}

.coffee-curved-card {
  position: absolute;
  top: 0;
  left: 50%;
  width: 320px;
  height: 440px;
  transform-origin: center 2750px;
  margin-left: -160px;
  border-radius: 16px;
  cursor: pointer;
  perspective: 1000px;
}

.coffee-curved-card .card-inner {
  width: 100%;
  height: 100%;
  position: relative;
  transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.5s ease;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 15px 35px rgba(0,0,0,0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.coffee-curved-card:hover .card-inner {
  transform: translateY(-20px);
  box-shadow: 0 25px 50px rgba(0,0,0,0.6), 0 0 0 1px rgba(215, 177, 132, 0.3);
}

.coffee-curved-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s ease;
}

.coffee-curved-card:hover img {
  transform: scale(1.08);
}

.coffee-curved-card .glass-label {
  position: absolute;
  bottom: 20px;
  left: 20px;
  right: 20px;
  padding: 16px;
  background: rgba(18, 16, 14, 0.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  color: #fff;
  font-size: 16px;
  font-weight: 500;
  text-align: center;
  pointer-events: none;
  transition: background 0.3s ease, border-color 0.3s ease;
}

.coffee-curved-card:hover .glass-label {
  background: rgba(30, 25, 22, 0.85);
  border-color: rgba(215, 177, 132, 0.4);
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

```
