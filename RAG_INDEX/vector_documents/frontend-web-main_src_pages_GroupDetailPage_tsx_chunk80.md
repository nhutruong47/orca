# Knowledge Document: GroupDetailPage.tsx (Chunk 81/136)

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
  "chunk_index": 80,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
a: newMetadata });
                                        setTeam(prev => prev ? { ...prev, metadata: newMetadata } : prev);
                                    } catch (e) { console.error(e); }
                                }
                            }} style={{ background: '#d4a574', color: '#fff', border: 'none', borderRadius: 10, padding: '0 16px', fontWeight: 600, cursor: 'pointer' }}>
                                Thêm
                            </button>
                        </div>
                        
                        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 24 }}>
                            <button onClick={() => setShowManageRolesModal(false)} style={{ padding: '10px 20px', borderRadius: 10, border: '1px solid #e2e8f0', background: '#fff', color: '#1e293b', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>
                                Xong
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Add Inventory Modal */}
            {showAddInventory && isAdmin && (
                <div className="modal-overlay" onClick={() => setShowAddInventory(false)} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(4px)', zIndex: 1000, position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 600, width: '90%', background: 'var(--bg-panel, #fff)', color: 'var(--text-primary, #1a1a1a)', borderRadius: 16, padding: '32px', border: '1px solid rgba(255,255,255,0.1)', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)' }}>
                        <h2 style={{ margin: '0 0 24px', fontSize: 20 }}>Nhập hàng hóa mới</h2>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
                            <div>
                                <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Tên hàng hóa <span style={{ color: '#dc2626' }}>*</span></label>

```
