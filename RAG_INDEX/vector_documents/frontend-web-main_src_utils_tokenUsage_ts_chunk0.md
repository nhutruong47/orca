# Knowledge Document: tokenUsage.ts (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/utils/tokenUsage.ts",
  "language": "ts",
  "module": "utils",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in utils.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```ts
export function estimateTokens(text: string | null | undefined) {
    if (!text) return 0;
    const normalized = text.trim();
    if (!normalized) return 0;
    const wordCount = normalized.split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.ceil(Math.max(normalized.length / 4, wordCount * 1.35)));
}

export function formatTokenCount(value: number) {
    if (value >= 1000000) return `${(value / 1000000).toFixed(1)}M`;
    if (value >= 1000) return `${(value / 1000).toFixed(value >= 10000 ? 0 : 1)}K`;
    return String(value);
}

```
