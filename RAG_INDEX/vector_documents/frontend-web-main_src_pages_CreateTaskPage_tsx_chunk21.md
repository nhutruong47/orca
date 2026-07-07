# Knowledge Document: CreateTaskPage.tsx (Chunk 22/66)

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
  "chunk_index": 21,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
        </button>
                                ))}
                            </div>
                        </section>
                    ) : (
                        <>
                            {messages.map(msg => (
                                <div key={msg.id} className={`task-gpt-message-row ${msg.role}`}>
                                    <article className="task-gpt-bubble">
                                        {msg.role === 'assistant' && <div className="task-gpt-assistant-head">ORCA</div>}
                                        <div className="markdown-content">
                                            <ReactMarkdown remarkPlugins={[remarkGfm]}>{friendlyTaskError(msg.content)}</ReactMarkdown>
                                        </div>
                                        {msg.result && !msg.result.needsClarification && !msg.isArchived && (
                                            <div className="task-gpt-result">
                                                <AiResultRefinementForm
                                                    result={msg.result}
                                                    members={team?.members || []}
                                                    onConfirm={(finalData) => handleCreateGoal(finalData)}
                                                    onAsk={(question) => {
                                                        setInput(question);
                                                        chatInputRef.current?.focus();
                                                    }}
                                                    isConfirmed={msg.isConfirmed}
                                                    isCancelled={msg.isCancelled}
                                                    isArchived={msg.isArchived}
                                                    onCancel={() => handleCancelDraft(msg.id)}
                                                />
                                            </div>
                                        )}
                                        {msg.result && msg.isArchived && (
                                            <div style={{
                                                marginTop: 12,
                                                padding: '10px 12px',

```
