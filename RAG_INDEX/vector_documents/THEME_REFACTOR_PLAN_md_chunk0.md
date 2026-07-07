# Knowledge Document: THEME_REFACTOR_PLAN.md (Chunk 1/7)

## Metadata
```json
{
  "file_path": "THEME_REFACTOR_PLAN.md",
  "language": "md",
  "module": "orca",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "report",
    "dashboard",
    "admin",
    "production",
    "warehouse",
    "inventory"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, dashboard, admin, production, warehouse, inventory

## Source Code Chunk
```md
# ORCA Platform - Theme Refactoring Plan

**Date:** July 7, 2026
**Status:** READY FOR IMPLEMENTATION

---

## Overview

This plan details the complete refactoring of the ORCA platform theme system, replacing all hardcoded colors with a centralized Design Token System.

---

## 1. Design Token System

### 1.1 Token Hierarchy

```
CSS Variables (index.css)
    │
    ├── Primitive Tokens (raw values)
    │   ├── Colors
    │   ├── Typography
    │   ├── Spacing
    │   └── Shadows
    │
    ├── Semantic Tokens (meaning)
    │   ├── Background
    │   ├── Surface
    │   ├── Text
    │   └── Status
    │
    └── Component Tokens (specific)
        ├── Button
        ├── Card
        └── Input
```

### 1.2 Complete Token Set

```css
/* ============================================
   ORCA Design Token System v4.0
   ============================================ */

/* --- Primitive Tokens --- */

/* Coffee Brown Scale */
--coffee-50:  #F5E7DA;
--coffee-100: #E8D2BC;
--coffee-200: #D4B695;
--coffee-300: #C99A73;
--coffee-400: #B58661;
--coffee-500: #A47551;  /* Primary */
--coffee-600: #8D6747;  /* Hover */
--coffee-700: #7B5A3D;  /* Active */
--coffee-800: #5E4530;
--coffee-900: #3F2E20;

/* Status Scale */
--green-50:   #ECF7EE;
--green-100:  #D5EFD9;
--green-500:  #5CB85C;
--green-600:  #4A9D4A;

--red-50:     #FCEBEB;
--red-100:    #F8D2D2;
--red-500:    #E65A5A;
--red-600:    #CB4444;

--blue-50:    #ECF2FE;
--blue-500:   #5B8DEF;

--gold-500:   #D8A64E;

/* --- Semantic Tokens --- */

/* Backgrounds */
--bg-primary:       var(--layer-1-bg);
--bg-secondary:     var(--layer-2-sidebar);
--bg-surface:       var(--layer-3-surface);
--bg-card:          var(--layer-4-card);
--bg-elevated:      var(--layer-5-elevated);
--bg-modal:         var(--layer-6-modal);
--bg-input:         var(--layer-5-elevated);

/* Text - CRITICAL: --text-inverse for white text */
--text-primary:     #F5F7FA;
--text-secondary:   #D2D7DE;
--text-muted:       #A5ADB8;
--text-disabled:    #777F89;
--text-placeholder: #8D95A1;
--text-inverse:     #FFFFFF;        /* For text on colored backgrounds */
--text-link:        #7FB5FF;

/* Borders */
--border-subtle:    #3A4048;
--border-default:   #515B67;
--border-strong:    #5B6672;

/* Status Colors */
--color-success:    var(--green-500);
--color-warning:    #E2B65C;
--color-danger:     var(--red-500);
--color-info:       var(--blue-500);


```
