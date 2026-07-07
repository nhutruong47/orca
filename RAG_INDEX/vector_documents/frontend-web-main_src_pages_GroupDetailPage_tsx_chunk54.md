# Knowledge Document: GroupDetailPage.tsx (Chunk 55/136)

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
  "chunk_index": 54,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
        <button onClick={() => { setUpdatingInvId(item.id); setUpdateInvQty(Number(item.quantity).toLocaleString('de-DE')); }} style={{ background: '#f8fafc', color: '#d4a574', border: '1px solid #e2e8f0', borderRadius: 6, padding: '4px 10px', fontSize: 11, fontWeight: 600, cursor: 'pointer' }}>Chỉnh sửa</button>
                                        )}
                                    </td>
                                    <td style={{ padding: '12px 16px' }}>
                                        {isAdmin && <button onClick={() => handleDeleteInventory(item.id)} style={{ background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer', fontSize: 16, opacity: 0.6 }}><ion-icon name="trash-outline"></ion-icon></button>}
                                    </td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>

                        {/* ===== CHAT PANEL (Messenger-style) ===== */}
            {showChat && (
                <div style={{
                    position: 'fixed', right: 80, bottom: 0,
                    width: chatExpanded ? 800 : 440, height: 480,
                    background: 'var(--bg-card, #ffffff)', boxShadow: 'var(--shadow-lg, 0 4px 24px rgba(0,0,0,0.15))',
                    zIndex: 9999, display: 'flex', flexDirection: 'row',
                    border: '1px solid var(--border, #e4e6eb)', borderBottom: 'none',
                    borderTopLeftRadius: 12, borderTopRightRadius: 12,
                    transition: 'width 0.3s ease',
                    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif',
                    overflow: 'hidden'
                }}>
                    {/* ===== LEFT: conversation list ===== */}
                    <div style={{
                        width: chatExpanded ? 320 : 0, flexShrink: 0,
                        display: 'flex', flexDirection: 'column',
                        borderRight: '1px solid var(--border, #e4e6eb)',
                        background: 'var(--bg-secondary, #fff)',
                        overflow: 'hidden',
                        transition: 'width 0.3s ease'
                    }}>
                        {/* Sidebar header — chỉ 1 nút đóng (X) gọn */}

```
