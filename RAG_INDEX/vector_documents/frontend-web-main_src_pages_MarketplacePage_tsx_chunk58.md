# Knowledge Document: MarketplacePage.tsx (Chunk 59/70)

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
  "chunk_index": 58,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
sách dự kiến (Budget Range)</label>
                                    <input value={rfqBudget} onChange={event => setRfqBudget(event.target.value)} placeholder="VD: 50tr - 100tr" />
                                </div>
                            </div>
                            <div className="mp-form-group">
                                <label>Ghi chú bổ sung (Additional Notes)</label>
                                <textarea rows={3} value={rfqNote} onChange={event => setRfqNote(event.target.value)} placeholder="Mô tả chi tiết yêu cầu của bạn..." />
                            </div>

                            {/* === Hồ sơ giao hàng === */}
                            <div style={{ borderTop: '1px solid rgba(255,255,255,0.1)', margin: '16px 0', paddingTop: 16 }}>
                                <h3 style={{ fontSize: '1rem', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
                                    <span className="material-symbols-outlined" style={{ fontSize: 20 }}>local_shipping</span>
                                    Thông tin giao nhận hàng
                                </h3>
                            </div>
                            <div className="mp-form-row">
                                <div className="mp-form-group">
                                    <label>SĐT liên hệ <span style={{ color: '#e57373' }}>*</span></label>
                                    <input value={deliveryPhone} onChange={event => setDeliveryPhone(event.target.value)} placeholder="VD: 0912 345 678" required />
                                </div>
                                <div className="mp-form-group">
                                    <label>SĐT phụ (nếu không liên lạc được)</label>
                                    <input value={deliveryPhoneAlt} onChange={event => setDeliveryPhoneAlt(event.target.value)} placeholder="Tùy chọn" />
                                </div>
                            </div>
                            <div className="mp-form-group">
                                <label>Địa chỉ giao hàng <span style={{ color: '#e57373' }}>*</span></label>
                                <input value={deliveryAddress} onChange={event => setDeliveryAddress(event.target.value)} placeholder="Địa chỉ cụ thể để xưởng giao hàng" required />
                            </div>

```
