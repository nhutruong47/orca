# Knowledge Document: Sidebar.tsx (Chunk 1/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Sidebar.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "report",
    "dashboard",
    "workspace",
    "admin",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, workspace, admin, payment

## Source Code Chunk
```tsx
import { useEffect, useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { teamService } from '../services/groupService';
import { interGroupOrderService } from '../services/interGroupOrderService';
import orcaLogo from '../assets/orca-logo.png';
import defaultAvatar from '../assets/default-avatar.png';

export default function Sidebar() {
    const { user, logout } = useAuth();
    const location = useLocation();
    const [userMenuOpen, setUserMenuOpen] = useState(false);
    const [pendingOrderCount, setPendingOrderCount] = useState(0);
    const displayName = user?.fullName || user?.username || 'Người dùng';
    const displayPlan = user?.aiPlan || 'free';

    const getPlanColor = (plan: string) => {
        if (user?.role === 'ADMIN') {
            return { bg: 'transparent', text: '#8b5cf6', label: 'Platform Admin' };
        }
        switch (plan.toLowerCase()) {
            case 'free': return { bg: 'transparent', text: '#9ca3af', label: 'Miễn phí' };
            case 'professional':
            case 'plus': return { bg: 'transparent', text: '#e7a766', label: 'Plus' };
            case 'pro': return { bg: 'transparent', text: '#8b5cf6', label: 'Pro' };
            case 'enterprise': return { bg: 'transparent', text: '#ec4899', label: 'Doanh nghiệp' };
            default: return { bg: 'transparent', text: '#9ca3af', label: plan };
        }
    };
    const planStyle = getPlanColor(displayPlan);

    useEffect(() => {
        if (!user || user.role === 'ADMIN') {
            setPendingOrderCount(0);
            return;
        }

        let cancelled = false;

        const fetchPendingOrders = async () => {
            try {
                const teams = await teamService.getMyTeams();
                const ownedTeams = teams.filter(team => team.ownerId === user.id);

                if (ownedTeams.length === 0) {
                    const myOutboundOrders = await interGroupOrderService.getMyOutboundOrders();
                    const nextCount = myOutboundOrders.filter(order => order.buyerViewed === false).length;
                    if (!cancelled) setPendingOrderCount(nextCount);
                    return;
                }

                const myOutboundOrders = await interGroupOrderService.getMyOutboundOrders();

```
