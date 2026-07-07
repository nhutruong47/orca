# Knowledge Document: CreateTaskPage.tsx (Chunk 66/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 65,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                            ))}
                        </div>
                    </div>
                )}

                {/* Footer Buttons */}
                {!isConfirmed && !isCancelled && !isArchived && (
                    <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 12, marginTop: 32 }}>
                        <button
                            onClick={onCancel}
                            style={{ padding: '12px 32px', borderRadius: '12px', border: '1px solid var(--border)', background: 'var(--bg-card)', color: 'var(--text-secondary)', fontWeight: 700, cursor: 'pointer' }}
                        >
                            Hủy
                        </button>
                        <button
                            onClick={() => onConfirm(editedResult)}
                            style={{ padding: '12px 32px', borderRadius: '12px', border: 'none', background: '#d4a574', color: '#fff', fontWeight: 700, cursor: 'pointer', boxShadow: '0 4px 12px rgba(212,165,116,0.3)' }}
                        >
                            Lưu thay đổi
                        </button>
                    </div>
                )}
                {isCancelled && (
                    <div style={{ marginTop: 20, textAlign: 'center', color: '#dc2626', fontWeight: 600, fontSize: 13, background: '#fef2f2', padding: '10px', borderRadius: '8px' }}>
                        Bản nháp này đã bị hủy.
                    </div>
                )}
                {isArchived && (
                    <div style={{ marginTop: 20, textAlign: 'center', color: '#6d28d9', fontWeight: 600, fontSize: 13, background: '#f5f3ff', padding: '10px', borderRadius: '8px' }}>
                        Đây là bản trước và đã được lưu trong lịch sử.
                    </div>
                )}
            </div>
        </div>
    );
}

```
