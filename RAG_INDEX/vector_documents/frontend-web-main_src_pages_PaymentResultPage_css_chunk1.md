# Knowledge Document: PaymentResultPage.css (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/PaymentResultPage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
ons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 8px;
}

.payment-result-primary,
.payment-result-secondary {
    min-height: 42px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 0 16px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 850;
}

.payment-result-primary {
    background: var(--shell-accent);
    color: var(--shell-button-text);
}

.payment-result-secondary {
    color: var(--shell-text);
    background: var(--shell-surface-soft);
    border: 1px solid var(--shell-border);
}

```
