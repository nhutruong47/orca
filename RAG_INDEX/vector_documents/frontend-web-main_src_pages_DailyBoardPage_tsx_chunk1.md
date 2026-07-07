# Knowledge Document: DailyBoardPage.tsx (Chunk 2/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DailyBoardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <div style={{ width: 8, height: 8, borderRadius: '50%', background: color }} />
                    <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)' }}>{label}</span>
                </div>
                <div style={{ display: 'flex', gap: 16, alignItems: 'baseline' }}>
                    <span style={{ fontSize: 14, fontWeight: 800, color }}>{actual.toLocaleString('vi-VN')}</span>
                    <span style={{ fontSize: 12, color: 'var(--text-muted)' }}>/ {target.toLocaleString('vi-VN')} kg</span>
                </div>
            </div>
            <ProgressBar value={actual} max={target} color={color} />
            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 4, fontSize: 11, color: 'var(--text-muted)' }}>
                <span>{pct.toFixed(1)}%</span>
                <span>Con {remaining.toLocaleString('vi-VN')} kg</span>
            </div>
        </div>
    );
}

export default function DailyBoardPage() {
    const { id } = useParams<{ id: string }>();
    const teamId = id || '';
    const [board, setBoard] = useState<any>(null);
    const [selectedDate, setSelectedDate] = useState(() => new Date().toISOString().split('T')[0]);
    const [loading, setLoading] = useState(true);
    const [updatingOrderId, setUpdatingOrderId] = useState<string | null>(null);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => { loadBoard(); }, [teamId, selectedDate]);

    const loadBoard = async () => {
        setLoading(true);
        setError('');
        try {
            const data = await productionService.getBoardByDate(teamId, selectedDate);
            setBoard(data);
        } catch (e: any) {
            setError(e?.response?.data?.error || 'Khong tai duoc du lieu');
        } finally {
            setLoading(false);
        }
    };

    const dateLabel = new Date(selectedDate + 'T00:00:00').toLocaleDateString('vi-VN', {
        weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
    });

    if (loading) return (
        <div style={{ padding: 40, textAlign: 'center' }}>

```
