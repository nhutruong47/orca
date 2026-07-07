# Knowledge Document: MarketplacePage.tsx (Chunk 2/70)

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
  "chunk_index": 1,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
mber;
    ratingMock?: number;
    reviewCountMock?: number;
    completedOrdersMock?: number;
    onTimeRateMock?: number;
    currentCapacityMock?: string;
    availableCapacityMock?: string;
    moqMock?: string;
    leadTimeMock?: string;
    statusBadgeMock?: 'Receiving Orders' | 'Nearly Full' | 'Temporarily Unavailable';
    specializationsMock?: string[];
    yearsInOperationMock?: number;
    employeeCountMock?: number;
    factorySizeMock?: string;

    capabilitiesMock?: {
        services: string[];
        coffeeTypes: string[];
        packagingFormats: string[];
    };
    equipmentMock?: {
        roasters: { model: string; capacity: string; year: string }[];
        packaging: string[];
        grinders: string[];
        qc: string[];
    };
    certificatesMock?: { name: string; issueDate: string; expDate: string; status: string }[];
    portfolioMock?: { name: string; type: string; image: string }[];
    reviewsMock?: { author: string; content: string; rating?: number; date?: string; company?: string }[];
};

const REGION_OPTIONS = ['Lâm Đồng', 'Đắk Lắk', 'Gia Lai', 'Kon Tum', 'Đồng Nai', 'Bình Dương', 'TP HCM', 'Khác'];
const FACTORY_TYPE_OPTIONS = [
    'Xưởng rang cà phê',
    'Xưởng gia công OEM',
    'Nhà máy chế biến',
    'Hợp tác xã',
    'Doanh nghiệp xuất khẩu',
    'Nhà cung cấp thiết bị',
];
const SPECIALTY_OPTIONS = [
    'Rang cà phê',
    'Gia công OEM',
    'Đóng gói',
    'Xay cà phê',
    'Sản xuất Private Label',
    'QC kiểm định',
    'Xuất khẩu',
    'Cung ứng cà phê nhân',
    'Thiết kế bao bì',
];
const CERTIFICATE_OPTIONS = ['HACCP', 'ISO 22000', 'ISO 9001', 'OCOP', 'FDA', 'Khác'];

const RFQ_SERVICE_OPTIONS = [
    { value: 'Roasting', label: 'Rang cà phê (Roasting)' },
    { value: 'Packaging', label: 'Đóng gói (Packaging)' },
    { value: 'OEM', label: 'Gia công OEM' },
    { value: 'Private Label', label: 'Private Label' },
    { value: 'Grinding', label: 'Xay cà phê (Grinding)' },
    { value: 'Green Coffee', label: 'Mua cà phê nhân' },
    { value: 'Blend Development', label: 'Phối trộn blend' },
    { value: 'Sample Roasting', label: 'Rang mẫu / Test profile' },
    { value: 'QC Cupping', label: 'QC / Cupping' },
    { value: 'Drying', label: 'Sấy / sơ chế' },
    { value: 'Other', label: 'Khác' },
];
const RFQ_UNIT_OPTIONS = [
    { value: 'kg', label: 'kg' },
    { value: 'ton', label: 'Tấn (Ton)' },

```
