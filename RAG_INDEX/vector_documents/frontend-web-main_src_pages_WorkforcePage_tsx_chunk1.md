# Knowledge Document: WorkforcePage.tsx (Chunk 2/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/WorkforcePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx
return <span style={{ fontSize: 11, color: '#f59e0b', fontWeight: 700 }}>Chua check-out</span>;
    return <span style={{ fontSize: 11, color: 'var(--text-muted)' }}>{status}</span>;
}

export default function WorkforcePage() {
    const { id } = useParams<{ id: string }>();
    const teamId = id || '';
    const [wf, setWf] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        loadWorkforce();
        const interval = setInterval(loadWorkforce, 30000);
        return () => clearInterval(interval);
    }, [teamId]);

    const loadWorkforce = async () => {
        try {
            const data = await productionService.getWorkforce(teamId);
            setWf(data);
        } catch (e: any) {
            setError(e?.response?.data?.error || 'Loi tai du lieu');
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

    if (!wf) return null;

    const stageHours = wf.stageHours || {};
    const totalRoastHours = (stageHours.RANG || 0) + (stageHours.RANH_VA_CHON || 0);
    const totalQcHours = (stageHours.QA || 0) + (stageHours.XAY || 0);

    return (
        <div style={{ padding: '24px 28px', margin: '0 auto' }}>
            {/* Header */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 20 }}>
                <button onClick={() => navigate(`/groups/${teamId}`)} style={{
                    background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                    width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: 'var(--text-secondary)', fontSize: 18,
                }}>
                    <ion-icon name="chevron-back-outline" />
                </button>

```
