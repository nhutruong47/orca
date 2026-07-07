# Knowledge Document: UpgradePlanPage.css (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
ht: 700;
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
    border: none !important;
}

.pricing-action:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.15);
}

.pricing-card.featured .pricing-action:hover {
    filter: brightness(1.15);
    background: var(--accent-gradient) !important;
    box-shadow: 0 0 15px rgba(212, 165, 116, 0.4);
}

/* Shine animation overlay (Sleen effect) */
.pricing-action::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 50%;
    height: 100%;
    background: linear-gradient(to right, transparent, rgba(255, 255, 255, 0.3), transparent);
    transform: skewX(-25deg);
    transition: left 0s;
    z-index: 1;
    pointer-events: none;
}

.pricing-action:hover::before {
    left: 200%;
    transition: left 0.6s ease-in-out;
}

.pricing-features {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.pricing-features li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 13px;
    font-weight: 600;
    line-height: 1.5;
    color: var(--text-secondary) !important;
}

.check-icon {
    flex-shrink: 0;
    color: var(--success) !important;
}

.pricing-card.featured .check-icon {
    color: var(--accent-primary) !important;
}

/* Theme overrides for specific cards if needed (Enterprise Card) */
.pricing-card.theme-dark {
    background: #0f1c2e !important;
    border-color: #1a2a40 !important;
}
.pricing-card.theme-dark h2,
.pricing-card.theme-dark .pricing-price strong,
.pricing-card.theme-dark .pricing-subtitle strong {
    color: #ffffff !important;
}
.pricing-card.theme-dark .pricing-price span,
.pricing-card.theme-dark .pricing-subtitle span,
.pricing-card.theme-dark .pricing-features li {
    color: #849bb3 !important;
}
.pricing-card.theme-dark .pricing-action {
    background: #ffffff !important;
    color: #0f1c2e !important;
    border-color: #ffffff !important;
}

```
