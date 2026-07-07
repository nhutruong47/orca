# Knowledge Document: MarketplacePage.tsx (Chunk 46/70)

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
  "chunk_index": 45,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
(', ') || emptyValue}</td>)}</tr>
                                </tbody>
                            </table>
                        </div>
                    </section>
                )}

                <section className="mp-open-requests">
                    <div className="mp-section-title-row">
                        <div>
                            <h2>Yêu cầu gia công đang mở</h2>
                            <p>Nhu cầu rang, đóng gói, OEM và kiểm định đang mở để xưởng gửi báo giá.</p>
                        </div>
                    </div>

                    {manufacturingRequests.length === 0 ? (
                        <div className="mp-empty mp-styled-empty">
                            <span className="material-symbols-outlined">request_quote</span>
                            <h3>Chưa có nhu cầu sản xuất đang mở</h3>
                            <p>Các nhu cầu gia công đang mở sẽ hiển thị tại đây khi có dữ liệu mới.</p>
                        </div>
                    ) : (
                        <div className="mp-request-grid">
                            {manufacturingRequests.map(request => (
                                <article className="mp-request-card" key={request.id}>
                                    <span>{request.type}</span>
                                    <h3>{request.title}</h3>
                                    <dl>
                                        <div><dt>Cà phê</dt><dd>{displayText(request.coffeeType)}</dd></div>
                                        <div><dt>Sản lượng</dt><dd>{displayText(request.quantity)}</dd></div>
                                        <div><dt>Deadline</dt><dd>{request.deadline ? new Date(request.deadline).toLocaleDateString('vi-VN') : emptyValue}</dd></div>
                                        <div><dt>Khu vực</dt><dd>{displayText(request.region)}</dd></div>
                                    </dl>
                                    <p>{request.details || 'Chưa cập nhật yêu cầu chi tiết'}</p>
                                </article>
                            ))}
                        </div>
                    )}
                </section>

                <section className="mp-cta">
                    <h2>Sẵn sàng đưa xưởng của bạn lên ORCA?</h2>

```
