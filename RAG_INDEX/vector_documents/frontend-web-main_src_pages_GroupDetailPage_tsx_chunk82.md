# Knowledge Document: GroupDetailPage.tsx (Chunk 83/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 82,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
target.value)} placeholder="VD: kg, hộp..." style={{ width: '100%', padding: '12px 16px', borderRadius: 10, border: '1px solid var(--border, #cbd5e1)', fontSize: 15, outline: 'none', background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                                </div>
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Mức báo sắp hết</label>
                                <input type="number" value={invThreshold} onChange={e => setInvThreshold(e.target.value)} placeholder="Cảnh báo khi nhỏ hơn hoặc bằng (VD: 10)" style={{ width: '100%', padding: '12px 16px', borderRadius: 10, border: '1px solid var(--border, #cbd5e1)', fontSize: 15, outline: 'none', background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                            </div>
                        </div>
                        <div style={{ display: 'flex', gap: 12, justifyContent: 'flex-end', marginTop: 32 }}>
                            <button onClick={() => setShowAddInventory(false)} style={{ padding: '12px 24px', borderRadius: 10, border: '1px solid var(--border, #e2e8f0)', background: 'transparent', color: 'var(--text-primary, #64748b)', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>Hủy</button>
                            <button onClick={handleAddInventory} disabled={loading || !invName.trim() || !invQty} style={{ padding: '12px 24px', borderRadius: 10, border: 'none', background: '#d4a574', color: '#fff', fontSize: 14, fontWeight: 600, cursor: 'pointer', opacity: (loading || !invName.trim() || !invQty) ? 0.6 : 1 }}>
                                {loading ? 'Đang lưu...' : 'Lưu vào kho'}
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Chat History Modal */}
            {showChatHistory && (
                <div className="modal-overlay" onClick={() => setShowChatHistory(false)} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(8px)' }}>

```
