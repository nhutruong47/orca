# Knowledge Document: index.css (Chunk 3/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/index.css",
  "language": "css",
  "module": "src",
  "business_domain": "admin",
  "tags": [
    "admin",
    "inventory",
    "dashboard"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
 0.14);
  --shell-profile-overlay: linear-gradient(90deg, rgba(18, 16, 14, 0.94), rgba(18, 16, 14, 0.68));
}

/* Responsive breakpoints */
@media (max-width: 1920px) {
  :root {
    --sidebar-width: 240px;
  }
}

@media (max-width: 1536px) {
  :root {
    --sidebar-width: 220px;
  }
}

@media (max-width: 1280px) {
  :root {
    --sidebar-width: 200px;
  }
}

@media (max-width: 1024px) {
  :root {
    --sidebar-width: 0;
    --topbar-height: 56px;
  }
}

@media (max-width: 768px) {
  :root {
    --sidebar-width: 0;
    --topbar-height: 48px;
  }
}

@media (max-width: 480px) {
  :root {
    --sidebar-width: 0;
    --topbar-height: 44px;
  }
}

/* ===== Light Theme Override — Roastery Marketplace Palette ===== */
body.theme-light {
  /* Warm cream & brown palette - inspired by premium coffee roastery aesthetic */
  --bg-primary: #fbf9f4;       /* off-white surface */
  --bg-secondary: #f0eee9;     /* light beige - sidebar */
  --bg-tertiary: #e8e5de;      /* medium beige */
  --bg-card: #fffcf8;          /* off-white cards */
  --bg-card-hover: #faf7f1;    /* warm cream hover */
  --bg-input: rgba(12, 9, 6, 0.04);

  /* Dark brown text for maximum contrast */
  --text-primary: #1b1c19;     /* very dark - body text */
  --text-secondary: #6b5344;   /* medium brown - secondary */
  --text-muted: #9b8b7e;       /* lighter brown - muted */
  --text-accent: #735a3a;      /* medium brown accent */

  /* Premium brown accents from roastery palette */
  --accent-primary: #322214;   /* dark brown - buttons, active */
  --accent-secondary: #735a3a; /* medium brown - secondary accent */
  --accent-gradient: linear-gradient(135deg, #785e3e 0%, #5c4a37 50%, #322214 100%);
  --accent-glow: rgba(50, 34, 20, 0.10);

  --success: #16a34a;
  --warning: #d97706;
  --danger: #c33030;
  --info: #6b5344;

  /* Strong borders for editorial clarity */
  --border: rgba(27, 28, 25, 0.08);
  --border-focus: rgba(50, 34, 20, 0.20);

  --shadow-sm: 0 2px 6px rgba(27, 28, 25, 0.04);
  --shadow-md: 0 8px 24px rgba(27, 28, 25, 0.06);
  --shadow-lg: 0 16px 40px rgba(27, 28, 25, 0.08);
  --shadow-glow: 0 0 24px rgba(50, 34, 20, 0.06);

  --bg-glass: rgba(251, 249, 244, 0.6);
  --bg-glass-hover: rgba(251, 249, 244, 0.9);
  --glass-border: rgba(27, 28, 25, 0.06);

  --card-bg: var(--bg-card);
  --border-color: var(--border);

  --shell-bg:

```
