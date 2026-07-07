# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 1/12)

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
  "chunk_index": 0,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { productionService, goalService, taskService, teamService } from '../services/groupService';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend, BarChart, Bar, PieChart, Pie, Cell } from 'recharts';

function MetricPill({ label, value, unit, color }: { label: string; value: string | number; unit?: string; color?: string }) {
    return (
        <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 12, padding: '14px 20px', flex: 1, minWidth: 140 }}>
            <div style={{ fontSize: 22, fontWeight: 800, color: color || 'var(--text-primary)' }}>
                {value}{unit && <span style={{ fontSize: 13, fontWeight: 400, color: 'var(--text-muted)', marginLeft: 4 }}>{unit}</span>}
            </div>
            <div style={{ fontSize: 12, color: 'var(--text-muted)', marginTop: 4 }}>{label}</div>
        </div>
    );
}

function SectionCard({ title, children }: { title: string; children: React.ReactNode }) {
    return (
        <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 24 }}>
            <h2 style={{ fontSize: 15, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 20 }}>{title}</h2>
            {children}
        </div>
    );
}

export default function ProductivityAnalyticsPage() {
    const { id } = useParams<{ id: string }>();
    const teamId = id || '';

    const today = new Date();
    const defaultStart = new Date(today);
    defaultStart.setDate(today.getDate() - 30);

    const [startDate, setStartDate] = useState(defaultStart.toISOString().split('T')[0]);
    const [endDate, setEndDate] = useState(today.toISOString().split('T')[0]);
    const [data, setData] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [team, setTeam] = useState<any>(null);
    const [allTasks, setAllTasks] = useState<any[]>([]);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => { loadAnalytics(); }, [teamId, startDate, endDate]);
    
    useEffect(() => {
        if (!teamId) return;
        teamService.getDetail(teamId).then(setTeam).catch(() => {});
        goalService.getByTeam(teamId).then(g => {

```
