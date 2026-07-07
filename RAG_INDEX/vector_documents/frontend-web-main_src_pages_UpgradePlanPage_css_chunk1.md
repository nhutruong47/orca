# Knowledge Document: UpgradePlanPage.css (Chunk 2/4)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/UpgradePlanPage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
d);
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
}

.pricing-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

/* === FEATURED CARD (Professional) === */
.pricing-card.featured {
    transform: scale(1.04);
    z-index: 10;
    box-shadow: var(--shadow-lg), var(--shadow-glow);
    border-color: var(--accent-secondary) !important;
    background: linear-gradient(180deg, rgba(212, 165, 116, 0.05) 0%, var(--bg-card) 100%) !important;
}

.pricing-card.featured:hover {
    transform: scale(1.04) translateY(-4px);
}

.pricing-ribbon {
    position: absolute;
    top: -14px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--accent-gradient);
    color: #fff;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    white-space: nowrap;
    box-shadow: var(--shadow-sm);
}

.pricing-card h2 {
    font-size: 22px;
    font-weight: 800;
    margin: 0 0 16px 0;
    color: var(--text-primary) !important;
}

.pricing-card.featured h2 {
    color: var(--accent-primary) !important;
}

.pricing-price {
    display: flex;
    align-items: baseline;
    gap: 4px;
    margin-bottom: 24px;
}

.pricing-price strong {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    color: var(--text-primary) !important;
}

.pricing-price span {
    font-size: 14px;
    font-weight: 600;
    color: var(--text-muted) !important;
}

.pricing-subtitle {
    margin-bottom: 32px;
}

.pricing-subtitle strong {
    display: block;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 6px;
    color: var(--text-primary) !important;
}

.pricing-subtitle span {
    display: block;
    font-size: 13px;
    opacity: 0.8;
    color: var(--text-secondary) !important;
}

/* === BUTTON === */
.pricing-action {
    width: 100%;
    padding: 14px;
    border-radius: 30px;
    font-size: 14px;
    font-weight: 700;
    cursor: pointer;
    border: 1px solid var(--border) !important;
    margin-bottom: 36px;
    transition: all 0.3s ease;
    background: rgba(255, 255, 255, 0.05) !important;
    color: var(--text-primary) !important;
    position: relative;
    overflow: hidden;
}

.pricing-card.featured .pricing-action {
    background: var(--accent-gradient) !important;
    color: #fff !important;

```
