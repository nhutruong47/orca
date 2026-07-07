# Knowledge Document: MarketplacePage.tsx (Chunk 36/70)

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
  "chunk_index": 35,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
Dịch vụ rang' && specialtyFilter === 'Rang cà phê')
                                    || (category.label === 'Dịch vụ đóng gói' && specialtyFilter === 'Đóng gói')
                                    || (category.label === 'Dịch vụ trọn gói' && specialtyFilter === 'Gia công OEM')
                                    ? 'active'
                                    : ''
                            }
                            onClick={() => {
                                if (category.label === 'Đăng nhu cầu') {
                                    handleOrderClick();
                                    return;
                                }
                                if (index === 0) {
                                    setRegionFilter('');
                                    setFactoryTypeFilter('');
                                    setSpecialtyFilter('');
                                    setStatusFilter('');
                                    setMinCapacityFilter('');
                                    setVerifiedFilter('');
                                    setCertificateFilter('');
                                    return;
                                }

                                setFactoryTypeFilter('');
                                setSpecialtyFilter('');
                                setStatusFilter('');

                                if (category.label === 'Nguyên liệu') setSpecialtyFilter('Cung ứng cà phê nhân');
                                if (category.label === 'Dịch vụ rang') setSpecialtyFilter('Rang cà phê');
                                if (category.label === 'Dịch vụ đóng gói') setSpecialtyFilter('Đóng gói');
                                if (category.label === 'Dịch vụ trọn gói') setSpecialtyFilter('Gia công OEM');
                            }}
                        >
                            <span className="material-symbols-outlined">{category.icon}</span>
                            {category.label}
                        </button>
                    ))}
                    <div className="mp-top-search mp-spotlight-search" style={{marginLeft: 'auto'}}>
                        <span className="material-symbols-outlined">search</span>
                        <input
                            type="text"
                            placeholder="Tìm hạt, xưởng, hoặc thiết bị..."

```
