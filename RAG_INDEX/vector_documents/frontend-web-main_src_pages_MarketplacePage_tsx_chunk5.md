# Knowledge Document: MarketplacePage.tsx (Chunk 6/70)

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
  "chunk_index": 5,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
 label: 'Dịch vụ trọn gói', icon: 'star' },
    { label: 'Đăng nhu cầu', icon: 'assignment' },
];

// Removed static featuredProducts array
const splitMultiValue = (value?: string | string[]) => {
    if (Array.isArray(value)) return value.filter(Boolean).map(item => item.trim()).filter(Boolean);
    if (!value) return [];
    return value.split(/[,;\n]/).map(item => item.trim()).filter(Boolean);
};

const toggleListValue = (values: string[], value: string) => (
    values.includes(value) ? values.filter(item => item !== value) : [...values, value]
);

const buildCapacityLabel = (team: Team) => {
    if (team.capacityValue && team.capacityUnit) return `${team.capacityValue} ${team.capacityUnit}`;
    return team.capacity || undefined;
};

const normalizeFactory = (team: Team): MarketplaceFactory => {
    let meta: any = {};
    if (team.metadata) {
        try {
            meta = JSON.parse(team.metadata);
        } catch (e) {
            console.warn('Failed to parse metadata for team', team.id);
        }
    }

    return {
        ...team,
        monthlyCapacity: buildCapacityLabel(team),
        services: splitMultiValue(team.specialty),
        availabilityStatus: 'UNKNOWN',
        verifiedFactory: team.verificationStatus === 'APPROVED',
        verifiedBusiness: team.verificationStatus === 'APPROVED' && Boolean(team.businessLicense),
        verifiedAddress: team.verificationStatus === 'APPROVED' && Boolean(team.businessAddress),
        verifiedCertification: team.verificationStatus === 'APPROVED' && Boolean(team.certificationDocument || team.certificates?.length),
        certifications: team.certificates?.length ? team.certificates : splitMultiValue(team.certificationDocument),

        trustScoreMock: team.trustScore || 85,
        ratingMock: team.rating || 4.5,
        reviewCountMock: team.reviewCount || 10,
        completedOrdersMock: team.completedOrders || 20,
        onTimeRateMock: team.completedOrders ? Math.round(((team.totalOrders || 0) - (team.cancelledOrders || 0)) / team.completedOrders * 100) : 90,
        currentCapacityMock: team.capacityValue ? `${team.capacityValue} ${team.capacityUnit}` : '5 Tấn / Tháng',
        availableCapacityMock: "1 Tấn",
        moqMock: team.moq || "50 kg",
        leadTimeMock: team.leadTime || "5 - 10 Ngày",

```
