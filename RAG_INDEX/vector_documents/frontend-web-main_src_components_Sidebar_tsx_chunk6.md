# Knowledge Document: Sidebar.tsx (Chunk 7/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Sidebar.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "report",
    "dashboard",
    "workspace",
    "admin",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, workspace, admin, payment

## Source Code Chunk
```tsx
anStyle.bg,
                                    color: planStyle.text,
                                    padding: planStyle.bg === 'transparent' ? '2px 0' : '2px 10px',
                                    borderRadius: '12px',
                                    fontSize: '10px',
                                    fontWeight: 800,
                                    textTransform: 'uppercase',
                                    display: 'inline-block',
                                    marginTop: '2px'
                                }}
                            >{planStyle.label}</span>
                        </div>
                        <ion-icon name={userMenuOpen ? 'chevron-down-outline' : 'storefront-outline'} style={{ marginLeft: 'auto', color: 'var(--shell-text-soft)', fontSize: '18px' }}></ion-icon>
                    </button>
                </div>
            )}
        </aside>
    );
}

```
