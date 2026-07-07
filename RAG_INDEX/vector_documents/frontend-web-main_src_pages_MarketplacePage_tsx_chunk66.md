# Knowledge Document: MarketplacePage.tsx (Chunk 67/70)

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
  "chunk_index": 66,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
div className="mp-form-group mp-verification-wide">
                                        <label>Chứng nhận</label>
                                        <div className="mp-publish-chip-grid">
                                            {CERTIFICATE_OPTIONS.map(option => (
                                                <button
                                                    type="button"
                                                    className={pubCertificates.includes(option) ? 'selected' : ''}
                                                    key={option}
                                                    onClick={() => setPubCertificates(toggleListValue(pubCertificates, option))}
                                                >
                                                    {option}
                                                </button>
                                            ))}
                                        </div>
                                    </div>
                                    <div className="mp-form-group mp-verification-wide">
                                        <label>File chứng nhận</label>
                                        <input value={pubCertificationDocument} onChange={event => setPubCertificationDocument(event.target.value)} placeholder="Link tài liệu nếu có" />
                                        <label className="mp-publish-file">
                                            <input type="file" accept="application/pdf,image/jpeg,image/png" onChange={event => handleDocumentFile(event, setPubCertificationDocument)} />
                                            <span className="material-symbols-outlined">upload_file</span>
                                            Tải chứng nhận
                                        </label>
                                    </div>
                                </div>
                            </div>
                            <div className="mp-publish-bottom-bar">
                                <button type="button" className="mp-cancel-btn" onClick={() => setShowPublishModal(false)}>Hủy</button>
                                <button type="submit" className="mp-submit-btn" disabled={publishing}>
                                    {publishing ? 'Đang gửi...' : editingPublishedTeam ? 'Lưu & gửi duyệt' : 'Đăng ký xưởng'}

```
