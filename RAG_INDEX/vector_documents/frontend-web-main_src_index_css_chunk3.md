# Knowledge Document: index.css (Chunk 4/10)

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
  "chunk_index": 3,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
dow-sm: 0 2px 6px rgba(27, 28, 25, 0.04);
  --shadow-md: 0 8px 24px rgba(27, 28, 25, 0.06);
  --shadow-lg: 0 16px 40px rgba(27, 28, 25, 0.08);
  --shadow-glow: 0 0 24px rgba(50, 34, 20, 0.06);

  --bg-glass: rgba(251, 249, 244, 0.6);
  --bg-glass-hover: rgba(251, 249, 244, 0.9);
  --glass-border: rgba(27, 28, 25, 0.06);

  --card-bg: var(--bg-card);
  --border-color: var(--border);

  --shell-bg:
    radial-gradient(circle at top left, rgba(120, 94, 62, 0.08), transparent 34%),
    linear-gradient(135deg, #fbf9f4 0%, #f5f1e9 48%, #ece7dc 100%);
  --shell-content-bg:
    linear-gradient(180deg, rgba(120, 94, 62, 0.035), transparent 260px),
    transparent;
  --shell-sidebar-bg: rgba(255, 252, 248, 0.96);
  --shell-topbar-bg: rgba(255, 252, 248, 0.9);
  --shell-surface: rgba(255, 252, 248, 0.88);
  --shell-surface-soft: rgba(50, 34, 20, 0.04);
  --shell-surface-hover: rgba(50, 34, 20, 0.06);
  --shell-border: rgba(50, 34, 20, 0.11);
  --shell-border-strong: rgba(50, 34, 20, 0.24);
  --shell-text: #1b1c19;
  --shell-text-soft: rgba(67, 52, 42, 0.74);
  --shell-text-muted: rgba(91, 74, 59, 0.58);
  --shell-title: #1b1c19;
  --shell-accent: #735a3a;
  --shell-accent-strong: #322214;
  --shell-accent-soft: rgba(120, 94, 62, 0.12);
  --shell-accent-line: #322214;
  --shell-button-text: #fbf9f4;
  --shell-danger: #b42318;
  --shell-danger-soft: rgba(180, 35, 24, 0.06);
  --shell-avatar-bg: linear-gradient(135deg, #322214 0%, #735a3a 100%);
  --shell-avatar-text: #fbf9f4;
  --shell-shadow: 0 18px 48px rgba(27, 28, 25, 0.08);
  --shell-hover-shadow: 0 22px 56px rgba(27, 28, 25, 0.10), 0 0 0 1px rgba(50, 34, 20, 0.04);
  --shell-profile-overlay: linear-gradient(90deg, rgba(255, 252, 248, 0.96), rgba(255, 252, 248, 0.72));
}

/* ===== Reset & Base ===== */
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  height: 100%;
  width: 100%;
  overflow: hidden;
}

body {
  font-family: var(--font);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#root {
  height: 100%;
}

a {
  text-decoration: none;
  color: inherit;
}

/* ===== Scrollbar ===== */
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--bg-tertiary);

```
