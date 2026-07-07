# Knowledge Document: GroupDetailPage.tsx (Chunk 135/136)

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
  "chunk_index": 134,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                color: '#d4a574', fontWeight: 900, fontSize: 17
                                        }}>
                                            {totalSalary.toLocaleString('vi-VN')} đ
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Action Buttons */}
                        <div style={{ padding: '16px 28px', borderTop: '1px solid var(--border)', display: 'flex', justifyContent: 'flex-end', gap: 12, background: 'var(--bg-input, rgba(255, 255, 255, 0.03))' }}>
                            <button
                                onClick={async () => {
                                    try {
                                        const res = await taskService.exportSalaryExcel(teamId);
                                        const url = window.URL.createObjectURL(new Blob([res.data]));
                                        const link = document.createElement('a');
                                        link.href = url;
                                        link.setAttribute('download', `bang-luong-${teamId}-${selectedMonth}.xlsx`);
                                        document.body.appendChild(link);
                                        link.click();
                                        link.remove();
                                    } catch (err) {
                                        alert('Không thể xuất file Excel bảng lương.');
                                    }
                                }}
                                style={{ padding: '10px 20px', borderRadius: 10, border: '1px solid #e2e8f0', background: '#fff', color: '#64748b', fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 8 }}
                            >
                                <svg width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                                Xuất Excel
                            </button>
                            <button
                                onClick={async () => {
                                    if (totalSalary <= 0) {

```
