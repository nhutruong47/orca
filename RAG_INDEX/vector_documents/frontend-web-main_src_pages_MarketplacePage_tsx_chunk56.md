# Knowledge Document: MarketplacePage.tsx (Chunk 57/70)

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
  "chunk_index": 56,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                                ))}
                                    </select>
                                </div>
                                <div className="mp-form-group">
                                    <label>Loại sản phẩm (Product Type)</label>
                                    <select value={rfqProductName} onChange={event => setRfqProductName(event.target.value)} required>
                                        <option value="">Chọn loại cà phê</option>
                                        {COFFEE_TYPE_OPTIONS.map(option => (
                                            <option key={option.value} value={option.value}>{option.label}</option>
                                        ))}
                                    </select>
                                </div>
                            </div>
                            <div className="mp-form-row">
                                <div className="mp-form-group">
                                    <label>Số lượng (Quantity)</label>
                                    <input type="number" min="1" value={rfqQuantity} onChange={event => setRfqQuantity(parseInt(event.target.value) || 1)} required />
                                </div>
                                <div className="mp-form-group">
                                    <label>Đơn vị (Unit)</label>
                                    <select value={rfqUnit} onChange={event => setRfqUnit(event.target.value)} required>
                                        {RFQ_UNIT_OPTIONS.map(option => (
                                            <option key={option.value} value={option.value}>{option.label}</option>
                                        ))}
                                    </select>
                                </div>
                            </div>
                            <div className="mp-form-row">
                                <div className="mp-form-group">
                                    <label>Mức rang (Roast Profile)</label>
                                    <select value={rfqQuality} onChange={event => setRfqQuality(event.target.value)}>
                                        <option value="">Không yêu cầu</option>
                                        {ROAST_PROFILE_OPTIONS.map(option => (

```
