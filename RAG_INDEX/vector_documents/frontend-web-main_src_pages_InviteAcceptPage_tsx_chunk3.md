# Knowledge Document: InviteAcceptPage.tsx (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization

## Source Code Chunk
```tsx
    </h1>
                            <p style={{ color: '#6b7280', fontSize: 14, lineHeight: 1.6, margin: '0 0 24px' }}>
                                Bạn được mời tham gia nhóm trên hệ thống{' '}
                                <span style={{ color: '#d4a574', fontWeight: 700 }}>ORCA</span>.
                            </p>

                            {/* Invite Code Display (boxy style) */}
                            {isCodeMode && inviteCode && (
                                <div style={{
                                    background: '#f8fafc', borderRadius: 16, padding: '24px 16px',
                                    border: '1px solid #e2e8f0', marginBottom: 24
                                }}>
                                    <div style={{ fontSize: 11, fontWeight: 700, color: '#9ca3af', textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 14 }}>
                                        Mã mời
                                    </div>
                                    <div style={{ display: 'flex', gap: 8, justifyContent: 'center', alignItems: 'center' }}>
                                        {inviteCode.split('').map((char, idx) => (
                                            <div key={idx} style={{
                                                width: 44, height: 54, background: '#fff', borderRadius: 12,
                                                border: '1px solid #e2e8f0',
                                                display: 'flex', alignItems: 'center', justifyContent: 'center',
                                                fontSize: 24, fontWeight: 800, color: '#4f46e5',
                                                boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
                                            }}>
                                                {char}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Token info display */}
                            {!isCodeMode && tokenInfo?.email && (
                                <div style={{
                                    marginBottom: 20, padding: '12px 16px',
                                    background: '#f8fafc', borderRadius: 12,

```
