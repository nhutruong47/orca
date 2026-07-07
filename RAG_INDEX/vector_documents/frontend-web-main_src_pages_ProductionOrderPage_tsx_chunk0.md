# Knowledge Document: ProductionOrderPage.tsx (Chunk 1/19)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionOrderPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
import { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate, useSearchParams } from 'react-router-dom';
import { productionService } from '../services/groupService';
import type { ProductionOrder } from '../types/types';



const PRODUCT_TYPES = [
    'Arabica',
    'Robusta',
    'Liberica',
    'Excelsa',
    'Blend',
    'Arabica Specialty',
    'Fine Robusta',
    'Culi / Peaberry',
    'Moka',
    'Catimor',
    'Bourbon',
    'Typica',
    'Caturra',
    'Gesha / Geisha',
    'Ethiopia Heirloom',
    'Colombia Supremo',
    'Brazil Santos',
    'Vietnam Robusta',
    'Ca phe nhan xanh',
    'Ca phe rang nguyen hat',
    'Ca phe rang xay',
    'Ca phe hoa tan',
    'Khac',
];
const PROCESS_TYPES = [
    'Rang nguyen hat',
    'Rang xay',
    'Rang sample / profile test',
    'Gia cong OEM',
    'Dong goi',
    'Xay ca phe',
    'Private Label',
    'QC / Cupping',
    'Phoi tron blend',
    'Khac',
];
const ROAST_LEVELS = ['Light', 'Medium Light', 'Medium', 'Medium-Dark', 'Dark', 'Espresso Roast', 'Theo profile rieng'];
const PACKAGE_SIZES = ['100g', '250g', '500g', '1kg', '2kg', '5kg', '10kg', '20kg', '25kg', '50kg', 'Drip bag', 'Capsule / Pod', 'Bulk', 'Custom'];
const STATUS_OPTIONS = [
    { value: 'PENDING', label: 'Cho xu ly', color: '#94a3b8' },
    { value: 'CONFIRMED', label: 'Da xac nhan', color: '#3b82f6' },
    { value: 'PLANNING', label: 'Dang ke hoach', color: '#8b5cf6' },
    { value: 'IN_PRODUCTION', label: 'Dang san xuat', color: '#f59e0b' },
    { value: 'COMPLETED', label: 'Hoan thanh', color: '#10b981' },
    { value: 'DELIVERED', label: 'Da giao', color: '#059669' },
    { value: 'CANCELLED', label: 'Da huy', color: '#ef4444' },
];

const createDefaultForm = () => ({
    title: '',
    description: '',
    customerName: '',
    productType: 'Robusta',
    processType: 'Rang nguyen hat',
    roastLevel: 'Medium',
    packageSize: '1kg',
    totalPackages: 0,
    outputTarget: 0,
    expectedYield: 0.85,
    expectedLoss: 0,
    unit: 'kg',
    orderDate: new Date().toISOString().split('T')[0],
    confirmDate: '',
    productionStartDate: new Date().toISOString().split('T')[0],
    customerDeliveryDate: '',
    safetyBufferDays: 2,
    recipientName: '',
    recipientPhone: '',
    shippingNote: '',
});

const toDateInput = (value?: string) => value ? value.substring(0, 10) : '';


```
