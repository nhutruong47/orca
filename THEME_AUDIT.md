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
| 915 | `#fff` | Card background | `var(--layer-4-card)` |
| 917 | `#fff` | Avatar | `var(--text-inverse)` |
| 922 | `#16a34a`, `#94a3b8` | Progress percentage | `var(--success)`, `var(--text-disabled)` |
| 975 | `#16a34a` | Progress bar complete | `var(--status-success)` |
| 1096 | `#fffaf3`, `#fff` | Modal gradient | `var(--layer-6-modal)` |
| 1170-1201 | `#d4a574`, `#fff`, `#f1f5f9`, `#64748b` | Task filter buttons | Semantic tokens |
| 1344 | `#d4a574` | Progress color | `var(--brand)` |
| 1424 | `#f5e6d3`, `#f9f1e3`, `#f0fdf4`, `#a0673c`, `#c9884a`, `#16a34a` | Priority badges | Semantic tokens |
| 1526 | `#d4a574`, `#94a3b8` | Table headers | `var(--brand)`, `var(--text-muted)` |
| 1537 | `#16a34a`, `#dcfce7`, `#d97706`, `#fef3c7` | Status badges | Semantic tokens |
| 1563-1564 | `#d4a574`, `#fff` | Input/button | `var(--brand)`, `var(--text-inverse)` |
| 1624 | `#d4a574`, `#fff`, `#e4e6eb`, `#050505` | Chat tabs | Semantic tokens |

### 2.2 AiAssistantPanel.tsx (HIGH)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 115-117 | `rgba(99,102,241,0.05)` | Panel background | `var(--module-ai-soft)` |
| 145 | `rgba(99,102,241,0.15)`, `#818cf8` | Icon container | `var(--module-ai-soft)`, `var(--module-ai)` |
| 157 | `rgba(99,102,241,0.18)`, `#a5b4fc` | Token button | Semantic tokens |
| 162 | `rgba(34,197,94,0.1)` | Trial active | `var(--status-success-soft)` |
| 170 | `rgba(124,92,255,0.16)`, `#a78bfa` | Upgrade link | `var(--module-finance-soft)`, `var(--module-finance)` |
| 225 | `rgba(99,102,241,0.2)` | User message bubble | `var(--module-ai-soft)` |
| 226 | `rgba(99,102,241,0.4)` | User message border | `var(--module-ai-line)` |
| 244-246 | `rgba(0,0,0,0.2)`, `rgba(99,102,241,0.2)` | Result container | Semantic tokens |
| 251 | `rgba(99,102,241,0.15)`, `#818cf8` | Source badge | Semantic tokens |
| 255 | `rgba(255, 193, 7, 0.1)` | Warning badge | `var(--status-warning-soft)` |
| 268 | `#60a5fa` | Quantity text | `var(--status-info)` |
| 272 | `#f87171` | Deadline text | `var(--status-danger)` |
| 286 | `rgba(99,102,241,0.2)`, `#818cf8` | Create goal button | Semantic tokens |
| 327-328 | `rgba(0,0,0,0.2)`, `rgba(99,102,241,0.3)` | Input background | Semantic tokens |

### 2.3 DashboardPage.css (MEDIUM)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 239 | `linear-gradient(90deg, #8b5e3c, #f5b15e)` | Chart gradient | CSS variable gradient |
| 463, 475, 484, 489 | `#d4a574`, `#f5b15e`, `#c28a52` | Various text | `var(--brand)`, semantic tokens |
| 643 | `#fff` | Button text | `var(--text-inverse)` |

### 2.4 App.css (MEDIUM)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 92 | `#6f4e37` | Old brand color | `var(--brand)` |
| 220 | `#8b949e` | Text muted | `var(--text-muted)` |
| 262, 292 | `#d4a574`, `#f5c58b` | Accent text | `var(--brand)` |
| 325-326 | `#20140c` | Borders | `var(--brand-active)` |
| 332-333 | `linear-gradient(135deg, #d8a66f, #a87540)`, `#d8a66f` | Old gradients | `var(--brand-gradient)` |
| 367 | `#f6dcc0` | Text accent | `var(--text-accent)` |
| 378-379 | `#211813`, `#f6dcc0` | Old dark bg | `var(--layer-1-bg)`, `var(--text-primary)` |

### 2.5 SettingsPage.css (MEDIUM)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 2-7 | `#f7f3ed`, `#fffdf9`, `#22170f`, etc. | Light theme hardcoded | Light theme CSS variables |
| 79, 96, 128 | `#ffe0bf`, `#8b5a2b`, `#c0b3a9` | Various text | Semantic tokens |
| 231 | `#f3eee7` | Background | `var(--layer-3-surface)` |
| 253 | `#2fb565` | Success | `var(--status-success)` |
| 270-271 | `#3a2414`, `#fff2e6` | Button | `var(--brand)`, `var(--text-inverse)` |
| 318 | `#f3c795` | Button hover | `var(--brand-hover)` |
| 361 | `#fbf7f1` | Card background | `var(--layer-4-card)` |
| 402, 406 | `linear-gradient(135deg, #1a1a2e, #16213e)`, `linear-gradient(135deg, #f0c27f, #e5b376)` | Auth page | Theme-aware gradients |

### 2.6 Profile.css (MEDIUM)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 34 | `#fff` | Avatar initials | `var(--text-inverse)` |
| 194 | `#000` | Avatar background | Semantic token |
| 241, 247 | `#86efac`, `#fca5a5` | Status indicators | `var(--status-success)`, `var(--status-danger)` |

### 2.7 VnpayMockCheckoutPage.css (MEDIUM)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 19-31 | `#1459c8`, `#0b3d90`, `#ffea00`, `#ed1c24` | Payment branding | Payment-specific tokens |
| 78, 190, 198, 205, etc. | `#fff`, `#ed1c24` | Various | Semantic tokens |

### 2.8 UpgradePlanPage.css (LOW)

| Line | Color | Issue | Should Use |
|------|-------|-------|------------|
| 114, 184 | `#fff` | Text on colored bg | `var(--text-inverse)` |

---

## 3. Component-Level Theme Issues

### 3.1 Recharts (Charts) - CRITICAL

Charts do NOT respond to theme changes. The following need theme-aware colors:

```tsx
// Current (broken)
<LineChart data={data}>
  <Line type="monotone" dataKey="value" stroke="#A47551" />
  <Line type="monotone" dataKey="value2" stroke="#5CB85C" />
</LineChart>

// Should be
<LineChart data={data}>
  <Line type="monotone" dataKey="value" stroke="var(--brand)" />
  <Line type="monotone" dataKey="value2" stroke="var(--status-success)" />
</LineChart>
```

### 3.2 Module-Specific Colors - HIGH

Each module has hardcoded accent colors that don't adapt:

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
--module-ai:          /* Gold */
--module-reports:     /* Indigo */
```
