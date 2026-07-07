# Knowledge Document: GroupDetailPage.tsx (Chunk 11/136)

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
  "chunk_index": 10,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
d, messageContent, chatTab === 'dm' && dmUserId ? dmUserId : undefined);
        setChatInput('');
        setChatAttachment(null);
        loadChatMessages();
    };

    const renderUnreadBadge = (count: number) => count > 0 ? (
        <span style={{
            minWidth: 20,
            height: 20,
            padding: '0 6px',
            borderRadius: 999,
            background: '#ef4444',
            color: '#fff',
            fontSize: 11,
            fontWeight: 800,
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            lineHeight: 1,
            boxShadow: '0 4px 10px rgba(239,68,68,0.28)'
        }}>{count > 99 ? '99+' : count}</span>
    ) : null;

    const closeModal = () => { setShowAddMember(false); setInviteEmail(''); setError(''); setSuccessMsg(''); };

    const handleInviteMember = async () => {
        if (!id || !inviteEmail.trim()) {
            setError('Vui lòng nhập email người được mời.');
            return;
        }
        try {
            setError('');
            setLoading(true);
            const result = await teamService.addMember(id, inviteEmail.trim());
            setSuccessMsg(result.message || 'Đã gửi lời mời.');
            setInviteEmail('');
            setTimeout(() => setSuccessMsg(''), 2500);
        } catch (e: any) {
            setError(e?.response?.data?.error || 'Không thể gửi lời mời.');
        } finally {
            setLoading(false);
        }
    };

    const toDatetimeInputValue = (value?: string) => {
        if (!value) return '';
        const date = new Date(value);
        if (Number.isNaN(date.getTime())) return '';
        const offset = date.getTimezoneOffset();
        const local = new Date(date.getTime() - offset * 60000);
        return local.toISOString().slice(0, 16);
    };

    const handleCreateGoal = async (useAi: boolean) => {
        if (!id || !goalTitle.trim()) return;
        if (useAi && !trialActive) { setError('AI đã hết hạn dùng thử!'); return; }
        setLoading(true);
        try {
            setError('');
            await goalService.create({ teamId: id, title: goalTitle, outputTarget: goalTarget, deadline: goalDeadline || undefined, useAi } as any);
            const g = await goalService.getByTeam(id);
            setGoals(g);

```
