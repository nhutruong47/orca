# Knowledge Document: MarketplacePage.tsx (Chunk 8/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 7,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
ctory);
};

const availabilityCopy = (status?: AvailabilityStatus) => {
    switch (status) {
        case 'AVAILABLE':
            return { label: 'Còn nhận đơn', className: 'available' };
        case 'LIMITED':
            return { label: 'Công suất hạn chế', className: 'limited' };
        case 'FULLY_BOOKED':
            return { label: 'Fully Booked', className: 'booked' };
        default:
            return { label: 'Chưa cập nhật', className: 'unknown' };
    }
};

const emptyValue = <span className="mp-empty-value">Chưa cập nhật</span>;


const displayPercent = (value?: number) => (typeof value === 'number' ? `${value}%` : emptyValue);
const displayText = (value?: any) => (value || value === 0 ? value : emptyValue);

const loadRequests = async (): Promise<ManufacturingRequest[]> => {
    try {
        const data = await manufacturingRequestService.getAll();
        return data as ManufacturingRequest[];
    } catch {
        return [];
    }
};

const translations = {
    vi: {
        trustScore: 'Điểm uy tín',
        rating: 'Đánh giá',
        orders: 'Đơn hàng',
        onTime: 'Đúng hạn',
        availableCapacity: 'Công suất trống',
        moq: 'SL tối thiểu',
        leadTime: 'Thời gian giao',
        roastery: 'Xưởng rang cà phê',
        vietnam: 'Việt Nam',
        yearsInOperation: 'Năm hoạt động',
        viewCapacity: 'Xem năng lực',
        sendRequest: 'Gửi yêu cầu',
        verifiedFactory: 'Xưởng đã xác thực',
        manageFactory: 'Quản lý xưởng',
        Receiving_Orders: 'Đang nhận đơn',
        Nearly_Full: 'Sắp kín lịch',
        Temporarily_Unavailable: 'Tạm ngưng',
        Arabica_Specialty: 'Arabica Đặc sản',
        OEM_Coffee: 'Gia công OEM'
    },
    en: {
        trustScore: 'Trust Score',
        rating: 'Rating',
        orders: 'Orders',
        onTime: 'On-time',
        availableCapacity: 'Available Capacity',
        moq: 'MOQ',
        leadTime: 'Lead Time',
        roastery: 'Roastery',
        vietnam: 'Vietnam',
        yearsInOperation: 'Years Operating',
        viewCapacity: 'View Capacity',
        sendRequest: 'Send Request',
        verifiedFactory: 'Verified Factory',
        manageFactory: 'Manage Factory',
        Receiving_Orders: 'Receiving Orders',
        Nearly_Full: 'Nearly Full',
        Temporarily_Unavailable: 'Temporarily Unavailable',
        Arabica_Specialty: 'Arabica Specialty',

```
