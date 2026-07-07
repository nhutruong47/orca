# Knowledge Document: GroupDetailPage.tsx (Chunk 77/136)

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
  "chunk_index": 76,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
         padding: '6px 12px', 
                                                borderRadius: 12, 
                                                border: isSelected ? '1px solid #d4a574' : '1px solid #e2e8f0', 
                                                background: isSelected ? '#fff7ed' : '#f8fafc', 
                                                color: isSelected ? '#d97706' : '#64748b', 
                                                fontSize: 13, 
                                                fontWeight: 600, 
                                                cursor: 'pointer' 
                                            }}
                                        >
                                            {role}
                                        </button>
                                    );
                                })}
                            </div>
                        )}
                        <input
                            value={editingLabels}
                            onChange={e => setEditingLabels(e.target.value)}
                            placeholder="Nhập vai trò khác (phân cách bởi dấu phẩy)..."
                            style={{ width: '100%', padding: '12px 14px', borderRadius: 10, border: '1px solid #cbd5e1', fontSize: 14, outline: 'none', background: '#f8fafc' }}
                            autoFocus
                            onKeyDown={e => e.key === 'Enter' && handleSaveLabels()}
                        />
                        <div style={{ display: 'flex', gap: 10, justifyContent: 'space-between', alignItems: 'center', marginTop: 24 }}>
                            <button onClick={() => { setShowLabelModal(false); setShowManageRolesModal(true); }} style={{ background: 'transparent', border: 'none', color: '#d4a574', fontSize: 13, fontWeight: 600, cursor: 'pointer', padding: 0, display: 'flex', alignItems: 'center', gap: 4 }}>
                                <ion-icon name="list-circle-outline"></ion-icon> Tạo vai trò
                            </button>
                            <div style={{ display: 'flex', gap: 10 }}>
                                <button onClick={() => setShowLabelModal(false)} style={{ padding: '10px 20px', borderRadius: 10, border: '1px solid #e2e8f0', background: '#fff', color: '#64748b', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Hủy</button>

```
