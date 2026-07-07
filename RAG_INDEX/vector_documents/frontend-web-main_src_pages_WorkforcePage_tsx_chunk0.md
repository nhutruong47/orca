# Knowledge Document: WorkforcePage.tsx (Chunk 1/8)

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
  "chunk_index": 0,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx
import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { productionService } from '../services/groupService';

const STAGE_COLOR: Record<string, string> = {
    RANG: '#d97706',
    RANH_VA_CHON: '#d97706',
    XAY: '#3b82f6',
    DONG_GOI: '#8b5cf6',
    QA: '#06b6d4',
};

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

function Avatar({ name, size = 36 }: { name: string; size?: number }) {
    const colors = ['#d4a574', '#8b5cf6', '#ec4899', '#f43f5e', '#f59e0b', '#10b981', '#06b6d4', '#3b82f6'];
    let hash = 0;
    for (const c of name) hash = (hash * 31 + c.charCodeAt(0)) % colors.length;
    return (
        <div style={{
            width: size, height: size, borderRadius: '50%',
            background: colors[hash], display: 'flex', alignItems: 'center', justifyContent: 'center',
            color: '#fff', fontWeight: 700, fontSize: size * 0.38, flexShrink: 0
        }}>
            {(name || '?').charAt(0).toUpperCase()}
        </div>
    );
}

function StatusBadge({ status }: { status: string }) {
    if (status === 'ON_TIME') return <span style={{ fontSize: 11, color: '#10b981', fontWeight: 700 }}>Dung gio</span>;
    if (status === 'LATE') return <span style={{ fontSize: 11, color: '#ef4444', fontWeight: 700 }}>Di tre</span>;
    if (status === 'MISSING_CHECKOUT') return <span style={{ fontSize: 11, color: '#f59e0b', fontWeight: 700 }}>Chua check-out</span>;
    return <span style={{ fontSize: 11, color: 'var(--text-muted)' }}>{status}</span>;
}

export default function WorkforcePage() {
    const { id } = useParams<{ id: string }>();
    const teamId = id || '';
    const [wf, setWf] = useState<any>(null);
    const [loading, setLoading] = useState(true);

```
