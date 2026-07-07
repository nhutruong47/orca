# Knowledge Document: THEME_AUDIT.md (Chunk 5/7)

## Metadata
```json
{
  "file_path": "THEME_AUDIT.md",
  "language": "md",
  "module": "orca",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "report",
    "payment",
    "dashboard",
    "production",
    "warehouse",
    "inventory",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, payment, dashboard, production, warehouse, inventory, chat

## Source Code Chunk
```md
| Module | Current | Should Be |
|--------|---------|-----------|
| Inventory | Green palette | `var(--module-inventory)` |
| Production | Orange palette | `var(--module-production)` |
| Warehouse | Teal palette | `var(--module-warehouse)` |
| Attendance | Blue palette | `var(--module-attendance)` |
| Finance | Purple palette | `var(--module-finance)` |
| AI | Gold palette | `var(--module-ai)` |

### 3.3 Inline Styles vs CSS Classes - HIGH

Many components use `style={{}}` with hardcoded values instead of CSS classes:

```tsx
// Problematic
<div style={{ background: '#2D333B', border: '1px solid #515B67' }}>

// Should be
<div className="card">
// or
<div style={{ background: 'var(--layer-4-card)', border: '1px solid var(--border-default)' }}>
```

---

## 4. Light Theme Issues

### 4.1 Incomplete Light Theme Tokens

Only partial light theme defined in `index.css`:

```css
body.theme-light {
  --layer-1-bg:          #F4EFE7;
  --layer-2-sidebar:     #EAE3D6;
  /* Missing: --layer-6-modal, borders, shadows */
}
```

### 4.2 Components Missing Light Theme Support

| Component | Issue |
|-----------|-------|
| GroupDetailPage | Uses `#fff` for cards in light mode |
| AiAssistantPanel | Purple/indigo hardcoded (only looks good in dark) |
| Charts | Dark-mode-only colors |
| Tables | Hardcoded borders |

---

## 5. Theme Switching Issues

### 5.1 Flash on Initial Load

Current implementation may flash wrong theme because:
1. No blocking script in `<head>`
2. Theme applied in React after hydration
3. System preference not respected on first visit

### 5.2 No System Theme Detection

```tsx
// Missing: Detect system preference
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
```

---

## 6. Action Items Summary

| Priority | Item | Estimated Impact |
|----------|------|------------------|
| CRITICAL | Replace all `#fff` text colors with `var(--text-inverse)` | 150+ occurrences |
| CRITICAL | Fix Recharts to use CSS variables | 12 chart components |
| HIGH | Complete light theme token set | 30+ missing tokens |
| HIGH | Add System theme detection | ThemeProvider |
| HIGH | Replace hardcoded hex colors in GroupDetailPage | 50+ occurrences |
| MEDIUM | Replace AiAssistantPanel hardcoded colors | 25+ occurrences |
| MEDIUM | Fix inline styles in Dashboard, Settings | 40+ occurrences |

```
