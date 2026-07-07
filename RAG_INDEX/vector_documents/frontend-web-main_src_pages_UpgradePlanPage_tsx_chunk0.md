# Knowledge Document: UpgradePlanPage.tsx (Chunk 1/3)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/UpgradePlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
import {
    CheckCircle2,
} from 'lucide-react';
import { paymentService } from '../services/paymentService';
import './UpgradePlanPage.css';

interface Plan {
    id: string;
    name: string;
    price: string;
    priceNote: string;
    subtitle: string;
    target: string;
    featured?: boolean;
    buttonText: string;
    features: string[];
    theme: 'light' | 'beige' | 'dark';
}

const plans: Plan[] = [
    {
        id: 'starter',
        name: 'Cơ bản',
        price: '0đ',
        priceNote: '/tháng',
        subtitle: 'AI quản lý công việc',
        target: 'Dành cho xưởng nhỏ',
        buttonText: 'Bắt đầu',
        features: [
            'AI tạo task từ đơn hàng',
            'AI giao việc cho nhân viên',
            'Theo dõi tiến độ sản xuất',
            'Quản lý đơn hàng và batch',
            'Báo cáo vận hành cơ bản'
        ],
        theme: 'light',
    },
    {
        id: 'professional',
        name: 'Plus',
        price: '129.000đ',
        priceNote: '/tháng',
        subtitle: 'Dùng AI 100 lần',
        target: 'Dành cho xưởng đang tăng trưởng',
        featured: true,
        buttonText: 'Nâng cấp ngay',
        features: [
            'Cảnh báo công việc có nguy cơ trễ',
            'Cảnh báo thiếu nguyên liệu',
            'Phân tích hiệu suất sản xuất',
            'Phát hiện điểm nghẽn trong quy trình',
            'Đề xuất tối ưu tiến độ và nguồn lực'
        ],
        theme: 'beige',
    },
    {
        id: 'enterprise',
        name: 'Doanh nghiệp',
        price: '249.000đ',
        priceNote: '/tháng',
        subtitle: 'Không giới hạn AI trong 30 ngày',
        target: 'Dành cho doanh nghiệp nhiều xưởng',
        buttonText: 'Nâng cấp ngay',
        features: [
            'Lập kế hoạch sản xuất dài hạn',
            'Dự báo nhu cầu và công suất',
            'Mô phỏng trước các kịch bản sản xuất',
            'Quản lý nhiều xưởng trên một nền tảng',
            'Thương hiệu riêng cho doanh nghiệp'
        ],
        theme: 'dark',
    },
];

export default function UpgradePlanPage() {

    const handleSelectPlan = async (plan: Plan) => {
        if (plan.id === 'starter') {
            return;
        }
        localStorage.setItem('orca-ai-plan-pending', plan.id);
        localStorage.setItem('orca-payment-method', 'PAYOS');
        
        try {

```
