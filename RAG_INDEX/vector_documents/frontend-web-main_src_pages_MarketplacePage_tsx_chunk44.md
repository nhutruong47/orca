# Knowledge Document: MarketplacePage.tsx (Chunk 45/70)

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
  "chunk_index": 44,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
/section>

                {selectedCompareFactories.length > 0 && (
                    <section className="mp-compare-panel">
                        <div className="mp-section-title-row">
                            <div>
                                <h2>So sánh xưởng</h2>
                                <p>So sánh 2-4 xưởng theo chỉ số năng lực chính.</p>
                            </div>
                            <button onClick={() => setCompareIds([])}>Xóa so sánh</button>
                        </div>
                        <div className="mp-compare-table-wrap">
                            <table className="mp-compare-table">
                                <thead>
                                    <tr>
                                        <th>Chỉ số</th>
                                        {selectedCompareFactories.map(factory => <th key={factory.id}>{factory.name}</th>)}
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr><td>Công suất</td>{selectedCompareFactories.map(factory => <td key={factory.id}>{displayText(factory.monthlyCapacity)}</td>)}</tr>
                                    <tr><td>MOQ</td>{selectedCompareFactories.map(factory => <td key={factory.id}>{displayText(factory.moq)}</td>)}</tr>
                                    <tr><td>Giá</td>{selectedCompareFactories.map(factory => <td key={factory.id}>{emptyValue}</td>)}</tr>
                                    <tr><td>Uy tín</td>{selectedCompareFactories.map(factory => <td key={factory.id}>{displayPercent(getTrustScore(factory))}</td>)}</tr>
                                    <tr><td>Đúng hạn</td>{selectedCompareFactories.map(factory => <td key={factory.id}>{displayPercent(factory.onTimeRate)}</td>)}</tr>
                                    <tr><td>Chứng nhận</td>{selectedCompareFactories.map(factory => <td key={factory.id}>{factory.certifications?.join(', ') || emptyValue}</td>)}</tr>
                                </tbody>
                            </table>
                        </div>
                    </section>
                )}

                <section className="mp-open-requests">
                    <div className="mp-section-title-row">
                        <div>
                            <h2>Yêu cầu gia công đang mở</h2>

```
