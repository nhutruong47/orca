# Knowledge Document: OrderManagementPage.tsx (Chunk 8/23)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/OrderManagementPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 7,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
"status-badge" style={getStyle('green')}><ion-icon name="cube-outline" style={{ fontSize: '13px' }}></ion-icon> Đã giao</span>;
            default: return <span className="status-badge" style={{ border: '1px solid var(--border-color)', background: 'rgba(255,255,255,0.05)' }}>{order.status}</span>;
        }
    };

    const deliveryFailureLabel = (action?: string) => {
        switch (action) {
            case 'RETRY_LATER': return 'Giao lại sau';
            case 'LEAVE_AT_DOOR': return 'Để hàng tại cổng/kho';
            case 'RETURN_TO_SENDER': return 'Trả hàng về cho xưởng';
            case 'CONTACT_ALTERNATIVE': return 'Liên hệ SĐT phụ';
            default: return action || 'Chưa chọn';
        }
    };

    const formatDeliveryTime = (from?: string, to?: string) => {
        if (!from && !to) return null;
        const fmt = (d: string) => new Date(d).toLocaleString('vi-VN', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' });
        if (from && to) return `${fmt(from)} → ${fmt(to)}`;
        if (from) return `Từ ${fmt(from)}`;
        return `Đến ${fmt(to!)}`;
    };



    return (
        <div className="page-container">
            <header className="page-header glass-panel" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '24px 32px', marginBottom: 24 }}>
                <div>
                    <h1 className="page-title text-glow-active" style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                        <span className="icon-container glow" style={{ width: 32, height: 32, fontSize: 20 }}><ion-icon name="cube-outline"></ion-icon></span> Quản lý đơn hàng
                    </h1>
                    <p className="page-subtitle">Theo dõi đơn đi đặt tại xưởng khác và đơn nhận gia công.</p>
                </div>
            </header>

            <div className="tabs-container glass-panel" style={{ marginBottom: '20px', display: 'inline-block', padding: 4 }}>
                <div className="tabs-header" style={{ gap: 8 }}>
                    <button
                        className={`tab-btn ${activeTab === 'outbound' ? 'active' : ''}`}
                        onClick={() => setActiveTab('outbound')}
                        style={{ display: 'flex', alignItems: 'center', gap: 4 }}
                    >

```
