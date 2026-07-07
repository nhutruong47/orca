# Knowledge Document: Marketplace.css (Chunk 38/44)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/Marketplace.css",
  "language": "css",
  "module": "pages",
  "business_domain": "factory",
  "tags": [
    "factory",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 37,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css

    }

    .mp-filter-grid,
    .mp-verification-grid {
        grid-template-columns: 1fr;
    }

    .mp-filter-footer {
        align-items: flex-start;
        flex-direction: column;
    }

    .mp-verification-status {
        width: fit-content;
        white-space: normal;
    }
}

@media (max-width: 720px) {
    .mp-factory-grid,
    .mp-request-grid,
    .mp-factory-image-preview-grid,
    .mp-card-capacity-grid,
    .mp-profile-grid,
    .mp-factory-actions,
    .mp-product-side-list {
        grid-template-columns: 1fr;
    }

    .mp-manufacturing-market .mp-market-hero {
        padding: 26px 20px;
    }

    .mp-feature-product-card {
        min-height: 460px;
    }

    .mp-feature-product-card > div {
        left: 22px;
        right: 22px;
        bottom: 24px;
    }

    .mp-feature-price {
        align-items: flex-start;
        flex-direction: column;
    }

    .mp-feature-price button {
        margin-left: 0;
    }
}

/* Clean Product Grid Styles (Marquee) */
.mp-marquee-container {
    width: 100%;
    overflow: hidden;
    padding: 20px 0;
    -webkit-mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
    mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
}

.mp-marquee-track {
    display: flex;
    width: max-content;
    animation: marquee 35s linear infinite;
    gap: 32px;
    padding: 0 16px;
}

.mp-marquee-container:hover .mp-marquee-track {
    animation-play-state: paused;
}

@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(calc(-50% - 16px)); }
}

.mp-clean-product-card {
    flex: 0 0 280px;
    display: flex;
    flex-direction: column;
    text-align: center;
    background: transparent;
    border: none;
}

.mp-cpc-image {
    width: 100%;
    aspect-ratio: 3 / 4;
    overflow: hidden;
    margin-bottom: 20px;
    cursor: pointer;
    border-radius: 8px;
    background: #171a1b;
}

.mp-cpc-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
}

.mp-cpc-image:hover img {
    transform: scale(1.04);
}

.mp-cpc-info h3 {
    margin: 0 0 8px;
    color: #fff;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.05em;
    font-family: 'Montserrat', sans-serif;
}

.mp-cpc-info p {
    margin: 0 0 14px;
    color: #a79d94;
    font-style: italic;

```
