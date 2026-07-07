# Knowledge Document: FactoryDashboardPage.tsx (Chunk 14/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 13,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
                          background: d.daysRemaining <= 1 ? '#ef4444' : d.daysRemaining <= 3 ? '#f59e0b' : 'rgba(16,185,129,0.1)',
                                        color: d.daysRemaining <= 1 ? '#fff' : d.daysRemaining <= 3 ? '#fff' : '#10b981'
                                    }}>
                                        {d.daysRemaining} ngay
                                    </span>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}

```
