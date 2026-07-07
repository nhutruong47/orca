# Knowledge Document: vite.config.ts (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/vite.config.ts",
  "language": "ts",
  "module": "frontend-web-main",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in frontend-web-main.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  define: {
    global: 'window',
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        secure: false,
      }
    }
  }
})

```
