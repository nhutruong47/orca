# Knowledge Document: MarketplacePage.tsx (Chunk 61/70)

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
  "chunk_index": 60,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                    <div className="mp-form-group">
                                <label>Ghi chú giao hàng</label>
                                <textarea rows={2} value={deliveryNote} onChange={event => setDeliveryNote(event.target.value)} placeholder="VD: Giao cổng sau, gọi trước 30 phút..." />
                            </div>
                            <div className="mp-modal-actions">
                                <button type="button" className="mp-cancel-btn" onClick={() => setShowOrderModal(false)}>Hủy</button>
                                <button type="submit" className="mp-submit-btn" disabled={submitting}>{submitting ? 'Đang gửi...' : 'Gửi yêu cầu'}</button>
                            </div>
                        </form>
                    </div>
                </div>
            )}

            {showPublishModal && (
                <div className="mp-publish-sheet-overlay" onClick={() => setShowPublishModal(false)}>
                    <div className="mp-publish-sheet" onClick={event => event.stopPropagation()}>
                        <div className="mp-publish-header">
                            <button type="button" className="mp-publish-back" onClick={() => setShowPublishModal(false)} aria-label="Quay lại">
                                <span className="material-symbols-outlined">arrow_back</span>
                            </button>
                            <h2>{editingPublishedTeam ? 'Cập nhật hồ sơ xưởng' : 'Workshop Registration'}</h2>
                        </div>
                        <form className="mp-publish-form" onSubmit={handlePublish}>
                            <div className="mp-form-group">
                                <label>Chọn xưởng</label>
                                <select
                                    value={publishTeamId}
                                    onChange={event => {
                                        const team = myTeams.find(item => item.id === event.target.value);
                                        if (team) fillPublishForm(team);
                                    }}
                                >
                                    {myTeams.map(team => <option key={team.id} value={team.id}>{team.name} {team.isPublished ? '(Đã đăng)' : ''}</option>)}
                                </select>
                            </div>

```
