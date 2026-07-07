# Knowledge Document: CreateTaskPage.tsx (Chunk 5/66)

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
  "chunk_index": 4,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
st pathSegments = window.location.pathname.split('/');
            const idx = pathSegments.indexOf('groups');
            const tid = idx >= 0 && idx + 1 < pathSegments.length ? pathSegments[idx + 1] : null;
            if (tid) {
                const saved = localStorage.getItem(`ai_task_chat_${tid}`);
                if (saved) {
                    return JSON.parse(saved).map((m: any) => ({
                        ...m,
                        timestamp: new Date(m.timestamp)
                    }));
                }
            }
        } catch (e) {
            console.error("Failed to map saved chat history", e);
        }
        return [];
    });
    const [loading, setLoading] = useState(false);
    const [trialActive, setTrialActive] = useState(true);
    const [trialDays, setTrialDays] = useState(30);

    const [showTokens, setShowTokens] = useState(false);
    const [showHistory, setShowHistory] = useState(false);
    const [selectedHistoryId, setSelectedHistoryId] = useState<string | null>(null);
    const totalTokens = messages.reduce((sum, message) => sum + estimateTokens(message.content), 0);

    const handleCopyMessage = (content: string) => {
        navigator.clipboard.writeText(content);
        alert('Đã copy nội dung!');
    };

    const handleDeleteMessage = (id: string) => {
        if (window.confirm('Bạn có chắc chắn muốn xóa đoạn chat này?')) {
            setMessages(prev => prev.filter(m => m.id !== id));
        }
    };

    const messagesEndRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (!teamId || teamId === 'undefined') {
            navigate('/groups');
            return;
        }
        teamService.getDetail(teamId).then(setTeam).catch(() => { });
        getTrialStatus().then(s => { 
            setTrialActive(s.aiTrialActive); 
            setTrialDays(s.daysRemaining); 
        }).catch(() => { });
    }, [teamId, navigate]);

    useEffect(() => {
        document.body.classList.add('task-studio-mode');
        return () => document.body.classList.remove('task-studio-mode');
    }, []);

    useEffect(() => {
        if (!categoryOpen) return;

        const handlePointerDown = (event: PointerEvent) => {
            if (!categoryMenuRef.current?.contains(event.target as Node)) {
                setCategoryOpen(false);
            }
        };


```
