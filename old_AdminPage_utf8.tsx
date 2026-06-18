import { useEffect, useMemo, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import {
  Activity,
  AlertTriangle,
  BellRing,
  Brain,
  Building2,
  CalendarDays,
  CheckCircle2,
  Cpu,
  CreditCard,
  Database,
  DollarSign,
  Download,
  FileBarChart,
  Filter,
  Gauge,
  GitBranch,
  GripVertical,
  Lock,
  MoreHorizontal,
  Plus,
  ReceiptText,
  RotateCcw,
  Search,
  Server,
  Settings,
  ShieldCheck,
  ShoppingCart,
  Unlock,
  Users,
  Workflow,
  XCircle
} from 'lucide-react';
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Line,
  LineChart,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from 'recharts';
import { useAuth } from '../context/AuthContext';
import { adminService } from '../services/adminService';
import type { AdminOrder, AdminOverview, AdminPayment, AdminTask, AdminTeam, AdminUser } from '../types/types';
import './AdminPage.css';

type AdminSection =
  | 'overview'
  | 'businesses'
  | 'users'
  | 'subscriptions'
  | 'billing'
  | 'ai'
  | 'monitoring'
  | 'audit'
  | 'workflow'
  | 'alerts'
  | 'reports';

type Severity = 'Critical' | 'High' | 'Medium' | 'Low';

const money = (value: number) =>
  new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND', maximumFractionDigits: 0 }).format(value);

const number = (value: number) => new Intl.NumberFormat('vi-VN').format(value);

const parseDateInput = (value: string, endOfDay = false) => {
  const date = new Date(`${value}T${endOfDay ? '23:59:59' : '00:00:00'}`);
  return Number.isNaN(date.getTime()) ? new Date() : date;
};

const formatInputDate = (date: Date) => date.toISOString().slice(0, 10);

const tabs: Array<{ id: AdminSection; label: string; icon: React.ElementType }> = [
  { id: 'overview', label: 'Tß╗òng quan', icon: Gauge },
  { id: 'businesses', label: 'Doanh nghiß╗çp / X╞░ß╗ƒng', icon: Building2 },
  { id: 'users', label: 'Ng╞░ß╗¥i d├╣ng to├án hß╗ç thß╗æng', icon: Users },
  { id: 'subscriptions', label: 'G├│i dß╗ïch vß╗Ñ', icon: ReceiptText },
  { id: 'billing', label: 'Thanh to├ín', icon: CreditCard },
  { id: 'ai', label: 'Quß║ún l├╜ AI', icon: Brain },
  { id: 'monitoring', label: 'Gi├ím s├ít hß╗ç thß╗æng', icon: Activity },
  { id: 'audit', label: 'Nhß║¡t k├╜ kiß╗âm to├ín', icon: ShieldCheck },
  { id: 'workflow', label: 'Quy tr├¼nh', icon: Workflow },
  { id: 'alerts', label: 'Trung t├óm cß║únh b├ío', icon: BellRing },
  { id: 'reports', label: 'B├ío c├ío ─æiß╗üu h├ánh', icon: FileBarChart }
];

type KpiTone = 'coffee' | 'blue' | 'amber' | 'green' | 'violet';

type KpiItem = {
  label: string;
  value: string;
  detail: string;
  icon: React.ElementType;
  tone: KpiTone;
};

const emptyOverview: AdminOverview = {
  totalUsers: 0,
  adminUsers: 0,
  memberUsers: 0,
  newUsersThisMonth: 0,
  newUsersPreviousMonth: 0,
  totalTeams: 0,
  publishedTeams: 0,
  newTeamsThisMonth: 0,
  newTeamsPreviousMonth: 0,
  totalGoals: 0,
  activeGoals: 0,
  totalTasks: 0,
  completedTasks: 0,
  overdueTasks: 0,
  totalOrders: 0,
  activeOrders: 0,
  totalProductionOrders: 0,
  activeProductionOrders: 0,
  overdueProductionOrders: 0,
  totalBatches: 0,
  activeBatches: 0,
  completedBatches: 0,
  paidPayments: 0,
  totalPayments: 0,
  revenueThisMonth: 0,
  revenuePreviousMonth: 0,
  revenueThisYear: 0,
  revenuePreviousYear: 0,
  revenueTotal: 0,
  orderStatusCounts: {},
  productionOrderStatusCounts: {},
  batchStatusCounts: {},
  taskStatusCounts: {},
  recentUsers: [],
  recentTeams: [],
};

const realDataNote = 'Tß╗½ dß╗» liß╗çu hß╗ç thß╗æng';





const getDate = (value: string | null | undefined) => {
  if (!value) return null;
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? null : date;
};

const sameMonth = (value: string | null | undefined, monthDate: Date) => {
  const date = getDate(value);
  return Boolean(date && date.getFullYear() === monthDate.getFullYear() && date.getMonth() === monthDate.getMonth());
};

const paymentDate = (payment: AdminPayment) => getDate(payment.paidAt || payment.createdAt);

const formatShortDate = (value: Date | string | null | undefined) => {
  const date = value instanceof Date ? value : getDate(value);
  return date ? date.toLocaleDateString('vi-VN') : '-';
};

const paymentCustomerName = (payment: AdminPayment) =>
  payment.fullName || payment.username || payment.email || 'Kh├┤ng r├╡ ng╞░ß╗¥i d├╣ng';

const buildKpis = (overview: AdminOverview): KpiItem[] => [
  { label: 'Doanh nghiß╗çp / x╞░ß╗ƒng', value: number(overview.totalTeams), detail: realDataNote, icon: Building2, tone: 'coffee' },
  { label: 'Tß╗òng ng╞░ß╗¥i d├╣ng', value: number(overview.totalUsers), detail: realDataNote, icon: Users, tone: 'blue' },
  { label: '─É╞ín ─æang xß╗¡ l├╜', value: number(overview.activeOrders + overview.activeProductionOrders), detail: '─É╞ín li├¬n x╞░ß╗ƒng + ─æ╞ín sß║ún xuß║Ñt', icon: ShoppingCart, tone: 'amber' },
  { label: 'Batch sß║ún xuß║Ñt', value: number(overview.totalBatches), detail: `${number(overview.activeBatches)} batch ─æang chß║íy`, icon: GitBranch, tone: 'green' }
];

const plans = [
  { name: 'C╞í bß║ún', price: 499000, period: 'Th├íng', users: 5, orders: 100, batches: 300, workshops: 1, ai: 5000, features: ['Bß║úng ─æ╞ín h├áng', 'Theo d├╡i l├┤ sß║ún xuß║Ñt', 'B├ío c├ío c╞í bß║ún'] },
  { name: 'T─âng tr╞░ß╗ƒng', price: 1499000, period: 'Th├íng', users: 30, orders: 1000, batches: 5000, workshops: 5, ai: 40000, features: ['Quy tr├¼nh QC', 'Trß╗ú l├╜ AI', 'Xuß║Ñt dß╗» liß╗çu thanh to├ín'] },
  { name: 'Doanh nghiß╗çp', price: 0, period: 'N─âm', users: 500, orders: 99999, batches: 99999, workshops: 50, ai: 500000, features: ['Cam kß║┐t dß╗ïch vß╗Ñ', 'Quy tr├¼nh t├╣y chß╗ënh', 'Giß╗¢i hß║ín AI ri├¬ng'] }
];

const systemMetrics = [
  { name: 'CPU', value: 68, icon: Cpu, tone: 'warning' },
  { name: 'RAM', value: 74, icon: Server, tone: 'warning' },
  { name: 'C╞í sß╗ƒ dß╗» liß╗çu', value: 42, icon: Database, tone: 'success' },
  { name: 'Y├¬u cß║ºu API', value: 81, icon: Activity, tone: 'danger' },
  { name: 'Tß╗╖ lß╗ç lß╗ùi', value: 2.8, icon: XCircle, tone: 'danger' },
  { name: 'Response Time', value: 184, icon: Gauge, tone: 'success' }
];

const realtimeData = [
  { time: '10:00', cpu: 44, ram: 58, api: 320, errors: 0.8 },
  { time: '10:05', cpu: 52, ram: 61, api: 390, errors: 1.1 },
  { time: '10:10', cpu: 68, ram: 67, api: 470, errors: 2.4 },
  { time: '10:15', cpu: 61, ram: 72, api: 430, errors: 1.7 },
  { time: '10:20', cpu: 74, ram: 76, api: 510, errors: 2.8 }
];

const auditLogs = [
  ['An Nguyen', '─É─âng nhß║¡p quß║ún trß╗ï', 'Bß║úng quß║ún trß╗ï', '02/06/2026 10:20', '14.169.2.10'],
  ['Bao Tran', 'Tß║ío ─æ╞ín h├áng', 'ORD-2092', '02/06/2026 10:14', '14.169.2.11'],
  ['Chi Le', 'Sß╗¡a batch', 'BATCH-842', '02/06/2026 09:58', '42.113.9.42'],
  ['Duy Pham', 'X├│a dß╗» liß╗çu', 'Workshop draft', '02/06/2026 09:35', '42.113.9.49'],
  ['Admin', '─Éß╗òi quyß╗ün', 'Manager -> Staff', '02/06/2026 09:02', '10.0.0.1']
].map(([user, action, target, time, ip]) => ({ user, action, target, time, ip }));

const alertRows: Array<{ title: string; source: string; severity: Severity; time: string }> = [
  { title: '─É╞ín h├áng OR-2041 trß╗à hß║ín 14 giß╗¥', source: 'Order SLA', severity: 'Critical', time: '2 ph├║t tr╞░ß╗¢c' },
  { title: 'Batch B-842 lß╗ùi QC lß║ºn 2', source: 'QC Engine', severity: 'High', time: '8 ph├║t tr╞░ß╗¢c' },
  { title: 'Subscription Ancient Grain hß║┐t hß║ín trong 3 ng├áy', source: 'Billing', severity: 'Medium', time: '21 ph├║t tr╞░ß╗¢c' },
  { title: 'X╞░ß╗ƒng ─É├á Lß║ít v╞░ß╗út 88% c├┤ng suß║Ñt', source: 'Capacity', severity: 'High', time: '38 ph├║t tr╞░ß╗¢c' },
  { title: 'User staff17 bß╗ï kh├│a do ─æ─âng nhß║¡p sai', source: 'Security', severity: 'Low', time: '1 giß╗¥ tr╞░ß╗¢c' },
  { title: 'API /ai/recommend response time cao', source: 'System', severity: 'Critical', time: '1 giß╗¥ tr╞░ß╗¢c' }
];

const featureRows = [
  'Quß║ún l├╜ ─æ╞ín h├áng',
  'Theo d├╡i l├┤ sß║ún xuß║Ñt',
  'Quy tr├¼nh QC',
  'Trß╗ú l├╜ AI',
  'Xuß║Ñt dß╗» liß╗çu thanh to├ín',
  'Quy tr├¼nh t├╣y chß╗ënh',
  'Hß╗ù trß╗ú ri├¬ng'
];

function KpiCard({ item }: { item: KpiItem }) {
  const Icon = item.icon;
  return (
    <article className={`admin-kpi admin-kpi-${item.tone}`}>
      <div className="admin-kpi-icon"><Icon size={20} /></div>
      <div>
        <span>{item.label}</span>
        <strong>{item.value}</strong>
        <small>{item.detail}</small>
      </div>
    </article>
  );
}

function MiniMetric({ label, value, icon: Icon }: { label: string; value: string; icon: React.ElementType }) {
  return (
    <article className="admin-mini-metric">
      <Icon size={18} />
      <span>{label}</span>
      <strong>{value}</strong>
    </article>
  );
}

function ChartPanel({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="admin-card admin-chart-card">
      <div className="admin-card-head">
        <h3>{title}</h3>
        <button type="button" className="admin-icon-button"><MoreHorizontal size={16} /></button>
      </div>
      <div className="admin-chart">{children}</div>
    </section>
  );
}

function StatusBadge({ value }: { value: string }) {
  const labels: Record<string, string> = {
    Critical: 'Nghi├¬m trß╗ìng',
    High: 'Cao',
    Medium: 'Trung b├¼nh',
    Low: 'Thß║Ñp',
    Active: '─Éang hoß║ít ─æß╗Öng',
    Trial: 'D├╣ng thß╗¡',
    Locked: '─É├ú kh├│a',
    APPROVED: '─É├ú duyß╗çt',
    PENDING: 'Chß╗¥ duyß╗çt',
    REJECTED: 'Tß╗½ chß╗æi',
    ACCEPTED: '─É├ú nhß║¡n',
    COMPLETED: 'Ho├án th├ánh',
    CANCELED: '─É├ú hß╗ºy',
    REJECTED_ORDER: 'Tß╗½ chß╗æi',
    free: 'Miß╗àn ph├¡',
  };
  return <span className={`admin-badge admin-badge-${value.toLowerCase().replaceAll(' ', '-')}`}>{labels[value] || value}</span>;
}

export default function AdminPage() {
  const { user } = useAuth();
  const [searchParams] = useSearchParams();
  const sectionParam = searchParams.get('section') as AdminSection | null;
  const active: AdminSection = tabs.some(tab => tab.id === sectionParam) ? sectionParam! : 'overview';
  const [overview, setOverview] = useState<AdminOverview>(emptyOverview);
  const [adminUsers, setAdminUsers] = useState<AdminUser[]>([]);
  const [adminTeams, setAdminTeams] = useState<AdminTeam[]>([]);
  const [adminOrders, setAdminOrders] = useState<AdminOrder[]>([]);
  const [adminTasks, setAdminTasks] = useState<AdminTask[]>([]);
  const [adminPayments, setAdminPayments] = useState<AdminPayment[]>([]);
  const [adminLoading, setAdminLoading] = useState(true);
  const [adminError, setAdminError] = useState('');
  const [query, setQuery] = useState('');
  const [status, setStatus] = useState('All');
  const [plan, setPlan] = useState('All');
  const [revenueFrom, setRevenueFrom] = useState('2026-05-01');
  const [revenueTo, setRevenueTo] = useState('2026-06-30');
  const [userPage, setUserPage] = useState(1);
  const [workflowStages, setWorkflowStages] = useState(['─É╞ín h├áng', 'Ph├ón c├┤ng', 'Sß║ún xuß║Ñt', 'QC', '─É├│ng g├│i', 'Giao h├áng']);
  const [dragIndex, setDragIndex] = useState<number | null>(null);

  useEffect(() => {
    if (user?.role !== 'ADMIN') {
      setAdminLoading(false);
      return;
    }

    setAdminLoading(true);
    setAdminError('');
    Promise.all([
      adminService.getOverview(),
      adminService.getUsers(),
      adminService.getTeams(),
      adminService.getOrders(),
      adminService.getTasks(),
      adminService.getPayments(),
    ])
      .then(([overviewData, userData, teamData, orderData, taskData, paymentData]) => {
        setOverview({ ...emptyOverview, ...overviewData });
        setAdminUsers(userData || []);
        setAdminTeams(teamData || []);
        setAdminOrders(orderData || []);
        setAdminTasks(taskData || []);
        setAdminPayments(paymentData || []);
      })
      .catch(() => {
        setAdminError('Kh├┤ng tß║úi ─æ╞░ß╗úc thß╗æng k├¬ thß║¡t tß╗½ hß╗ç thß╗æng.');
      })
      .finally(() => setAdminLoading(false));
  }, [user?.role]);

  const kpis = useMemo(() => buildKpis(overview), [overview]);

  const systemTrendData = useMemo(() => {
    const now = new Date();
    return Array.from({ length: 6 }, (_, offset) => {
      const monthDate = new Date(now.getFullYear(), now.getMonth() - (5 - offset), 1);
      return {
        month: `T${monthDate.getMonth() + 1}`,
        users: adminUsers.filter(item => sameMonth(item.createdAt, monthDate)).length,
        teams: adminTeams.filter(item => sameMonth(item.createdAt, monthDate)).length,
        orders: adminOrders.filter(item => sameMonth(item.createdAt, monthDate)).length,
        tasks: adminTasks.filter(item => sameMonth(item.createdAt, monthDate)).length,
      };
    });
  }, [adminUsers, adminTeams, adminOrders, adminTasks]);

  const aiUsage = useMemo(() => {
    const paidUsers = adminUsers.filter(item => item.aiPlan && item.aiPlan !== 'free');
    const freeUsers = adminUsers.filter(item => !item.aiPlan || item.aiPlan === 'free');
    const planCount = new Set(adminUsers.map(item => item.aiPlan || 'free')).size;
    return [
      { label: 'Tß╗òng user', value: number(adminUsers.length), icon: Users },
      { label: 'User c├│ g├│i AI', value: number(paidUsers.length), icon: Brain },
      { label: 'User g├│i free', value: number(freeUsers.length), icon: Gauge },
      { label: 'Loß║íi g├│i ─æang c├│', value: number(planCount), icon: ReceiptText },
    ];
  }, [adminUsers]);

  const userRows = useMemo(() => {
    return adminUsers
      .map(item => ({
        id: item.id,
        name: item.fullName || item.username,
        email: item.email,
        phone: item.chipId || '-',
        company: '-',
        role: item.role,
        status: item.aiPlan || 'free',
        lastLogin: item.createdAt ? formatShortDate(item.createdAt) : '-'
      }))
      .filter(item => `${item.name} ${item.email} ${item.role}`.toLowerCase().includes(query.toLowerCase()))
      .slice((userPage - 1) * 6, userPage * 6);
  }, [adminUsers, query, userPage]);

  const businessRows = adminTeams.map(item => ({
    id: item.id,
    name: item.name,
    code: item.id.slice(0, 8),
    owner: item.ownerName || '-',
    email: '-',
    phone: '-',
    employees: item.memberCount,
    orders: item.totalOrders,
    batches: 0,
    plan: '-',
    date: item.createdAt ? formatShortDate(item.createdAt) : '-',
    status: item.published ? 'Published' : 'Private',
    verificationStatus: item.verificationStatus || 'NOT_SUBMITTED',
    businessLicense: item.businessLicense || '',
    businessAddress: item.businessAddress || '',
    websiteUrl: item.websiteUrl || '',
    certificationDocument: item.certificationDocument || '',
    verificationRejectReason: item.verificationRejectReason || ''
  })).filter(item => {
    const matchesText = `${item.name} ${item.code} ${item.owner}`.toLowerCase().includes(query.toLowerCase());
    const matchesStatus = status === 'All' || item.status === status;
    const matchesPlan = plan === 'All' || item.plan === plan;
    return matchesText && matchesStatus && matchesPlan;
  });

  const updateTeamVerification = async (teamId: string, nextStatus: 'APPROVED' | 'REJECTED') => {
    const rejectReason = nextStatus === 'REJECTED'
      ? window.prompt('L├╜ do tß╗½ chß╗æi hß╗ô s╞í x├íc minh?', 'Hß╗ô s╞í ch╞░a ─æß╗º th├┤ng tin.')
      : '';
    if (nextStatus === 'REJECTED' && rejectReason === null) return;
    try {
      const updated = await adminService.updateTeamVerification(teamId, nextStatus, rejectReason || '');
      setAdminTeams(current => current.map(item => item.id === teamId ? { ...item, ...updated } : item));
    } catch {
      window.alert('Kh├┤ng thß╗â cß║¡p nhß║¡t trß║íng th├íi x├íc minh.');
    }
  };

  const revenueReport = useMemo(() => {
    const fromDate = parseDateInput(revenueFrom);
    const toDate = parseDateInput(revenueTo, true);
    const safeFrom = fromDate <= toDate ? fromDate : toDate;
    const safeTo = fromDate <= toDate ? toDate : fromDate;
    const rangePayments = adminPayments.filter(item => {
      const date = paymentDate(item);
      return Boolean(date && date >= safeFrom && date <= safeTo);
    });
    const paidPayments = rangePayments.filter(item => item.status === 'PAID');
    const total = paidPayments.reduce((sum, item) => sum + Number(item.amount), 0);
    const pending = rangePayments
      .filter(item => item.status === 'PENDING')
      .reduce((sum, item) => sum + Number(item.amount), 0);
    const failed = rangePayments
      .filter(item => item.status === 'FAILED')
      .reduce((sum, item) => sum + Number(item.amount), 0);
    const dailyMap = paidPayments.reduce<Record<string, { amount: number; time: number }>>((acc, item) => {
      const date = paymentDate(item);
      const dateKey = formatShortDate(date);
      const current = acc[dateKey] || { amount: 0, time: date?.getTime() || 0 };
      acc[dateKey] = { amount: current.amount + Number(item.amount), time: current.time };
      return acc;
    }, {});
    const timeline = Object.entries(dailyMap)
      .map(([date, data]) => ({ date, revenue: Math.round(data.amount / 1000000), time: data.time }))
      .sort((a, b) => a.time - b.time);
    const customerMap = paidPayments.reduce<Record<string, number>>((acc, item) => {
      const name = paymentCustomerName(item);
      acc[name] = (acc[name] || 0) + Number(item.amount);
      return acc;
    }, {});
    const topCustomers = Object.entries(customerMap)
      .map(([name, value]) => ({ name, value: Math.round(value / 1000000), amount: value }))
      .sort((a, b) => b.amount - a.amount)
      .slice(0, 5);
    const rangeDays = Math.max(1, Math.ceil((safeTo.getTime() - safeFrom.getTime()) / 86400000));

    return {
      fromDate: safeFrom,
      toDate: safeTo,
      rangeInvoices: rangePayments,
      paidInvoices: paidPayments,
      total,
      pending,
      failed,
      rangeDays,
      averagePerDay: Math.round(total / rangeDays),
      topCustomers,
      timeline: timeline.length > 0 ? timeline : [{ date: 'Kh├┤ng c├│', revenue: 0 }],
    };
  }, [adminPayments, revenueFrom, revenueTo]);

  const exportRevenueReport = () => {
    const lines = [
      'ORCA - Bao cao doanh thu',
      `Tu ngay: ${formatInputDate(revenueReport.fromDate)}`,
      `Den ngay: ${formatInputDate(revenueReport.toDate)}`,
      `Doanh thu da thu: ${money(revenueReport.total)}`,
      `Dang cho thanh toan: ${money(revenueReport.pending)}`,
      `That bai: ${money(revenueReport.failed)}`,
      '',
      'Hoa don:',
      ...revenueReport.rangeInvoices.map(item => `${item.txnRef}, ${paymentCustomerName(item)}, ${item.planId}, ${money(Number(item.amount))}, ${formatShortDate(paymentDate(item))}, ${item.bankCode || '-'}, ${item.status}`),
    ];
    const blob = new Blob([lines.join('\n')], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `orca-revenue-${revenueFrom}-${revenueTo}.txt`;
    link.click();
    URL.revokeObjectURL(url);
  };

  const moveStage = (from: number, to: number) => {
    if (from === to) return;
    setWorkflowStages(current => {
      const next = [...current];
      const [item] = next.splice(from, 1);
      next.splice(to, 0, item);
      return next;
    });
  };

  if (user?.role !== 'ADMIN') {
    return (
      <div className="admin-access">
        <ShieldCheck size={40} />
        <h1>Kh├┤ng c├│ quyß╗ün truy cß║¡p bß║úng quß║ún trß╗ï</h1>
        <p>T├ái khoß║ún hiß╗çn tß║íi cß║ºn vai tr├▓ quß║ún trß╗ï vi├¬n ─æß╗â xem dß╗» liß╗çu to├án nß╗ün tß║úng.</p>
      </div>
    );
  }

  if (adminLoading) {
    return (
      <div className="admin-access">
        <Activity size={40} />
        <h1>─Éang tß║úi thß╗æng k├¬ hß╗ç thß╗æng</h1>
        <p>ORCA ─æang lß║Ñy sß╗æ liß╗çu thß║¡t tß╗½ c╞í sß╗ƒ dß╗» liß╗çu.</p>
      </div>
    );
  }

  if (adminError) {
    return (
      <div className="admin-access">
        <AlertTriangle size={40} />
        <h1>Kh├┤ng tß║úi ─æ╞░ß╗úc thß╗æng k├¬</h1>
        <p>{adminError}</p>
      </div>
    );
  }

  return (
    <div className="admin-console">
      <header className="admin-hero">
        <div>
          <span className="admin-eyebrow">Quß║ún trß╗ï ORCA SaaS</span>
          <h1>Tß╗òng quan hß╗ç thß╗æng</h1>
          <p>Trung t├óm ─æiß╗üu h├ánh cho Coffee Production Management Platform: doanh nghiß╗çp, user, billing, AI, monitoring, audit v├á b├ío c├ío ─æiß╗üu h├ánh.</p>
        </div>
        <div className="admin-hero-actions">
          <button type="button" className="admin-button admin-button-soft"><CalendarDays size={16} /> 30 ng├áy</button>
          <button type="button" className="admin-button admin-button-primary"><Download size={16} /> Xuß║Ñt b├ío c├ío</button>
        </div>
      </header>

      {active === 'overview' && (
        <>
          <section className="admin-kpi-grid">
            {kpis.map(item => <KpiCard key={item.label} item={item} />)}
          </section>
          <section className="admin-grid-2">
            <ChartPanel title="─É╞ín ph├ít sinh theo th├íng">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={systemTrendData}>
                  <defs>
                    <linearGradient id="revenueFill" x1="0" x2="0" y1="0" y2="1">
                      <stop offset="0%" stopColor="#d4a574" stopOpacity={0.45} />
                      <stop offset="100%" stopColor="#d4a574" stopOpacity={0.02} />
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Area dataKey="orders" stroke="#d4a574" fill="url(#revenueFill)" strokeWidth={3} />
                </AreaChart>
              </ResponsiveContainer>
            </ChartPanel>
            <ChartPanel title="User mß╗¢i theo th├íng">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={systemTrendData}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Line dataKey="users" stroke="#60a5fa" strokeWidth={3} dot={false} />
                </LineChart>
              </ResponsiveContainer>
            </ChartPanel>
            <ChartPanel title="X╞░ß╗ƒng mß╗¢i theo th├íng">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={systemTrendData}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="teams" fill="#8b5cf6" radius={[8, 8, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </ChartPanel>
            <ChartPanel title="C├┤ng viß╗çc tß║ío theo th├íng">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={systemTrendData}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="tasks" fill="#22c55e" radius={[8, 8, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </ChartPanel>
          </section>
          <section className="admin-card">
            <div className="admin-card-head">
              <h3>Danh s├ích cß║únh b├ío hß╗ç thß╗æng</h3>
              <button type="button" className="admin-button admin-button-soft">Xem tß║Ñt cß║ú</button>
            </div>
            <div className="admin-alert-list">
              {alertRows.slice(0, 5).map(item => (
                <div key={item.title} className={`admin-alert admin-alert-${item.severity.toLowerCase()}`}>
                  <AlertTriangle size={18} />
                  <div><strong>{item.title}</strong><span>{item.source} ┬╖ {item.time}</span></div>
                  <StatusBadge value={item.severity} />
                </div>
              ))}
            </div>
          </section>
        </>
      )}

      {active === 'businesses' && (
        <section className="admin-card">
          <div className="admin-card-head">
            <div><h3>Quß║ún l├╜ doanh nghiß╗çp / x╞░ß╗ƒng</h3><p>Xem, th├¬m, chß╗ënh sß╗¡a, kh├│a hoß║╖c x├│a doanh nghiß╗çp.</p></div>
            <button type="button" className="admin-button admin-button-primary"><Plus size={16} /> Th├¬m doanh nghiß╗çp</button>
          </div>
          <div className="admin-toolbar">
            <label><Search size={16} /><input value={query} onChange={event => setQuery(event.target.value)} placeholder="T├¼m t├¬n, m├ú, ng╞░ß╗¥i ─æß║íi diß╗çn..." /></label>
            <select value={status} onChange={event => setStatus(event.target.value)}><option value="All">Tß║Ñt cß║ú</option><option value="Active">─Éang hoß║ít ─æß╗Öng</option><option value="Trial">D├╣ng thß╗¡</option><option value="Locked">─É├ú kh├│a</option></select>
            <select value={plan} onChange={event => setPlan(event.target.value)}><option value="All">Tß║Ñt cß║ú</option><option value="Starter">C╞í bß║ún</option><option value="Growth">T─âng tr╞░ß╗ƒng</option><option value="Enterprise">Doanh nghiß╗çp</option></select>
            <button type="button" className="admin-button admin-button-soft"><Filter size={16} /> Ng├áy ─æ─âng k├╜</button>
          </div>
          <div className="admin-table-wrap">
            <table className="admin-table">
              <thead><tr><th>T├¬n doanh nghiß╗çp</th><th>M├ú</th><th>─Éß║íi diß╗çn</th><th>Email</th><th>─Éiß╗çn thoß║íi</th><th>NV</th><th>─É╞ín</th><th>Batch</th><th>G├│i</th><th>Ng├áy ─ÉK</th><th>Trß║íng th├íi</th><th>X├íc minh</th><th></th></tr></thead>
              <tbody>
                {businessRows.map(item => (
                  <tr key={item.code}>
                    <td><strong>{item.name}</strong></td><td>{item.code}</td><td>{item.owner}</td><td>{item.email}</td><td>{item.phone}</td><td>{item.employees}</td><td>{item.orders}</td><td>{item.batches}</td><td>{item.plan}</td><td>{item.date}</td><td><StatusBadge value={String(item.status)} /></td>
                    <td>
                      <div className="admin-verification-cell">
                        <StatusBadge value={String(item.verificationStatus)} />
                        <small>GPL: {item.businessLicense || '-'}</small>
                        <small>─ÉC: {item.businessAddress || '-'}</small>
                        {item.websiteUrl && <small>Web: {item.websiteUrl}</small>}
                        {item.certificationDocument && <small>Cert: {item.certificationDocument}</small>}
                        {item.verificationRejectReason && <small>L├╜ do: {item.verificationRejectReason}</small>}
                      </div>
                    </td>
                    <td>
                      <div className="admin-row-actions">
                        <button>Sß╗¡a</button>
                        {item.verificationStatus === 'PENDING' && <>
                          <button onClick={() => updateTeamVerification(item.id, 'APPROVED')}><CheckCircle2 size={14} /> Duyß╗çt</button>
                          <button onClick={() => updateTeamVerification(item.id, 'REJECTED')}><XCircle size={14} /> Tß╗½ chß╗æi</button>
                        </>}
                        <button><Lock size={14} /> Kh├│a</button>
                        <button>X├│a</button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {active === 'users' && (
        <section className="admin-card">
          <div className="admin-card-head">
            <div><h3>Quß║ún l├╜ ng╞░ß╗¥i d├╣ng to├án hß╗ç thß╗æng</h3><p>Tß║ío ng╞░ß╗¥i d├╣ng, ─æß║╖t lß║íi mß║¡t khß║⌐u, g├ín vai tr├▓ v├á chuyß╗ân doanh nghiß╗çp.</p></div>
            <button type="button" className="admin-button admin-button-primary"><Plus size={16} /> Tß║ío ng╞░ß╗¥i d├╣ng</button>
          </div>
          <div className="admin-toolbar">
            <label><Search size={16} /><input value={query} onChange={event => { setQuery(event.target.value); setUserPage(1); }} placeholder="T├¼m ng╞░ß╗¥i d├╣ng, email, doanh nghiß╗çp..." /></label>
            <button type="button" className="admin-button admin-button-soft"><Filter size={16} /> Role / trß║íng th├íi</button>
          </div>
          <div className="admin-table-wrap">
            <table className="admin-table">
              <thead><tr><th>Ng╞░ß╗¥i d├╣ng</th><th>Email</th><th>S─ÉT</th><th>Doanh nghiß╗çp</th><th>Vai tr├▓</th><th>Trß║íng th├íi</th><th>Lß║ºn ─æ─âng nhß║¡p cuß╗æi</th><th></th></tr></thead>
              <tbody>
                {userRows.map((item, index) => (
                  <tr key={`${item.email}-${index}`}>
                    <td><div className="admin-user-cell"><span>{item.name.charAt(0)}</span><strong>{item.name}</strong></div></td><td>{item.email}</td><td>{item.phone}</td><td>{item.company}</td><td>{item.role}</td><td><StatusBadge value={item.status} /></td><td>{item.lastLogin}</td>
                    <td><div className="admin-row-actions"><button>Sß╗¡a</button><button><RotateCcw size={14} /> ─Éß║╖t lß║íi</button><button>{item.status === 'Locked' ? <Unlock size={14} /> : <Lock size={14} />} {item.status === 'Locked' ? 'K├¡ch hoß║ít' : 'Kh├│a'}</button></div></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="admin-pagination"><button disabled={userPage === 1} onClick={() => setUserPage(1)}>1</button><button disabled={userPage === 2} onClick={() => setUserPage(2)}>2</button><span>Hiß╗ân thß╗ï 6 user / trang</span></div>
        </section>
      )}

      {active === 'subscriptions' && (
        <section className="admin-card">
          <div className="admin-card-head"><div><h3>Quß║ún l├╜ g├│i dß╗ïch vß╗Ñ SaaS</h3><p>C├íc g├│i C╞í bß║ún, T─âng tr╞░ß╗ƒng, Doanh nghiß╗çp c├╣ng giß╗¢i hß║ín ng╞░ß╗¥i d├╣ng, ─æ╞ín h├áng, l├┤ sß║ún xuß║Ñt, x╞░ß╗ƒng v├á ─æiß╗âm AI.</p></div><button className="admin-button admin-button-primary"><Plus size={16} /> Tß║ío g├│i</button></div>
          <div className="admin-plan-grid">
            {plans.map(item => <article className="admin-plan" key={item.name}><h4>{item.name}</h4><strong>{item.price ? money(item.price) : 'Li├¬n hß╗ç'}</strong><span>{item.period}</span><div className="admin-plan-limits"><p>{item.users} ng╞░ß╗¥i d├╣ng</p><p>{number(item.orders)} ─æ╞ín h├áng</p><p>{number(item.batches)} l├┤</p><p>{item.workshops} x╞░ß╗ƒng</p><p>{number(item.ai)} ─æiß╗âm AI</p></div><ul>{item.features.map(feature => <li key={feature}>{feature}</li>)}</ul><div className="admin-row-actions"><button>Sß╗¡a</button><button>X├│a</button></div></article>)}
          </div>
          <div className="admin-feature-table">
            <table className="admin-table"><thead><tr><th>T├¡nh n─âng</th>{plans.map(item => <th key={item.name}>{item.name}</th>)}</tr></thead><tbody>{featureRows.map(feature => <tr key={feature}><td>{feature}</td>{plans.map((item, index) => <td key={`${item.name}-${feature}`}>{index === 0 && feature.includes('Custom') ? <XCircle size={16} /> : <CheckCircle2 size={16} />}</td>)}</tr>)}</tbody></table>
          </div>
        </section>
      )}

      {active === 'billing' && (
        <>
          <section className="admin-card admin-revenue-filter">
            <div>
              <span className="admin-eyebrow">Revenue Report</span>
              <h3>Doanh thu theo khoß║úng thß╗¥i gian</h3>
              <p>Admin chß╗ìn ng├áy bß║»t ─æß║ºu v├á ng├áy kß║┐t th├║c ─æß╗â xem, lß╗ìc bß║úng h├│a ─æ╞ín v├á xuß║Ñt b├ío c├ío doanh thu theo ─æ├║ng khoß║úng ─æ├│.</p>
            </div>
            <div className="admin-date-range">
              <label>
                <span>Tß╗½ ng├áy</span>
                <input type="date" value={revenueFrom} onChange={event => setRevenueFrom(event.target.value)} />
              </label>
              <label>
                <span>─Éß║┐n ng├áy</span>
                <input type="date" value={revenueTo} onChange={event => setRevenueTo(event.target.value)} />
              </label>
              <button type="button" className="admin-button admin-button-primary" onClick={exportRevenueReport}>
                <Download size={16} /> Xuß║Ñt doanh thu
              </button>
            </div>
          </section>

          <section className="admin-mini-grid">
            <MiniMetric label="Doanh thu trong khoß║úng" value={money(revenueReport.total)} icon={DollarSign} />
            <MiniMetric label="Sß╗æ ng├áy ─æ├ú chß╗ìn" value={number(revenueReport.rangeDays)} icon={CalendarDays} />
            <MiniMetric label="Trung b├¼nh / ng├áy" value={money(revenueReport.averagePerDay)} icon={ReceiptText} />
            <MiniMetric label="Chß╗¥ + lß╗ùi" value={money(revenueReport.pending + revenueReport.failed)} icon={AlertTriangle} />
          </section>
          <section className="admin-grid-2">
            <ChartPanel title="Biß╗âu ─æß╗ô doanh thu theo ng├áy"><ResponsiveContainer width="100%" height="100%"><AreaChart data={revenueReport.timeline}><CartesianGrid strokeDasharray="3 3" vertical={false} /><XAxis dataKey="date" /><YAxis /><Tooltip formatter={(value) => [`${value} triß╗çu`, 'Doanh thu']} /><Area dataKey="revenue" stroke="#d4a574" fill="#d4a57433" strokeWidth={3} /></AreaChart></ResponsiveContainer></ChartPanel>
            <ChartPanel title="Top kh├ích h├áng theo khoß║úng ng├áy">{revenueReport.topCustomers.length > 0 ? <ResponsiveContainer width="100%" height="100%"><PieChart><Pie data={revenueReport.topCustomers} dataKey="value" nameKey="name" outerRadius={92}>{revenueReport.topCustomers.map((_, index) => <Cell key={index} fill={['#d4a574', '#60a5fa', '#22c55e', '#8b5cf6', '#f97316'][index]} />)}</Pie><Tooltip formatter={(value) => [`${value} triß╗çu`, 'Doanh thu']} /></PieChart></ResponsiveContainer> : <div className="admin-chart-empty">Kh├┤ng c├│ doanh thu trong khoß║úng ng├áy ─æ├ú chß╗ìn.</div>}</ChartPanel>
          </section>
          <section className="admin-card"><div className="admin-card-head"><div><h3>Billing Management</h3><p>Hiß╗ân thß╗ï {number(revenueReport.rangeInvoices.length)} giao dß╗ïch thß║¡t trong khoß║úng ─æ├ú chß╗ìn.</p></div></div><div className="admin-table-wrap"><table className="admin-table"><thead><tr><th>M├ú giao dß╗ïch</th><th>Ng╞░ß╗¥i d├╣ng</th><th>G├│i</th><th>Sß╗æ tiß╗ün</th><th>Ng├áy thanh to├ín</th><th>Ng├ón h├áng</th><th>Trß║íng th├íi</th></tr></thead><tbody>{revenueReport.rangeInvoices.length === 0 ? <tr><td colSpan={7} style={{ textAlign: 'center', padding: 24, color: 'var(--text-secondary)' }}>Ch╞░a c├│ giao dß╗ïch thanh to├ín thß║¡t trong khoß║úng n├áy.</td></tr> : revenueReport.rangeInvoices.map(item => <tr key={item.id}><td>{item.txnRef}</td><td>{paymentCustomerName(item)}</td><td>{item.planId}</td><td>{money(Number(item.amount))}</td><td>{formatShortDate(paymentDate(item))}</td><td>{item.bankCode || '-'}</td><td><StatusBadge value={String(item.status)} /></td></tr>)}</tbody></table></div></section>
        </>
      )}

      {active === 'ai' && (
        <>
          <section className="admin-mini-grid">{aiUsage.map(item => <MiniMetric key={item.label} label={item.label} value={item.value} icon={item.icon} />)}</section>
          <section className="admin-card">
            <div className="admin-card-head"><div><h3>Quß║ún l├╜ AI</h3><p>Giß╗¢i hß║ín sß╗¡ dß╗Ñng AI, bß║¡t/tß║»t AI, quß║ún l├╜ ─æiß╗âm v├á lß╗ïch sß╗¡ AI.</p></div><button className="admin-button admin-button-primary"><Settings size={16} /> Cß║Ñu h├¼nh AI</button></div>
            <div className="admin-ai-controls"><label><input type="checkbox" defaultChecked /> Bß║¡t AI to├án hß╗ç thß╗æng</label><label><input type="checkbox" defaultChecked /> Giß╗¢i hß║ín theo g├│i</label><label><input type="checkbox" /> Chß║╖n khi v╞░ß╗út chi ph├¡</label></div>
            <div className="admin-table-wrap"><table className="admin-table"><thead><tr><th>User</th><th>Email</th><th>G├│i AI</th><th>Hß║┐t hß║ín</th></tr></thead><tbody>{adminUsers.length === 0 ? <tr><td colSpan={4} style={{ textAlign: 'center', padding: 24, color: 'var(--text-secondary)' }}>Ch╞░a c├│ user trong hß╗ç thß╗æng.</td></tr> : adminUsers.slice(0, 6).map(item => <tr key={item.id}><td>{item.fullName || item.username}</td><td>{item.email || '-'}</td><td>{item.aiPlan || 'free'}</td><td>{item.aiPlanExpiresAt ? formatShortDate(item.aiPlanExpiresAt) : '-'}</td></tr>)}</tbody></table></div>
          </section>
        </>
      )}

      {active === 'monitoring' && (
        <>
          <section className="admin-system-grid">{systemMetrics.map(item => { const Icon = item.icon; return <article className={`admin-system-card admin-system-${item.tone}`} key={item.name}><Icon size={20} /><span>{item.name}</span><strong>{item.value}{item.name === 'Response Time' ? 'ms' : '%'}</strong><div><i style={{ width: `${Math.min(Number(item.value), 100)}%` }} /></div></article>; })}</section>
          <ChartPanel title="Biß╗âu ─æß╗ô realtime CPU / RAM / API / Error"><ResponsiveContainer width="100%" height="100%"><LineChart data={realtimeData}><CartesianGrid strokeDasharray="3 3" vertical={false} /><XAxis dataKey="time" /><YAxis /><Tooltip /><Line dataKey="cpu" stroke="#d4a574" strokeWidth={2} /><Line dataKey="ram" stroke="#60a5fa" strokeWidth={2} /><Line dataKey="api" stroke="#22c55e" strokeWidth={2} /><Line dataKey="errors" stroke="#ef4444" strokeWidth={2} /></LineChart></ResponsiveContainer></ChartPanel>
          <section className="admin-card"><h3>Nhß║¡t k├╜ hß╗ç thß╗æng</h3><div className="admin-log-list"><p><StatusBadge value="Critical" /> ─Éß╗Ö trß╗à API v╞░ß╗út 800ms tß║íi /api/ai/recommend</p><p><StatusBadge value="Medium" /> Nh├│m kß║┐t nß╗æi c╞í sß╗ƒ dß╗» liß╗çu ─æß║ít 78%</p><p><StatusBadge value="Low" /> Sao l╞░u hß║▒ng ng├áy ho├án tß║Ñt</p></div></section>
        </>
      )}

      {active === 'audit' && (
        <section className="admin-card">
          <div className="admin-card-head"><div><h3>Nhß║¡t k├╜ kiß╗âm to├ín</h3><p>Theo d├╡i ai ─æ─âng nhß║¡p, tß║ío ─æ╞ín h├áng, sß╗¡a l├┤, x├│a dß╗» liß╗çu v├á ─æß╗òi quyß╗ün.</p></div></div>
          <div className="admin-toolbar"><label><Search size={16} /><input value={query} onChange={event => setQuery(event.target.value)} placeholder="T├¼m user, h├ánh ─æß╗Öng, IP..." /></label><button className="admin-button admin-button-soft"><Filter size={16} /> N├óng cao</button></div>
          <div className="admin-table-wrap"><table className="admin-table"><thead><tr><th>Ng╞░ß╗¥i d├╣ng</th><th>H├ánh ─æß╗Öng</th><th>─Éß╗æi t╞░ß╗úng</th><th>Thß╗¥i gian</th><th>IP</th></tr></thead><tbody>{auditLogs.filter(item => `${item.user} ${item.action} ${item.ip}`.toLowerCase().includes(query.toLowerCase())).map(item => <tr key={`${item.user}-${item.time}`}><td>{item.user}</td><td>{item.action}</td><td>{item.target}</td><td>{item.time}</td><td>{item.ip}</td></tr>)}</tbody></table></div>
        </section>
      )}

      {active === 'workflow' && (
        <section className="admin-card">
          <div className="admin-card-head"><div><h3>Quß║ún l├╜ quy tr├¼nh</h3><p>K├⌐o thß║ú ─æß╗â sß║»p xß║┐p quy tr├¼nh: ─É╞ín h├áng | Ph├ón c├┤ng | Sß║ún xuß║Ñt | QC | ─É├│ng g├│i | Giao h├áng.</p></div><button className="admin-button admin-button-primary"><Plus size={16} /> Tß║ío quy tr├¼nh</button></div>
          <div className="admin-workflow-board">
            {workflowStages.map((stage, index) => (
              <div key={stage} className="admin-workflow-step" draggable onDragStart={() => setDragIndex(index)} onDragOver={event => event.preventDefault()} onDrop={() => { if (dragIndex !== null) moveStage(dragIndex, index); setDragIndex(null); }}>
                <GripVertical size={18} /><span>{index + 1}</span><strong>{stage}</strong><button>Sß╗¡a</button>
              </div>
            ))}
          </div>
        </section>
      )}

      {active === 'alerts' && (
        <section className="admin-card">
          <div className="admin-card-head"><div><h3>Trung t├óm cß║únh b├ío</h3><p>Cß║únh b├ío realtime theo Critical, High, Medium, Low.</p></div><button className="admin-button admin-button-primary"><BellRing size={16} /> Tß║ío rule</button></div>
          <div className="admin-alert-list">{alertRows.map(item => <div key={item.title} className={`admin-alert admin-alert-${item.severity.toLowerCase()}`}><AlertTriangle size={18} /><div><strong>{item.title}</strong><span>{item.source} ┬╖ {item.time}</span></div><StatusBadge value={item.severity} /></div>)}</div>
        </section>
      )}

      {active === 'reports' && (
        <>
          <section className="admin-card">
            <div className="admin-card-head"><div><h3>B├ío c├ío ─æiß╗üu h├ánh</h3><p>Doanh thu, t─âng tr╞░ß╗ƒng, doanh nghiß╗çp mß╗¢i, user mß╗¢i, batch, hiß╗çu suß║Ñt x╞░ß╗ƒng, nh├ón vi├¬n v├á QC pass rate.</p></div><div className="admin-row-actions"><button><Download size={14} /> PDF</button><button><Download size={14} /> Excel</button><button><CalendarDays size={14} /> Chß╗ìn khoß║úng thß╗¥i gian</button></div></div>
          </section>
          <section className="admin-kpi-grid">{kpis.slice(0, 8).map(item => <KpiCard key={`report-${item.label}`} item={{ ...item, icon: FileBarChart }} />)}</section>
        </>
      )}
    </div>
  );
}
