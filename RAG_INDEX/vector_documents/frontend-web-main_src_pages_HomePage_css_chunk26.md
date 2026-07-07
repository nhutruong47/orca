# Knowledge Document: HomePage.css (Chunk 27/34)

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
  "chunk_index": 26,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
problem-list {
  display: grid;
  gap: 16px;
}

.coffee-problem-row {
  min-height: auto;
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: start;
  gap: 14px;
  padding: 18px !important;
  background: rgba(255, 255, 255, 0.055) !important;
  border: 1px solid rgba(247, 234, 217, 0.08) !important;
  border-radius: 8px !important;
  box-shadow: none;
}

.coffee-problem-row:hover {
  transform: translateX(4px);
  background: rgba(255, 255, 255, 0.085) !important;
  border-color: rgba(247, 234, 217, 0.16) !important;
}

.coffee-problem-row strong {
  color: var(--readable-gold) !important;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.12em;
}

.coffee-problem-row svg {
  display: none;
}

.coffee-problem-row p {
  margin: 0;
  max-width: none;
  color: rgba(255, 250, 240, 0.9) !important;
  font-size: 1rem;
  font-weight: 650;
  line-height: 1.72;
  text-shadow: 0 3px 14px rgba(0, 0, 0, 0.42);
}

.coffee-stat-card p,
.coffee-story__copy p,
.coffee-section-heading p,
.coffee-pricing-card p,
.coffee-role-card p {
  color: rgba(18, 33, 31, 0.78) !important;
  font-weight: 620;
}

.coffee-button--light {
  color: #412D15;
  background: linear-gradient(135deg, #fff7d8, #ffd166);
  box-shadow: 0 14px 34px rgba(65, 45, 21, 0.24);
}

.coffee-button--ghost {
  color: #fffaf0;
  background: rgba(65, 45, 21, 0.38);
  border-color: rgba(255, 209, 102, 0.34);
}

@media (max-width: 980px) {
  .coffee-nav {
    grid-template-columns: 1fr;
    gap: 10px;
  }

  .coffee-story,
  .coffee-cinema__panel,
  .coffee-product-grid,
  .coffee-workshop-grid,
  .coffee-stat-grid,
  .coffee-role-grid,
  .coffee-ai-grid,
  .coffee-pricing-grid,
  .coffee-support-grid {
    grid-template-columns: 1fr;
  }

  .coffee-pricing .upgrade-grid {
    grid-template-columns: 1fr;
    max-width: 420px;
  }

  .coffee-pricing .plan-card {
    min-height: auto;
  }

  .coffee-ai-hero {
    grid-template-columns: 1fr;
  }

  .coffee-ai-orb {
    justify-self: start;
  }

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

```
