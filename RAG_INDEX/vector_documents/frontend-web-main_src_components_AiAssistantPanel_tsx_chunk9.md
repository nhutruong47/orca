# Knowledge Document: AiAssistantPanel.tsx (Chunk 10/10)

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
  "chunk_index": 9,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
'Enter' && !e.shiftKey) {
                            e.preventDefault();
                            handleSend();
                        }
                    }}
                    placeholder={trialActive ? 'Nhập yêu cầu quản lý xưởng...' : 'Dùng thử đã hết hạn'}
                    disabled={!trialActive || loading}
                    style={{
                        flex: 1, fontSize: 13,
                        background: 'rgba(0,0,0,0.2)',
                        border: '1px solid rgba(99,102,241,0.3)',
                        borderRadius: '12px',
                        padding: '10px 14px'
                    }}
                />
                <button
                    className="btn btn-primary"
                    onClick={handleSend}
                    disabled={!trialActive || loading || !input.trim()}
                    style={{ whiteSpace: 'nowrap', fontSize: 13, padding: '0 18px', borderRadius: '12px' }}
                >
                    <ion-icon name="send-outline" style={{ fontSize: '16px' }}></ion-icon>
                </button>
            </div>
            </>
            )}
        </div>
    );
}

```
