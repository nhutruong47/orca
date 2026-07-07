# Knowledge Document: DailyBoardPage.tsx (Chunk 3/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DailyBoardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
            setError(e?.response?.data?.error || 'Khong tai duoc du lieu');
        } finally {
            setLoading(false);
        }
    };

    const dateLabel = new Date(selectedDate + 'T00:00:00').toLocaleDateString('vi-VN', {
        weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
    });

    if (loading) return (
        <div style={{ padding: 40, textAlign: 'center' }}>
            <div style={{ color: 'var(--text-muted)', fontSize: 14 }}>Dang tai du lieu...</div>
        </div>
    );

    if (error) return (
        <div style={{ padding: 40, textAlign: 'center' }}>
            <div style={{ color: '#ef4444', fontSize: 14, background: 'rgba(239,68,68,0.1)', border: '1px solid rgba(239,68,68,0.2)', borderRadius: 12, padding: 16, display: 'inline-block' }}>{error}</div>
        </div>
    );

    const roast = board?.roast || {};
    const qc = board?.qc || {};
    const packaging = board?.packaging || {};
    const totalTarget = board?.totalTargetKg || 0;
    const totalActual = board?.totalActualKg || 0;
    const completionRate = board?.completionRate || 0;
    const remaining = Math.max(0, totalTarget - totalActual);

    return (
        <div style={{ padding: '24px 28px', margin: '0 auto' }}>
            {/* Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 24 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                    <button onClick={() => navigate(`/groups/${teamId}`)} style={{
                        background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                        width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                        color: 'var(--text-secondary)', fontSize: 18, flexShrink: 0
                    }}>
                        <ion-icon name="chevron-back-outline" />
                    </button>
                    <div>
                        <h1 style={{ fontSize: 20, fontWeight: 800, color: 'var(--text-primary)', marginBottom: 4 }}>Bang San Xuat Ngay</h1>
                        <p style={{ fontSize: 13, color: 'var(--text-muted)', margin: 0 }}>{dateLabel}</p>
                    </div>
                </div>

```
