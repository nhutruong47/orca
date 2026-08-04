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
import {
    Bar,
    BarChart,
    CartesianGrid,
    Cell,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from 'recharts';
import { useAuth } from '../context/AuthContext';
import { teamService, taskService, goalService } from '../services/groupService';
import type { Task, Team, Goal } from '../types/types';
import './DashboardPage.css';

const teamImages = [
    'https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?auto=format&fit=crop&w=900&q=84',
    'https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?auto=format&fit=crop&w=900&q=84',
    'https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=900&q=84',
];

interface TeamProductivityDatum {
    id: string;
    name: string;
    productivity: number;
    completedTasks: number;
    totalTasks: number;
}

interface ProductivityTooltipProps {
    active?: boolean;
    payload?: Array<{ payload: TeamProductivityDatum }>;
}

function getTeamTaskProgress(goals: Goal[]) {
    const totalTasks = goals.reduce((sum, goal) => sum + (goal.totalTasks || 0), 0);
    const completedTasks = Math.min(
        totalTasks,
        goals.reduce((sum, goal) => sum + (goal.completedTasks || 0), 0),
    );
    const productivity = totalTasks > 0
        ? Math.round((completedTasks / totalTasks) * 100)
        : 0;

    return { totalTasks, completedTasks, productivity };
}

function ProductivityTooltip({ active, payload }: ProductivityTooltipProps) {
    const datum = payload?.[0]?.payload;
    if (!active || !datum) return null;

    return (
        <div className="dashboard-productivity-tooltip">
            <strong>{datum.name}</strong>
            <span>{datum.productivity}% hoàn thành</span>
            <small>
                {datum.totalTasks > 0
                    ? `${datum.completedTasks}/${datum.totalTasks} công việc`
                    : 'Chưa có công việc'}
            </small>
        </div>
    );
}

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
    const [reduceMotion, setReduceMotion] = useState(() =>
        typeof window !== 'undefined'
        && typeof window.matchMedia === 'function'
        && window.matchMedia('(prefers-reduced-motion: reduce)').matches
    );

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
                    teamData.forEach((t: Team, i: number) => {
                        allGoals[t.id] = goalsArray[i] || [];
                    });
                    setTeamGoals(allGoals);
                });
            }
        }).finally(() => setLoading(false));
    }, [user?.id]);

    useEffect(() => {
        if (typeof window.matchMedia !== 'function') return;

        const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
        const handleMotionChange = (event: MediaQueryListEvent) => setReduceMotion(event.matches);
        motionQuery.addEventListener('change', handleMotionChange);
        return () => motionQuery.removeEventListener('change', handleMotionChange);
    }, []);

    const activeTasks = useMemo(() => myTasks.filter(task => task.status !== 'COMPLETED'), [myTasks]);
    const completedTasks = useMemo(() => myTasks.filter(task => task.status === 'COMPLETED'), [myTasks]);
    const progress = myTasks.length ? Math.round((completedTasks.length / myTasks.length) * 100) : 0;
    const recentTasks = myTasks.slice(0, 5);
    const displayName = user?.fullName || user?.username || 'ORCA';
    const primaryTeam = teams[0];
    const teamProductivityData = useMemo<TeamProductivityDatum[]>(() =>
        teams
            .map(team => {
                const { totalTasks, completedTasks, productivity } = getTeamTaskProgress(
                    teamGoals[team.id] || [],
                );
                return {
                    id: team.id,
                    name: team.name,
                    productivity,
                    completedTasks,
                    totalTasks,
                };
            })
            .sort((a, b) =>
                b.productivity - a.productivity
                || b.completedTasks - a.completedTasks
                || a.name.localeCompare(b.name, 'vi')
            ),
        [teamGoals, teams],
    );
    const productivityChartHeight = Math.max(240, teamProductivityData.length * 52);

    const goToTeamFeature = (featurePath: string) => {
        if (!primaryTeam) {
            navigate('/groups');
            return;
        }
        navigate(`/groups/${primaryTeam.id}${featurePath}`);
    };

    const quickActions = [
        {
            label: 'Tạo công việc',
            caption: primaryTeam ? 'Giao task trong nhóm đầu tiên' : 'Chọn nhóm để tạo task',
            icon: ClipboardList,
            onClick: () => goToTeamFeature('/create-task'),
        },
        {
            label: 'Đơn hàng',
            caption: 'Theo dõi mua bán và xử lý đơn',
            icon: PackageCheck,
            onClick: () => navigate('/orders'),
        },
        {
            label: 'Lịch sản xuất',
            caption: primaryTeam ? 'Xem lịch của nhóm gần nhất' : 'Cần có nhóm xưởng',
            icon: CalendarDays,
            onClick: () => goToTeamFeature('/calendar'),
        },
        {
            label: 'Nhân sự',
            caption: primaryTeam ? 'Chấm công và ca làm' : 'Cần có nhóm xưởng',
            icon: UserRoundCog,
            onClick: () => goToTeamFeature('/workforce'),
        },
        {
            label: 'Tin nhắn nhóm',
            caption: primaryTeam ? 'Mở nhóm và khung chat' : 'Cần có nhóm xưởng',
            icon: MessageCircle,
            onClick: () => goToTeamFeature(''),
        },
        {
            label: 'Thị trường',
            caption: 'Tìm xưởng và đơn hợp tác',
            icon: Store,
            onClick: () => navigate('/marketplace'),
        },
    ];

    const stats = [
        {
            label: 'Nhóm xưởng',
            value: teams.length,
            caption: 'Không gian đang tham gia',
            icon: Factory,
            tone: 'teal',
        },
        {
            label: 'Việc đang làm',
            value: activeTasks.length,
            caption: 'Cần theo dõi hôm nay',
            icon: ClipboardList,
            tone: 'amber',
        },
        {
            label: 'Tiến độ',
            value: `${progress}%`,
            caption: `${completedTasks.length}/${myTasks.length} công việc hoàn thành`,
            icon: CheckCircle2,
            tone: 'green',
        },
        {
            label: 'Lịch hôm nay',
            value: getTodayLabel(),
            caption: 'Cập nhật theo múi giờ Việt Nam',
            icon: CalendarDays,
            tone: 'blue',
        },
    ];

    const openTeamWorkspace = (teamId: string | number) => {
        navigate(`/groups/${teamId}`);
    };

    const currentHour = new Date().getHours();
    const isOverloaded = activeTasks.length > 0 && currentHour >= 17;
    const totalTarget = myTasks.reduce((sum, task) => sum + (task.outputTarget || 0), 0);
    const totalActual = myTasks.reduce((sum, task) => sum + (task.actualOutput || 0), 0);
    const isOverachieving = totalTarget > 0 && totalActual > totalTarget;

    if (loading) {
        return (
            <div className="dashboard-page dashboard-loading">
                <div className="btn-spinner" />
                <p>Đang tải dashboard...</p>
            </div>
        );
    }

    return (
        <div className="dashboard-page">
            <section className="dashboard-command">
                <div className="dashboard-command-main">
                    <span className="dashboard-eyebrow">Tổng quan vận hành</span>
                    <h1>Xin chào, {displayName}</h1>
                    <p>Theo dõi nhóm xưởng, tiến độ và việc cần xử lý trong ngày từ một màn hình gọn hơn.</p>
                    <div className="dashboard-command-actions">
                        <button className="dashboard-primary-action" onClick={() => navigate('/groups')} type="button">
                            <Plus size={18} />
                            Mở nhóm xưởng
                        </button>
                        <button onClick={() => goToTeamFeature('/create-task')} type="button">
                            <ClipboardList size={18} />
                            Tạo công việc
                        </button>
                    </div>
                </div>

                <div className={`dashboard-ops-card ${isOverachieving ? 'overachieving' : isOverloaded ? 'overloaded' : ''}`} aria-label="Trạng thái vận hành">
                    <div className="dashboard-ops-head">
                        <Activity size={18} />
                        <span>Nhịp vận hành</span>
                    </div>
                    <strong>{isOverachieving ? 'Phát triển vượt mong đợi' : isOverloaded ? 'Quá tải công việc' : activeTasks.length > 0 ? 'Đang có việc cần bám' : 'Không có việc quá tải'}</strong>
                    <p>{isOverachieving ? `Sản lượng đạt ${totalActual}/${totalTarget}, vượt mức kế hoạch đề ra.` : isOverloaded ? `Đã hết ngày nhưng còn ${activeTasks.length} task chưa xong.` : activeTasks.length > 0 ? `${activeTasks.length} task chưa hoàn thành.` : 'Bạn có thể tạo thêm kế hoạch hoặc kiểm tra nhóm xưởng.'}</p>
                    <div className="dashboard-progress-track">
                        <span style={{ width: `${progress}%`, background: isOverachieving ? 'var(--success)' : isOverloaded ? 'var(--danger)' : undefined }} />
                    </div>
                    <small style={{ color: isOverachieving ? 'var(--success)' : isOverloaded ? 'var(--danger)' : undefined }}>{progress}% hoàn thành</small>
                </div>
            </section>

            <section className="dashboard-quick-actions" aria-label="Lối tắt chức năng">
                {quickActions.map(action => {
                    const Icon = action.icon;
                    return (
                        <button key={action.label} type="button" onClick={action.onClick}>
                            <span className="dashboard-quick-icon">
                                <Icon size={18} />
                            </span>
                            <span>
                                <strong>{action.label}</strong>
                                <small>{action.caption}</small>
                            </span>
                        </button>
                    );
                })}
            </section>

            <section className="dashboard-stat-grid" aria-label="Tổng quan nhanh">
                {stats.map(stat => {
                    const Icon = stat.icon;
                    return (
                        <article className={`dashboard-stat-card ${stat.tone}`} key={stat.label}>
                            <div className="dashboard-stat-icon">
                                <Icon size={19} />
                            </div>
                            <div>
                                <span>{stat.label}</span>
                                <strong>{stat.value}</strong>
                                <p>{stat.caption}</p>
                            </div>
                        </article>
                    );
                })}
            </section>

            <div className="dashboard-workspace-grid">
                <section className="dashboard-panel dashboard-teams-panel">
                    <div className="dashboard-section-head">
                        <div>
                            <span>Không gian làm việc</span>
                            <h2>Nhóm đang vận hành</h2>
                        </div>
                        <button onClick={() => navigate('/groups')} type="button">
                            Xem tất cả
                            <ArrowRight size={16} />
                        </button>
                    </div>

                    {teams.length > 0 ? (
                        <div className="dashboard-team-list">
                            {teams.slice(0, 3).map((team, index) => {
                                const goals = teamGoals[team.id] || [];
                                const {
                                    totalTasks: totalTeamTasks,
                                    completedTasks: completedTeamTasks,
                                    productivity: teamProgress,
                                } = getTeamTaskProgress(goals);
                                const progressTone = totalTeamTasks === 0
                                    ? 'empty'
                                    : teamProgress >= 100
                                        ? 'complete'
                                        : 'active';
                                const statusColor = progressTone === 'complete'
                                    ? '#10b981'
                                    : progressTone === 'active'
                                        ? '#f59e0b'
                                        : '#a8a29e';
                                const statusTitle = progressTone === 'complete'
                                    ? 'Tất cả công việc đã hoàn thành'
                                    : progressTone === 'active'
                                        ? 'Nhóm đang thực hiện công việc'
                                        : 'Nhóm chưa có công việc';

                                return (
                                <article
                                    className="dashboard-team-card"
                                    key={team.id}
                                    role="button"
                                    tabIndex={0}
                                    onClick={() => openTeamWorkspace(team.id)}
                                    onKeyDown={(event) => {
                                        if (event.key === 'Enter' || event.key === ' ') {
                                            event.preventDefault();
                                            openTeamWorkspace(team.id);
                                        }
                                    }}
                                    aria-label={`Mở nơi làm việc của nhóm ${team.name}`}
                                    style={{ position: 'relative' }}
                                >
                                    <img src={teamImages[index % teamImages.length]} alt={team.name} />
                                    <div className="dashboard-team-body">
                                        <div>
                                            <h3 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                                {team.name}
                                                <span
                                                    style={{
                                                        display: 'inline-block',
                                                         width: 10,
                                                         height: 10,
                                                         borderRadius: '50%',
                                                         backgroundColor: statusColor,
                                                         boxShadow: `0 0 8px ${statusColor}66`,
                                                         flexShrink: 0
                                                     }}
                                                     title={statusTitle}
                                                 />
                                             </h3>
                                             <p>{team.description || team.specialty || 'Nhóm xưởng đang được quản lý trên ORCA.'}</p>
                                         </div>
                                         <div className="dashboard-team-progress">
                                             <div className="dashboard-team-progress-head">
                                                 <span>Tiến độ công việc</span>
                                                 <strong>{teamProgress}%</strong>
                                             </div>
                                             <div
                                                 className="dashboard-team-progress-track"
                                                 role="progressbar"
                                                 aria-label={`Tiến độ công việc của nhóm ${team.name}`}
                                                 aria-valuemin={0}
                                                 aria-valuemax={100}
                                                 aria-valuenow={teamProgress}
                                             >
                                                 <span
                                                     className={`dashboard-team-progress-fill ${progressTone}`}
                                                     style={{ width: `${teamProgress}%` }}
                                                 />
                                             </div>
                                             <small>
                                                 {totalTeamTasks > 0
                                                     ? `${completedTeamTasks}/${totalTeamTasks} công việc hoàn thành`
                                                     : 'Chưa có công việc'}
                                             </small>
                                         </div>
                                         <dl>
                                            <div>
                                                <dt>Thành viên</dt>
                                                <dd>{team.memberCount}</dd>
                                            </div>
                                            <div>
                                                <dt>Ngày tạo</dt>
                                                <dd>{formatDate(team.createdAt)}</dd>
                                            </div>
                                        </dl>
                                    </div>
                                </article>
                                );
                            })}
                        </div>
                    ) : (
                        <div className="dashboard-empty">
                            <Factory size={34} />
                            <h3>Chưa có nhóm xưởng</h3>
                            <p>Tạo nhóm đầu tiên để bắt đầu quản lý nhân sự, quy trình và công việc sản xuất.</p>
                            <button onClick={() => navigate('/groups')} type="button">Tạo nhóm</button>
                        </div>
                    )}
                </section>

                <section className="dashboard-panel dashboard-tasks-panel">
                    <div className="dashboard-section-head">
                        <div>
                            <span>Công việc</span>
                            <h2>Việc gần đây</h2>
                        </div>
                        <button onClick={() => goToTeamFeature('/create-task')} type="button">
                            Tạo công việc
                            <ArrowRight size={16} />
                        </button>
                    </div>

                    <div className="dashboard-task-list">
                        {recentTasks.length > 0 ? recentTasks.map(task => (
                            <article className="dashboard-task-row" key={task.id}>
                                <div className="dashboard-task-mark">
                                    {task.status === 'COMPLETED' ? <CheckCircle2 size={18} /> : <Clock3 size={18} />}
                                </div>
                                <div className="dashboard-task-copy">
                                    <h3>{task.title}</h3>
                                    <p>{task.description || task.goalTitle || 'Không có mô tả.'}</p>
                                </div>
                                <span className={`dashboard-task-status ${task.status.toLowerCase().replaceAll('_', '-')}`}>
                                    {statusText(task.status)}
                                </span>
                            </article>
                        )) : (
                            <div className="dashboard-empty dashboard-empty-compact">
                                <ClipboardList size={34} />
                                <h3>Chưa có công việc mới</h3>
                                <p>Khi có task được giao, danh sách sẽ hiện ở đây.</p>
                            </div>
                        )}
                    </div>
                </section>
            </div>

            {teamProductivityData.length > 0 && (
                <section
                    className="dashboard-panel dashboard-productivity-panel"
                    aria-labelledby="dashboard-productivity-title"
                >
                    <div className="dashboard-section-head dashboard-productivity-head">
                        <div>
                            <span>Hiệu suất vận hành</span>
                            <h2 id="dashboard-productivity-title">So sánh năng suất nhóm</h2>
                            <p>Tỷ lệ công việc hoàn thành trên tổng công việc của từng nhóm.</p>
                        </div>
                        <div className="dashboard-productivity-legend" aria-label="Chú thích biểu đồ">
                            <span><i className="active" />Đang thực hiện</span>
                            <span><i className="complete" />Hoàn thành 100%</span>
                            <span><i className="empty" />Chưa có công việc</span>
                        </div>
                    </div>

                    <div className="dashboard-productivity-chart">
                        <ResponsiveContainer width="100%" height={productivityChartHeight}>
                            <BarChart
                                data={teamProductivityData}
                                layout="vertical"
                                margin={{ top: 8, right: 34, bottom: 8, left: 8 }}
                                accessibilityLayer
                            >
                                <CartesianGrid
                                    stroke="var(--border)"
                                    strokeDasharray="4 4"
                                    horizontal={false}
                                />
                                <XAxis
                                    type="number"
                                    domain={[0, 100]}
                                    tickFormatter={value => `${value}%`}
                                    tick={{ fill: 'var(--text-muted)', fontSize: 11 }}
                                    axisLine={{ stroke: 'var(--border)' }}
                                    tickLine={false}
                                />
                                <YAxis
                                    type="category"
                                    dataKey="name"
                                    width={118}
                                    tickFormatter={value => value.length > 17 ? `${value.slice(0, 16)}…` : value}
                                    tick={{ fill: 'var(--text-primary)', fontSize: 12, fontWeight: 700 }}
                                    axisLine={false}
                                    tickLine={false}
                                />
                                <Tooltip
                                    content={<ProductivityTooltip />}
                                    cursor={{ fill: 'var(--accent-soft)', opacity: 0.45 }}
                                />
                                <Bar
                                    dataKey="productivity"
                                    name="Hoàn thành"
                                    unit="%"
                                    barSize={18}
                                    radius={[0, 8, 8, 0]}
                                    isAnimationActive={!reduceMotion}
                                    animationDuration={500}
                                >
                                    {teamProductivityData.map(team => (
                                        <Cell
                                            key={team.id}
                                            fill={team.totalTasks === 0
                                                ? 'var(--text-muted)'
                                                : team.productivity >= 100
                                                    ? 'var(--success)'
                                                    : 'var(--primary)'}
                                        />
                                    ))}
                                </Bar>
                            </BarChart>
                        </ResponsiveContainer>
                    </div>
                </section>
            )}
        </div>
    );
}
