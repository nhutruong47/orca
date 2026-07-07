# Knowledge Document: GroupDetailPage.tsx (Chunk 3/136)

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
  "chunk_index": 2,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
tage] = useState('Roasting');
    const [editTaskDueTime, setEditTaskDueTime] = useState('');
    const [editTaskPriority, setEditTaskPriority] = useState(2);
    const [editTaskUnit, setEditTaskUnit] = useState('');

    const inferUnitFromText = (text: string, stage?: string): string => {
        const lower = (text || '').toLowerCase();
        const map: { keys: string[]; unit: string }[] = [
            { keys: ['gói', 'goi', 'pack', 'package', 'packet', 'túi', 'tui', 'bịch', 'bich'], unit: 'gói' },
            { keys: ['hộp', 'hop', 'box', 'thùng', 'thung', 'carton'], unit: 'hộp' },
            { keys: ['chai', 'bottle', 'lọ', 'lo'], unit: 'chai' },
            { keys: ['tem', 'nhãn', 'nhan', 'label', 'sticker'], unit: 'tem' },
            { keys: ['mẫu', 'mau', 'sample'], unit: 'mẫu' },
            { keys: ['đơn', 'don', 'order', 'đơn hàng'], unit: 'đơn' },
        ];
        for (const m of map) {
            if (m.keys.some(k => lower.includes(k))) return m.unit;
        }
        const stageMap: Record<string, string> = {
            DONG_GOI: 'gói',
            Packaging: 'gói',
            DAN_TEM: 'tem',
            Labeling: 'tem',
            QA: 'mẫu',
            QC: 'mẫu',
            GIAO_HANG: 'đơn',
            Delivery: 'đơn',
            Shipping: 'đơn',
            Roasting: 'kg',
            RANG: 'kg',
            SAY: 'kg',
            Drying: 'kg',
        };
        if (stage && stageMap[stage]) return stageMap[stage];
        return 'kg';
    };

    // Ad Settings
    const [showAdSettings, setShowAdSettings] = useState(false);
    const [adSpecialty, setAdSpecialty] = useState('');
    const [adCapacity, setAdCapacity] = useState('');
    const [adRegion, setAdRegion] = useState('');
    const [isPublished, setIsPublished] = useState(false);

    // Chat History
    const [showChatHistory, setShowChatHistory] = useState(false);
    const [activeChatLog, setActiveChatLog] = useState<AiChatLogMsg[]>([]);
    const [activeGoalTitle, setActiveGoalTitle] = useState('');

    // Job Labels
    const [showMemberRoles, setShowMemberRoles] = useState(false);
    const [showLabelModal, setShowLabelModal] = useState(false);
    const [selectedMemberForLabels, setSelectedMemberForLabels] = useState<any>(null);
    const [editingLabels, setEditingLabels] = useState<string>('');

    // Inventory

```
