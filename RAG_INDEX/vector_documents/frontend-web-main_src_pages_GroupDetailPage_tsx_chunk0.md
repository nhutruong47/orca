# Knowledge Document: GroupDetailPage.tsx (Chunk 1/136)

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
  "chunk_index": 0,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
import { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { teamService, goalService, taskService, getTrialStatus, chatService, inventoryService } from '../services/groupService';
import { attendanceService } from '../services/attendanceService';
import type { Team, Goal, Task, ChatMsg, SalaryReport, AiChatLogMsg } from '../types/types';

import SockJS from 'sockjs-client';
import { Client } from '@stomp/stompjs';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { estimateTokens, formatTokenCount } from '../utils/tokenUsage';

function getInitials(name: string) {
    return name.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();
}
function avatarColor(name: string) {
    const colors = ['#d4a574', '#8b5cf6', '#ec4899', '#f43f5e', '#f59e0b', '#10b981', '#06b6d4', '#3b82f6'];
    let hash = 0;
    for (const c of name) hash = (hash * 31 + c.charCodeAt(0)) % colors.length;
    return colors[hash];
}
const STATUS_COLORS: Record<string, { bg: string; color: string; label: string }> = {
    PENDING: { bg: '#fef3c7', color: '#d97706', label: 'Chờ xử lý' },
    IN_PROGRESS: { bg: '#dbeafe', color: '#2563eb', label: 'Đang làm' },
    COMPLETED: { bg: '#dcfce7', color: '#16a34a', label: 'Hoàn thành' },
};
Object.assign(STATUS_COLORS, {
    PENDING: { bg: '#f8fafc', color: '#64748b', label: 'Cho xu ly' },
    BLOCKED: { bg: '#fee2e2', color: '#dc2626', label: 'Bi khoa' },
    READY: { bg: '#dcfce7', color: '#16a34a', label: 'San sang' },
    WAITING_APPROVAL: { bg: '#fef3c7', color: '#d97706', label: 'Cho duyet' },
    COMPLETED: { bg: '#dcfce7', color: '#16a34a', label: 'Hoan thanh' },
    CANCELLED: { bg: '#f1f5f9', color: '#64748b', label: 'Da huy' },
});
const MEMBER_COLORS = ['#d4a574', '#f59e0b', '#10b981', '#ec4899', '#f43f5e', '#06b6d4', '#8b5cf6', '#3b82f6'];




export default function GroupDetailPage() {
    const { id } = useParams<{ id: string }>();
    const { user } = useAuth();
    const navigate = useNavigate();
    const [team, setTeam] = useState<Team | null>(null);
    const [goals, setGoals] = useState<Goal[]>([]);
    const [allTasks, setAllTasks] = useState<Task[]>([]);
    const [selectedGoalId, setSelectedGoalId] = useState<string | null>(null);

```
