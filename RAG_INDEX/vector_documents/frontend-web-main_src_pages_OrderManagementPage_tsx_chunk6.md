# Knowledge Document: OrderManagementPage.tsx (Chunk 7/23)

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
  "chunk_index": 6,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
ion-icon> Yêu cầu báo giá</span>;
            case 'QUOTED': return <span className="status-badge" style={getStyle('blue')}><ion-icon name="pricetag-outline" style={{ fontSize: '13px' }}></ion-icon> Đã báo giá</span>;
            case 'PENDING': return <span className="status-badge" style={getStyle('yellow')}><ion-icon name="time-outline" style={{ fontSize: '13px' }}></ion-icon> Chờ xử lý</span>;
            case 'ACCEPTED': return <span className="status-badge" style={getStyle('green')}><ion-icon name="checkmark-circle-outline" style={{ fontSize: '13px' }}></ion-icon> Đã nhận làm</span>;
            case 'CONFIRMED': return <span className="status-badge" style={getStyle('green')}><ion-icon name="checkmark-done-circle-outline" style={{ fontSize: '13px' }}></ion-icon> Đã xác nhận</span>;
            case 'IN_PRODUCTION': return <span className="status-badge" style={getStyle('blue')}><ion-icon name="construct-outline" style={{ fontSize: '13px' }}></ion-icon> Đang sản xuất</span>;
            case 'QC': return <span className="status-badge" style={getStyle('orange')}><ion-icon name="flask-outline" style={{ fontSize: '13px' }}></ion-icon> Kiểm định QC</span>;
            case 'COMPLETED': return <span className="status-badge" style={getStyle('green')}><ion-icon name="checkmark-circle-outline" style={{ fontSize: '13px' }}></ion-icon> Hoàn thành</span>;
            case 'CANCELED': return <span className="status-badge" style={getStyle('red')}><ion-icon name="ban-outline" style={{ fontSize: '13px' }}></ion-icon> Đã hủy</span>;
            case 'REJECTED': return <span className="status-badge" style={getStyle('red')}><ion-icon name="close-circle-outline" style={{ fontSize: '13px' }}></ion-icon> Bị từ chối</span>;
            case 'SHIPPING': return <span className="status-badge" style={getStyle('blue')}><ion-icon name="car-outline" style={{ fontSize: '13px' }}></ion-icon> Đang giao</span>;
            case 'DELIVERED': return <span className="status-badge" style={getStyle('green')}><ion-icon name="cube-outline" style={{ fontSize: '13px' }}></ion-icon> Đã giao</span>;
            default: return <span className="status-badge" style={{ border: '1px solid var(--border-color)', background: 'rgba(255,255,255,0.05)' }}>{order.status}</span>;
        }
    };

    const deliveryFailureLabel = (action?: string) => {
        switch (action) {

```
