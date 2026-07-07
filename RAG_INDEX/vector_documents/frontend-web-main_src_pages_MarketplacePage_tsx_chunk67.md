# Knowledge Document: MarketplacePage.tsx (Chunk 68/70)

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
  "chunk_index": 67,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
className="mp-publish-bottom-bar">
                                <button type="button" className="mp-cancel-btn" onClick={() => setShowPublishModal(false)}>Hủy</button>
                                <button type="submit" className="mp-submit-btn" disabled={publishing}>
                                    {publishing ? 'Đang gửi...' : editingPublishedTeam ? 'Lưu & gửi duyệt' : 'Đăng ký xưởng'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}

            {showAiMatching && (
                <div className="mp-modal-overlay" style={{background: 'rgba(9, 10, 11, 0.95)', backdropFilter: 'blur(8px)', zIndex: 10000}}>
                    <div className="mp-modal" style={{background: 'transparent', border: 'none', boxShadow: 'none', color: '#fff', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100%'}}>
                        {aiMatchingProgress < 100 ? (
                            <>
                                <div className="btn-spinner" style={{width: 80, height: 80, border: '4px solid rgba(212, 165, 116, 0.2)', borderTopColor: '#d4a574', borderRadius: '50%', marginBottom: 24}}></div>
                                <h2 style={{fontSize: 24, marginBottom: 12, color: '#ece8e1'}}>AI Matching Đang Phân Tích...</h2>
                                <p style={{color: '#a79d94', fontSize: 15, marginBottom: 32, maxWidth: 400}}>Hệ thống ORCA đang phân tích RFQ của bạn và tìm kiếm các xưởng phù hợp nhất dựa trên công suất, profile rang và độ tin cậy.</p>
                                <div style={{width: 300, background: 'rgba(255,255,255,0.1)', height: 6, borderRadius: 3, overflow: 'hidden'}}>
                                    <div style={{height: '100%', background: '#d4a574', width: `${aiMatchingProgress}%`, transition: 'width 0.3s ease'}}></div>
                                </div>
                            </>
                        ) : (
                            <div style={{background: '#171a1b', border: '1px solid rgba(255,255,255,0.05)', borderRadius: 16, padding: 32, width: '100%', maxWidth: 600, textAlign: 'left', animation: 'fadeIn 0.5s ease'}}>

```
