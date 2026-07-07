# Knowledge Document: ProductionOrderPage.tsx (Chunk 13/19)

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
  "chunk_index": 12,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
ize: 13, fontWeight: 700, color: 'var(--text-muted)', marginBottom: 12, textTransform: 'uppercase', letterSpacing: 1 }}>Thong tin don hang</h3>
                            </div>

                            
                            <Field label="Tieu de don hang" required>
                                <input value={form.title} onChange={e => handleChange('title', e.target.value)} required
                                    placeholder="VD: Don hang Caphe Highlands 06/2026"
                                    style={inputStyle} />
                            </Field>

                            <Field label="Ten khach hang">
                                <input value={form.customerName} onChange={e => handleChange('customerName', e.target.value)}
                                    placeholder="VD: Highlands Coffee"
                                    style={inputStyle} />
                            </Field>

                            <Field label="Mo ta">
                                <textarea value={form.description} onChange={e => handleChange('description', e.target.value)}
                                    placeholder="Ghi chu them ve don hang..."
                                    rows={2} style={{ ...inputStyle, resize: 'vertical' }} />
                            </Field>

                            
                            {/* San pham */}
                            <div style={{ gridColumn: '1 / -1' }}>
                                <h3 style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-muted)', marginBottom: 12, marginTop: 8, textTransform: 'uppercase', letterSpacing: 1 }}>Thong tin san pham</h3>
                            </div>

                            <Field label="Loai san pham">
                                <select value={form.productType} onChange={e => handleChange('productType', e.target.value)} style={inputStyle}>
                                    {PRODUCT_TYPES.map(t => <option key={t} value={t}>{t}</option>)}
                                </select>
                            </Field>

                            <Field label="Quy trinh">
                                <select value={form.processType} onChange={e => handleChange('processType', e.target.value)} style={inputStyle}>
                                    {PROCESS_TYPES.map(t => <option key={t} value={t}>{t}</option>)}

```
