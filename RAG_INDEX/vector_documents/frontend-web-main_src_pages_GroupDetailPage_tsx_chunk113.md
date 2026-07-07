# Knowledge Document: GroupDetailPage.tsx (Chunk 114/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 113,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx

                                                                }}
                                                                style={{
                                                                    width: '85%',
                                                                    background: '#cbd5e1',
                                                                    color: '#0f172a',
                                                                    border: 'none',
                                                                    padding: '10px 16px',
                                                                    borderRadius: 10,
                                                                    fontWeight: 700,
                                                                    fontSize: 13,
                                                                    cursor: 'pointer',
                                                                    display: 'flex',
                                                                    alignItems: 'center',
                                                                    justifyContent: 'center',
                                                                    gap: 6,
                                                                    transition: 'background 0.2s'
                                                                }}
                                                                onMouseEnter={e => e.currentTarget.style.background = '#e2e8f0'}
                                                                onMouseLeave={e => e.currentTarget.style.background = '#cbd5e1'}
                                                            >
                                                                <ion-icon name="add" style={{ fontSize: 16 }}></ion-icon>
                                                                Tạo công việc mới
                                                            </button>
                                                        )}
                                                    </>
                                                ) : (
                                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxHeight: 200, overflowY: 'auto', paddingRight: 4 }}>

```
