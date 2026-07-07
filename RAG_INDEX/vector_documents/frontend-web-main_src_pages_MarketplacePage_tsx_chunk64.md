# Knowledge Document: MarketplacePage.tsx (Chunk 65/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 64,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
ndex + 1}`} />
                                                <button type="button" onClick={() => {
                                                    const next = pubFactoryImages.filter((_, itemIndex) => itemIndex !== index);
                                                    setPubFactoryImages(next);
                                                    setPubFactoryImageUrl(next[0] || '');
                                                }}>Xóa ảnh</button>
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </div>
                            <div className="mp-verification-form">
                                <div className="mp-verification-form-head">
                                    <div>
                                        <h3>Xác minh xưởng</h3>
                                        <p>Điền thông tin để quản trị viên kiểm tra và duyệt hồ sơ.</p>
                                    </div>
                                    {selectedPublishTeam && (
                                        <span className={`mp-verification-status ${publishVerificationStatus.toLowerCase()}`}>
                                            {verificationStatusLabel(publishVerificationStatus)}
                                        </span>
                                    )}
                                </div>
                                {selectedPublishTeam?.verificationRejectReason && (
                                    <div className="mp-verification-note">
                                        Lý do từ chối: {selectedPublishTeam.verificationRejectReason}
                                    </div>
                                )}
                                <div className="mp-verification-grid">
                                    <div className="mp-form-group">
                                        <label>Giấy phép kinh doanh</label>
                                        <input value={pubBusinessLicense} onChange={event => setPubBusinessLicense(event.target.value)} placeholder="Link tài liệu hoặc tải file bên dưới" />
                                        <label className="mp-publish-file">

```
