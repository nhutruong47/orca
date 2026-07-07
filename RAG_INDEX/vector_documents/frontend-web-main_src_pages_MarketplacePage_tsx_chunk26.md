# Knowledge Document: MarketplacePage.tsx (Chunk 27/70)

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
  "chunk_index": 26,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
.id, review.id)} style={{padding: '6px 10px', borderRadius: 8, border: '1px solid rgba(239,68,68,0.35)', background: 'rgba(239,68,68,0.08)', color: '#fca5a5', cursor: 'pointer'}}>Xóa</button>
                                        </div>
                                    )}
                                </>
                            )}
                        </div>
                    ))}
                </div>
            </div>
        );
    };

    const renderProfileTab = (factory: MarketplaceFactory) => {
        switch (activeProfileTab) {
            case 'overview':
                return (
                    <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '20px'}}>
                        <p style={{fontSize: '15px', color: '#ece8e1', lineHeight: '1.6'}}>{factory.description || 'Chưa cập nhật mô tả xưởng'}</p>
                        <div className="mp-profile-grid" style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px'}}>
                            {renderMetric('Năm hoạt động', factory.yearsInOperationMock + ' Năm')}
                            {renderMetric('Quy mô nhân sự', factory.employeeCountMock + ' Người')}
                            {renderMetric('Diện tích', factory.factorySizeMock)}
                            {renderMetric('Loại hình', factory.factoryType)}
                            {renderMetric('Công suất', factory.currentCapacityMock)}
                            {renderMetric('Đơn đã hoàn thành', factory.completedOrdersMock)}
                        </div>
                    </div>
                );
            case 'capabilities':
                return (
                    <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '24px'}}>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Dịch vụ gia công</h4>
                            <div className="mp-detail-tags">
                                {factory.capabilitiesMock?.services.map(s => <span key={s}>{s}</span>)}
                            </div>
                        </div>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Dòng cà phê</h4>
                            <div className="mp-detail-tags">

```
