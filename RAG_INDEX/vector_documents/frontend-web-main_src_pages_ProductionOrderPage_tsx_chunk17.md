# Knowledge Document: ProductionOrderPage.tsx (Chunk 18/19)

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
  "chunk_index": 17,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
o vao buoi sang, lien he truoc khi giao..."
                                        rows={2} style={{ ...inputStyle, resize: 'vertical' }} />
                                </Field>
                            </div>
                        </div>

                        {/* Actions */}
                        <div style={{ display: 'flex', gap: 12, marginTop: 28, justifyContent: 'flex-end' }}>
                            <button type="button" onClick={cancelForm}
                                style={{ padding: '10px 24px', borderRadius: 10, border: '1px solid var(--border)', background: 'var(--bg-input)', fontSize: 14, fontWeight: 600, cursor: 'pointer', color: 'var(--text-secondary)' }}>
                                Huy
                            </button>
                            <button type="submit" disabled={saving}
                                style={{ padding: '10px 28px', borderRadius: 10, border: 'none', background: 'linear-gradient(135deg, #10b981, #059669)', fontSize: 14, fontWeight: 700, cursor: saving ? 'not-allowed' : 'pointer', color: '#fff', opacity: saving ? 0.7 : 1 }}>
                                {saving ? 'Dang luu...' : editingOrderId ? 'Luu thay doi' : 'Tao don hang'}
                            </button>
                        </div>
                    </form>
                </div>
            )}
        </div>
    );
}

function Field({ label, required, error, children }: { label: string; required?: boolean; error?: string; children: React.ReactNode }) {
    return (
        <div style={{ marginBottom: 4 }}>
            <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)', marginBottom: 6 }}>
                {label} {required && <span style={{ color: '#ef4444' }}>*</span>}
            </label>
            {children}
            {error && (
                <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#ef4444', fontSize: 12, fontWeight: 650, marginTop: 6 }}>
                    <ion-icon name="alert-circle-outline" style={{ fontSize: 15 }} />
                    <span>{error}</span>
                </div>
            )}
        </div>
    );
}

const inputStyle: React.CSSProperties = {
    width: '100%', padding: '10px 14px', borderRadius: 10, border: '1px solid var(--border)',

```
