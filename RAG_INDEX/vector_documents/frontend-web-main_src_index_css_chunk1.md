# Knowledge Document: index.css (Chunk 2/10)

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
  "chunk_index": 1,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
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
  --space-lg: clamp(16px, 2.5vw, 24px);
  --space-xl: clamp(24px, 3.5vw, 32px);
  --space-2xl: clamp(32px, 4.5vw, 48px);

  /* Aliases for component CSS */
  --card-bg: var(--bg-card);
  --border-color: var(--border);

  /* Unified app shell tokens */
  --shell-bg:
    radial-gradient(circle at top left, rgba(212, 165, 116, 0.14), transparent 30%),
    radial-gradient(circle at 78% 8%, rgba(139, 94, 60, 0.12), transparent 32%),
    linear-gradient(135deg, #0b0a09 0%, #14110e 48%, #1d1711 100%);
  --shell-content-bg:
    linear-gradient(180deg, rgba(212, 165, 116, 0.055), transparent 240px),
    transparent;
  --shell-sidebar-bg: rgba(12, 11, 10, 0.96);
  --shell-topbar-bg: rgba(18, 16, 14, 0.88);
  --shell-surface: rgba(28, 25, 22, 0.86);
  --shell-surface-soft: rgba(255, 221, 195, 0.052);
  --shell-surface-hover: rgba(212, 165, 116, 0.095);
  --shell-border: rgba(212, 165, 116, 0.16);
  --shell-border-strong: rgba(245, 177, 94, 0.44);
  --shell-text: #eadfd2;
  --shell-text-soft: rgba(226, 205, 184, 0.76);
  --shell-text-muted: rgba(190, 162, 132, 0.66);
  --shell-title: #fff4e8;
  --shell-accent: #d4a574;
  --shell-accent-strong: #b97832;
  --shell-accent-soft: rgba(212, 165, 116, 0.16);
  --shell-accent-line: #f5b15e;
  --shell-button-text: #241204;
  --shell-danger: #ffb4ab;
  --shell-danger-soft: rgba(255, 180, 171, 0.07);
  --shell-avatar-bg: linear-gradient(135deg, #f5c284 0%, #c7772d 100%);
  --shell-avatar-text: #241204;
  --shell-shadow: 0 18px 48px rgba(0, 0, 0, 0.24);
  --shell-hover-shadow: 0 22px 56px rgba(0, 0, 0, 0.28), 0 0 0 1px rgba(212, 165, 116, 0.14);
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

```
