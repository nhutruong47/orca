# Knowledge Document: GroupDetailPage.tsx (Chunk 108/136)

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
  "chunk_index": 107,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                  else if (ev.type === 'END') dotColor = '#ef4444';
                                                                      else if (ev.type === 'BETWEEN') dotColor = '#f59e0b';
                                                                      if (ev.task.status === 'COMPLETED') dotColor = '#10b981';

                                                                      return (
                                                                          <span
                                                                              key={evIdx}
                                                                              style={{
                                                                                  width: 6,
                                                                                  height: 6,
                                                                                  borderRadius: '50%',
                                                                                  background: dotColor
                                                                              }}
                                                                              title={`${ev.task.title}`}
                                                                          />
                                                                      );
                                                                  })}
                                                              </div>
                                                          )}
                                                     </div>
                                                 );
                                             })}
                                        </div>

                                        {/* Legend indicator */}
                                        <div style={{ display: 'flex', gap: 16, fontSize: 12, fontWeight: 500, color: '#8e8e93', borderTop: '1px solid #232328', paddingTop: 16, flexWrap: 'wrap' }}>
                                             <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#f59e0b' }}></span> Đang làm</span>

```
