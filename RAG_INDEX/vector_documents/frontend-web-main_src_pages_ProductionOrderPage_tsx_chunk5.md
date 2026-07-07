# Knowledge Document: ProductionOrderPage.tsx (Chunk 6/19)

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
  "chunk_index": 5,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                        width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                        color: 'var(--text-secondary)', fontSize: 18, flexShrink: 0
                    }} title="Quay lại nhóm">
                        <ion-icon name="chevron-back-outline" />
                    </button>
                    <h1 style={{ fontSize: 22, fontWeight: 800, color: 'var(--text-primary)', margin: 0 }}>Don hang San xuat</h1>
                </div>
                <button
                    onClick={startCreate}
                    style={{ background: 'linear-gradient(135deg, #10b981, #059669)', color: '#fff', border: 'none', borderRadius: 10, padding: '10px 20px', fontSize: 14, fontWeight: 700, cursor: 'pointer' }}
                >
                    + Tao don hang moi
                </button>
            </div>

            {error && (
                <div style={{ background: 'rgba(239,68,68,0.1)', border: '1px solid rgba(239,68,68,0.3)', borderRadius: 10, padding: '12px 16px', marginBottom: 16, color: '#ef4444', fontSize: 13 }}>
                    {error}
                </div>
            )}

            {/* Tab */}
            <div style={{ display: 'flex', gap: 4, marginBottom: 20, background: 'var(--bg-input)', borderRadius: 10, padding: 4, width: 'fit-content' }}>
                {[['list', 'Danh sach'], ['create', 'Tao don hang']].map(([tab, label]) => (
                    <button key={tab} onClick={() => tab === 'create' ? startCreate() : cancelForm()} style={{
                        padding: '8px 20px', borderRadius: 8, border: 'none', cursor: 'pointer', fontSize: 13, fontWeight: 600,
                        background: activeTab === tab ? '#fff' : 'transparent',
                        color: activeTab === tab ? 'var(--text-primary)' : 'var(--text-secondary)',
                        boxShadow: activeTab === tab ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'
                    }}>{tab === 'create' && editingOrderId ? 'Sua don hang' : label}</button>
                ))}
            </div>

            {/* List */}
            {activeTab === 'list' && (
                loading ? (
                    <div style={{ textAlign: 'center', padding: 40, color: 'var(--text-muted)' }}>Dang tai...</div>

```
