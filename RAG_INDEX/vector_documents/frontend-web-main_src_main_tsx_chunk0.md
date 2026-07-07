# Knowledge Document: main.tsx (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/main.tsx",
  "language": "tsx",
  "module": "src",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in src.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

```
