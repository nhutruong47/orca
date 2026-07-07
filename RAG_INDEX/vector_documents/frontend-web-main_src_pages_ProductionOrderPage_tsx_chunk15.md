# Knowledge Document: ProductionOrderPage.tsx (Chunk 16/19)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionOrderPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 15,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                    {/* Ngay thang */}
                            <div style={{ gridColumn: '1 / -1' }}>
                                <h3 style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-muted)', marginBottom: 12, marginTop: 8, textTransform: 'uppercase', letterSpacing: 1 }}>Lich trinh</h3>
                            </div>

                            <Field label="Ngay nhan don">
                                <input type="date" value={form.orderDate} onChange={e => handleChange('orderDate', e.target.value)} style={inputStyle} />
                            </Field>

                            <Field label="Ngay xac nhan">
                                <input type="date" value={form.confirmDate} onChange={e => handleChange('confirmDate', e.target.value)} style={inputStyle} />
                            </Field>

                            <Field label="Ngay bat dau san xuat">
                                <input type="date" value={form.productionStartDate} onChange={e => handleChange('productionStartDate', e.target.value)} style={inputStyle} />
                            </Field>

                            <Field label="Ngay giao cho khach" required error={fieldErrors.customerDeliveryDate}>
                                <input
                                    ref={customerDeliveryDateRef}
                                    type="date"
                                    value={form.customerDeliveryDate}
                                    onChange={e => handleChange('customerDeliveryDate', e.target.value)}
                                    style={{
                                        ...inputStyle,
                                        borderColor: fieldErrors.customerDeliveryDate ? '#ef4444' : 'var(--border)',
                                        boxShadow: fieldErrors.customerDeliveryDate ? '0 0 0 3px rgba(239, 68, 68, 0.16)' : 'none',
                                    }}
                                />
                            </Field>

                            <Field label="So ngay du phong">
                                <input type="number" value={form.safetyBufferDays} onChange={e => handleChange('safetyBufferDays', parseInt(e.target.value) || 2)}
                                    min="0" max="10" style={inputStyle} />

```
