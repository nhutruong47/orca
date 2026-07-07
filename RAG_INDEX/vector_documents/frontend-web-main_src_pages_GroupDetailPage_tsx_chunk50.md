# Knowledge Document: GroupDetailPage.tsx (Chunk 51/136)

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
  "chunk_index": 50,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                                     <button onClick={cancelEditTask} title="Hủy" style={{ background: '#fff', border: '1px solid #e2e8f0', borderRadius: 7, color: '#64748b', cursor: 'pointer', fontSize: 13, width: 28, height: 28, display: 'grid', placeItems: 'center' }}><ion-icon name="close-outline"></ion-icon></button>
                                                        </>
                                                    ) : (
                                                        <>
                                                            <button onClick={() => startEditTask(t)} title="Sửa" style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: 7, color: '#64748b', cursor: 'pointer', fontSize: 13, width: 28, height: 28, display: 'grid', placeItems: 'center' }}><ion-icon name="create-outline"></ion-icon></button>
                                                            <button onClick={() => handleDeleteTask(t.id)} title="Xóa" style={{ background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer', fontSize: 16, opacity: 0.75, width: 28, height: 28, display: 'grid', placeItems: 'center' }}><ion-icon name="trash-outline"></ion-icon></button>
                                                        </>
                                                    )}
                                                </div>
                                            )}
                                        </td>
                                    </tr>
                                );
                            });
                        })()}
                    </tbody>
                </table>
            </div>

            {/* ===== BẢNG LƯƠNG ===== */}
            {isAdmin && (
                <SalaryPanel
                    teamId={id!}
                />
            )}

            {/* ===== BẢNG KHO HÀNG (INVENTORY) ===== */}
            <div style={{ background: '#fff', borderRadius: 14, border: '1px solid #e2e8f0', overflow: 'hidden', marginBottom: 18 }}>
                <div style={{ padding: '16px 24px', borderBottom: '1px solid #e2e8f0', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>

```
