# Knowledge Document: OrderManagementPage.tsx (Chunk 11/23)

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
  "chunk_index": 10,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
            onMouseLeave={e => e.currentTarget.style.background = 'transparent'}
                        >
                            &times;
                        </button>
                        
                        <div style={{ marginBottom: 32 }}>
                            <h2 style={{ margin: 0, fontSize: 28, color: 'var(--text-primary)', fontWeight: 800 }}>Đơn xưởng khác đặt</h2>
                            <p style={{ margin: '8px 0 0', color: 'var(--text-secondary)', fontSize: 16 }}>
                                Tạo nhanh đơn bán/gia công thủ công cho xưởng đang chọn.
                            </p>
                        </div>
                        
                        <form onSubmit={handleCreateManualInboundOrder} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px 32px' }}>
                            <div style={{ gridColumn: '1/-1' }}>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Tên đơn hàng *</label>
                                <input
                                    value={manualOrderForm.title}
                                    onChange={event => handleManualOrderChange('title', event.target.value)}
                                    placeholder="VD: Đơn gia công rang 20kg Robusta"
                                    style={{ width: '100%', padding: '16px 20px', borderRadius: 12, border: '1px solid var(--border-color)', background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 16, outline: 'none' }}
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', fontSize: 16, color: 'var(--text-primary)', marginBottom: 10, fontWeight: 600 }}>Khách / xưởng đặt *</label>
                                <input
                                    value={manualOrderForm.customerName}
                                    onChange={event => handleManualOrderChange('customerName', event.target.value)}
                                    placeholder="Tên khách hoặc xưởng đặt"

```
