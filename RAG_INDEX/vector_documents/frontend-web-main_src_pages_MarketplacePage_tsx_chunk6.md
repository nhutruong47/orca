# Knowledge Document: MarketplacePage.tsx (Chunk 7/70)

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
  "chunk_index": 6,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
20,
        onTimeRateMock: team.completedOrders ? Math.round(((team.totalOrders || 0) - (team.cancelledOrders || 0)) / team.completedOrders * 100) : 90,
        currentCapacityMock: team.capacityValue ? `${team.capacityValue} ${team.capacityUnit}` : '5 Tấn / Tháng',
        availableCapacityMock: "1 Tấn",
        moqMock: team.moq || "50 kg",
        leadTimeMock: team.leadTime || "5 - 10 Ngày",
        statusBadgeMock: (team.statusBadge as 'Receiving Orders' | 'Nearly Full' | 'Temporarily Unavailable') || 'Receiving Orders',
        specializationsMock: splitMultiValue(team.specialty).length > 0 ? splitMultiValue(team.specialty) : ['Arabica Specialty', 'OEM Coffee'],
        yearsInOperationMock: team.yearsInOperation || 2,
        employeeCountMock: team.employeeCount || 10,
        factorySizeMock: team.factorySize || "500 m2",

        capabilitiesMock: meta.capabilitiesMock || {
            services: splitMultiValue(team.specialty).length > 0 ? splitMultiValue(team.specialty) : ['Rang cà phê', 'Đóng gói', 'Gia công OEM'],
            coffeeTypes: COFFEE_TYPE_OPTIONS.slice(0, 16).map(option => option.label),
            packagingFormats: PACKAGING_FORMAT_OPTIONS.map(option => option.label)
        },
        equipmentMock: meta.equipmentMock || {
            roasters: [],
            packaging: [],
            grinders: [],
            qc: []
        },
        certificatesMock: meta.certificatesMock || [],
        portfolioMock: meta.portfolioMock || [],
        reviewsMock: meta.reviewsMock || []
    };
};

const getCompletionRate = (factory: MarketplaceFactory) => {
    if (!factory.totalOrders) return undefined;
    return Math.round(((factory.completedOrders || 0) / factory.totalOrders) * 100);
};

const getTrustScore = (factory: MarketplaceFactory) => {
    if (!factory.totalOrders) return undefined;
    if (typeof factory.trustScore === 'number') return factory.trustScore;
    return getCompletionRate(factory);
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

```
