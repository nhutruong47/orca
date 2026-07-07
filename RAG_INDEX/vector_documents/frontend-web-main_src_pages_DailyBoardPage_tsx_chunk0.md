# Knowledge Document: DailyBoardPage.tsx (Chunk 1/10)

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
  "chunk_index": 0,
  "total_chunks": 10
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

const RISK_COLOR: Record<string, string> = {
    NONE: '#10b981', LOW: '#10b981', MEDIUM: '#f59e0b', HIGH: '#ef4444', CRITICAL: '#dc2626',
};
const RISK_LABEL: Record<string, string> = {
    NONE: 'On dinh', LOW: 'Thap', MEDIUM: 'Trung binh', HIGH: 'Cao', CRITICAL: 'Nguy cap',
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

function ProgressBar({ value, max = 100, color, height = 8 }: { value: number; max?: number; color?: string; height?: number }) {
    const pct = Math.min(100, Math.max(0, (value / max) * 100));
    const barColor = color || (pct >= 100 ? '#10b981' : pct >= 80 ? '#f59e0b' : '#ef4444');
    return (
        <div style={{ background: 'var(--bg-input)', borderRadius: height, height, overflow: 'hidden' }}>
            <div style={{ width: `${pct}%`, height: '100%', background: barColor, borderRadius: height, transition: 'width 0.5s ease' }} />
        </div>
    );
}

function StageRow({ label, target, actual, color }: { label: string; target: number; actual: number; color: string }) {
    const pct = target > 0 ? (actual / target) * 100 : 0;
    const remaining = Math.max(0, target - actual);
    return (
        <div style={{ marginBottom: 16 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <div style={{ width: 8, height: 8, borderRadius: '50%', background: color }} />
                    <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)' }}>{label}</span>

```
