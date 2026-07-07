# Knowledge Document: MarketplacePage.tsx (Chunk 66/70)

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
  "chunk_index": 65,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                          <div className="mp-form-group">
                                        <label>Giấy phép kinh doanh</label>
                                        <input value={pubBusinessLicense} onChange={event => setPubBusinessLicense(event.target.value)} placeholder="Link tài liệu hoặc tải file bên dưới" />
                                        <label className="mp-publish-file">
                                            <input type="file" accept="application/pdf,image/jpeg,image/png" onChange={event => handleDocumentFile(event, setPubBusinessLicense)} />
                                            <span className="material-symbols-outlined">upload_file</span>
                                            Tải giấy phép
                                        </label>
                                    </div>
                                    <div className="mp-form-group">
                                        <label>Địa chỉ xưởng</label>
                                        <input value={pubBusinessAddress} onChange={event => setPubBusinessAddress(event.target.value)} placeholder="Địa chỉ pháp lý / địa chỉ xưởng" />
                                    </div>
                                    <div className="mp-form-group">
                                        <label>Website doanh nghiệp</label>
                                        <input value={pubWebsiteUrl} onChange={event => setPubWebsiteUrl(event.target.value)} placeholder="https://..." />
                                    </div>
                                    <div className="mp-form-group">
                                        <label>Facebook doanh nghiệp</label>
                                        <input value={pubFacebookUrl} onChange={event => setPubFacebookUrl(event.target.value)} placeholder="https://facebook.com/..." />
                                    </div>
                                    <div className="mp-form-group mp-verification-wide">
                                        <label>Chứng nhận</label>
                                        <div className="mp-publish-chip-grid">
                                            {CERTIFICATE_OPTIONS.map(option => (
                                                <button
                                                    type="button"

```
