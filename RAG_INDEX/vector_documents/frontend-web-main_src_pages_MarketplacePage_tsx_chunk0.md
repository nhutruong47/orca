# Knowledge Document: MarketplacePage.tsx (Chunk 1/70)

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
  "chunk_index": 0,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
import { useEffect, useMemo, useState } from 'react';
import type { SyntheticEvent } from 'react';
import { inventoryService, teamService } from '../services/groupService';
import { interGroupOrderService, reviewService, manufacturingRequestService } from '../services/interGroupOrderService';
import type { Team, InterGroupOrder, InventoryItem, Review, ReviewSummary } from '../types/types';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import Sidebar from '../components/Sidebar';
import './Marketplace.css';
import gsap from 'gsap';
import { useGSAP } from '@gsap/react';
import { useRef } from 'react';

type FactoryProfileTab = 'overview' | 'capabilities' | 'equipment' | 'certificates' | 'reviews' | 'portfolio' | 'rfq';
type AvailabilityStatus = 'AVAILABLE' | 'LIMITED' | 'FULLY_BOOKED' | 'UNKNOWN';

type ManufacturingRequest = {
    id: string;
    type: 'Roasting' | 'Packaging' | 'OEM' | 'Quality control';
    title: string;
    coffeeType: string;
    quantity: string;
    deadline: string;
    region: string;
    details: string;
    createdAt: string;
};

type MarketplaceFactory = Team & {
    rating?: number;
    monthlyCapacity?: string;
    availableCapacity?: string;
    moq?: string;
    onTimeRate?: number;
    avgResponseTime?: string;
    repeatCustomerRate?: number;
    availabilityStatus?: AvailabilityStatus;
    coffeeTypes?: string[];
    services?: string[];
    roasters?: string[];
    packagingMachines?: string[];
    grinders?: string[];
    qcEquipment?: string[];
    certifications?: string[];
    verifiedFactory?: boolean;
    verifiedBusiness?: boolean;
    verifiedAddress?: boolean;
    verifiedCertification?: boolean;
    portfolioProjects?: string[];
    notableCustomers?: string[];
    processedCoffeeLines?: string[];
    reviews?: { author: string; content: string; rating?: number; date?: string; company?: string }[];

    // New Mock Fields for B2B Redesign
    trustScoreMock?: number;
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

```
