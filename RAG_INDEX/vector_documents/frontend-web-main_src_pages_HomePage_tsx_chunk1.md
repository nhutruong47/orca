# Knowledge Document: HomePage.tsx (Chunk 2/17)

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
  "chunk_index": 1,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
'Cập nhật tiến độ từng mẻ sản xuất từ lúc nhận đơn đến khi hoàn tất QC.', icon: Package },
  { label: 'Xưởng', value: 'Liên kết đa đối tác', detail: 'Kết nối nhiều xưởng gia công để điều phối đơn theo năng lực và lịch sản xuất.', icon: Factory }
];

const problems = [
  'Đơn hàng nằm rải rác giữa chat, file Excel và cuộc gọi nội bộ.',
  'Khó biết batch đang ở công đoạn nào và ai đang phụ trách.',
  'Thông tin QC, mẫu thử và lịch giao hàng không được nối thành một luồng.',
  'Chủ xưởng thiếu số liệu để dự báo công suất và điều phối nhân sự.'
];

const solutions = [
  'Gom đơn hàng, xưởng, nhân viên và batch vào một bảng điều phối duy nhất.',
  'Theo dõi tiến độ từng batch theo thời gian thực, từ nhận nguyên liệu đến bàn giao.',
  'Chuẩn hóa giao việc, QC, tasting notes và lịch giao hàng cho từng đơn sản xuất.'
];

const featureSlides = [
  {
    title: 'Quản lý đơn gia công',
    text: 'Tạo đơn, chọn xưởng, đặt deadline và theo dõi trạng thái trong một luồng ngắn gọn.',
    image: 'https://images.pexels.com/photos/4226787/pexels-photo-4226787.jpeg?auto=compress&cs=tinysrgb&w=1200&fit=crop'
  },
  {
    title: 'Theo dõi batch sản xuất',
    text: 'Nắm profile rang, khối lượng, QC và người phụ trách của từng batch.',
    image: 'https://images.pexels.com/photos/37540261/pexels-photo-37540261.jpeg?auto=compress&cs=tinysrgb&w=1200&fit=crop'
  },
  {
    title: 'Phân quyền nhân viên',
    text: 'Giao việc theo vai trò: quản lý xưởng, QC, đóng gói, giao hàng và admin.',
    image: 'https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1200&q=85'
  },
  {
    title: 'Báo cáo vận hành',
    text: 'Xem công suất, tỷ lệ trễ hẹn, chất lượng batch và hiệu quả từng xưởng.',
    image: 'https://images.pexels.com/photos/7693142/pexels-photo-7693142.jpeg?auto=compress&cs=tinysrgb&w=1200&fit=crop'
  }
];

const workflowSteps = [
  'Tiếp nhận đơn hàng',
  'Chọn xưởng phù hợp',
  'Giao việc cho nhân viên',
  'Theo dõi batch và QC',
  'Bàn giao và nghiệm thu'
];

const curvedShowcaseImages = [
  {
    title: 'Bảng điều hành sản xuất',
    image: 'https://images.pexels.com/photos/35968323/pexels-photo-35968323.jpeg?auto=compress&cs=tinysrgb&w=800&fit=crop'
  },
  {
    title: 'Quản lý đơn hàng',
    image: 'https://images.pexels.com/photos/4226787/pexels-photo-4226787.jpeg?auto=compress&cs=tinysrgb&w=800&fit=crop'
  },
  {

```
