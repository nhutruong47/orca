# Knowledge Document: COMPONENT_STANDARDIZATION.md (Chunk 4/4)

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
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: production, chat

## Source Code Chunk
```md
ng</span>
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

```
