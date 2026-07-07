# Knowledge Document: MarketplacePage.tsx (Chunk 63/70)

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
  "chunk_index": 62,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
"
                                                className={selected ? 'selected' : ''}
                                                key={option}
                                                onClick={() => setPubSpecialty(toggleListValue(splitMultiValue(pubSpecialty), option).join(', '))}
                                            >
                                                {option}
                                            </button>
                                        );
                                    })}
                                </div>
                            </div>
                            <section className="mp-publish-section">
                                <h3>Năng lực sản xuất</h3>
                            </section>
                            <div className="mp-form-row mp-publish-capacity-row">
                                <div className="mp-form-group">
                                    <label>Công suất</label>
                                    <input type="number" value={pubCapacityValue} onChange={event => setPubCapacityValue(event.target.value)} placeholder="0" />
                                </div>
                                <div className="mp-form-group">
                                    <label>Đơn vị</label>
                                    <select value={pubCapacityUnit} onChange={event => setPubCapacityUnit(event.target.value)}>
                                        <option value="kg/tháng">kg/tháng</option>
                                        <option value="tấn/tháng">tấn/tháng</option>
                                    </select>
                                </div>
                            </div>
                            <div className="mp-form-group">
                                <label>Mô tả năng lực</label>
                                <textarea
                                    rows={4}
                                    value={pubDescription}
                                    onChange={event => setPubDescription(event.target.value)}
                                    placeholder="Tối thiểu 30 ký tự mô tả chi tiết năng lực vận hành của xưởng..."
                                />
                            </div>
                            <section className="mp-publish-section">
                                <h3>Hình ảnh & Pháp lý</h3>

```
