# Knowledge Document: THEME_AUDIT.md (Chunk 3/7)

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
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, payment, dashboard, production, warehouse, inventory, chat

## Source Code Chunk
```md
9,102,241,0.2)` | User message bubble | `var(--module-ai-soft)` |
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

```
