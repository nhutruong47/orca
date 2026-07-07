# Knowledge Document: ionicons.d.ts (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/ionicons.d.ts",
  "language": "ts",
  "module": "src",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```ts
// TypeScript declaration for ionicons web components in React 18+ JSX
import 'react';

declare module 'react' {
    namespace JSX {
        interface IntrinsicElements {
            'ion-icon': React.DetailedHTMLProps<React.HTMLAttributes<HTMLElement>, HTMLElement> & {
                name?: string;
                src?: string;
                size?: 'small' | 'large';
            };
        }
    }
}

```
