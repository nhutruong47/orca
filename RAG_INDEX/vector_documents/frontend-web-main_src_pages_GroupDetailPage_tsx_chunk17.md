# Knowledge Document: GroupDetailPage.tsx (Chunk 18/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 17,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
        @keyframes pulse-ai-btn {
                            0% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.7); }
                            70% { box-shadow: 0 0 0 10px rgba(245, 158, 11, 0); }
                            100% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0); }
                        }
                        `}
                    </style>
                    {team.inviteCode && (
                        <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: 'var(--bg-input)', padding: '8px 14px', borderRadius: 10, border: '1px solid var(--border)' }}>
                            <ion-icon name="key-outline" style={{ fontSize: 14, color: 'var(--text-muted)' }}></ion-icon>
                            <span style={{ fontSize: 12, color: 'var(--text-secondary)' }}>Mã mời:</span>
                            <span onClick={() => navigator.clipboard.writeText(team.inviteCode || '')} style={{ fontWeight: 800, letterSpacing: 3, color: 'var(--accent-primary)', cursor: 'pointer' }}>{team.inviteCode}</span>
                        </div>
                    )}

                    {/* NÚT AI NỔI BẬT ĐƯA LÊN TRƯỚC */}
                    {isAdmin && (
                        <button
                            onClick={() => navigate(`/groups/${team.id}/create-task`)}
                            style={{
                                background: 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
                                color: '#fff',
                                border: 'none',
                                borderRadius: 10,
                                padding: '8px 20px',
                                fontSize: 14,
                                fontWeight: 800,
                                cursor: 'pointer',
                                display: 'flex',
                                alignItems: 'center',
                                gap: 8,
                                textShadow: '0 1px 2px rgba(0,0,0,0.28)',
                                animation: 'pulse-ai-btn 2s infinite',
                                transition: 'all 0.3s ease'
                            }}
                        >
                            <ion-icon name="sparkles" style={{ fontSize: '18px' }}></ion-icon>
                            Phân chia công việc tự động
                        </button>

```
