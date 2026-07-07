# Knowledge Document: GroupDetailPage.tsx (Chunk 2/136)

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
  "chunk_index": 1,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
 default function GroupDetailPage() {
    const { id } = useParams<{ id: string }>();
    const { user } = useAuth();
    const navigate = useNavigate();
    const [team, setTeam] = useState<Team | null>(null);
    const [goals, setGoals] = useState<Goal[]>([]);
    const [allTasks, setAllTasks] = useState<Task[]>([]);
    const [selectedGoalId, setSelectedGoalId] = useState<string | null>(null);
    const [memberRoleFilter, setMemberRoleFilter] = useState<string>('ALL');
    const [teamRoles, setTeamRoles] = useState<string[]>([]);
    const [showManageRolesModal, setShowManageRolesModal] = useState(false);
    const [newRoleName, setNewRoleName] = useState('');
    const [showAddMember, setShowAddMember] = useState(false);
    const [inviteEmail, setInviteEmail] = useState('');
    const [showCreateGoal, setShowCreateGoal] = useState(false);
    const [goalTitle, setGoalTitle] = useState('');
    const [goalTarget, setGoalTarget] = useState('');
    const [goalDeadline, setGoalDeadline] = useState('');
    const [error, setError] = useState('');
    const [successMsg, setSuccessMsg] = useState('');
    const [loading, setLoading] = useState(false);
    const [trialActive, setTrialActive] = useState(true);
    const [trialDays, setTrialDays] = useState(30);
    const [showAddTask, setShowAddTask] = useState(false);
    const [newTaskTitle, setNewTaskTitle] = useState('');
    const [newTaskDesc, setNewTaskDesc] = useState('');
    const [newTaskWorkload, setNewTaskWorkload] = useState('');
    const [newTaskStage, setNewTaskStage] = useState('Roasting');
    const [newTaskUnit, setNewTaskUnit] = useState('');
    const [newTaskDueTime, setNewTaskDueTime] = useState('');
    const [newTaskPriority, setNewTaskPriority] = useState(2);
    const [editingTaskId, setEditingTaskId] = useState<string | null>(null);
    const [editTaskTitle, setEditTaskTitle] = useState('');
    const [editTaskDesc, setEditTaskDesc] = useState('');
    const [editTaskStage, setEditTaskStage] = useState('Roasting');
    const [editTaskDueTime, setEditTaskDueTime] = useState('');
    const [editTaskPriority, setEditTaskPriority] = useState(2);
    const [editTaskUnit, setEditTaskUnit] = useState('');

    const inferUnitFromText = (text: string, stage?: string): string => {
        const lower = (text || '').toLowerCase();
        const map: { keys: string[]; unit: string }[] = [

```
