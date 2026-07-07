# Knowledge Document: ProductionPlanPage.tsx (Chunk 22/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 21,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
                                       ['Gio tang ca', `${myAttendance.overtimeHours}h`],
                                                    ['Tong gio', `${myAttendance.actualWorkHours}h`],
                                                    ['Check-out', new Date(myAttendance.checkOutTime).toLocaleTimeString('vi-VN')],
                                                ].map(([label, value]) => (
                                                    <div key={label as string} style={{ background: 'rgba(16,185,129,0.1)', borderRadius: 8, padding: '8px 12px' }}>
                                                        <div style={{ fontSize: 11, color: '#059669', marginBottom: 2 }}>{label}</div>
                                                        <div style={{ fontSize: 15, fontWeight: 800, color: '#10b981' }}>{value}</div>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    )}
                </>
            )}
        </div>
    );
}

```
