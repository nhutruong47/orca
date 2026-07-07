# Knowledge Document: GroupDetailPage.tsx (Chunk 4/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
Msg[]>([]);
    const [activeGoalTitle, setActiveGoalTitle] = useState('');

    // Job Labels
    const [showMemberRoles, setShowMemberRoles] = useState(false);
    const [showLabelModal, setShowLabelModal] = useState(false);
    const [selectedMemberForLabels, setSelectedMemberForLabels] = useState<any>(null);
    const [editingLabels, setEditingLabels] = useState<string>('');

    // Inventory
    const [inventoryItems, setanys] = useState<any[]>([]);
    const [showAddInventory, setShowAddInventory] = useState(false);
    const [invName, setInvName] = useState('');
    const [invQty, setInvQty] = useState('');
    const [invUnit, setInvUnit] = useState('');
    const [invThreshold, setInvThreshold] = useState('');
    // For updating quantity inline
    const [updatingInvId, setUpdatingInvId] = useState<string | null>(null);
    const [updateInvQty, setUpdateInvQty] = useState('');

    // Task Filtering
    const [taskFilter, setTaskFilter] = useState<'my' | 'all'>('all');

    const [showStatsModal, setShowStatsModal] = useState(false);
    const [showScheduleModal, setShowScheduleModal] = useState(false);
    const [calendarDate, setCalendarDate] = useState(new Date(2026, 5, 20));
    const [selectedCalendarDay, setSelectedCalendarDay] = useState<number>(20);

    // Chat
    const [chatTab, setChatTab] = useState<'group' | 'dm'>('group');
    const [chatMessages, setChatMessages] = useState<ChatMsg[]>([]);
    const [chatInput, setChatInput] = useState('');
    const [dmUserId, setDmUserId] = useState<string | null>(null);
    const [showChat, setShowChat] = useState(false);
    const showChatTokens = false;
    const [chatExpanded, setChatExpanded] = useState(true);
    const [showVideoCall, setShowVideoCall] = useState(false);
    const [chatAttachment, setChatAttachment] = useState<File | null>(null);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const [unreadGroupCount, setUnreadGroupCount] = useState(0);
    const [unreadDmCounts, setUnreadDmCounts] = useState<Record<string, number>>({});
    const chatEndRef = useRef<HTMLDivElement>(null);
    const stompClientRef = useRef<Client | null>(null);

    // Refs for WebSocket callbacks to always have the latest state without resubscribing
    const chatTabRef = useRef<'group' | 'dm'>(chatTab);
    const dmUserIdRef = useRef<string | null>(dmUserId);

```
