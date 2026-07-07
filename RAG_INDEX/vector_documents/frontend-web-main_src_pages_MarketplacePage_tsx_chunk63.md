# Knowledge Document: MarketplacePage.tsx (Chunk 64/70)

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
  "chunk_index": 63,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                            onChange={event => setPubDescription(event.target.value)}
                                    placeholder="Tối thiểu 30 ký tự mô tả chi tiết năng lực vận hành của xưởng..."
                                />
                            </div>
                            <section className="mp-publish-section">
                                <h3>Hình ảnh & Pháp lý</h3>
                            </section>
                            <div className="mp-form-group mp-publish-upload-group">
                                <label>Ảnh xưởng (1-10 ảnh)</label>
                                <label className="mp-publish-upload">
                                    <input type="file" accept="image/jpeg,image/png,image/webp" multiple onChange={handleFactoryImageFile} />
                                    <span className="material-symbols-outlined">add_photo_alternate</span>
                                    <strong>Thêm ảnh xưởng</strong>
                                    <small>JPG, PNG, WEBP tối đa 5MB/ảnh</small>
                                </label>
                                <input value={pubFactoryImageUrl} onChange={event => {
                                    setPubFactoryImageUrl(event.target.value);
                                    setPubFactoryImages(event.target.value ? [event.target.value, ...pubFactoryImages.slice(1)] : pubFactoryImages.slice(1));
                                }} placeholder="Hoặc dán URL ảnh đại diện xưởng" />
                                {pubFactoryImages.length > 0 && (
                                    <div className="mp-factory-image-preview-grid">
                                        {pubFactoryImages.map((image, index) => (
                                            <div className="mp-factory-image-preview" key={`${image}-${index}`}>
                                                <img src={image} alt={`Ảnh xưởng ${index + 1}`} />
                                                <button type="button" onClick={() => {
                                                    const next = pubFactoryImages.filter((_, itemIndex) => itemIndex !== index);
                                                    setPubFactoryImages(next);
                                                    setPubFactoryImageUrl(next[0] || '');

```
