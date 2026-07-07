# Knowledge Document: ProductionOrderPage.tsx (Chunk 2/19)

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
  "chunk_index": 1,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
edYield: 0.85,
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

export default function ProductionOrderPage() {
    const { id } = useParams<{ id: string }>();
    const teamId = id || '';
    const navigate = useNavigate();
    const [searchParams] = useSearchParams();

    const [orders, setOrders] = useState<ProductionOrder[]>([]);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [error, setError] = useState('');
    const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});
    const [activeTab, setActiveTab] = useState<'list' | 'create'>('list');
    const [editingOrderId, setEditingOrderId] = useState<string | null>(null);
    const customerDeliveryDateRef = useRef<HTMLInputElement>(null);

    const [form, setForm] = useState(createDefaultForm);

    useEffect(() => {
        loadOrders();
        if (searchParams.get('mode') === 'create') {
            startCreate();
        }
    }, [teamId]);

    const loadOrders = async () => {
        try {
            const data = await productionService.getOrders(teamId);
            setOrders(data || []);
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    const handleChange = (field: string, value: any) => {
        if (fieldErrors[field]) {
            setFieldErrors(prev => {
                const next = { ...prev };
                delete next[field];
                return next;
            });
        }
        if (error) setError('');
        setForm(prev => ({ ...prev, [field]: value }));
    };

    const startCreate = () => {
        setEditingOrderId(null);
        setForm(createDefaultForm());
        setError('');
        setFieldErrors({});
        setActiveTab('create');
    };

    const startEdit = (order: ProductionOrder) => {
        setEditingOrderId(order.id);
        setForm({
            title: order.title || '',
            description: order.description || '',

```
