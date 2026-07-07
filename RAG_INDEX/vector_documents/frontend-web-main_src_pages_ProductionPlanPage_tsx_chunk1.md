# Knowledge Document: ProductionPlanPage.tsx (Chunk 2/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
onst [plans, setPlans] = useState<ProductionPlan[]>([]);
    const [selectedPlan, setSelectedPlan] = useState<ProductionPlan | null>(null);
    const [dailyTargets, setDailyTargets] = useState<DailyTarget[]>([]);
    const [targetEdits, setTargetEdits] = useState<Record<string, { actual: number; target: number }>>({});
    const [savingTargetId, setSavingTargetId] = useState<string | null>(null);
    const [activeTab, setActiveTab] = useState<'overview' | 'daily' | 'attendance'>('overview');
    const [loading, setLoading] = useState(true);
    const [generating, setGenerating] = useState(false);
    const [approving, setApproving] = useState(false);

    // Attendance
    const [shiftType, setShiftType] = useState<ShiftType>('SANG');
    const [stage, setStage] = useState<ProductionStage>('RANG');
    const [breakMinutes, setBreakMinutes] = useState(30);
    const [myAttendance, setMyAttendance] = useState<any>(null);
    const [loadingAttendance, setLoadingAttendance] = useState(false);

    useEffect(() => { loadOrders(); }, []);
    useEffect(() => {
        if (teamId && userId) loadMyAttendance();
    }, [teamId, userId]);

    const loadOrders = async () => {
        try {
            const data = await productionService.getOrders(teamId, true);
            setOrders(data || []);
        } catch (e) { console.error(e); }
        setLoading(false);
    };

    const loadMyAttendance = async () => {
        try {
            const att = await attendanceService.getTodayAttendance(teamId);
            setMyAttendance(att);
        } catch (e) { console.error(e); }
    };

    const handleSelectOrder = async (order: ProductionOrder) => {
        setSelectedOrder(order);
        try {
            const allPlans = await productionService.getPlansByOrder(order.id);
            setPlans(allPlans || []);
            if (allPlans?.length > 0) {
                setSelectedPlan(allPlans[0]);
                await loadPlanTargets(allPlans[0].id!);
            } else {
                setSelectedPlan(null);
                setDailyTargets([]);
            }
        } catch (e) { console.error(e); }
    };

    const handleGeneratePlan = async () => {
        if (!selectedOrder) return;
        setGenerating(true);
        try {
            const plan = await productionService.generatePlan(selectedOrder.id);
            setPlans(prev => [plan, ...prev]);

```
