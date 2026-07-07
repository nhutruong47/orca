# Knowledge Document: ProductionOrderPage.tsx (Chunk 17/19)

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
  "chunk_index": 16,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                         }}
                                />
                            </Field>

                            <Field label="So ngay du phong">
                                <input type="number" value={form.safetyBufferDays} onChange={e => handleChange('safetyBufferDays', parseInt(e.target.value) || 2)}
                                    min="0" max="10" style={inputStyle} />
                                <div style={{ fontSize: 11, color: 'var(--text-muted)', marginTop: 4 }}>
                                    Han noi bo se tu dong = Ngay giao - Du phong
                                </div>
                            </Field>

                            {/* Giao hang */}
                            <div style={{ gridColumn: '1 / -1' }}>
                                <h3 style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-muted)', marginBottom: 12, marginTop: 8, textTransform: 'uppercase', letterSpacing: 1 }}>Thong tin giao hang</h3>
                            </div>

                            <Field label="Nguoi nhan hang">
                                <input value={form.recipientName} onChange={e => handleChange('recipientName', e.target.value)}
                                    placeholder="Ten nguoi nhan" style={inputStyle} />
                            </Field>

                            <Field label="SDT nguoi nhan">
                                <input value={form.recipientPhone} onChange={e => handleChange('recipientPhone', e.target.value)}
                                    placeholder="0912 345 678" style={inputStyle} />
                            </Field>

                            <div style={{ gridColumn: '1 / -1' }}>
                                <Field label="Ghi chu giao hang">
                                    <textarea value={form.shippingNote} onChange={e => handleChange('shippingNote', e.target.value)}
                                        placeholder="VD: Giao vao buoi sang, lien he truoc khi giao..."
                                        rows={2} style={{ ...inputStyle, resize: 'vertical' }} />
                                </Field>
                            </div>
                        </div>

                        {/* Actions */}
                        <div style={{ display: 'flex', gap: 12, marginTop: 28, justifyContent: 'flex-end' }}>

```
