# Knowledge Document: CreateTaskPage.tsx (Chunk 17/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 16,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
sk-gpt-suggestions {
                        grid-template-columns: 1fr;
                    }
                    .task-gpt-message-row.user .task-gpt-bubble,
                    .task-gpt-bubble {
                        max-width: 92%;
                    }
                    .task-gpt-mode {
                        display: none;
                    }
                    .task-gpt-composer {
                        grid-template-columns: auto minmax(0, 1fr) auto;
                    }
                }
            `}</style>

            {showHistory && (
                <div className="modal-overlay" onClick={() => setShowHistory(false)} style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', zIndex: 1000, display: 'flex', justifyContent: 'flex-end' }}>
                    <div className="history-panel" onClick={e => e.stopPropagation()} style={{ width: 400, maxWidth: '100%', background: '#fff', height: '100%', padding: '20px', display: 'flex', flexDirection: 'column', boxShadow: '-5px 0 20px rgba(0,0,0,0.1)', overflowY: 'auto' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
                            <h2 style={{ margin: 0, fontSize: 18, fontWeight: 700 }}>
                                Lịch sử bản nháp ({draftMessages.length})
                            </h2>
                            <button onClick={() => setShowHistory(false)} style={{ background: 'none', border: 'none', fontSize: 24, cursor: 'pointer', color: '#64748b' }}>
                                <ion-icon name="close-outline"></ion-icon>
                            </button>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                            {draftMessages.length === 0 ? (
                                <p style={{ color: '#94a3b8', fontSize: 14, textAlign: 'center', marginTop: 40 }}>Chưa có bản nháp nào.</p>
                            ) : (
                                draftMessages.map(msg => (

```
