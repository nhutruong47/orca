# Knowledge Document: ProductionOrderPage.tsx (Chunk 15/19)

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
  "chunk_index": 14,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                       <Field label="Ty le thu hoi (%)">
                                <input type="number" value={(form.expectedYield as any) * 100}
                                    onChange={e => handleChange('expectedYield', (parseFloat(e.target.value) || 0) / 100)}
                                    min="0" max="100" step="0.1" style={inputStyle} />
                            </Field>

                            {inputRequired > 0 && (
                                <div style={{ gridColumn: '1 / -1', background: 'rgba(16,185,129,0.08)', border: '1px solid rgba(16,185,129,0.2)', borderRadius: 10, padding: '14px 18px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                    <span style={{ fontSize: 13, color: '#059669', fontWeight: 600 }}>Nguyen lieu can mua:</span>
                                    <span style={{ fontSize: 18, fontWeight: 800, color: '#10b981' }}>{inputRequired.toLocaleString('vi-VN')} kg</span>
                                </div>
                            )}

                            <Field label="Tong so goi">
                                <input type="number" value={form.totalPackages} onChange={e => handleChange('totalPackages', parseInt(e.target.value) || 0)}
                                    placeholder="VD: 10000" min="0" style={inputStyle} />
                            </Field>

                            <Field label="Don vi">
                                <select value={form.unit} onChange={e => handleChange('unit', e.target.value)} style={inputStyle}>
                                    <option value="kg">kg</option>
                                    <option value="tui">Tui</option>
                                    <option value="bao">Bao</option>
                                </select>
                            </Field>

                            {/* Ngay thang */}
                            <div style={{ gridColumn: '1 / -1' }}>
                                <h3 style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-muted)', marginBottom: 12, marginTop: 8, textTransform: 'uppercase', letterSpacing: 1 }}>Lich trinh</h3>
                            </div>

                            <Field label="Ngay nhan don">

```
