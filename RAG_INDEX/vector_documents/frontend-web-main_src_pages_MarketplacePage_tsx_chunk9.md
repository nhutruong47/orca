# Knowledge Document: MarketplacePage.tsx (Chunk 10/70)

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
  "chunk_index": 9,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
State('');
    const [selectedFactory, setSelectedFactory] = useState<MarketplaceFactory | null>(null);
    const [selectedProduct, setSelectedProduct] = useState<any>(null);
    const [showProductFactories, setShowProductFactories] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);
    const [activeProfileTab, setActiveProfileTab] = useState<FactoryProfileTab>('overview');
    const [compareIds, setCompareIds] = useState<string[]>([]);

    const [manufacturingRequests, setManufacturingRequests] = useState<ManufacturingRequest[]>([]);

    const [showChatModal, setShowChatModal] = useState(false);
    const [chatTarget, setChatTarget] = useState<MarketplaceFactory | null>(null);
    const [chatDraft, setChatDraft] = useState('');
    const [chatMessages, setChatMessages] = useState<{sender: 'me' | 'other', text: string}[]>([]);
    const [factoryReviewsSummary, setFactoryReviewsSummary] = useState<Record<string, ReviewSummary>>({});
    const [factoryReviews, setFactoryReviews] = useState<Record<string, Review[]>>({});
    const [reviewsLoading, setReviewsLoading] = useState(false);
    const [editingReviewId, setEditingReviewId] = useState<string | null>(null);
    const [editReviewRating, setEditReviewRating] = useState(5);
    const [editReviewStatus, setEditReviewStatus] = useState<'ON_TIME' | 'LATE' | 'NOT_DELIVERED'>('ON_TIME');
    const [editReviewComment, setEditReviewComment] = useState('');

    const [showOrderModal, setShowOrderModal] = useState(false);
    const [selectedSeller, setSelectedSeller] = useState<Team | null>(null);
    const [buyerTeamId, setBuyerTeamId] = useState('');
    const [rfqTitle, setRfqTitle] = useState('');
    const [rfqRequestType, setRfqRequestType] = useState(RFQ_SERVICE_OPTIONS[0].value);
    const [rfqProductName, setRfqProductName] = useState('');
    const [rfqQuantity, setRfqQuantity] = useState(1);
    const [rfqUnit, setRfqUnit] = useState(RFQ_UNIT_OPTIONS[0].value);
    const [rfqDeadline, setRfqDeadline] = useState('');
    const [rfqBudget, setRfqBudget] = useState('');
    const [rfqQuality, setRfqQuality] = useState('');
    const [rfqPackaging, setRfqPackaging] = useState('');
    const [rfqNote, setRfqNote] = useState('');
    const [submitting, setSubmitting] = useState(false);
    const [showAiMatching, setShowAiMatching] = useState(false);

```
