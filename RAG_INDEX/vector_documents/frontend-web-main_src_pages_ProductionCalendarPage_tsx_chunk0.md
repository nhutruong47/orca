# Knowledge Document: ProductionCalendarPage.tsx (Chunk 1/12)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionCalendarPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { productionService } from '../services/groupService';

function ProgressBar({ value, max = 100, color }: { value: number; max?: number; color?: string }) {
    const pct = Math.min(100, Math.max(0, (value / max) * 100));
    const barColor = color || (pct >= 100 ? '#10b981' : pct >= 80 ? '#f59e0b' : '#ef4444');
    return (
        <div style={{ background: 'var(--bg-input)', borderRadius: 4, height: 6, overflow: 'hidden' }}>
            <div style={{ width: `${pct}%`, height: '100%', background: barColor, borderRadius: 4, transition: 'width 0.4s' }} />
        </div>
    );
}

export default function ProductionCalendarPage() {
    const { id } = useParams<{ id: string }>();
    const teamId = id || '';

    const today = new Date();
    const defaultStart = new Date(today);
    defaultStart.setDate(today.getDate() - today.getDay() + 1);
    const defaultEnd = new Date(defaultStart);
    defaultEnd.setDate(defaultStart.getDate() + 13);

    const [weekStart, setWeekStart] = useState(() => defaultStart.toISOString().split('T')[0]);
    const [calendar, setCalendar] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        loadCalendar();
    }, [teamId, weekStart]);

    const loadCalendar = async () => {
        setLoading(true);
        try {
            const start = weekStart;
            const end = new Date(new Date(weekStart).getTime() + 13 * 86400000).toISOString().split('T')[0];
            const data = await productionService.getCalendarBoard(teamId, start, end);
            setCalendar(data || []);
        } catch (e) { console.error(e); setCalendar([]); }
        finally { setLoading(false); }
    };

    const prevWeek = () => {
        const d = new Date(new Date(weekStart).getTime() - 14 * 86400000);
        setWeekStart(d.toISOString().split('T')[0]);
    };
    const nextWeek = () => {
        const d = new Date(new Date(weekStart).getTime() + 14 * 86400000);
        setWeekStart(d.toISOString().split('T')[0]);
    };
    const thisWeek = () => {
        const d = new Date();
        d.setDate(today.getDate() - today.getDay() + 1);
        setWeekStart(d.toISOString().split('T')[0]);
    };

    const formatWeekRange = () => {

```
