# Knowledge Document: THEME_REFACTOR_PLAN.md (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, dashboard, admin, production, warehouse, inventory

## Source Code Chunk
```md
23, 90, 61, 0.12);
    --brand-softer:       rgba(123, 90, 61, 0.06);
    --brand-line:         rgba(123, 90, 61, 0.35);
    --brand-on:           #FFFFFF;
    
    /* Background aliases */
    --bg-primary:         #FAFAFA;
    --bg-secondary:       #F0F0F0;
    --bg-surface:         #FFFFFF;
    --bg-card:            #FFFFFF;
    --bg-elevated:        #F8F9FA;
    --bg-modal:           #FFFFFF;
    --bg-input:           #F3F4F6;
    
    /* Status - Keep saturation high for visibility */
    --status-success:     #059669;
    --status-success-soft: rgba(5, 150, 105, 0.10);
    --status-warning:      #D97706;
    --status-warning-soft: rgba(217, 119, 6, 0.10);
    --status-danger:       #DC2626;
    --status-danger-soft: rgba(220, 38, 38, 0.10);
    --status-info:         #2563EB;
    --status-info-soft:    rgba(37, 99, 235, 0.10);
    
    /* Module accents - Soft variants for light */
    --module-dashboard-soft:  rgba(123, 90, 61, 0.08);
    --module-inventory-soft:  rgba(5, 150, 105, 0.08);
    --module-production-soft: rgba(217, 119, 6, 0.08);
    --module-warehouse-soft:  rgba(6, 182, 182, 0.08);
    --module-attendance-soft: rgba(37, 99, 235, 0.08);
    --module-finance-soft:   rgba(139, 92, 246, 0.08);
    --module-ai-soft:        rgba(217, 164, 78, 0.08);
    --module-reports-soft:    rgba(99, 102, 243, 0.08);
}
```

---

## 4. Migration Tasks

### 4.1 Priority 1: Critical Replacements

| File | Pattern | Replacement | Count |
|------|---------|------------|-------|
| GroupDetailPage.tsx | `#fff` | `var(--text-inverse)` | 15 |
| GroupDetailPage.tsx | `#16a34a` | `var(--status-success)` | 4 |
| GroupDetailPage.tsx | `#d4a574` | `var(--brand)` | 8 |
| AiAssistantPanel.tsx | `rgba(99,102,241,*)` | `var(--module-ai-soft)` | 12 |
| AiAssistantPanel.tsx | `#818cf8` | `var(--module-ai)` | 5 |
| AiAssistantPanel.tsx | `#a5b4fc` | `var(--module-ai)` | 1 |

### 4.2 Priority 2: Component Refactoring

1. **ThemeAwareChart** - Recharts wrapper
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

```
