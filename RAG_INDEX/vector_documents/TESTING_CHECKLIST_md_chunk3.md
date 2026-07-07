# Knowledge Document: TESTING_CHECKLIST.md (Chunk 4/5)

## Metadata
```json
{
  "file_path": "TESTING_CHECKLIST.md",
  "language": "md",
  "module": "orca",
  "business_domain": "admin",
  "tags": [
    "admin",
    "inventory",
    "production",
    "dashboard"
  ],
  "logical_type": "Generic",
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, production, dashboard

## Source Code Chunk
```md
-------|
| AI Assistant Panel | ☐ | ☐ | ☐ | ☐ |
| AI Plan Generation | ☐ | ☐ | ☐ | ☐ |
| AI Task Suggestions | ☐ | ☐ | ☐ | ☐ |

### 3.3 Responsive Testing

| Breakpoint | Width | Sidebar | Content | Status |
|------------|-------|---------|---------|--------|
| Mobile | < 480px | Hidden | Full width | ☐ |
| Tablet | < 768px | Hidden | Adjusted | ☐ |
| Desktop | < 1024px | Collapsed | Normal | ☐ |
| Large | < 1280px | Normal | Normal | ☐ |

---

## 4. Accessibility Testing

### 4.1 Color Contrast

| Element | Ratio | WCAG AA | WCAG AAA | Status |
|---------|-------|---------|----------|--------|
| Text on dark bg | > 4.5:1 | ✓ | - | ☐ |
| Text on light bg | > 4.5:1 | ✓ | - | ☐ |
| Large text | > 3:1 | ✓ | - | ☐ |
| UI components | > 3:1 | ✓ | - | ☐ |

### 4.2 Focus States

| Element | Focus Visible | Focus Ring | Status |
|---------|--------------|------------|--------|
| Buttons | ✓ | Brand ring | ☐ |
| Inputs | ✓ | Brand ring | ☐ |
| Links | ✓ | Brand ring | ☐ |
| Tabs | ✓ | Ring | ☐ |

---

## 5. Performance Testing

### 5.1 Theme Switching

| Metric | Target | Status |
|--------|--------|--------|
| Theme switch time | < 100ms | ☐ |
| No layout shift | 0px | ☐ |
| No FOUC | No flash | ☐ |

### 5.2 RAG Performance

| Metric | Target | Status |
|--------|--------|--------|
| Embedding time | < 500ms | ☐ |
| Retrieval time | < 200ms | ☐ |
| Total query time | < 2s | ☐ |

---

## 6. Cross-Browser Testing

| Browser | Version | Dark Mode | Light Mode | Status |
|---------|---------|----------|-----------|--------|
| Chrome | Latest | ✓ | ✓ | ☐ |
| Firefox | Latest | ✓ | ✓ | ☐ |
| Safari | Latest | ✓ | ✓ | ☐ |
| Edge | Latest | ✓ | ✓ | ☐ |

---

## 7. Test Execution Guide

### 7.1 Quick Smoke Test

1. Open app in dark mode
2. Toggle to light mode - verify instant switch
3. Toggle to system - verify follows OS
4. Navigate to Dashboard - verify no broken styles
5. Open AI panel - verify theme-consistent styling

### 7.2 Full Regression Test

1. Complete all checkboxes in sections 1-5
2. Document any failures
3. Create tickets for issues found
4. Re-test after fixes

### 7.3 Pre-Release Checklist

- [ ] All dark mode tests pass
- [ ] All light mode tests pass
- [ ] System theme detection works
- [ ] No theme flash on load
- [ ] All components use CSS variables
- [ ] No hardcoded colors in components
- [ ] Charts adapt to theme

```
