# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 2/12)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductivityAnalyticsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
e<any>(null);
    const [allTasks, setAllTasks] = useState<any[]>([]);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => { loadAnalytics(); }, [teamId, startDate, endDate]);
    
    useEffect(() => {
        if (!teamId) return;
        teamService.getDetail(teamId).then(setTeam).catch(() => {});
        goalService.getByTeam(teamId).then(g => {
            Promise.all(g.map(goal => taskService.getByGoal(goal.id)))
                .then(taskArrays => setAllTasks(taskArrays.flat()))
                .catch(() => {});
        }).catch(() => {});
    }, [teamId]);

    const loadAnalytics = async () => {
        setLoading(true);
        setError('');
        try {
            const result = await productionService.getAnalytics(teamId, startDate, endDate);
            setData(result);
        } catch (e: any) {
            setError(e?.response?.data?.error || 'Khong tai duoc du lieu');
        } finally {
            setLoading(false);
        }
    };

    if (loading) return (
        <div style={{ padding: 40, textAlign: 'center', color: 'var(--text-muted)', fontSize: 14 }}>Dang tai...</div>
    );

    if (error) return (
        <div style={{ padding: 40, textAlign: 'center' }}>
            <div style={{ color: '#ef4444', fontSize: 13, background: 'rgba(239,68,68,0.1)', border: '1px solid rgba(239,68,68,0.2)', borderRadius: 12, padding: 16, display: 'inline-block' }}>{error}</div>
        </div>
    );

    
    const os = data?.orderStats || {};
    const stageEff = data?.stageEfficiency || [];
    const orderAnalytics = data?.orderAnalytics || [];
    const dailyTrend = data?.dailyTrend || [];

    const MEMBER_COLORS = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#f97316', '#14b8a6'];
    const DONUT_COLORS = ['#16a34a', '#eab308', '#94a3b8'];

    const totalTasks = allTasks.length;
    const inProgressTasks = allTasks.filter(t => t.status === 'IN_PROGRESS').length;
    const completedTasks = allTasks.filter(t => t.status === 'COMPLETED').length;
    const pendingTasks = allTasks.filter(t => t.status === 'PENDING').length;
    const completionPct = totalTasks ? Math.round((completedTasks / totalTasks) * 100) : 0;

    const memberStats = (team?.members || []).map((m: any, idx: number) => {
        const memberTasks = allTasks.filter(t => t.memberId === m.userId);

```
