# Knowledge Document: ProductionOrderPage.tsx (Chunk 14/19)

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
  "chunk_index": 13,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
={t}>{t}</option>)}
                                </select>
                            </Field>

                            <Field label="Quy trinh">
                                <select value={form.processType} onChange={e => handleChange('processType', e.target.value)} style={inputStyle}>
                                    {PROCESS_TYPES.map(t => <option key={t} value={t}>{t}</option>)}
                                </select>
                            </Field>

                            <Field label="Muc rang">
                                <select value={form.roastLevel} onChange={e => handleChange('roastLevel', e.target.value)} style={inputStyle}>
                                    {ROAST_LEVELS.map(t => <option key={t} value={t}>{t}</option>)}
                                </select>
                            </Field>

                            <Field label="Quy cach dong goi">
                                <select value={form.packageSize} onChange={e => handleChange('packageSize', e.target.value)} style={inputStyle}>
                                    {PACKAGE_SIZES.map(t => <option key={t} value={t}>{t}</option>)}
                                </select>
                            </Field>

                            {/* So luong */}
                            <div style={{ gridColumn: '1 / -1' }}>
                                <h3 style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-muted)', marginBottom: 12, marginTop: 8, textTransform: 'uppercase', letterSpacing: 1 }}>So luong &amp; San luong</h3>
                            </div>

                            <Field label="San luong can lam (kg)" required>
                                <input type="number" value={form.outputTarget} onChange={e => handleChange('outputTarget', parseFloat(e.target.value) || 0)} required
                                    placeholder="VD: 10000" min="0" step="0.01" style={inputStyle} />
                            </Field>

                            <Field label="Ty le thu hoi (%)">
                                <input type="number" value={(form.expectedYield as any) * 100}
                                    onChange={e => handleChange('expectedYield', (parseFloat(e.target.value) || 0) / 100)}
                                    min="0" max="100" step="0.1" style={inputStyle} />
                            </Field>


```
