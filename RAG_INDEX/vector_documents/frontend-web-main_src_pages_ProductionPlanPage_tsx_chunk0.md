# Knowledge Document: ProductionPlanPage.tsx (Chunk 1/22)

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
  "chunk_index": 0,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { productionService } from '../services/groupService';
import { attendanceService } from '../services/attendanceService';
import { useAuth } from '../context/AuthContext';
import type { ProductionOrder, ProductionPlan, DailyTarget } from '../types/types';
import type { ShiftType, ProductionStage } from '../services/attendanceService';

const STATUS_LABELS: Record<string, string> = {
    PENDING: 'Cho xu ly',
    CONFIRMED: 'Da xac nhan',
    PLANNING: 'Dang ke hoach',
    IN_PRODUCTION: 'Dang san xuat',
    COMPLETED: 'Hoan thanh',
    DELIVERED: 'Da giao',
    CANCELLED: 'Da huy',
    DRAFT: 'Ban nhap',
    APPROVED: 'Da duyet',
    IN_PROGRESS: 'Dang thuc hien',
};

const STAGE_LABELS: Record<string, string> = {
    RANH_VA_CHON: 'Rang & Chon',
    RANG: 'Rang',
    XAY: 'Xay',
    DONG_GOI: 'Dong goi',
    QA: 'Kiem tra chat luong',
};

const SHIFT_LABELS: Record<string, string> = {
    SANG: 'Ca Sang (6h-14h)',
    CHIEU: 'Ca Chieu (14h-22h)',
    DEM: 'Ca Dem (22h-6h)',
    NGAY: 'Ca Ngay (6h-18h)',
};

const STAGE_UNIT: Record<string, { unit: string; max: number }> = {
    RANG: { unit: 'kg', max: 99999 },
    RANH_VA_CHON: { unit: 'kg', max: 99999 },
    XAY: { unit: 'kg', max: 99999 },
    DONG_GOI: { unit: 'goi', max: 99999 },
    QA: { unit: 'mau', max: 99999 },
    GIAO_HANG: { unit: 'don', max: 99999 },
    DAN_TEM: { unit: 'tem', max: 99999 },
};

const PROGRESS_COLOR = '#d4a574';

const unitForStage = (stage?: string) => STAGE_UNIT[stage || '']?.unit || 'kg';

export default function ProductionPlanPage() {
    const { id } = useParams<{ id: string }>();
    const { userId } = useAuth();
    const teamId = id || '';
    const navigate = useNavigate();

    const [orders, setOrders] = useState<ProductionOrder[]>([]);
    const [selectedOrder, setSelectedOrder] = useState<ProductionOrder | null>(null);
    const [plans, setPlans] = useState<ProductionPlan[]>([]);
    const [selectedPlan, setSelectedPlan] = useState<ProductionPlan | null>(null);
    const [dailyTargets, setDailyTargets] = useState<DailyTarget[]>([]);
    const [targetEdits, setTargetEdits] = useState<Record<string, { actual: number; target: number }>>({});
    const [savingTargetId, setSavingTargetId] = useState<string | null>(null);

```
