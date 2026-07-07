# Knowledge Document: THEME_AUDIT.md (Chunk 2/7)

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
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, payment, dashboard, production, warehouse, inventory, chat

## Source Code Chunk
```md
--text-inverse)` |
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

```
