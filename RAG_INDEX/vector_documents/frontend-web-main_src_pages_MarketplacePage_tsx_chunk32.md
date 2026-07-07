# Knowledge Document: MarketplacePage.tsx (Chunk 33/70)

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
  "chunk_index": 32,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
/div>
                            ))}
                        </div>
                    </div>
                );
            case 'rfq':
                return (
                    <div className="mp-profile-overview">
                        <p>Gửi yêu cầu Báo giá & Gia công (RFQ) trực tiếp tới xưởng này. Xưởng sẽ phản hồi trong vòng {factory.leadTimeMock}.</p>
                        <button
                            className="mp-submit-btn"
                            disabled={factory.ownerId === user?.id}
                            onClick={() => handleOrderClick(factory)}
                        >
                            {factory.ownerId === user?.id ? 'Xưởng của bạn' : 'Gửi yêu cầu RFQ'}
                        </button>
                    </div>
                );
            default:
                return null;
        }
    };

    if (loading) {
        return (
            <div className="mp-body" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
                <div className="btn-spinner" />
            </div>
        );
    }

    return (
        <div className="mp-body mp-market-style mp-manufacturing-market" ref={container}>
            <Sidebar />

            <header className="mp-topbar">
                <div className="mp-top-spacer" />
                <div className="mp-top-actions">
                    <button aria-label="Thông báo">
                        <span className="material-symbols-outlined">notifications</span>
                    </button>
                    <button aria-label="Lịch sử">
                        <span className="material-symbols-outlined">history</span>
                    </button>
                    <button aria-label="Đơn liên xưởng" onClick={() => navigate('/orders')}>
                        <span className="material-symbols-outlined">receipt_long</span>
                    </button>
                    <button aria-label="Bộ lọc" onClick={() => document.getElementById('mp-filters')?.scrollIntoView({ behavior: 'smooth', block: 'center' })}>
                        <span className="material-symbols-outlined">tune</span>
                    </button>

```
