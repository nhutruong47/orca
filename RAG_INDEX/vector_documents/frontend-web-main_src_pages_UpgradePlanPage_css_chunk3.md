# Knowledge Document: UpgradePlanPage.css (Chunk 4/4)

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
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
rd.theme-dark .pricing-subtitle strong {
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
.pricing-card.theme-dark .pricing-action:hover {
    background: #f0f4f8 !important;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
}
.pricing-card.theme-dark .pricing-action::before {
    background: linear-gradient(to right, transparent, rgba(15, 28, 46, 0.15), transparent);
}
.pricing-card.theme-dark .check-icon {
    color: #62dbcb !important;
}

@media (max-width: 960px) {
    .pricing-grid {
        grid-template-columns: 1fr;
        max-width: 400px;
        gap: 32px;
    }
    
    .pricing-card.featured {
        transform: scale(1);
        padding: 40px 32px;
    }
    
    .pricing-card.featured:hover {
        transform: translateY(-4px);
    }
}

```
