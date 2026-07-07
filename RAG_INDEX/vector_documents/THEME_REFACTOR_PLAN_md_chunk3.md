# Knowledge Document: THEME_REFACTOR_PLAN.md (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, report, dashboard, admin, production, warehouse, inventory

## Source Code Chunk
```md
turn 'dark';
        const saved = localStorage.getItem('orca-theme');
        if (saved === 'light') return 'light';
        if (saved === 'dark') return 'dark';
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    });

    // Update resolved theme when theme or system preference changes
    useEffect(() => {
        const updateResolvedTheme = () => {
            if (theme === 'system') {
                const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                setResolvedTheme(prefersDark ? 'dark' : 'light');
            } else {
                setResolvedTheme(theme);
            }
        };

        updateResolvedTheme();

        // Listen for system theme changes
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        const handler = () => {
            if (theme === 'system') {
                updateResolvedTheme();
            }
        };
        mediaQuery.addEventListener('change', handler);
        return () => mediaQuery.removeEventListener('change', handler);
    }, [theme]);

    // Apply theme to DOM
    useLayoutEffect(() => {
        localStorage.setItem('orca-theme', theme);
        
        const actualTheme = resolvedTheme;
        
        document.body.classList.remove('theme-dark', 'theme-light');
        document.documentElement.classList.remove('theme-dark', 'theme-light');
        document.body.classList.add(`theme-${actualTheme}`);
        document.documentElement.classList.add(`theme-${actualTheme}`);
        document.documentElement.setAttribute('data-theme', actualTheme);
        
        // Set color-scheme for native elements
        document.documentElement.style.colorScheme = actualTheme;
    }, [resolvedTheme, theme]);

    const toggleTheme = () => {
        setThemeState(prev => {
            if (prev === 'dark') return 'light';
            if (prev === 'light') return 'system';
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

```
