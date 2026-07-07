# Knowledge Document: InviteAcceptPage.tsx (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization

## Source Code Chunk
```tsx
                     fontWeight: 700, fontSize: 15,
                                cursor: loading ? 'not-allowed' : 'pointer',
                                transition: 'all 0.2s', marginBottom: 12,
                                boxShadow: loading ? 'none' : '0 10px 15px -3px rgba(212,165,116,0.3)'
                            }}
                        >
                            {loading
                                ? <><ion-icon name="sync-outline" style={{ fontSize: '16px', verticalAlign: 'middle', marginRight: 6 }}></ion-icon> Đang xử lý...</>
                                : isAuthenticated
                                    ? <><ion-icon name="checkmark-circle-outline" style={{ fontSize: '16px', verticalAlign: 'middle', marginRight: 6 }}></ion-icon> Chấp nhận & Tham gia</>
                                    : <><ion-icon name="log-in-outline" style={{ fontSize: '16px', verticalAlign: 'middle', marginRight: 6 }}></ion-icon> Đăng nhập để tham gia</>}
                        </button>

                        {!isAuthenticated && (
                            <button
                                onClick={() => navigate(`/register?returnUrl=${encodeURIComponent(location.pathname + location.search)}`)}
                                style={{
                                    width: '100%', padding: '12px', borderRadius: 12,
                                    border: '1px solid #e2e8f0', background: '#f8fafc',
                                    color: '#374151', fontWeight: 600, fontSize: 14, cursor: 'pointer',
                                }}
                            >
                                <ion-icon name="person-add-outline" style={{ fontSize: '16px', verticalAlign: 'middle', marginRight: 6 }}></ion-icon> Chưa có tài khoản? Đăng ký ngay
                            </button>
                        )}
                    </>
                )}

                {error && (
                    <button
                        onClick={() => navigate('/login')}
                        style={{
                            width: '100%', padding: '14px', borderRadius: 12,
                            border: 'none', background: '#d4a574',
                            color: '#ffffff', fontWeight: 700, fontSize: 15, cursor: 'pointer',
                            boxShadow: '0 10px 15px -3px rgba(212,165,116,0.3)'

```
