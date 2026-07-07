# Knowledge Document: THEME_REFACTOR_PLAN.md (Chunk 7/7)

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
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, dashboard, admin, production, warehouse, inventory

## Source Code Chunk
```md
pper
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

```
