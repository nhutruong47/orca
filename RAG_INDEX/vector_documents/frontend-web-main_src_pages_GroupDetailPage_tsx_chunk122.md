# Knowledge Document: GroupDetailPage.tsx (Chunk 123/136)

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
  "chunk_index": 122,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                           <button onClick={() => {
                                                                // Convert to format required by datetime-local: YYYY-MM-DDThh:mm
                                                                const toLocalString = (dateStr: string) => {
                                                                    if (!dateStr) return '';
                                                                    const d = new Date(dateStr);
                                                                    d.setMinutes(d.getMinutes() - d.getTimezoneOffset());
                                                                    return d.toISOString().slice(0,16);
                                                                };
                                                                setEditingAttendance({
                                                                    id: item.id,
                                                                    checkInTime: toLocalString(item.checkInTime),
                                                                    checkOutTime: toLocalString(item.checkOutTime)
                                                                });
                                                            }} style={{ background: 'transparent', color: '#60a5fa', border: '1px solid #60a5fa', borderRadius: 6, padding: '4px 10px', fontSize: 12, cursor: 'pointer' }}>Sửa</button>
                                                        )}
                                                    </td>
                                                </tr>
                                            );
                                        })}
                                    </tbody>
                                </table>
                            )}
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

function SalaryPanel({ teamId }: { teamId: string }) {
    const [salaryData, setSalaryData] = useState<SalaryReport[]>([]);
    const [loadingSalary, setLoadingSalary] = useState(false);
    const [showSalary, setShowSalary] = useState(false);
    const [selectedMonth, setSelectedMonth] = useState(() => {
        const now = new Date();

```
