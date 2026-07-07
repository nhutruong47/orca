# Knowledge Document: OrderManagementPage.tsx (Chunk 6/23)

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
  "chunk_index": 5,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
              deliveryAddress: manualOrderForm.deliveryAddress.trim() || undefined,
                deliveryNote: manualOrderForm.deliveryNote.trim() || undefined,
            });

            setOrders(prev => [created, ...prev]);
            setActiveTab('inbound');
            setShowManualOrderForm(false);
            setManualOrderForm(DEFAULT_MANUAL_ORDER_FORM);
        } catch (err: any) {
            setManualCreateError(err?.response?.data?.message || err?.response?.data?.error || 'Không thể tạo đơn thủ công.');
            console.error(err);
        } finally {
            setManualCreateLoading(false);
        }
    };

    const getStatusBadge = (order: InterGroupOrder) => {
        const getStyle = (type: 'yellow' | 'green' | 'red' | 'blue' | 'orange') => {
            switch (type) {
                case 'yellow': return { background: 'rgba(234, 179, 8, 0.1)', color: '#eab308', border: '1px solid rgba(234, 179, 8, 0.2)' };
                case 'green': return { background: 'rgba(34, 197, 94, 0.1)', color: '#22c55e', border: '1px solid rgba(34, 197, 94, 0.2)' };
                case 'red': return { background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', border: '1px solid rgba(239, 68, 68, 0.2)' };
                case 'blue': return { background: 'rgba(59, 130, 246, 0.1)', color: '#3b82f6', border: '1px solid rgba(59, 130, 246, 0.2)' };
                case 'orange': return { background: 'rgba(249, 115, 22, 0.1)', color: '#f97316', border: '1px solid rgba(249, 115, 22, 0.2)' };
                default: return {};
            }
        };

        if (order.cancelRequested) return <span className="status-badge" style={getStyle('red')}><ion-icon name="alert-circle-outline" style={{ fontSize: '13px' }}></ion-icon> Yêu cầu hủy</span>;
        
        switch (order.status) {
            case 'RFQ_CREATED': return <span className="status-badge" style={getStyle('yellow')}><ion-icon name="document-text-outline" style={{ fontSize: '13px' }}></ion-icon> Yêu cầu báo giá</span>;
            case 'QUOTED': return <span className="status-badge" style={getStyle('blue')}><ion-icon name="pricetag-outline" style={{ fontSize: '13px' }}></ion-icon> Đã báo giá</span>;
            case 'PENDING': return <span className="status-badge" style={getStyle('yellow')}><ion-icon name="time-outline" style={{ fontSize: '13px' }}></ion-icon> Chờ xử lý</span>;

```
