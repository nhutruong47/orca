# Knowledge Document: MarketplacePage.tsx (Chunk 58/70)

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
  "chunk_index": 57,
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
                                    <label>Mức rang (Roast Profile)</label>
                                    <select value={rfqQuality} onChange={event => setRfqQuality(event.target.value)}>
                                        <option value="">Không yêu cầu</option>
                                        {ROAST_PROFILE_OPTIONS.map(option => (
                                            <option key={option.value} value={option.value}>{option.label}</option>
                                        ))}
                                    </select>
                                </div>
                                <div className="mp-form-group">
                                    <label>Quy cách đóng gói (Packaging)</label>
                                    <select value={rfqPackaging} onChange={event => setRfqPackaging(event.target.value)}>
                                        <option value="">Không yêu cầu</option>
                                        {PACKAGING_FORMAT_OPTIONS.map(option => (
                                            <option key={option.value} value={option.value}>{option.label}</option>
                                        ))}
                                    </select>
                                </div>
                            </div>
                            <div className="mp-form-row">
                                <div className="mp-form-group">
                                    <label>Ngày nhận hàng dự kiến (Target Date)</label>
                                    <input type="date" value={rfqDeadline} onChange={event => setRfqDeadline(event.target.value)} />
                                </div>
                                <div className="mp-form-group">
                                    <label>Ngân sách dự kiến (Budget Range)</label>
                                    <input value={rfqBudget} onChange={event => setRfqBudget(event.target.value)} placeholder="VD: 50tr - 100tr" />
                                </div>
                            </div>
                            <div className="mp-form-group">
                                <label>Ghi chú bổ sung (Additional Notes)</label>

```
