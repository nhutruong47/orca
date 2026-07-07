# Knowledge Document: InviteAcceptPage.tsx (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization

## Source Code Chunk
```tsx
  </div>
                                </div>
                            )}

                            {/* Token info display */}
                            {!isCodeMode && tokenInfo?.email && (
                                <div style={{
                                    marginBottom: 20, padding: '12px 16px',
                                    background: '#f8fafc', borderRadius: 12,
                                    border: '1px solid #e2e8f0', fontSize: 13, color: '#6b7280'
                                }}>
                                    Gửi đến: <strong style={{ color: '#d4a574' }}>{tokenInfo.email}</strong>
                                </div>
                            )}
                        </>
                    )}
                </div>

                {/* Buttons */}
                {!done && !error && (
                    <>
                        {!isAuthenticated && (
                            <p style={{
                                fontSize: 13, color: '#6b7280', marginBottom: 20,
                                padding: '12px', background: '#fef3c7', borderRadius: 12,
                                border: '1px dashed #f59e0b'
                            }}>
                                ⚠️ Bạn cần <strong>đăng nhập</strong> hoặc <strong>tạo tài khoản</strong> trước khi tham gia nhóm.
                            </p>
                        )}

                        <button
                            onClick={handleAccept}
                            disabled={loading}
                            style={{
                                width: '100%', padding: '14px', borderRadius: 12, border: 'none',
                                background: loading ? '#e2e8f0' : '#d4a574',
                                color: loading ? '#9ca3af' : '#ffffff',
                                fontWeight: 700, fontSize: 15,
                                cursor: loading ? 'not-allowed' : 'pointer',
                                transition: 'all 0.2s', marginBottom: 12,
                                boxShadow: loading ? 'none' : '0 10px 15px -3px rgba(212,165,116,0.3)'
                            }}
                        >
                            {loading

```
