# Knowledge Document: vercel.json (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/vercel.json",
  "language": "json",
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
```json
{
    "buildCommand": "npm run build",
    "installCommand": "npm install",
    "devCommand": "npm run dev",
    "rewrites": [
        {
            "source": "/(.*)",
            "destination": "/"
        }
    ]
}
```
