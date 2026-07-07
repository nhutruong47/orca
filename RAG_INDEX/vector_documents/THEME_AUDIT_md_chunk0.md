# Knowledge Document: THEME_AUDIT.md (Chunk 1/7)

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
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, payment, dashboard, production, warehouse, inventory, chat

## Source Code Chunk
```md
# ORCA Platform - Theme Audit Report

**Date:** July 7, 2026
**Auditor:** Lead Software Architect
**Status:** IN PROGRESS

---

## Executive Summary

The ORCA platform has a **foundation** for a unified theme system via CSS variables in `index.css`, but suffers from **severe inconsistency** due to:

1. Hardcoded hex colors in TSX inline styles
2. Inconsistent theme application (some components only support dark mode)
3. Mixed color references (CSS variables + hardcoded values in same component)
4. Module-specific color palettes that don't adapt to theme
5. No System theme detection
6. Theme flashing on initial load
7. Recharts/visualization components ignoring dark mode

---

## 1. CSS Variable System (index.css)

### ✓ Existing Good Practices

```css
/* 7-Layer Visual Depth */
--layer-1-bg:           #18191C;  /* L1 - Application Background */
--layer-2-sidebar:      #1F2328;  /* L2 - Sidebar */
--layer-3-surface:      #252A31;  /* L3 - Main Content */
--layer-4-card:         #2D333B;  /* L4 - Card */
--layer-5-elevated:     #353C45;  /* L5 - Elevated Card */
--layer-6-modal:        #3F4852;  /* L6 - Modal */
--layer-7-hover:        #464F5A;  /* L7 - Hover */

/* Semantic Tokens */
--text-primary:         #F5F7FA;
--text-secondary:      #D2D7DE;
--status-success:      #5CB85C;
--status-danger:       #E65A5A;
```

### ✗ Missing Tokens

```css
/* MISSING - Need to add */
--color-bg-inverse:     /* For inverted backgrounds */
--color-surface-tinted:  /* Tinted surface variant */
--color-overlay-light:   /* Light overlay */
--color-overlay-dark:    /* Dark overlay */

/* Semantic aliases missing */
--color-primary:         /* Should map to --brand */
--color-secondary:       /* Should map to --module-ai (gold) */
```

---

## 2. Hardcoded Colors Found

### 2.1 GroupDetailPage.tsx (CRITICAL)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 482 | `#fff` | Text on colored backgrounds | `var(--text-inverse)` |
| 756 | `#fff` | Avatar initials | `var(--text-inverse)` |
| 863 | `#fff7ed`, `#fed7aa` | Unread badge colors | `var(--module-ai-soft)`, `var(--brand-line)` |
| 875 | `#f9f1e3`, `#f8fafc`, `#fff7ed`, `#f0fdf4` | Stat card backgrounds | `var(--layer-4-card)` |
| 898-904 | `#d4a574`, `#fff`, `#64748b` | Filter buttons | `var(--brand)`, `var(--text-inverse)`, `var(--text-muted)` |

```
