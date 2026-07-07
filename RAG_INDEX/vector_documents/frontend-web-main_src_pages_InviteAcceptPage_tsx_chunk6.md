# Knowledge Document: InviteAcceptPage.tsx (Chunk 7/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/InviteAcceptPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "authorization",
  "tags": [
    "authorization"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization

## Source Code Chunk
```tsx
           onClick={() => navigate('/login')}
                        style={{
                            width: '100%', padding: '14px', borderRadius: 12,
                            border: 'none', background: '#d4a574',
                            color: '#ffffff', fontWeight: 700, fontSize: 15, cursor: 'pointer',
                            boxShadow: '0 10px 15px -3px rgba(212,165,116,0.3)'
                        }}
                    >
                        <ion-icon name="arrow-back-outline" style={{ fontSize: '16px', verticalAlign: 'middle', marginRight: 6 }}></ion-icon> Về trang đăng nhập
                    </button>
                )}

                <p style={{ marginTop: 24, fontSize: 11, color: '#9ca3af' }}>
                    ORCA — Quản lý xưởng cà phê
                </p>
            </div>

            <style>{`
                @keyframes fadeInUp {
                    from { opacity: 0; transform: translateY(20px); }
                    to { opacity: 1; transform: translateY(0); }
                }
            `}</style>
        </div>
    );
}

```
