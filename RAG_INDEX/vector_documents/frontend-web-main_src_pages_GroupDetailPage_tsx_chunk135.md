# Knowledge Document: GroupDetailPage.tsx (Chunk 136/136)

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
  "chunk_index": 135,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
e="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                                Xuất Excel
                            </button>
                            <button
                                onClick={async () => {
                                    if (totalSalary <= 0) {
                                        alert('Hiện tại chưa thể phát lương do chưa có dữ liệu lương cần thanh toán.');
                                        return;
                                    }
                                    if (window.confirm(`Bạn có chắc chắn muốn thanh toán tổng cộng ${totalSalary.toLocaleString('vi-VN')} đ cho nhân viên?`)) {
                                        try {
                                            const res = await taskService.payoutSalary(teamId);
                                            alert(res.message || 'Thanh toán lương thành công!');
                                        } catch (err: any) {
                                            alert(err.response?.data?.error || 'Thanh toán thất bại hoặc không có số dư.');
                                        }
                                    }
                                }}
                                style={{ padding: '10px 20px', borderRadius: 10, border: 'none', background: '#d4a574', color: '#fff', fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 8 }}
                            >
                                <svg width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                                Phát lương
                            </button>
                        </div>
                    </div>
                </div>
            )}


            <style>{`
                @keyframes spin { to { transform: rotate(360deg); } }
            `}</style>
        </div>
    );
}

```
