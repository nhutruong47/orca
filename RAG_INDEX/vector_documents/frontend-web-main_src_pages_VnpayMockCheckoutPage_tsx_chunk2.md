# Knowledge Document: VnpayMockCheckoutPage.tsx (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
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

    const handleConfirm = async () => {
        if (!qrPayment || confirming) return;
        setConfirming(true);
        setError('');
        try {
            const response = await paymentService.confirmVirtualQrPayment(qrPayment.txnRef);
            if (response.status === 'SUCCESS' || response.status === 'PAID') {
                localStorage.setItem('orca-ai-plan', response.planId);
            }
            const params = new URLSearchParams({
                status: response.status,
                txnRef: response.txnRef,
                planId: response.planId,
                message: response.message || `Thanh toán qua ${config.shortLabel} thành công`,
            });
            navigate(`/payment-result?${params.toString()}`);
        } catch (err) {
            const maybeAxios = err as { response?: { data?: { message?: string; error?: string } }; message?: string };
            setError(maybeAxios.response?.data?.message || maybeAxios.response?.data?.error || maybeAxios.message || 'Không thể xác nhận giao dịch.');
            setConfirming(false);
        }
    };

    return (
        <div className={`vnpay-mock-page ${config.className}`}>
            <header className="vnpay-mock-header">
                <Link to="/upgrade" className="vnpay-back">
                    <ArrowLeft size={18} />
                    <span>Quay lại</span>
                </Link>
                <div className="vnpay-brand">
                    <span>{config.shortLabel}</span>
                    <strong>QR</strong>
                </div>
                <button type="button" className="vnpay-close" onClick={() => navigate('/upgrade')} title="Hủy thanh toán">
                    <X size={20} />
                </button>
            </header>

            <main className="vnpay-mock-shell">
                <section className="payment-order-card">
                    <aside className="payment-order-info">

```
