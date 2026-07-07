# Knowledge Document: Layout.tsx (Chunk 1/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Layout.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "notification",
  "tags": [
    "notification",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
import { useState, useRef, useEffect } from 'react';
import { Outlet, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Sidebar from './Sidebar';
import { Bell, MoreHorizontal, MessageCircle, Edit, Sparkles } from 'lucide-react';
import { teamService, notificationService } from '../services/groupService';
import type { AppNotification } from '../types/types';
import defaultAvatar from '../assets/default-avatar.png';

export default function Layout() {
    const { user, logout } = useAuth();
    const navigate = useNavigate();
    const [showNotifications, setShowNotifications] = useState(false);
    const [showMessages, setShowMessages] = useState(false);
    const [activeTab, setActiveTab] = useState('all');
    const notifRef = useRef<HTMLDivElement>(null);
    const msgRef = useRef<HTMLDivElement>(null);

    const [notifications, setNotifications] = useState<AppNotification[]>([]);
    const [messageGroups, setMessageGroups] = useState<any[]>([]);
    const [showUpgradeModal, setShowUpgradeModal] = useState(false);

    useEffect(() => {
        const handlePaymentRequired = () => {
            setShowUpgradeModal(true);
        };
        window.addEventListener('payment-required', handlePaymentRequired);
        return () => window.removeEventListener('payment-required', handlePaymentRequired);
    }, []);

    useEffect(() => {
        if (user) {
            teamService.getMyTeams().then(teams => {
                const mapped = teams.map(t => ({
                    id: t.id,
                    name: t.name,
                    avatar: `https://ui-avatars.com/api/?name=${encodeURIComponent(t.name)}&background=0284c7&color=fff`,
                    lastMessage: t.description || 'Nhấn để mở đoạn chat của nhóm',
                    time: new Date(t.createdAt).toLocaleDateString('vi-VN'),
                    unreadCount: 0,
                    isActive: false
                }));
                setMessageGroups(mapped);
            }).catch(console.error);

            notificationService.getAll().then(setNotifications).catch(console.error);
        }
    }, [user]);

    useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            if (notifRef.current && !notifRef.current.contains(event.target as Node)) {
                setShowNotifications(false);
            }

```
