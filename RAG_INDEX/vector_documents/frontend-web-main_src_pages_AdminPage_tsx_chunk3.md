# Knowledge Document: AdminPage.tsx (Chunk 4/16)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/AdminPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "report",
    "dashboard",
    "admin",
    "workspace",
    "production",
    "factory",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, admin, workspace, production, factory, payment

## Source Code Chunk
```tsx
ử', Locked: 'Đã khóa',
    APPROVED: 'Đã duyệt', PENDING: 'Chờ duyệt', REJECTED: 'Từ chối',
    Suspended: 'Tạm đình chỉ',
    PAID: 'Đã thanh toán', FAILED: 'Thất bại', REFUNDED: 'Hoàn tiền',
    Published: 'Công khai', Private: 'Nội bộ',
    ADMIN: 'Admin Nền Tảng', MEMBER: 'Thành viên', FACTORY_OWNER: 'Chủ xưởng',
    free: 'Miễn phí', professional: 'Chuyên nghiệp', enterprise: 'Doanh nghiệp',
    SUCCESS: 'Thành công'
  };

  return <span className={`admin-badge ${type}`}>{labels[value] || value}</span>;
}

export default function AdminPage() {
  const { user } = useAuth();
  const [searchParams] = useSearchParams();
  const sectionParam = searchParams.get('section') as AdminSection | null;
  const active: AdminSection = sidebarModules.some(tab => tab.id === sectionParam) ? sectionParam! : 'overview';
  
  const [overview, setOverview] = useState<AdminOverview>(emptyOverview);
  const [adminUsers, setAdminUsers] = useState<AdminUser[]>([]);
  const [adminTeams, setAdminTeams] = useState<AdminTeam[]>([]);
  const [adminPayments, setAdminPayments] = useState<AdminPayment[]>([]);
  const [plans] = useState<any[]>(initialPlans);
  
  const [adminLoading, setAdminLoading] = useState(true);
  const [adminError, setAdminError] = useState('');
  
  const [query, setQuery] = useState('');
  const [status, setStatus] = useState('All');
  const [userPage, setUserPage] = useState(1);
  const [revenueFrom] = useState('2026-06-01');
  const [revenueTo] = useState('2026-06-30');

  const handleNotImplemented = () => {
    alert('Tính năng này đang được bảo trì hoặc đang trong quá trình phát triển.');
  };

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
      adminService.getPayments(),
    ])
      .then(([overviewData, userData, teamData, paymentData]) => {
        setOverview({ ...emptyOverview, ...overviewData });
        setAdminUsers(userData || []);
        setAdminTeams(teamData || []);
        setAdminPayments(paymentData || []);
      })
      .catch(() => {
        setAdminError('Không tải được thống kê thật từ hệ thống.');
      })
      .finally(() => setAdminLoading(false));
  }, [user?.role]);



  const revenueReport = useMemo(() => {

```
