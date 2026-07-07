# ORCA Platform - Component Standardization

**Date:** July 7, 2026
**Status:** IN PROGRESS

---

## Overview

This document defines the standardized component system for ORCA, ensuring consistency across all UI elements.

---

## 1. Button System

### 1.1 Button Variants

```tsx
// Primary - Brand color
<button className="btn btn-primary">Action</button>

// Secondary - Elevated background
<button className="btn btn-secondary">Action</button>

// Ghost - Transparent with hover
<button className="btn btn-ghost">Action</button>

// Danger - Error/delete actions
<button className="btn btn-danger">Delete</button>

// AI - Gold accent for AI features
<button className="btn btn-ai">AI Action</button>
```

### 1.2 Button Sizes

```tsx
<button className="btn btn-sm">Small</button>
<button className="btn">Default</button>
<button className="btn btn-lg">Large</button>
<button className="btn btn-icon">
  <ion-icon name="add"></ion-icon>
</button>
```

### 1.3 Button States

- **Default**: Standard appearance
- **Hover**: Slight lift + shadow increase
- **Active**: Pressed down effect
- **Disabled**: 50% opacity, no pointer events
- **Loading**: Spinner + disabled state

---

## 2. Card System

### 2.1 Card Variants

```tsx
// Standard card with hover effect
<div className="card">
  <div className="card-header">
    <h3 className="card-title">Title</h3>
  </div>
  <div className="card-body">
    Content here
  </div>
</div>

// Elevated card - for modals/dialogs
<div className="card card-elevated">...</div>

// Modal card - highest elevation
<div className="card card-modal">...</div>

// Flat card - dashed border, no shadow
<div className="card card-flat">...</div>
```

### 2.2 Card Anatomy

```html
<div class="card">
  <div class="card-header">
    <h3 class="card-title">Title</h3>
    <span class="card-subtitle">Subtitle</span>
  </div>
  <div class="card-section">
    Section content
  </div>
  <div class="card-section">
    Another section
  </div>
</div>
```

---

## 3. Form Elements

### 3.1 Input Fields

```tsx
// Standard input
<input className="input" type="text" placeholder="Enter text..." />

// With icon
<div className="input-icon-wrap">
  <ion-icon name="search"></ion-icon>
  <input className="input" placeholder="Search..." />
</div>

// Form group with label
<div className="form-group">
  <label className="form-label">Email</label>
  <input className="form-input" type="email" />
</div>
```

### 3.2 Select

```tsx
<select className="input">
  <option value="1">Option 1</option>
  <option value="2">Option 2</option>
</select>
```

### 3.3 Textarea

```tsx
<textarea className="input" rows={4} placeholder="Description..." />
```

---

## 4. Data Display

### 4.1 Tables

```tsx
<table className="data-table">
  <thead>
    <tr>
      <th>Column 1</th>
      <th>Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data 1</td>
      <td>Data 2</td>
    </tr>
  </tbody>
</table>
```

### 4.2 KPI Cards

```tsx
<div className="kpi-card" style={{ '--kpi-accent': 'var(--brand)' }}>
  <div className="kpi-card-head">
    <div className="kpi-icon-container">
      <ion-icon name="chart"></ion-icon>
    </div>
    <span className="kpi-trend up">+12%</span>
  </div>
  <div className="kpi-label">Revenue</div>
  <div className="kpi-value">1,234,567</div>
</div>
```

### 4.3 Progress Bars

```tsx
<div className="progress-track">
  <div className="progress-fill" style={{ width: '75%' }} />
</div>

// With status color
<div className="progress-fill success" style={{ width: '100%' }} />
```

---

## 5. Navigation

### 5.1 Tabs

```tsx
<div className="tabs-container">
  <button className="tab-btn active">Tab 1</button>
  <button className="tab-btn">Tab 2</button>
  <button className="tab-btn">Tab 3</button>
</div>
```

### 5.2 Page Header

```tsx
<div className="page-header">
  <div className="page-header-content">
    <h1 className="page-title">
      <ion-icon name="cube"></ion-icon>
      Page Title
    </h1>
    <p className="page-subtitle">Page description text</p>
  </div>
  <div className="page-header-actions">
    <button className="btn btn-primary">Action</button>
  </div>
</div>
```

---

## 6. Feedback

### 6.1 Empty State

```tsx
<div className="empty-state">
  <ion-icon name="folder-open"></ion-icon>
  <h3 className="empty-state-title">No data</h3>
  <p>Description of empty state</p>
  <button className="btn btn-primary">Create</button>
</div>
```

### 6.2 Loading Spinner

```tsx
<div className="loading-screen">
  <div className="loading-spinner"></div>
  <p>Loading...</p>
</div>
```

### 6.3 Modal

```tsx
<div className="modal-overlay" onClick={onClose}>
  <div className="modal" onClick={e => e.stopPropagation()}>
    <div className="modal-header">
      <h2>Modal Title</h2>
      <button className="modal-close-btn" onClick={onClose}>
        <ion-icon name="close"></ion-icon>
      </button>
    </div>
    <div className="modal-body">
      Modal content
    </div>
    <div className="modal-footer">
      <button className="btn btn-secondary">Cancel</button>
      <button className="btn btn-primary">Confirm</button>
    </div>
  </div>
</div>
```

---

## 7. Chat Components

### 7.1 Message Bubble

```tsx
// Outgoing message
<div className="chat-message own">
  <div className="chat-bubble">
    Message text
  </div>
</div>

// Incoming message
<div className="chat-message incoming">
  <div className="chat-bubble">
    Message text
  </div>
</div>
```

### 7.2 Chat Input

```tsx
<div className="chat-input-floating">
  <input className="chat-input" placeholder="Type a message..." />
  <button className="chat-send-btn">
    <ion-icon name="send"></ion-icon>
  </button>
</div>
```

---

## 8. Utility Classes

### 8.1 Text Colors

```html
<span class="text-primary">Primary</span>
<span class="text-secondary">Secondary</span>
<span class="text-muted">Muted</span>
<span class="text-success">Success</span>
<span class="text-warning">Warning</span>
<span class="text-danger">Danger</span>
<span class="text-link">Link</span>
```

### 8.2 Animation Helpers

```html
<div class="fade-in">Fade In</div>
<div class="scale-in">Scale In</div>
<div class="rise-in">Rise In</div>
```

---

## 9. Icon Usage

### 9.1 Icon Sizes

- Small: 16px (inside small buttons, badges)
- Default: 18-20px (navigation, lists)
- Medium: 22-24px (cards, headers)
- Large: 32-48px (empty states, illustrations)

### 9.2 Icon Containers

```tsx
// Standard icon container
<div className="icon-container">
  <ion-icon name="cube"></ion-icon>
</div>

// Module-colored container
<div className="icon-container mod-production">
  <ion-icon name="construct"></ion-icon>
</div>
```

---

## 10. Responsive Behavior

### 10.1 Breakpoints

| Name | Width | Usage |
|------|-------|-------|
| Mobile | < 480px | Single column, stacked layouts |
| Tablet | < 768px | Condensed navigation |
| Desktop | < 1024px | Standard layout |
| Large | < 1280px | Full sidebar |
| XL | < 1536px | Reduced sidebar |
| XXL | < 1920px | Full sidebar |

### 10.2 Spacing Responsive

```css
/* Mobile */
--content-px: 12px;
--content-py: 16px;
--topbar-height: 44px;

/* Tablet */
@media (min-width: 768px) {
  --content-px: 16px;
}

/* Desktop */
@media (min-width: 1024px) {
  --sidebar-width: 0; /* Hidden */
  --topbar-height: 56px;
}
```

---

## 11. Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--s-1` | 4px | Tight spacing |
| `--s-2` | 8px | Icon gaps |
| `--s-3` | 12px | Input padding |
| `--s-4` | 16px | Standard gap |
| `--s-5` | 20px | Card padding |
| `--s-6` | 24px | Section spacing |
| `--s-7` | 32px | Page sections |
| `--s-8` | 40px | Large spacing |
| `--s-9` | 48px | Section breaks |

---

## 12. Border Radius Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--r-xs` | 6px | Badges |
| `--r-sm` | 8px | Inputs, small buttons |
| `--r-md` | 10px | Standard elements |
| `--r-lg` | 14px | Cards |
| `--r-xl` | 18px | Large cards |
| `--r-2xl` | 22px | Modal, chat |
| `--r-full` | 999px | Pills, avatars |
