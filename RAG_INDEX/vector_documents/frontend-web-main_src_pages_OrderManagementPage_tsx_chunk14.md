# Knowledge Document: OrderManagementPage.tsx (Chunk 15/23)

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
  "chunk_index": 14,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
              <div style={{ gridColumn: '1/-1', display: 'flex', justifyContent: 'flex-end', gap: 16, marginTop: 16 }}>
                                <button
                                    type="button"
                                    className="btn btn-secondary"
                                    onClick={() => {
                                        setShowManualOrderForm(false);
                                        setManualCreateError('');
                                    }}
                                    style={{ padding: '14px 28px', fontSize: 16 }}
                                >
                                    Hủy
                                </button>
                                <button type="submit" className="btn btn-primary" disabled={manualCreateLoading} style={{ opacity: manualCreateLoading ? 0.65 : 1, padding: '14px 28px', fontSize: 16 }}>
                                    {manualCreateLoading ? 'Đang tạo...' : 'Tạo đơn thủ công'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}

            {loading ? (
                <div className="empty-state" style={{ padding: '40px 20px' }}>
                    <p>Đang tải đơn hàng...</p>
                </div>
            ) : orders.length === 0 ? (
                <div className="empty-state glass-panel" style={{ padding: '80px 20px', borderStyle: 'dashed' }}>
                    <div className="empty-icon"><span className="icon-container glow" style={{ width: 64, height: 64, fontSize: 40 }}><ion-icon name="cube-outline"></ion-icon></span></div>
                    <p>Chưa có đơn hàng nào trong thư mục này.</p>
                </div>
            ) : (
                <div className="table-responsive glass-panel" style={{ padding: 16 }}>
                    <table className="goals-table" style={{ width: '100%', borderCollapse: 'collapse' }}>
                        <thead>
                            <tr>
                                <th style={{ textAlign: 'left', padding: '12px' }}>Đơn hàng</th>
                                <th style={{ textAlign: 'left', padding: '12px' }}>{activeTab === 'outbound' ? 'Nhà cung cấp (Bán)' : 'Người đặt (Mua)'}</th>

```
