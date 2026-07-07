# Knowledge Document: UpgradePlanPage.css (Chunk 1/4)

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
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
.pricing-page {
    min-height: 100%;
    background: transparent;
    font-family: var(--font, 'Inter', sans-serif);
    padding: clamp(32px, 5vw, 64px) 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: var(--text-primary);
}

.pricing-header {
    text-align: center;
    margin-bottom: 24px;
    margin-top: 20px;
}

.pricing-header h1 {
    font-size: 32px;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 12px;
}

.pricing-header p {
    font-size: 15px;
    color: var(--text-secondary);
    margin: 0;
}

.pricing-payment-methods {
    display: flex;
    gap: 16px;
    margin-bottom: 48px;
    justify-content: center;
}

.pricing-payment-methods button {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    color: var(--text-secondary);
}

.pricing-payment-methods button:hover {
    background: var(--bg-card-hover);
    color: var(--text-primary);
}

.pricing-payment-methods button.active.mb-bank {
    border-color: #1459c8;
    color: #1459c8;
    background: rgba(20, 89, 200, 0.1);
}

.pricing-payment-methods button.active.vnpay {
    border-color: #1459c8;
    color: #1459c8;
    background: rgba(20, 89, 200, 0.1);
}

.pricing-payment-methods button.active.payos {
    border-color: #2e7d32;
    color: #2e7d32;
    background: rgba(46, 125, 50, 0.1);
}

.pricing-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1000px;
    width: 100%;
    align-items: stretch;
}

/* === BASE CARD (Starter) === */
.pricing-card {
    position: relative;
    border-radius: 16px;
    padding: 40px 32px;
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: var(--shadow-md);
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

```
