# Knowledge Document: InviteAcceptPage.tsx (Chunk 3/7)

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
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization

## Source Code Chunk
```tsx
stifyContent: 'center',
                        margin: '0 auto 20px',
                        fontSize: 36
                    }}>
                        {error ? <ion-icon name="close-circle-outline" style={{ fontSize: '36px', color: '#ef4444' }}></ion-icon>
                            : done ? <ion-icon name="checkmark-circle-outline" style={{ fontSize: '36px', color: '#10b981' }}></ion-icon>
                            : <ion-icon name="people-outline" style={{ fontSize: '36px', color: '#d4a574' }}></ion-icon>}
                    </div>

                    {done ? (
                        <>
                            <h1 style={{ color: '#111827', fontSize: 26, fontWeight: 800, margin: '0 0 12px' }}>
                                Tham gia thành công! 🎉
                            </h1>
                            <p style={{ color: '#6b7280', fontSize: 15, lineHeight: 1.6, margin: 0 }}>
                                {joinedTeamName
                                    ? <>Bạn đã gia nhập nhóm <strong style={{ color: '#d4a574' }}>{joinedTeamName}</strong>.</>
                                    : 'Bạn đã được thêm vào nhóm.'}
                                <br />Đang chuyển về trang Nhóm xưởng...
                            </p>
                        </>
                    ) : error ? (
                        <>
                            <h1 style={{ color: '#ef4444', fontSize: 26, fontWeight: 800, margin: '0 0 12px' }}>
                                Không thể tham gia
                            </h1>
                            <p style={{ color: '#6b7280', fontSize: 15, lineHeight: 1.6, margin: 0 }}>
                                {error}
                            </p>
                        </>
                    ) : (
                        <>
                            <h1 style={{ color: '#111827', fontSize: 26, fontWeight: 800, margin: '0 0 8px' }}>
                                Lời mời tham gia nhóm
                            </h1>
                            <p style={{ color: '#6b7280', fontSize: 14, lineHeight: 1.6, margin: '0 0 24px' }}>
                                Bạn được mời tham gia nhóm trên hệ thống{' '}
                                <span style={{ color: '#d4a574', fontWeight: 700 }}>ORCA</span>.
                            </p>

                            {/* Invite Code Display (boxy style) */}

```
