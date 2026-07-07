# Knowledge Document: COMPONENT_STANDARDIZATION.md (Chunk 1/4)

## Metadata
```json
{
  "file_path": "COMPONENT_STANDARDIZATION.md",
  "language": "md",
  "module": "orca",
  "business_domain": "production",
  "tags": [
    "production",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: production, chat

## Source Code Chunk
```md
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

```
