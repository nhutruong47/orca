# Knowledge Document: FactoryDashboardPage.tsx (Chunk 1/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { productionService } from '../services/groupService';

const STAGE_LABELS: Record<string, string> = {
    RANH_VA_CHON: 'Rang & Chon',
    RANG: 'Rang',
    XAY: 'Xay',
    DONG_GOI: 'Dong goi',
    QA: 'Kiem tra chat luong',
};

const SHIFT_LABELS: Record<string, string> = {
    SANG: 'Ca Sang',
    CHIEU: 'Ca Chieu',
    DEM: 'Ca Dem',
    NGAY: 'Ca Ngay',
};

export default function FactoryDashboardPage() {
    const { id } = useParams<{ id: string }>();
    const teamId = id || '';
    const [dashboard, setDashboard] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [updatingProgress, setUpdatingProgress] = useState<string | null>(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (teamId) loadDashboard();
    }, [teamId]);

    const loadDashboard = async () => {
        try {
            const data = await productionService.getDashboard(teamId);
            setDashboard(data);
        } catch (e) {
            console.error('Loi dashboard:', e);
        } finally {
            setLoading(false);
        }
    };

    const updateOrderProgress = async (orderId: string, newPercent: number) => {
        setUpdatingProgress(orderId);
        try {
            await productionService.updateOrder(orderId, { progressPercent: newPercent });
            setDashboard((prev: any) => ({
                ...prev,
                activeOrders: prev.activeOrders?.map((o: any) =>
                    o.id === orderId ? { ...o, progressPercent: newPercent } : o
                ),
            }));
        } catch (e) {
            console.error('Loi cap nhat tien do:', e);
            alert('Khong the cap nhat tien do');
        } finally {
            setUpdatingProgress(null);
        }
    };

    if (loading) return (
        <div style={{ padding: 40, textAlign: 'center', color: 'var(--text-muted)' }}>
            Dang tai dashboard...
        </div>
    );

    if (!dashboard) return (
        <div style={{ padding: 40, textAlign: 'center', color: 'var(--text-muted)' }}>
            Khong co du lieu
        </div>
    );

    const todayTarget = dashboard.todayTarget || {};
    const completionRate = todayTarget.completionRate || 0;

```
