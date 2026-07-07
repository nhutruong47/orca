# Knowledge Document: ErrorBoundary.tsx (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/ErrorBoundary.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "dashboard",
  "tags": [
    "dashboard"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard

## Source Code Chunk
```tsx
       >
                        Thử lại
                    </button>
                    <button
                        onClick={() => window.location.href = '/dashboard'}
                        style={{
                            padding: '10px 28px', borderRadius: 10, border: '1px solid var(--border)',
                            background: 'var(--bg-input)', color: 'var(--text-primary)',
                            fontSize: 14, fontWeight: 600, cursor: 'pointer', marginTop: 12
                        }}
                    >
                        Về trang chủ
                    </button>
                </div>
            );
        }
        return this.props.children;
    }
}

```
