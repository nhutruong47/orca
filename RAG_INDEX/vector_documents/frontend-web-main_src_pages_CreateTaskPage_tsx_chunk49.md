# Knowledge Document: CreateTaskPage.tsx (Chunk 50/66)

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
  "chunk_index": 49,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
  }}
                            >
                                <div style={{ width: 18, height: 18, border: '2px solid currentColor', borderRadius: '50%', opacity: 0.5 }}></div> Gửi
                            </button>
                        </div>
                        <div style={{ marginTop: 12, fontSize: 12, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: 4 }}>
                            <ion-icon name="sparkles"></ion-icon> AI sẽ tạo công việc, phân công và hạn chót.
                        </div>
                    </div>
                </div>
            </div>
            <style>{`
                .dot-typing {
                    position: relative;
                    left: -9999px;
                    width: 6px;
                    height: 6px;
                    border-radius: 5px;
                    background-color: transparent;
                    color: inherit;
                    box-shadow: 9984px 0 0 0 currentcolor, 9999px 0 0 0 currentcolor, 10014px 0 0 0 currentcolor;
                    animation: dot-typing 1.5s infinite linear;
                }
                @keyframes dot-typing {
                    0% { box-shadow: 9984px 0 0 0 currentcolor, 9999px 0 0 0 currentcolor, 10014px 0 0 0 currentcolor; }
                    16.667% { box-shadow: 9984px -6px 0 0 currentcolor, 9999px 0 0 0 currentcolor, 10014px 0 0 0 currentcolor; }
                    33.333% { box-shadow: 9984px 0 0 0 currentcolor, 9999px -6px 0 0 currentcolor, 10014px 0 0 0 currentcolor; }
                    50% { box-shadow: 9984px 0 0 0 currentcolor, 9999px 0 0 0 currentcolor, 10014px -6px 0 0 currentcolor; }
                    66.667% { box-shadow: 9984px 0 0 0 currentcolor, 9999px 0 0 0 currentcolor, 10014px 0 0 0 currentcolor; }
                    100% { box-shadow: 9984px 0 0 0 currentcolor, 9999px 0 0 0 currentcolor, 10014px 0 0 0 currentcolor; }
                }
                @keyframes slideUp {
                    from { transform: translateY(20px); opacity: 0; }
                    to { transform: translateY(0); opacity: 1; }
                }
                .markdown-content { white-space: pre-wrap; font-size: 14px; }
                .markdown-content table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 13px; background: #fff; }

```
