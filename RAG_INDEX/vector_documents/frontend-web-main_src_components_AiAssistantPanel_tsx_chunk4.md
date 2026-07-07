# Knowledge Document: AiAssistantPanel.tsx (Chunk 5/10)

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
  "chunk_index": 4,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
lid rgba(124,92,255,0.28)' }}>
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
                        marginLeft: 'auto', background: 'none', border: 'none',
                        cursor: 'pointer', color: 'var(--text-secondary)', fontSize: 20,
                        padding: '2px 4px', display: 'flex', alignItems: 'center',
                        borderRadius: 6, transition: 'color 0.15s',
                    }}
                >
                    <ion-icon name={isCollapsed ? 'expand-outline' : 'remove-outline'}></ion-icon>
                </button>
            </div>

            {/* Nội dung — chỉ hiện khi không collapsed */}
            {!isCollapsed && (
            <>
            {/* Chat Messages Area */}
            <div className="ai-chat-container" style={{
                flex: 1,
                overflowY: 'auto',
                minHeight: '200px',
                maxHeight: `${panelHeight - 180}px`,
                padding: '16px 20px 0',
                display: 'flex',
                flexDirection: 'column',
                gap: '16px',
            }}>
                {messages.length === 0 ? (
                    <div style={{ margin: 'auto', textAlign: 'center', opacity: 0.5 }}>
                        <ion-icon name="chatbubbles-outline" style={{ fontSize: '40px', marginBottom: '8px' }}></ion-icon>
                        <p style={{ margin: 0, fontSize: '13px' }}>Hãy bắt đầu bằng cách nhập yêu cầu của bạn</p>
                        <p style={{ margin: '4px 0 0', fontSize: '11px' }}>VD: "Rang gấp 200kg cà phê Robusta trước cuối tuần"</p>
                    </div>
                ) : (
                    messages.map((msg) => (
                        <div key={msg.id} style={{
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start',
                        }}>
                            {/* Message Bubble */}

```
