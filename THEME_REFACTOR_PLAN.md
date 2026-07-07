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

/* Status with soft backgrounds */
--success:         var(--green-500);
--success-soft:    rgba(92, 184, 92, 0.14);
--success-line:    rgba(92, 184, 92, 0.40);

--warning:         #E2B65C;
--warning-soft:     rgba(226, 182, 92, 0.14);
--warning-line:     rgba(226, 182, 92, 0.40);

--danger:          var(--red-500);
--danger-soft:      rgba(230, 90, 90, 0.14);
--danger-line:     rgba(230, 90, 90, 0.40);

--info:            var(--blue-500);
--info-soft:       rgba(91, 141, 239, 0.14);
--info-line:       rgba(91, 141, 239, 0.40);

/* Brand */
--brand:           var(--coffee-500);
--brand-hover:     var(--coffee-600);
--brand-active:    var(--coffee-700);
--brand-soft:      rgba(164, 117, 81, 0.14);
--brand-line:      rgba(164, 117, 81, 0.40);
--brand-on:        #FFFFFF;        /* Text on brand color */

/* Module Accents */
--module-dashboard:   var(--coffee-500);
--module-inventory:   var(--green-500);
--module-production:  var(--orange-500);
--module-warehouse:   var(--teal-500);
--module-attendance:  var(--blue-500);
--module-finance:     var(--purple-500);
--module-ai:         var(--gold-500);
--module-reports:     var(--indigo-500);

/* Module soft variants */
--module-dashboard-soft:   rgba(164, 117, 81, 0.14);
--module-inventory-soft:   rgba(92, 184, 92, 0.14);
--module-production-soft:  rgba(217, 130, 43, 0.14);
--module-warehouse-soft:   rgba(41, 182, 182, 0.14);
--module-attendance-soft:  rgba(91, 141, 239, 0.14);
--module-finance-soft:    rgba(139, 124, 246, 0.14);
--module-ai-soft:        rgba(216, 166, 78, 0.14);
--module-reports-soft:    rgba(99, 116, 243, 0.14);

/* Typography */
--font-sans:  'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
--font-mono:  'JetBrains Mono', 'SF Mono', Menlo, monospace;

--fs-xs:    11px;
--fs-sm:    12px;
--fs-base:  13px;
--fs-md:    14px;
--fs-lg:    16px;
--fs-xl:    20px;
--fs-2xl:   24px;
--fs-3xl:   32px;

/* Spacing */
--s-1:  4px;
--s-2:  8px;
--s-3:  12px;
--s-4:  16px;
--s-5:  20px;
--s-6:  24px;
--s-7:  32px;
--s-8:  40px;

/* Border Radius */
--r-sm:    6px;
--r-md:    8px;
--r-lg:    14px;
--r-xl:    18px;
--r-2xl:   22px;
--r-full:  999px;

/* Shadows */
--shadow-xs:  0 1px 2px rgba(0, 0, 0, 0.20);
--shadow-sm:  0 2px 8px rgba(0, 0, 0, 0.32);
--shadow-md:  0 8px 24px rgba(0, 0, 0, 0.44);
--shadow-lg:  0 16px 40px rgba(0, 0, 0, 0.58);
--shadow-ring-focus: 0 0 0 3px rgba(164, 117, 81, 0.32);

/* Transitions */
--t-fast:   140ms;
--t-base:   200ms;
--t-slow:   320ms;
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
```

---

## 2. ThemeProvider Implementation

### 2.1 Enhanced ThemeProvider with System Support

```typescript
// src/context/ThemeProvider.tsx
import { createContext, useContext, useState, useEffect, useLayoutEffect, type ReactNode } from 'react';

type Theme = 'dark' | 'light' | 'system';

interface ThemeContextType {
    theme: Theme;
    resolvedTheme: 'dark' | 'light';
    toggleTheme: () => void;
    setTheme: (theme: Theme) => void;
}

const ThemeContext = createContext<ThemeContextType>({
    theme: 'system',
    resolvedTheme: 'dark',
    toggleTheme: () => {},
    setTheme: () => {},
});

export function ThemeProvider({ children }: { children: ReactNode }) {
    const [theme, setThemeState] = useState<Theme>(() => {
        const saved = localStorage.getItem('orca-theme');
        return (saved === 'light' || saved === 'dark' || saved === 'system') 
            ? saved 
            : 'system';
    });

    const [resolvedTheme, setResolvedTheme] = useState<'dark' | 'light'>(() => {
        if (typeof window === 'undefined') return 'dark';
        const saved = localStorage.getItem('orca-theme');
        if (saved === 'light') return 'light';
        if (saved === 'dark') return 'dark';
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    });

    // Update resolved theme when theme or system preference changes
    useEffect(() => {
        const updateResolvedTheme = () => {
            if (theme === 'system') {
                const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                setResolvedTheme(prefersDark ? 'dark' : 'light');
            } else {
                setResolvedTheme(theme);
            }
        };

        updateResolvedTheme();

        // Listen for system theme changes
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        const handler = () => {
            if (theme === 'system') {
                updateResolvedTheme();
            }
        };
        mediaQuery.addEventListener('change', handler);
        return () => mediaQuery.removeEventListener('change', handler);
    }, [theme]);

    // Apply theme to DOM
    useLayoutEffect(() => {
        localStorage.setItem('orca-theme', theme);
        
        const actualTheme = resolvedTheme;
        
        document.body.classList.remove('theme-dark', 'theme-light');
        document.documentElement.classList.remove('theme-dark', 'theme-light');
        document.body.classList.add(`theme-${actualTheme}`);
        document.documentElement.classList.add(`theme-${actualTheme}`);
        document.documentElement.setAttribute('data-theme', actualTheme);
        
        // Set color-scheme for native elements
        document.documentElement.style.colorScheme = actualTheme;
    }, [resolvedTheme, theme]);

    const toggleTheme = () => {
        setThemeState(prev => {
            if (prev === 'dark') return 'light';
            if (prev === 'light') return 'system';
            return 'dark';
        });
    };

    const setTheme = (newTheme: Theme) => {
        setThemeState(newTheme);
    };

    return (
        <ThemeContext.Provider value={{ theme, resolvedTheme, toggleTheme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

export const useTheme = () => useContext(ThemeContext);
```

---

## 3. Complete Light Theme

```css
/* ============================================
   LIGHT THEME - Complete Implementation
   ============================================ */
body.theme-light {
    /* 7-Layer Visual Depth - Light variants */
    --layer-1-bg:           #FAFAFA;
    --layer-2-sidebar:      #F0F0F0;
    --layer-3-surface:      #FFFFFF;
    --layer-4-card:         #FFFFFF;
    --layer-5-elevated:     #F8F9FA;
    --layer-6-modal:        #FFFFFF;
    --layer-7-hover:        #F0F2F5;
    
    /* Borders */
    --border-subtle:        #E5E7EB;
    --border-default:       #D1D5DB;
    --border-strong:        #9CA3AF;
    --border-focus:         var(--coffee-500);
    
    /* Text - Dark for light background */
    --text-primary:         #1F2937;
    --text-secondary:       #4B5563;
    --text-muted:          #9CA3AF;
    --text-disabled:       #D1D5DB;
    --text-placeholder:    #9CA3AF;
    --text-inverse:        #FFFFFF;
    --text-link:           #2563EB;
    
    /* Shadows - Softer for light */
    --shadow-xs:  0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-sm:  0 2px 4px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
    --shadow-md:  0 4px 12px rgba(0, 0, 0, 0.08);
    --shadow-lg:  0 8px 24px rgba(0, 0, 0, 0.12);
    --shadow-ring-focus: 0 0 0 3px rgba(164, 117, 81, 0.25);
    
    /* Brand - Darker for contrast */
    --brand:              var(--coffee-700);
    --brand-hover:        var(--coffee-800);
    --brand-active:       var(--coffee-900);
    --brand-light:        var(--coffee-500);
    --brand-tint:         var(--coffee-100);
    --brand-soft:         rgba(123, 90, 61, 0.12);
    --brand-softer:       rgba(123, 90, 61, 0.06);
    --brand-line:         rgba(123, 90, 61, 0.35);
    --brand-on:           #FFFFFF;
    
    /* Background aliases */
    --bg-primary:         #FAFAFA;
    --bg-secondary:       #F0F0F0;
    --bg-surface:         #FFFFFF;
    --bg-card:            #FFFFFF;
    --bg-elevated:        #F8F9FA;
    --bg-modal:           #FFFFFF;
    --bg-input:           #F3F4F6;
    
    /* Status - Keep saturation high for visibility */
    --status-success:     #059669;
    --status-success-soft: rgba(5, 150, 105, 0.10);
    --status-warning:      #D97706;
    --status-warning-soft: rgba(217, 119, 6, 0.10);
    --status-danger:       #DC2626;
    --status-danger-soft: rgba(220, 38, 38, 0.10);
    --status-info:         #2563EB;
    --status-info-soft:    rgba(37, 99, 235, 0.10);
    
    /* Module accents - Soft variants for light */
    --module-dashboard-soft:  rgba(123, 90, 61, 0.08);
    --module-inventory-soft:  rgba(5, 150, 105, 0.08);
    --module-production-soft: rgba(217, 119, 6, 0.08);
    --module-warehouse-soft:  rgba(6, 182, 182, 0.08);
    --module-attendance-soft: rgba(37, 99, 235, 0.08);
    --module-finance-soft:   rgba(139, 92, 246, 0.08);
    --module-ai-soft:        rgba(217, 164, 78, 0.08);
    --module-reports-soft:    rgba(99, 102, 243, 0.08);
}
```

---

## 4. Migration Tasks

### 4.1 Priority 1: Critical Replacements

| File | Pattern | Replacement | Count |
|------|---------|------------|-------|
| GroupDetailPage.tsx | `#fff` | `var(--text-inverse)` | 15 |
| GroupDetailPage.tsx | `#16a34a` | `var(--status-success)` | 4 |
| GroupDetailPage.tsx | `#d4a574` | `var(--brand)` | 8 |
| AiAssistantPanel.tsx | `rgba(99,102,241,*)` | `var(--module-ai-soft)` | 12 |
| AiAssistantPanel.tsx | `#818cf8` | `var(--module-ai)` | 5 |
| AiAssistantPanel.tsx | `#a5b4fc` | `var(--module-ai)` | 1 |

### 4.2 Priority 2: Component Refactoring

1. **ThemeAwareChart** - Recharts wrapper
2. **UnifiedButton** - Single button component
3. **UnifiedCard** - Single card component
4. **UnifiedBadge** - Single badge component
5. **StatusBadge** - Auto-colored status badges

### 4.3 Priority 3: Page-Level Fixes

| Page | Issues | Effort |
|------|--------|--------|
| DashboardPage | Gradient colors | 2h |
| SettingsPage | Light theme colors | 3h |
| AdminPage | Inline styles | 4h |
| InventoryPage | Module colors | 2h |
| ProductionOrderPage | Status colors | 2h |

---

## 5. Testing Checklist

- [ ] Dark mode: All pages render correctly
- [ ] Light mode: All pages render correctly
- [ ] System theme: Respects OS preference
- [ ] Theme toggle: Instant switch, no flash
- [ ] Charts: Colors adapt to theme
- [ ] Icons: All visible and correct color
- [ ] Text contrast: WCAG AA compliant
- [ ] Input focus: Ring visible in both themes
- [ ] Buttons: All states work in both themes
- [ ] Cards: Hover effects in both themes
- [ ] Tables: Borders and text visible
- [ ] Modals: Backdrop and content visible

---

## 6. Rollout Plan

### Day 1: Foundation
- [ ] Complete token system in index.css
- [ ] Update ThemeProvider with system support
- [ ] Complete light theme
- [ ] Add theme flash prevention script

### Day 2: Core Components
- [ ] Create ThemeAwareChart wrapper
- [ ] Fix GroupDetailPage.tsx
- [ ] Fix AiAssistantPanel.tsx

### Day 3: Remaining Pages
- [ ] Fix DashboardPage
- [ ] Fix SettingsPage
- [ ] Fix AdminPage
- [ ] Fix remaining pages

### Day 4: Polish
- [ ] Create unified component library
- [ ] Add missing tokens
- [ ] Test all pages
- [ ] Fix any issues

---

## 7. Quick Reference: Token Usage

```typescript
// Text on colored backgrounds
style={{ color: 'var(--text-inverse)' }}

// Primary button
className="btn btn-primary"

// Card
className="card"

// Status badge
className="badge badge-success"

// Custom background
style={{ background: 'var(--bg-card)' }}

// Custom border
style={{ borderColor: 'var(--border-default)' }}

// Priority colors
// High: var(--status-danger)
// Medium: var(--status-warning)
// Low: var(--status-success)
```
