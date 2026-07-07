# Knowledge Document: HomePage.tsx (Chunk 5/17)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/HomePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "factory",
  "tags": [
    "factory",
    "dashboard",
    "admin",
    "workspace",
    "production",
    "warehouse",
    "inventory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 4,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
',
    name: 'Chuyên nghiệp',
    price: '129.000đ',
    priceNote: '/tháng',
    subTitle: 'AI điều phối sản xuất',
    description: 'Dành cho xưởng đang tăng trưởng',
    features: [
      'Cảnh báo công việc có nguy cơ trễ',
      'Cảnh báo thiếu nguyên liệu',
      'Phân tích hiệu suất sản xuất',
      'Phát hiện điểm nghẽn trong quy trình',
      'Đề xuất tối ưu tiến độ và nguồn lực',
    ],
    accent: 'professional',
    featured: true,
  },
  {
    id: 'enterprise',
    name: 'Doanh nghiệp',
    price: '249.000đ',
    priceNote: '/tháng',
    subTitle: 'AI quản lý doanh nghiệp',
    description: 'Dành cho doanh nghiệp nhiều xưởng',
    features: [
      'Lập kế hoạch sản xuất dài hạn',
      'Dự báo nhu cầu và công suất',
      'Mô phỏng trước các kịch bản sản xuất',
      'Quản lý nhiều xưởng trên một nền tảng',
      'Thương hiệu riêng cho doanh nghiệp',
    ],
    accent: 'enterprise',
  },
];

const supportOptions = [
  {
    title: 'Hotline hỗ trợ',
    detail: 'Trao đổi nhanh khi cần xử lý tài khoản, thanh toán hoặc lỗi vận hành.',
    action: '0328 416 716',
    icon: Phone,
  },
  {
    title: 'Email hỗ trợ',
    detail: 'Gửi mô tả vấn đề, ảnh màn hình hoặc yêu cầu tích hợp cho đội ORCA.',
    action: 'orca@gmail.com',
    icon: Mail,
  },
  {
    title: 'Hướng dẫn sử dụng',
    detail: 'Thiết lập xưởng, phân quyền nhân viên, tạo đơn và dùng AI lập kế hoạch.',
    action: 'Xem tài liệu',
    icon: ShieldCheck,
  },
  {
    title: 'Triển khai cho xưởng',
    detail: 'Đồng hành cấu hình quy trình, dữ liệu mẫu và luồng bàn giao cho đội sản xuất.',
    action: 'Đặt lịch tư vấn',
    icon: Users,
  },
];

export default function HomePage() {
  const navigate = useNavigate();
  const [featureIndex, setFeatureIndex] = useState(0);
  const [navScrolled, setNavScrolled] = useState(false);
  const [navHidden, setNavHidden] = useState(false);
  const wheelRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!wheelRef.current) return;
    
    const anim = gsap.to(wheelRef.current, {
      rotation: -360,
      duration: 160,
      ease: 'none',
      repeat: -1,
    });

    const handleMouseEnter = () => anim.pause();
    const handleMouseLeave = () => anim.play();

    const wheelEl = wheelRef.current;
    wheelEl.addEventListener('mouseenter', handleMouseEnter);
    wheelEl.addEventListener('mouseleave', handleMouseLeave);


```
