# Knowledge Document: VnpayMockCheckoutPage.tsx (Chunk 1/5)

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
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
import { useEffect, useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { ArrowLeft, CheckCircle2, Clock3, Copy, ExternalLink, QrCode, Smartphone, X } from 'lucide-react';
import QRCode from 'qrcode';
import { paymentService, type PaymentMethod, type VirtualQrPaymentResponse } from '../services/paymentService';
import './VnpayMockCheckoutPage.css';

const planMap: Record<string, { name: string; amount: number }> = {
    professional: { name: 'Chuyên nghiệp', amount: 129000 },
    enterprise: { name: 'Doanh nghiệp', amount: 249000 },
};

const methodConfig: Record<PaymentMethod, {
    label: string;
    shortLabel: string;
    className: string;
    instruction: string;
}> = {
    MB_BANK: {
        label: 'Thanh toán chuyển khoản MB Bank',
        shortLabel: 'MB Bank',
        className: 'mb-bank',
        instruction: 'Mở ứng dụng ngân hàng, quét mã VietQR và xác nhận chuyển khoản.',
    },
    VNPAY: {
        label: 'Cổng thanh toán VNPay QR',
        shortLabel: 'VNPay',
        className: 'vnpay',
        instruction: 'Mở mobile banking hoặc ví hỗ trợ VNPay QR để quét mã thử nghiệm.',
    },
    PAYOS: {
        label: 'Thanh toán qua PayOS',
        shortLabel: 'PayOS',
        className: 'payos',
        instruction: 'Quét mã VietQR trên cổng PayOS để thanh toán.',
    },
};

function formatCurrency(value: number) {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND',
        maximumFractionDigits: 0,
    }).format(value);
}

function RealQr({ payload, label }: { payload: string; label: string }) {
    const [dataUrl, setDataUrl] = useState('');

    useEffect(() => {
        let mounted = true;
        setDataUrl('');

        QRCode.toDataURL(payload, {
            errorCorrectionLevel: 'Q',
            margin: 2,
            width: 216,
            color: {
                dark: '#111827',
                light: '#ffffff',
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


```
