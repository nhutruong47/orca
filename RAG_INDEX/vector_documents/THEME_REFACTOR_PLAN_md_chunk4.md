# Knowledge Document: THEME_REFACTOR_PLAN.md (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, dashboard, admin, production, warehouse, inventory

## Source Code Chunk
```md
            return 'dark';
        });
    };

    const setTheme = (newTheme: Theme) => {
        setThemeState(newTheme);
    };

    return (
        <ThemeContext.Provider value={{ theme, resolvedTheme, toggleTheme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

export const useTheme = () => useContext(ThemeContext);
```

---

## 3. Complete Light Theme

```css
/* ============================================
   LIGHT THEME - Complete Implementation
   ============================================ */
body.theme-light {
    /* 7-Layer Visual Depth - Light variants */
    --layer-1-bg:           #FAFAFA;
    --layer-2-sidebar:      #F0F0F0;
    --layer-3-surface:      #FFFFFF;
    --layer-4-card:         #FFFFFF;
    --layer-5-elevated:     #F8F9FA;
    --layer-6-modal:        #FFFFFF;
    --layer-7-hover:        #F0F2F5;
    
    /* Borders */
    --border-subtle:        #E5E7EB;
    --border-default:       #D1D5DB;
    --border-strong:        #9CA3AF;
    --border-focus:         var(--coffee-500);
    
    /* Text - Dark for light background */
    --text-primary:         #1F2937;
    --text-secondary:       #4B5563;
    --text-muted:          #9CA3AF;
    --text-disabled:       #D1D5DB;
    --text-placeholder:    #9CA3AF;
    --text-inverse:        #FFFFFF;
    --text-link:           #2563EB;
    
    /* Shadows - Softer for light */
    --shadow-xs:  0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-sm:  0 2px 4px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
    --shadow-md:  0 4px 12px rgba(0, 0, 0, 0.08);
    --shadow-lg:  0 8px 24px rgba(0, 0, 0, 0.12);
    --shadow-ring-focus: 0 0 0 3px rgba(164, 117, 81, 0.25);
    
    /* Brand - Darker for contrast */
    --brand:              var(--coffee-700);
    --brand-hover:        var(--coffee-800);
    --brand-active:       var(--coffee-900);
    --brand-light:        var(--coffee-500);
    --brand-tint:         var(--coffee-100);
    --brand-soft:         rgba(123, 90, 61, 0.12);
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

```
