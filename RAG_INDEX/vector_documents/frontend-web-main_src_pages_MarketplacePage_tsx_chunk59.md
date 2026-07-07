# Knowledge Document: MarketplacePage.tsx (Chunk 60/70)

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
  "chunk_index": 59,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
       </div>
                            <div className="mp-form-group">
                                <label>Địa chỉ giao hàng <span style={{ color: '#e57373' }}>*</span></label>
                                <input value={deliveryAddress} onChange={event => setDeliveryAddress(event.target.value)} placeholder="Địa chỉ cụ thể để xưởng giao hàng" required />
                            </div>
                            <div className="mp-form-row">
                                <div className="mp-form-group">
                                    <label>Giờ giao mong muốn (từ)</label>
                                    <input type="datetime-local" value={deliveryFrom} onChange={event => setDeliveryFrom(event.target.value)} />
                                </div>
                                <div className="mp-form-group">
                                    <label>Giờ giao mong muốn (đến)</label>
                                    <input type="datetime-local" value={deliveryTo} onChange={event => setDeliveryTo(event.target.value)} />
                                </div>
                            </div>
                            <div className="mp-form-group">
                                <label>Nếu không liên lạc được / không nhận hàng</label>
                                <select value={deliveryFailureAction} onChange={event => setDeliveryFailureAction(event.target.value)}>
                                    <option value="RETRY_LATER">Giao lại sau</option>
                                    <option value="LEAVE_AT_DOOR">Để hàng tại cổng/kho</option>
                                    <option value="RETURN_TO_SENDER">Trả hàng về cho xưởng</option>
                                    <option value="CONTACT_ALTERNATIVE">Liên hệ SĐT phụ</option>
                                </select>
                            </div>
                            <div className="mp-form-group">
                                <label>Ghi chú giao hàng</label>
                                <textarea rows={2} value={deliveryNote} onChange={event => setDeliveryNote(event.target.value)} placeholder="VD: Giao cổng sau, gọi trước 30 phút..." />
                            </div>
                            <div className="mp-modal-actions">

```
