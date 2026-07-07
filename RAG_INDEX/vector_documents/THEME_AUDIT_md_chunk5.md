# Knowledge Document: THEME_AUDIT.md (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, payment, dashboard, production, warehouse, inventory, chat

## Source Code Chunk
```md
 | Fix Recharts to use CSS variables | 12 chart components |
| HIGH | Complete light theme token set | 30+ missing tokens |
| HIGH | Add System theme detection | ThemeProvider |
| HIGH | Replace hardcoded hex colors in GroupDetailPage | 50+ occurrences |
| MEDIUM | Replace AiAssistantPanel hardcoded colors | 25+ occurrences |
| MEDIUM | Fix inline styles in Dashboard, Settings | 40+ occurrences |
| LOW | Clean up legacy colors in App.css | 15+ occurrences |

---

## 7. Recommended Solution

### Phase 1: Foundation (Day 1)
1. Complete missing light theme tokens
2. Add `var(--text-inverse)` and other missing semantic tokens
3. Implement System theme detection in ThemeProvider
4. Add theme flash prevention

### Phase 2: Core Components (Day 2-3)
1. Create `ThemeAwareChart` wrapper for Recharts
2. Fix GroupDetailPage inline styles
3. Fix AiAssistantPanel inline styles
4. Create unified component library (Button, Card, Badge, etc.)

### Phase 3: Remaining Pages (Day 4-5)
1. Fix all remaining page CSS files
2. Audit and fix module-specific colors
3. Verify all components in light mode

### Phase 4: Testing (Day 6)
1. Test all pages in dark mode
2. Test all pages in light mode
3. Test system theme switching
4. Fix any remaining issues

---

## Appendix: Color Reference Map

### Semantic Tokens (MUST USE)

```css
/* Backgrounds */
--bg-primary:      /* Layer 1 - App background */
--bg-secondary:    /* Layer 2 - Sidebar */
--bg-surface:      /* Layer 3 - Surface */
--bg-card:         /* Layer 4 - Card */
--bg-elevated:     /* Layer 5 - Elevated */
--bg-modal:        /* Layer 6 - Modal */

/* Text */
--text-primary:    /* Main text */
--text-secondary:  /* Secondary text */
--text-muted:      /* Muted text */
--text-disabled:   /* Disabled text */
--text-inverse:    /* Text on colored backgrounds (#fff) */
--text-link:       /* Links */

/* Status */
--color-success:   /* Success state */
--color-warning:   /* Warning state */
--color-danger:    /* Danger state */
--color-info:      /* Info state */

/* Brand */
--color-primary:   /* Primary brand color */
--color-on-primary: /* Text on primary */
```

### Module Accent Tokens

```css
--module-dashboard:    /* Coffee Brown */
--module-inventory:    /* Green */
--module-production:   /* Burnt Orange */
--module-warehouse:    /* Teal */
--module-attendance:   /* Blue */
--module-finance:      /* Purple */

```
