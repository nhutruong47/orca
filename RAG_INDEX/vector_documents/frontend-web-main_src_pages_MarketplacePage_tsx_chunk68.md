# Knowledge Document: MarketplacePage.tsx (Chunk 69/70)

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
  "chunk_index": 68,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
574', width: `${aiMatchingProgress}%`, transition: 'width 0.3s ease'}}></div>
                                </div>
                            </>
                        ) : (
                            <div style={{background: '#171a1b', border: '1px solid rgba(255,255,255,0.05)', borderRadius: 16, padding: 32, width: '100%', maxWidth: 600, textAlign: 'left', animation: 'fadeIn 0.5s ease'}}>
                                <div style={{display: 'flex', alignItems: 'center', gap: 12, marginBottom: 24}}>
                                    <span className="material-symbols-outlined" style={{fontSize: 32, color: '#10b981'}}>check_circle</span>
                                    <h2 style={{margin: 0, color: '#ece8e1'}}>Phân tích hoàn tất!</h2>
                                </div>
                                <p style={{color: '#a79d94', marginBottom: 24}}>RFQ của bạn đã được ghi nhận. AI ORCA đã tự động phân bổ RFQ này cho <strong>Top 5 xưởng phù hợp nhất</strong>.</p>

                                <div style={{display: 'flex', flexDirection: 'column', gap: 12, marginBottom: 32}}>
                                    {[1, 2, 3].map((_, idx) => {
                                        const matchFactory = featuredFactories[idx] || factories[idx] || {name: 'Xưởng gia công Cà phê'};
                                        return (
                                        <div key={idx} style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: 16, background: 'rgba(255,255,255,0.03)', borderRadius: 8, border: '1px solid rgba(255,255,255,0.05)'}}>
                                            <div style={{display: 'flex', alignItems: 'center', gap: 12}}>
                                                <div style={{width: 44, height: 44, borderRadius: '50%', background: 'rgba(16, 185, 129, 0.1)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#10b981', fontWeight: 700}}>{95 - idx * 3}%</div>
                                                <div>
                                                    <strong style={{display: 'block', color: '#ece8e1', marginBottom: 4}}>{matchFactory.name}</strong>
                                                    <span style={{fontSize: 12, color: '#a79d94'}}>Phù hợp Profile • Còn công suất</span>
                                                </div>

```
