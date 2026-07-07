# Knowledge Document: MarketplacePage.tsx (Chunk 9/70)

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
  "chunk_index": 8,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
',
        yearsInOperation: 'Years Operating',
        viewCapacity: 'View Capacity',
        sendRequest: 'Send Request',
        verifiedFactory: 'Verified Factory',
        manageFactory: 'Manage Factory',
        Receiving_Orders: 'Receiving Orders',
        Nearly_Full: 'Nearly Full',
        Temporarily_Unavailable: 'Temporarily Unavailable',
        Arabica_Specialty: 'Arabica Specialty',
        OEM_Coffee: 'OEM Coffee'
    }
};

export default function MarketplacePage() {
    const container = useRef<HTMLDivElement>(null);

    useGSAP(() => {
        const tl = gsap.timeline();
        tl.from('.mp-market-hero-copy h1, .mp-market-hero-copy p', { y: 30, opacity: 0, duration: 0.8, stagger: 0.2, ease: 'power3.out' })
          .from('.mp-top-search', { scaleX: 0.95, opacity: 0, duration: 0.5, ease: 'power2.out' }, '-=0.4')
          .from('.mp-factory-card', { y: 40, opacity: 0, duration: 0.6, stagger: 0.05, ease: 'power3.out' }, '-=0.2');
    }, { scope: container });

    const { user } = useAuth();
    const navigate = useNavigate();
    const [language, setLanguage] = useState<'vi' | 'en'>('vi');
    const t = translations[language] as Record<string, string>;

    const [allTeams, setAllTeams] = useState<Team[]>([]);
    const [myTeams, setMyTeams] = useState<Team[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [searchQuery, setSearchQuery] = useState('');
    const [regionFilter, setRegionFilter] = useState('');
    const [factoryTypeFilter, setFactoryTypeFilter] = useState('');
    const [specialtyFilter, setSpecialtyFilter] = useState('');
    const [statusFilter, setStatusFilter] = useState('');
    const [minCapacityFilter, setMinCapacityFilter] = useState('');
    const [verifiedFilter, setVerifiedFilter] = useState('');
    const [certificateFilter, setCertificateFilter] = useState('');
    const [minRatingFilter, setMinRatingFilter] = useState('');
    const [selectedFactory, setSelectedFactory] = useState<MarketplaceFactory | null>(null);
    const [selectedProduct, setSelectedProduct] = useState<any>(null);
    const [showProductFactories, setShowProductFactories] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);
    const [activeProfileTab, setActiveProfileTab] = useState<FactoryProfileTab>('overview');

```
