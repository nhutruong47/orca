# Knowledge Document: GroupDetailPage.tsx (Chunk 124/136)

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
  "chunk_index": 123,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
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
        return `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;
    });
    const [hourlyRateOverride, setHourlyRateOverride] = useState<Record<string, number>>({});
    const [editingRate, setEditingRate] = useState<string | null>(null);
    const [tempRate, setTempRate] = useState('');

    const loadSalary = async () => {
        setLoadingSalary(true);
        try {
            const data = await taskService.getSalaryReport(teamId);
            setSalaryData(data);
        } catch { /* ignore */ }
        setLoadingSalary(false);
    };

    const handleRateEdit = (memberId: string, currentRate: number) => {
        setEditingRate(memberId);
        setTempRate(currentRate.toString());
    };

    const handleRateSave = (memberId: string) => {
        const newRate = parseFloat(tempRate);
        if (!isNaN(newRate) && newRate > 0) {
            setHourlyRateOverride(prev => ({ ...prev, [memberId]: newRate }));
        }
        setEditingRate(null);
    };

    const getEffectiveRate = (memberId: string, defaultRate: number) => {
        return hourlyRateOverride[memberId] || defaultRate;
    };

    const calculateSalary = (report: SalaryReport) => {
        const rate = getEffectiveRate(report.memberId, report.hourlyRate);
        const billableHours = (report.regularHours && report.regularHours > 0) ? report.regularHours : report.totalWorkload;
        const overtimeHours = report.overtimeHours || 0;
        const overtimeRate = report.overtimeRate || (rate * 1.5);
        return Math.round((billableHours * rate) + (overtimeHours * overtimeRate));
    };

    const totalSalary = salaryData.reduce((sum, s) => sum + calculateSalary(s), 0);
    const totalTasks = salaryData.reduce((sum, s) => sum + s.totalTasks, 0);
    const totalCompleted = salaryData.reduce((sum, s) => sum + s.completedTasks, 0);
    const totalWorkload = salaryData.reduce((sum, s) => sum + s.totalWorkload, 0);

```
