# Knowledge Document: CreateTaskPage.tsx (Chunk 4/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
Thực hiện công việc ${addedTaskTitle.toLowerCase()} theo yêu cầu của kế hoạch.`,
                    priority: 3,
                    workload: 1,
                    suggestedAssigneeId: null,
                    suggestedAssigneeName: null,
                    suggestedReason: 'Chưa tìm thấy người phụ trách phù hợp. Bạn có thể chọn thủ công.',
                },
            ],
        };
    }

    const removedTaskIndex = getRequestedRemovedTaskIndex(instruction, original.tasks.length);
    if (removedTaskIndex !== null && revised.tasks.length >= original.tasks.length) {
        return {
            ...revised,
            tasks: original.tasks.filter((_, index) => index !== removedTaskIndex),
        };
    }

    return revised;
};

function friendlyTaskError(error?: string) {
    const text = error || '';
    const lower = text.toLowerCase();
    if (lower.includes('payment_required') || lower.includes('hết hạn gói miễn phí')) {
        return 'Gói miễn phí đã hết hạn.';
    }
    if (lower.includes('could not execute statement') || (lower.includes('constraint') && lower.includes('sql'))) {
        return 'Không thể lưu kế hoạch do dữ liệu bị trùng hoặc không hợp lệ. Vui lòng bấm tạo lại.';
    }
    return text || 'Không thể tạo công việc, vui lòng thử lại';
}

export default function CreateTaskPage() {
    const { id: teamId } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const chatInputRef = useRef<HTMLTextAreaElement>(null);
    const categoryMenuRef = useRef<HTMLDivElement>(null);

    const [team, setTeam] = useState<Team | null>(null);
    const [category, setCategory] = useState('Rang xay');
    const [categoryOpen, setCategoryOpen] = useState(false);
    const [priority, setPriority] = useState('Trung bình');
    const categoryOptions = ['Rang xay', 'Sơ chế', 'Đóng gói'];

    const [input, setInput] = useState('');
    const [messages, setMessages] = useState<ChatMessage[]>(() => {
        try {
            const pathSegments = window.location.pathname.split('/');
            const idx = pathSegments.indexOf('groups');
            const tid = idx >= 0 && idx + 1 < pathSegments.length ? pathSegments[idx + 1] : null;
            if (tid) {
                const saved = localStorage.getItem(`ai_task_chat_${tid}`);
                if (saved) {
                    return JSON.parse(saved).map((m: any) => ({

```
