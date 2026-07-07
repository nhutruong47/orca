# Knowledge Document: HomePage.tsx (Chunk 4/17)

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
  "chunk_index": 3,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
a xưởng.',
    icon: ClipboardCheck
  },
  {
    title: 'Giao việc cho nhân viên',
    text: 'Tự động phân công công việc cho từng người và theo dõi trạng thái thực hiện.',
    icon: Users
  },
  {
    title: 'Theo dõi tiến độ đơn hàng',
    text: 'Biết đơn hàng nào đang sản xuất, đã hoàn thành đến đâu và công đoạn nào đang bị chậm.',
    icon: BarChart3
  },
  {
    title: 'Cảnh báo sớm vấn đề',
    text: 'Thông báo khi có nguy cơ trễ giao hàng, thiếu nguyên liệu hoặc công việc bị tồn đọng',
    icon: AlertTriangle
  }
];

const workshops = [
  {
    name: 'Arabica Cầu Đất Washed',
    rating: '98%',
    description: 'Cà phê đặc sản với hương hoa nhài, vị chua thanh của cam chanh và hậu vị ngọt kéo dài.',
    tags: ['Light Roast', 'Specialty', '100% Arabica'],
    image: 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=1000&q=85'
  },
  {
    name: 'Robusta Honey Fine',
    rating: '96%',
    description: 'Tuyển chọn từ những trái chín mọng, lên men mật ong mang lại thể chất đậm đà, hương chocolate.',
    tags: ['Medium Roast', 'High Caffeine', 'Fine Robusta'],
    image: 'https://images.unsplash.com/photo-1559525839-b184a4d698c7?auto=format&fit=crop&w=1000&q=85'
  },
  {
    name: 'Signature Espresso Blend',
    rating: '99%',
    description: 'Tỷ lệ hoàn hảo 70% Robusta và 30% Arabica. Lớp crema dày mịn, hương vị cân bằng cho pha máy.',
    tags: ['Dark Roast', 'Espresso', 'Blend'],
    image: 'https://images.unsplash.com/photo-1587734195503-904fca47e0e9?auto=format&fit=crop&w=1000&q=85'
  }
];

const pricingPlans = [
  {
    id: 'starter',
    name: 'Cơ bản',
    price: '0đ',
    priceNote: '/tháng',
    subTitle: 'AI quản lý công việc',
    description: 'Dành cho xưởng nhỏ',
    features: [
      'AI tạo task từ đơn hàng',
      'AI giao việc cho nhân viên',
      'Theo dõi tiến độ sản xuất',
      'Quản lý đơn hàng và batch',
      'Báo cáo vận hành cơ bản',
    ],
    accent: 'starter',
  },
  {
    id: 'professional',
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

```
