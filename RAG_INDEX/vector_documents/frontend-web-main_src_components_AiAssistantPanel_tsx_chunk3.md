# Knowledge Document: AiAssistantPanel.tsx (Chunk 4/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/AiAssistantPanel.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "payment",
  "tags": [
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
                        Trợ lý AI ORCA
                    </h3>
                    <p style={{ margin: 0, fontSize: 11, color: 'var(--text-secondary)' }}>
                        Mô tả mục tiêu công việc bằng ngôn ngữ tự nhiên
                    </p>
                </div>
                <button
                    type="button"
                    onClick={() => setShowTokens(prev => !prev)}
                    style={{ fontSize: 10, padding: '4px 10px', borderRadius: 20, background: showTokens ? 'rgba(99,102,241,0.18)' : 'rgba(255,255,255,0.05)', color: showTokens ? '#a5b4fc' : 'var(--text-secondary)', fontWeight: 700, border: '1px solid rgba(99,102,241,0.24)', cursor: 'pointer' }}
                >
                    {showTokens ? `Token: ${formatTokenCount(totalTokens)}` : 'Xem token'}
                </button>
                {trialActive ? (
                    <span style={{ fontSize: 10, padding: '3px 10px', borderRadius: 20, background: 'rgba(34,197,94,0.1)', color: '#22c55e', fontWeight: 600, display: 'flex', alignItems: 'center', gap: 4 }}>
                        <ion-icon name="checkmark-circle-outline" style={{ fontSize: '12px' }}></ion-icon> Còn {trialDays} ngày
                    </span>
                ) : (
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap', justifyContent: 'flex-end' }}>
                        <span style={{ fontSize: 10, padding: '3px 10px', borderRadius: 20, background: 'rgba(239,68,68,0.1)', color: '#ef4444', fontWeight: 600, display: 'flex', alignItems: 'center', gap: 4 }}>
                            <ion-icon name="close-circle-outline" style={{ fontSize: '12px' }}></ion-icon> Hết hạn
                        </span>
                        <Link to="/upgrade" style={{ fontSize: 10, padding: '4px 10px', borderRadius: 20, background: 'rgba(124,92,255,0.16)', color: '#a78bfa', fontWeight: 700, border: '1px solid rgba(124,92,255,0.28)' }}>
                            Nâng cấp
                        </Link>
                    </div>
                )}
                {/* Nút đóng / thu gọn */}
                <button
                    type="button"
                    onClick={() => setIsCollapsed(c => !c)}
                    title={isCollapsed ? 'Mở rộng' : 'Thu gọn'}
                    style={{

```
