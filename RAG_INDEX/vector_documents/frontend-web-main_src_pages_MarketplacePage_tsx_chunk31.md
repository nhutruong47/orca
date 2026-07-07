# Knowledge Document: MarketplacePage.tsx (Chunk 32/70)

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
  "chunk_index": 31,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
div style={{display: 'flex', gap: 16, marginTop: 8}}>
                                                <span style={{fontSize: 12, color: '#a79d94'}}>✓ {completed} đơn đúng hẹn</span>
                                                <span style={{fontSize: 12, color: '#a79d94'}}>⚠ {late} đơn trễ</span>
                                            </div>
                                        </div>
                                    </div>
                                    <div style={{fontSize: 13, color: 'var(--text-muted)', padding: '0 4px'}}>
                                        Đánh giá chi tiết sẽ hiển thị sau khi có đơn hàng được hoàn thành.
                                    </div>
                                </>
                            );
                        })()}
                    </div>
                );
            case 'portfolio':
                return (
                    <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '16px'}}>
                        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px'}}>
                            {factory.portfolioMock?.map((p, i) => (
                                <div key={i} style={{background: 'rgba(255,255,255,0.03)', borderRadius: '8px', overflow: 'hidden', border: '1px solid rgba(255,255,255,0.05)'}}>
                                    <img src={p.image} alt={p.name} style={{width: '100%', height: '140px', objectFit: 'cover'}} />
                                    <div style={{padding: '12px'}}>
                                        <strong style={{color: '#ece8e1', display: 'block', marginBottom: '4px'}}>{p.name}</strong>
                                        <span style={{fontSize: '12px', color: '#d4a574', background: 'rgba(212, 165, 116, 0.1)', padding: '4px 8px', borderRadius: '4px'}}>{p.type}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                );
            case 'rfq':
                return (
                    <div className="mp-profile-overview">
                        <p>Gửi yêu cầu Báo giá & Gia công (RFQ) trực tiếp tới xưởng này. Xưởng sẽ phản hồi trong vòng {factory.leadTimeMock}.</p>
                        <button

```
