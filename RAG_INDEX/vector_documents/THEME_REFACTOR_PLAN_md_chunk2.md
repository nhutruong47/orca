# Knowledge Document: THEME_REFACTOR_PLAN.md (Chunk 3/7)

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
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, dashboard, admin, production, warehouse, inventory

## Source Code Chunk
```md
243, 0.14);

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
--s-6:  24px;
--s-7:  32px;
--s-8:  40px;

/* Border Radius */
--r-sm:    6px;
--r-md:    8px;
--r-lg:    14px;
--r-xl:    18px;
--r-2xl:   22px;
--r-full:  999px;

/* Shadows */
--shadow-xs:  0 1px 2px rgba(0, 0, 0, 0.20);
--shadow-sm:  0 2px 8px rgba(0, 0, 0, 0.32);
--shadow-md:  0 8px 24px rgba(0, 0, 0, 0.44);
--shadow-lg:  0 16px 40px rgba(0, 0, 0, 0.58);
--shadow-ring-focus: 0 0 0 3px rgba(164, 117, 81, 0.32);

/* Transitions */
--t-fast:   140ms;
--t-base:   200ms;
--t-slow:   320ms;
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
```

---

## 2. ThemeProvider Implementation

### 2.1 Enhanced ThemeProvider with System Support

```typescript
// src/context/ThemeProvider.tsx
import { createContext, useContext, useState, useEffect, useLayoutEffect, type ReactNode } from 'react';

type Theme = 'dark' | 'light' | 'system';

interface ThemeContextType {
    theme: Theme;
    resolvedTheme: 'dark' | 'light';
    toggleTheme: () => void;
    setTheme: (theme: Theme) => void;
}

const ThemeContext = createContext<ThemeContextType>({
    theme: 'system',
    resolvedTheme: 'dark',
    toggleTheme: () => {},
    setTheme: () => {},
});

export function ThemeProvider({ children }: { children: ReactNode }) {
    const [theme, setThemeState] = useState<Theme>(() => {
        const saved = localStorage.getItem('orca-theme');
        return (saved === 'light' || saved === 'dark' || saved === 'system') 
            ? saved 
            : 'system';
    });

    const [resolvedTheme, setResolvedTheme] = useState<'dark' | 'light'>(() => {
        if (typeof window === 'undefined') return 'dark';
        const saved = localStorage.getItem('orca-theme');
        if (saved === 'light') return 'light';
        if (saved === 'dark') return 'dark';
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    });

    // Update resolved theme when theme or system preference changes
    useEffect(() => {
        const updateResolvedTheme = () => {

```
