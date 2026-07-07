# Knowledge Document: DashboardPage.tsx (Chunk 1/9)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "workspace",
  "tags": [
    "workspace",
    "factory",
    "dashboard",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, factory, dashboard, chat

## Source Code Chunk
```tsx
import { useEffect, useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
    Activity,
    ArrowRight,
    CalendarDays,
    CheckCircle2,
    ClipboardList,
    Clock3,
    Factory,
    MessageCircle,
    PackageCheck,
    Plus,
    UserRoundCog,
    Store,
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { teamService, taskService, goalService } from '../services/groupService';
import type { Task, Team, Goal } from '../types/types';
import './DashboardPage.css';

const teamImages = [
    'https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?auto=format&fit=crop&w=900&q=84',
    'https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?auto=format&fit=crop&w=900&q=84',
    'https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=900&q=84',
];

function statusText(status: string) {
    if (status === 'COMPLETED') return 'Hoàn thành';
    if (status === 'IN_PROGRESS') return 'Đang làm';
    return 'Chờ xử lý';
}

function formatDate(value: string | null | undefined) {
    if (!value) return '-';
    return new Date(value).toLocaleDateString('vi-VN', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
    });
}

function getTodayLabel() {
    return new Date().toLocaleDateString('vi-VN', {
        weekday: 'long',
        day: '2-digit',
        month: '2-digit',
    });
}

export default function DashboardPage() {
    const { user } = useAuth();
    const navigate = useNavigate();
    const [teams, setTeams] = useState<Team[]>([]);
    const [myTasks, setMyTasks] = useState<Task[]>([]);
    const [teamGoals, setTeamGoals] = useState<Record<string, Goal[]>>({});
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        Promise.all([
            teamService.getMyTeams().catch(() => []),
            user?.id ? taskService.getMyTasks(user.id).catch(() => []) : Promise.resolve([]),
        ]).then(([teamData, tasksData]) => {
            setTeams(teamData || []);
            setMyTasks(tasksData || []);
            if (teamData && teamData.length > 0) {
                Promise.all(teamData.map((t: Team) => goalService.getByTeam(t.id).catch(() => [])))
                .then(goalsArray => {
                    const allGoals: Record<string, Goal[]> = {};

```
