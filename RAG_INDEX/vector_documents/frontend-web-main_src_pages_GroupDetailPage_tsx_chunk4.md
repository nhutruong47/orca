# Knowledge Document: GroupDetailPage.tsx (Chunk 5/136)

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
  "chunk_index": 4,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx

    const [unreadDmCounts, setUnreadDmCounts] = useState<Record<string, number>>({});
    const chatEndRef = useRef<HTMLDivElement>(null);
    const stompClientRef = useRef<Client | null>(null);

    // Refs for WebSocket callbacks to always have the latest state without resubscribing
    const chatTabRef = useRef<'group' | 'dm'>(chatTab);
    const dmUserIdRef = useRef<string | null>(dmUserId);
    const showChatRef = useRef(showChat);
    const unreadDmTotal = Object.values(unreadDmCounts).reduce((sum, count) => sum + count, 0);
    const unreadTotal = unreadGroupCount + unreadDmTotal;
    useEffect(() => { chatTabRef.current = chatTab; }, [chatTab]);
    useEffect(() => { dmUserIdRef.current = dmUserId; }, [dmUserId]);
    useEffect(() => { showChatRef.current = showChat; }, [showChat]);

    // Online presence + DM previews
    const [onlineUsers, setOnlineUsers] = useState<string[]>([]);
    const [dmPreviews, setDmPreviews] = useState<ChatMsg[]>([]);

    const currentMember = team?.members?.find(m => m.userId === user?.id);
    const isSystemAdmin = user?.role === 'ADMIN';
    const isAdmin = currentMember?.groupRole === 'ADMIN' || currentMember?.groupRole === 'OWNER' || team?.ownerId === user?.id;
    const isManager = !isSystemAdmin && isAdmin;

    useEffect(() => {
        if (!team || !user) return;
        setTaskFilter(isAdmin ? 'all' : 'my');
    }, [team?.id, user?.id, isAdmin]);

    useEffect(() => {
        if (!id) return;
        teamService.getDetail(id).then(data => {
            setTeam(data);
            if (data.metadata) {
                try {
                    const parsed = JSON.parse(data.metadata);
                    if (parsed.roles && Array.isArray(parsed.roles)) {
                        setTeamRoles(parsed.roles);
                    }
                } catch (e) { console.error('Error parsing metadata', e); }
            }
        }).catch(() => { });
        goalService.getByTeam(id).then(g => {
            setGoals(g);
            // Load all tasks for all goals
            Promise.all(g.map(goal => taskService.getByGoal(goal.id)))
                .then(taskArrays => setAllTasks(taskArrays.flat()))
                .catch(() => { });
        }).catch(() => { });

```
