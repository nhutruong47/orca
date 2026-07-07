# ORCA Platform - Testing Checklist

**Date:** July 7, 2026
**Status:** READY FOR TESTING

---

## Overview

This document provides a comprehensive testing checklist for verifying the theme system and RAG architecture standardization.

---

## 1. Theme System Testing

### 1.1 Dark Mode Testing

| Test | Page | Expected Result | Status |
|------|------|----------------|--------|
| Background colors | All | `--layer-1-bg: #18191C` | ☐ |
| Sidebar | All | `--layer-2-sidebar: #1F2328` | ☐ |
| Card background | All | `--layer-4-card: #2D333B` | ☐ |
| Modal background | All | `--layer-6-modal: #3F4852` | ☐ |
| Text primary | All | `#F5F7FA` | ☐ |
| Text secondary | All | `#D2D7DE` | ☐ |
| Brand color | All | `#A47551` | ☐ |
| Status success | All | `#5CB85C` | ☐ |
| Status danger | All | `#E65A5A` | ☐ |
| Status warning | All | `#E2B65C` | ☐ |

### 1.2 Light Mode Testing

| Test | Page | Expected Result | Status |
|------|------|----------------|--------|
| Background colors | All | `--layer-1-bg: #FAFAFA` | ☐ |
| Sidebar | All | `--layer-2-sidebar: #F0F0F0` | ☐ |
| Card background | All | `--layer-4-card: #FFFFFF` | ☐ |
| Modal background | All | `--layer-6-modal: #FFFFFF` | ☐ |
| Text primary | All | `#1F2937` | ☐ |
| Text secondary | All | `#4B5563` | ☐ |
| Brand color | All | `#7B5A3D` | ☐ |
| Status success | All | `#059669` | ☐ |
| Status danger | All | `#DC2626` | ☐ |
| Status warning | All | `#D97706` | ☐ |

### 1.3 System Theme Testing

| Test | Scenario | Expected Result | Status |
|------|----------|----------------|--------|
| Initial load (dark system) | No saved preference | Dark theme applied | ☐ |
| Initial load (light system) | No saved preference | Light theme applied | ☐ |
| System switch (dark→light) | While app running | Theme updates immediately | ☐ |
| System switch (light→dark) | While app running | Theme updates immediately | ☐ |
| User override preserved | After system change | User preference maintained | ☐ |

### 1.4 Theme Flash Prevention

| Test | Expected Result | Status |
|------|----------------|--------|
| Initial page load | No flash of wrong theme | ☐ |
| Hard refresh (Ctrl+F5) | No flash | ☐ |
| Direct URL navigation | No flash | ☐ |

### 1.5 Theme Toggle

| Test | Action | Expected Result | Status |
|------|--------|----------------|--------|
| Dark → Light | Toggle button | Instant switch | ☐ |
| Light → System | Toggle button | System theme applied | ☐ |
| System → Dark | Toggle button | Dark theme applied | ☐ |
| Theme persisted | Close browser | Theme saved in localStorage | ☐ |

### 1.6 Component Testing

#### Buttons
| Test | State | Expected | Status |
|------|-------|----------|--------|
| Primary button | Default (dark) | `var(--brand)` bg, white text | ☐ |
| Primary button | Hover | Slight lift, darker shade | ☐ |
| Primary button | Active | Pressed effect | ☐ |
| Primary button | Light mode | Darker brand, white text | ☐ |
| Danger button | Dark mode | Red bg, white text | ☐ |
| Danger button | Light mode | Darker red, white text | ☐ |

#### Cards
| Test | Expected | Status |
|------|----------|--------|
| Card hover effect | Lift + shadow increase | ☐ |
| Card border | Subtle border visible | ☐ |
| Elevated card | Higher contrast | ☐ |

#### Status Badges
| Test | Expected | Status |
|------|----------|--------|
| Success badge | Green soft bg, dark green text | ☐ |
| Warning badge | Yellow soft bg, dark yellow text | ☐ |
| Danger badge | Red soft bg, dark red text | ☐ |
| Light mode badges | Adjusted for light bg | ☐ |

#### Forms
| Test | Expected | Status |
|------|----------|--------|
| Input focus | Brand color ring | ☐ |
| Input focus | Light mode ring | ☐ |
| Input disabled | Reduced opacity | ☐ |
| Select dropdown | Native dropdown | ☐ |

---

## 2. RAG System Testing

### 2.1 Knowledge Indexing

| Test | Expected Result | Status |
|------|----------------|--------|
| Index single document | Vector stored | ☐ |
| Index batch documents | All vectors stored | ☐ |
| Delete document | Vector removed | ☐ |
| Reindex source | Old vectors replaced | ☐ |

### 2.2 Retrieval

| Test | Query | Expected Result | Status |
|------|-------|----------------|--------|
| Exact match | Known product name | Relevant doc returned | ☐ |
| Semantic match | Synonym query | Relevant doc returned | ☐ |
| No match | Unknown topic | Empty results | ☐ |
| Source filter | Filter by inventory | Only inventory docs | ☐ |

### 2.3 Response Format

| Test | Field | Expected | Status |
|------|-------|----------|--------|
| Answer field | Response | Non-empty string | ☐ |
| Reasoning summary | Analysis | Non-empty string | ☐ |
| Confidence score | 0-1 | Valid number | ☐ |
| Confidence level | high/medium/low | Valid enum | ☐ |
| Sources | Citations | Array with relevance | ☐ |
| Suggestions | Actions | Array with type | ☐ |

### 2.4 Hallucination Prevention

| Test | Input | Expected Result | Status |
|------|-------|----------------|--------|
| Unknown query | Random nonsense | Low confidence | ☐ |
| Out of domain | Politics, sports | "Cannot find" response | ☐ |
| Partial match | Vague query | Partial answer | ☐ |

### 2.5 Prompt Injection Prevention

| Test | Input | Expected Result | Status |
|------|-------|----------------|--------|
| Injection attempt | "Ignore instructions..." | Filtered/rejected | ☐ |
| Code injection | "```system" | Filtered | ☐ |
| Role play | "You are now..." | Filtered | ☐ |

---

## 3. Page-by-Page Testing

### 3.1 Core Pages

| Page | Dark Mode | Light Mode | Charts | Theme Toggle |
|------|----------|-----------|--------|-------------|
| Dashboard | ☐ | ☐ | ☐ | ☐ |
| Group Detail | ☐ | ☐ | ☐ | ☐ |
| Inventory | ☐ | ☐ | ☐ | ☐ |
| Production Orders | ☐ | ☐ | ☐ | ☐ |
| Settings | ☐ | ☐ | ☐ | ☐ |
| Admin | ☐ | ☐ | ☐ | ☐ |
| Profile | ☐ | ☐ | ☐ | ☐ |

### 3.2 AI Features

| Feature | Dark Mode | Light Mode | Citations | Confidence |
|---------|-----------|-----------|-----------|------------|
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
- [ ] Status badges visible in both themes
- [ ] Text readable in both themes
- [ ] Focus states visible in both themes

---

## 8. Known Issues

| Issue | Severity | Status | Notes |
|-------|----------|--------|-------|
| SettingsPage hardcoded colors | Medium | Pending | CSS file needs refactor |
| GroupDetailPage inline styles | Medium | Pending | Major refactor needed |
| Charts theme adaptation | Low | Design system ready | Component wrapper created |
| Recharts hardcoded colors | Medium | Design system ready | ThemeAwareChart created |

---

## 9. Test Results Summary

```
Total Tests: ____
Passed: ____
Failed: ____
Blocked: ____

Date: ________________
Tester: ________________
```
