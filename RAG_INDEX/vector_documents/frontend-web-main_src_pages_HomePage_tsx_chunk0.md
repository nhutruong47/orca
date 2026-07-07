# Knowledge Document: HomePage.tsx (Chunk 1/17)

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
  "chunk_index": 0,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
import { useEffect, useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import gsap from 'gsap';
import {
  AlertTriangle,
  ArrowDown,
  ArrowRight,
  BarChart3,
  Brain,
  Check,
  CheckCircle,
  ClipboardCheck,
  Factory,
  Mail,
  MapPin,
  Package,
  Phone,
  ShieldCheck,
  Sparkles,
  Sprout,
  Star,
  Users
} from 'lucide-react';
import orcaLogo from '../assets/orca-logo.png';
import './HomePage.css';
import './UpgradePlanPage.css';

const productionPoster =
  'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1600&q=85';

const solutionPoster =
  'https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=1600&q=85';

const solutionVideo =
  'https://www.shutterstock.com/shutterstock/videos/4061367707/preview/stock-footage-cafe-workers-standing-near-coffee-machine-station-female-operating-equipment-and-pressing-controls.mp4';

const productionVideo =
  'https://www.shutterstock.com/shutterstock/videos/3852235011/preview/stock-footage-caucasian-man-male-guy-clipboard-inventory-inspection-coffee-warehouse-packaging-shelf-factory.mp4';

const roastingVideo =
  'https://www.shutterstock.com/shutterstock/videos/1107166639/preview/stock-footage-production-of-fresh-fried-coffee-beans-roast-master-opens-roasting-coffee-machine-roasted-coffee.mp4';

const navItems = [
  { label: 'Trang chủ', target: 'hero' },
  { label: 'Giới thiệu', target: 'solution' },
  { label: 'Tính năng', target: 'features' },
  { label: 'Hỏi đáp', target: 'ai' },
  { label: 'Hỗ trợ', target: 'support' }
];

const stats = [
  { label: 'Đơn hàng', value: 'Quản lý tập trung', detail: 'Theo dõi yêu cầu gia công, trạng thái xử lý và lịch bàn giao trong một nơi.', icon: ClipboardCheck },
  { label: 'Nhân viên', value: 'Phân quyền theo vai trò', detail: 'Tách rõ quyền của quản lý xưởng, nhân viên rang, QC, đóng gói và admin.', icon: Users },
  { label: 'Batch', value: 'Theo dõi realtime', detail: 'Cập nhật tiến độ từng mẻ sản xuất từ lúc nhận đơn đến khi hoàn tất QC.', icon: Package },
  { label: 'Xưởng', value: 'Liên kết đa đối tác', detail: 'Kết nối nhiều xưởng gia công để điều phối đơn theo năng lực và lịch sản xuất.', icon: Factory }
];

const problems = [
  'Đơn hàng nằm rải rác giữa chat, file Excel và cuộc gọi nội bộ.',
  'Khó biết batch đang ở công đoạn nào và ai đang phụ trách.',

```
