# Knowledge Document: ThemeContext.tsx (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/context/ThemeContext.tsx",
  "language": "tsx",
  "module": "context",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in context.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
import { createContext, useContext, useState, useLayoutEffect, type ReactNode } from 'react';

type Theme = 'dark' | 'light';

interface ThemeContextType {
    theme: Theme;
    toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType>({
    theme: 'dark',
    toggleTheme: () => { },
});

export function ThemeProvider({ children }: { children: ReactNode }) {
    const [theme, setTheme] = useState<Theme>(() => {
        const saved = localStorage.getItem('orca-theme');
        return (saved === 'light' || saved === 'dark') ? saved : 'dark';
    });

    useLayoutEffect(() => {
        localStorage.setItem('orca-theme', theme);
        document.body.classList.remove('theme-dark', 'theme-light');
        document.documentElement.classList.remove('theme-dark', 'theme-light');
        document.body.classList.add(`theme-${theme}`);
        document.documentElement.classList.add(`theme-${theme}`);
        document.documentElement.setAttribute('data-theme', theme);
    }, [theme]);

    const toggleTheme = () => setTheme(prev => prev === 'dark' ? 'light' : 'dark');

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

export const useTheme = () => useContext(ThemeContext);

```
