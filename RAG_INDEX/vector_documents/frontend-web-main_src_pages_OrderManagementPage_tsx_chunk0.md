# Knowledge Document: OrderManagementPage.tsx (Chunk 1/23)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/OrderManagementPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { teamService } from '../services/groupService';
import { interGroupOrderService } from '../services/interGroupOrderService';
import type { Team, InterGroupOrder } from '../types/types';

const PERSONAL_BUYER = '__personal__';

const DEFAULT_MANUAL_ORDER_FORM = {
    title: '',
    description: '',
    quantity: 1,
    deadline: new Date().toISOString().split('T')[0],
    customerName: '',
    contactPhone: '',
    deliveryAddress: '',
    deliveryNote: '',
};
export default function OrderManagementPage() {
    const { user } = useAuth();
    const [, setMyTeams] = useState<Team[]>([]);
    const [selectedTeam, setSelectedTeam] = useState<string>(PERSONAL_BUYER);
    const [activeTab, setActiveTab] = useState<'outbound' | 'inbound'>('outbound');

    const [orders, setOrders] = useState<InterGroupOrder[]>([]);
    const [loading, setLoading] = useState(true);
    const [expandedOrderId, setExpandedOrderId] = useState<string | null>(null);
    const [unreadOutboundCount, setUnreadOutboundCount] = useState(0);

    const [showManualOrderForm, setShowManualOrderForm] = useState(false);
    const [manualCreateLoading, setManualCreateLoading] = useState(false);
    const [manualCreateError, setManualCreateError] = useState('');
    const [manualOrderForm, setManualOrderForm] = useState(DEFAULT_MANUAL_ORDER_FORM);

    useEffect(() => {
        const fetchTeams = async () => {
            try {
                const teams = await teamService.getMyTeams();
                // We only care about teams where the user is the owner (can manage orders)
                const ownedTeams = teams.filter(t => t.ownerId === user?.id);
                setMyTeams(ownedTeams);
                if (ownedTeams.length > 0) {
                    setSelectedTeam(ownedTeams[0].id);
                } else {
                    setSelectedTeam('');
                }
            } catch (err) {
                console.error(err);
            }
        };
        fetchTeams();
    }, [user]);

    useEffect(() => {
        if (activeTab === 'inbound' && (selectedTeam === PERSONAL_BUYER || selectedTeam === '')) {
            setOrders([]);
            setLoading(false);
            return;
        }

        const fetchOrders = async () => {
            setLoading(true);
            try {

```
