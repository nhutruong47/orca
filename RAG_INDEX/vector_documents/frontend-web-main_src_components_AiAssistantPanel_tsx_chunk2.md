# Knowledge Document: AiAssistantPanel.tsx (Chunk 3/10)

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
  "chunk_index": 2,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
> = {
        high: { label: 'Cao', color: '#a0673c', icon: '●' },
        medium: { label: 'Trung bình', color: '#d4a574', icon: '●' },
        low: { label: 'Thấp', color: '#22c55e', icon: '●' },
    };

    return (
        <div style={{
            background: 'linear-gradient(135deg, rgba(99,102,241,0.05) 0%, rgba(168,85,247,0.03) 100%)',
            border: '1px solid rgba(99,102,241,0.2)',
            borderRadius: 16,
            marginBottom: 20,
            display: 'flex',
            flexDirection: 'column',
            height: isCollapsed ? 'auto' : panelHeight,
            transition: isCollapsed ? 'height 0.2s ease' : 'none',
            overflow: 'hidden',
            position: 'relative',
        }}>
            {/* Resize handle */}
            {!isCollapsed && (
                <div
                    onMouseDown={startResize}
                    style={{
                        position: 'absolute', top: 0, left: 0, right: 0,
                        height: 4, cursor: 'ns-resize', zIndex: 2,
                        borderRadius: '16px 16px 0 0',
                    }}
                    title="Kéo dãn khung"
                />
            )}

            {/* Header */}
            <div style={{
                display: 'flex', alignItems: 'center', gap: 10,
                padding: '16px 20px 0',
                flexShrink: 0,
            }}>
                <span className="icon-container glow" style={{ width: 36, height: 36, fontSize: 20, background: 'rgba(99,102,241,0.15)', borderColor: 'rgba(99,102,241,0.3)', color: '#818cf8' }}><ion-icon name="hardware-chip-outline"></ion-icon></span>
                <div>
                    <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: 'var(--text-primary)' }}>
                        Trợ lý AI ORCA
                    </h3>
                    <p style={{ margin: 0, fontSize: 11, color: 'var(--text-secondary)' }}>
                        Mô tả mục tiêu công việc bằng ngôn ngữ tự nhiên
                    </p>
                </div>
                <button
                    type="button"
                    onClick={() => setShowTokens(prev => !prev)}

```
