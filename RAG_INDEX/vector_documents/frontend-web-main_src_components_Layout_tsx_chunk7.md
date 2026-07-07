# Knowledge Document: Layout.tsx (Chunk 8/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Layout.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "notification",
  "tags": [
    "notification",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 7,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
v>
                        <h3 style={{ marginBottom: '12px' }}>Nâng cấp để tiếp tục</h3>
                        <p style={{ color: '#64748b', marginBottom: '24px', fontSize: '15px' }}>
                            Chọn gói phù hợp để tiếp tục sử dụng trợ lý AI ORCA.
                        </p>
                        <div className="upgrade-required-actions">
                            <button
                                className="btn-secondary upgrade-required-button"
                                onClick={() => setShowUpgradeModal(false)}
                            >
                                Đóng
                            </button>
                            <button
                                className="btn-primary upgrade-required-button upgrade-required-primary"
                                onClick={() => {
                                    setShowUpgradeModal(false);
                                    navigate('/nang-cap-goi');
                                }}
                            >
                                Nâng cấp gói
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

```
