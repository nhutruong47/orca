# Knowledge Document: index.css (Chunk 1/10)

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
  "chunk_index": 0,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
/* ===================================================
   ORCA Management System - Global Styles
   Modern Dark Theme with Indigo/Emerald Palette
   =================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ===== CSS Variables / Design Tokens ===== */
:root {
  /* Colors — Dark Navy / Space Theme with Coffee Gold Accents */
  --bg-primary: #0a0e17;
  /* Deep navy space */
  --bg-secondary: #0f1524;
  /* Slightly lighter navy */
  --bg-tertiary: #1a2235;
  --bg-card: rgba(15, 21, 36, 0.85);
  --bg-card-hover: rgba(26, 34, 53, 0.95);
  --bg-input: rgba(255, 255, 255, 0.03);

  --text-primary: #fdf8f4;
  /* Crema white */
  --text-secondary: #d1bfae;
  /* Latte */
  --text-muted: #8c7765;
  --text-accent: #e5b376;

  --accent-primary: #d4a574;
  /* Gold/Caramel */
  --accent-secondary: #8b5e3c;
  --accent-gradient: linear-gradient(135deg, #d4a574 0%, #a67b4c 50%, #8b5e3c 100%);
  --accent-glow: rgba(212, 165, 116, 0.25);

  --success: #3fb950;
  --warning: #d49c57;
  --danger: #e24b4b;
  --info: #6a96bd;

  --border: rgba(255, 255, 255, 0.08);
  --border-focus: rgba(212, 165, 116, 0.5);

  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.6);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.6);
  --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.8);
  --shadow-glow: 0 0 20px rgba(212, 165, 116, 0.15);
  --shadow-neon: 0 0 15px rgba(212, 165, 116, 0.4);
  --shadow-neon-strong: 0 0 25px rgba(212, 165, 116, 0.6);

  --bg-glass: rgba(15, 21, 36, 0.4);
  --bg-glass-hover: rgba(15, 21, 36, 0.6);
  --glass-border: rgba(255, 255, 255, 0.1);

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 24px;

  --font: 'Inter', system-ui, -apple-system, sans-serif;
  --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);

  --sidebar-width: 260px;
  --topbar-height: 64px;

  /* Responsive Typography Scaling */
  --fs-xs: clamp(10px, 2vw, 12px);
  --fs-sm: clamp(12px, 2.5vw, 14px);
  --fs-base: clamp(13px, 3vw, 15px);
  --fs-lg: clamp(14px, 3.5vw, 18px);
  --fs-xl: clamp(16px, 4vw, 20px);
  --fs-2xl: clamp(18px, 4.5vw, 24px);
  --fs-3xl: clamp(22px, 5.5vw, 28px);
  --fs-4xl: clamp(28px, 7vw, 36px);
  --fs-5xl: clamp(36px, 8.5vw, 48px);

  /* Responsive Spacing */
  --space-xs: clamp(4px, 1vw, 8px);
  --space-sm: clamp(8px, 1.5vw, 12px);
  --space-md: clamp(12px, 2vw, 16px);

```
