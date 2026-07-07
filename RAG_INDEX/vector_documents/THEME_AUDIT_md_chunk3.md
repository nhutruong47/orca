# Knowledge Document: THEME_AUDIT.md (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, payment, dashboard, production, warehouse, inventory, chat

## Source Code Chunk
```md
9, 96, 128 | `#ffe0bf`, `#8b5a2b`, `#c0b3a9` | Various text | Semantic tokens |
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


```
