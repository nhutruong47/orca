# Knowledge Document: WorkforcePage.tsx (Chunk 8/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/WorkforcePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 7,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx
{ fontWeight: 600 }}>{w.userName}</span>
                                        </td>
                                        <td style={{ padding: '10px 16px', color: STAGE_COLOR[w.stage] || 'var(--text-secondary)', fontWeight: 600, textTransform: 'capitalize' }}>
                                            {w.stage?.replace('_', ' ').toLowerCase()}
                                        </td>
                                        <td style={{ padding: '10px 16px', color: 'var(--text-secondary)', textTransform: 'capitalize' }}>{w.shiftType?.toLowerCase()}</td>
                                        <td style={{ padding: '10px 16px', fontWeight: 700, color: '#10b981' }}>{(w.regularHours || 0).toFixed(1)}h</td>
                                        <td style={{ padding: '10px 16px', fontWeight: 700, color: '#f59e0b' }}>{(w.overtimeHours || 0).toFixed(1)}h</td>
                                        <td style={{ padding: '10px 16px', fontWeight: 900, color: '#8b5cf6' }}>{(w.actualWorkHours || 0).toFixed(1)}h</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            )}
        </div>
    );
}

```
