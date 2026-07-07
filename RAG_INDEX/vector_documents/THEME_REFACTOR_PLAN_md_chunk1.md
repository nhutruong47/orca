# Knowledge Document: THEME_REFACTOR_PLAN.md (Chunk 2/7)

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
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, dashboard, admin, production, warehouse, inventory

## Source Code Chunk
```md
89;
--text-placeholder: #8D95A1;
--text-inverse:     #FFFFFF;        /* For text on colored backgrounds */
--text-link:        #7FB5FF;

/* Borders */
--border-subtle:    #3A4048;
--border-default:   #515B67;
--border-strong:    #5B6672;

/* Status Colors */
--color-success:    var(--green-500);
--color-warning:    #E2B65C;
--color-danger:     var(--red-500);
--color-info:       var(--blue-500);

/* Status with soft backgrounds */
--success:         var(--green-500);
--success-soft:    rgba(92, 184, 92, 0.14);
--success-line:    rgba(92, 184, 92, 0.40);

--warning:         #E2B65C;
--warning-soft:     rgba(226, 182, 92, 0.14);
--warning-line:     rgba(226, 182, 92, 0.40);

--danger:          var(--red-500);
--danger-soft:      rgba(230, 90, 90, 0.14);
--danger-line:     rgba(230, 90, 90, 0.40);

--info:            var(--blue-500);
--info-soft:       rgba(91, 141, 239, 0.14);
--info-line:       rgba(91, 141, 239, 0.40);

/* Brand */
--brand:           var(--coffee-500);
--brand-hover:     var(--coffee-600);
--brand-active:    var(--coffee-700);
--brand-soft:      rgba(164, 117, 81, 0.14);
--brand-line:      rgba(164, 117, 81, 0.40);
--brand-on:        #FFFFFF;        /* Text on brand color */

/* Module Accents */
--module-dashboard:   var(--coffee-500);
--module-inventory:   var(--green-500);
--module-production:  var(--orange-500);
--module-warehouse:   var(--teal-500);
--module-attendance:  var(--blue-500);
--module-finance:     var(--purple-500);
--module-ai:         var(--gold-500);
--module-reports:     var(--indigo-500);

/* Module soft variants */
--module-dashboard-soft:   rgba(164, 117, 81, 0.14);
--module-inventory-soft:   rgba(92, 184, 92, 0.14);
--module-production-soft:  rgba(217, 130, 43, 0.14);
--module-warehouse-soft:   rgba(41, 182, 182, 0.14);
--module-attendance-soft:  rgba(91, 141, 239, 0.14);
--module-finance-soft:    rgba(139, 124, 246, 0.14);
--module-ai-soft:        rgba(216, 166, 78, 0.14);
--module-reports-soft:    rgba(99, 116, 243, 0.14);

/* Typography */
--font-sans:  'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
--font-mono:  'JetBrains Mono', 'SF Mono', Menlo, monospace;

--fs-xs:    11px;
--fs-sm:    12px;
--fs-base:  13px;
--fs-md:    14px;
--fs-lg:    16px;
--fs-xl:    20px;
--fs-2xl:   24px;
--fs-3xl:   32px;

/* Spacing */
--s-1:  4px;
--s-2:  8px;
--s-3:  12px;
--s-4:  16px;
--s-5:  20px;

```
