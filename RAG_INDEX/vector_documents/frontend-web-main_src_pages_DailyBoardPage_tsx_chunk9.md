# Knowledge Document: DailyBoardPage.tsx (Chunk 10/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DailyBoardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 9,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
sPercent: val })
                                                    .catch(() => alert('Khong the cap nhat tien do'))
                                                    .finally(() => setUpdatingOrderId(null));
                                            }}
                                            disabled={updatingOrderId === row.orderId}
                                            style={{
                                                width: '100%',
                                                accentColor: '#10b981',
                                                cursor: 'pointer',
                                                height: 4,
                                            }}
                                        />
                                    </div>
                                    <div style={{ fontSize: 14, fontWeight: 800, color: '#10b981', minWidth: 48, textAlign: 'right', display: 'flex', alignItems: 'center', gap: 4 }}>
                                        {(row.progressPercent || 0).toFixed(0)}%
                                        {updatingOrderId === row.orderId && (
                                            <ion-icon name="sync" style={{ fontSize: 12, color: 'var(--text-muted)', animation: 'spin 1s linear infinite' }} />
                                        )}
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

```
