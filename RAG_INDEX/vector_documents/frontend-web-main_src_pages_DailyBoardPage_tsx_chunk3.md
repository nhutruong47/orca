# Knowledge Document: DailyBoardPage.tsx (Chunk 4/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DailyBoardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
     <ion-icon name="chevron-back-outline" />
                    </button>
                    <div>
                        <h1 style={{ fontSize: 20, fontWeight: 800, color: 'var(--text-primary)', marginBottom: 4 }}>Bang San Xuat Ngay</h1>
                        <p style={{ fontSize: 13, color: 'var(--text-muted)', margin: 0 }}>{dateLabel}</p>
                    </div>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <button onClick={() => { const d = new Date(selectedDate); d.setDate(d.getDate() - 1); setSelectedDate(d.toISOString().split('T')[0]); }} style={{
                        background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                        width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                        color: 'var(--text-secondary)', fontSize: 18,
                    }}>
                        <ion-icon name="chevron-back-outline" />
                    </button>
                    <input
                        type="date"
                        value={selectedDate}
                        onChange={e => setSelectedDate(e.target.value)}
                        style={{
                            padding: '8px 14px', borderRadius: 10, border: '1px solid var(--border)',
                            background: 'var(--bg-input)', color: 'var(--text-primary)', fontSize: 13, cursor: 'pointer', outline: 'none'
                        }}
                    />
                    <button onClick={() => { const d = new Date(selectedDate); d.setDate(d.getDate() + 1); setSelectedDate(d.toISOString().split('T')[0]); }} style={{
                        background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                        width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                        color: 'var(--text-secondary)', fontSize: 18,
                    }}>
                        <ion-icon name="chevron-forward-outline" />
                    </button>
                </div>
            </div>

            {/* Tong quan */}
            <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 24, marginBottom: 20 }}>

```
