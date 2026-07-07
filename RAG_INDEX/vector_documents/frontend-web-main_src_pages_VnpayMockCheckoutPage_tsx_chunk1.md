# Knowledge Document: VnpayMockCheckoutPage.tsx (Chunk 2/5)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/VnpayMockCheckoutPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
 '#ffffff',
            },
        })
            .then(url => {
                if (mounted) setDataUrl(url);
            })
            .catch(() => {
                if (mounted) setDataUrl('');
            });

        return () => {
            mounted = false;
        };
    }, [payload]);

    if (!dataUrl) {
        return <div className="qr-render-error">Không thể render QR</div>;
    }

    return <img className="real-qr" src={dataUrl} alt={`QR thanh toán ${label}`} />;
}

export default function VnpayMockCheckoutPage() {
    const [searchParams] = useSearchParams();
    const navigate = useNavigate();
    const planId = searchParams.get('planId') || 'professional';
    const plan = planMap[planId] ?? planMap.professional;
    const methodParam = searchParams.get('method')?.toUpperCase();
    const method: PaymentMethod = methodParam === 'MB_BANK' ? 'MB_BANK' : 'VNPAY';
    const config = methodConfig[method];
    const [qrPayment, setQrPayment] = useState<VirtualQrPaymentResponse | null>(null);
    const [loading, setLoading] = useState(true);
    const [confirming, setConfirming] = useState(false);
    const [copied, setCopied] = useState(false);
    const [error, setError] = useState('');
    const openPaymentUrl = qrPayment?.deeplink || qrPayment?.payUrl || '';

    useEffect(() => {
        let mounted = true;
        setLoading(true);
        setError('');
        setQrPayment(null);

        paymentService.createVirtualQrPayment(planId, method)
            .then(response => {
                if (!mounted) return;
                setQrPayment(response);
            })
            .catch(err => {
                if (!mounted) return;
                const maybeAxios = err as { response?: { data?: { message?: string; error?: string } }; message?: string };
                setError(maybeAxios.response?.data?.message || maybeAxios.response?.data?.error || maybeAxios.message || 'Không thể tạo mã QR thanh toán.');
            })
            .finally(() => {
                if (mounted) setLoading(false);
            });

        return () => {
            mounted = false;
        };
    }, [method, planId]);

    const handleCopy = async () => {
        if (!qrPayment) return;
        await navigator.clipboard.writeText(qrPayment.txnRef);
        setCopied(true);
        window.setTimeout(() => setCopied(false), 1600);
    };


```
