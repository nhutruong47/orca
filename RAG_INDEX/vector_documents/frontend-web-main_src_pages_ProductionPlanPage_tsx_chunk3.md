# Knowledge Document: ProductionPlanPage.tsx (Chunk 4/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
tualQcKg: edit.actual,
                actualPackagedKg: edit.actual,
                notes: target.notes
            });
            setDailyTargets(prev => prev.map(t => t.id === target.id ? updated : t));
            setTargetEdits(prev => {
                const next = { ...prev };
                delete next[target.id!];
                return next;
            });
        } catch (e: any) {
            alert(e.response?.data?.error || 'Loi luu tien do');
        } finally {
            setSavingTargetId(null);
        }
    };

    const handleCheckIn = async () => {
        if (!userId || !teamId) return;
        setLoadingAttendance(true);
        try {
            const result = await attendanceService.checkIn(teamId, {
                shiftType, stage, orderId: selectedOrder?.id, breakMinutes
            });
            setMyAttendance(result);
            alert('Check-in thanh cong!');
        } catch (e: any) {
            alert(e.response?.data?.error || e.message || 'Loi check-in');
        } finally {
            setLoadingAttendance(false);
        }
    };

    const handleCheckOut = async () => {
        if (!userId || !teamId) return;
        setLoadingAttendance(true);
        try {
            const result = await attendanceService.checkOut(teamId);
            setMyAttendance(result);
            alert('Check-out thanh cong!');
        } catch (e: any) {
            alert(e.response?.data?.error || e.message || 'Loi check-out');
        } finally {
            setLoadingAttendance(false);
        }
    };

    if (loading) return <div style={{ padding: 40, textAlign: 'center', color: 'var(--text-muted)' }}>Dang tai...</div>;

    return (
        <div style={{ padding: 24, margin: '0 auto' }}>
            {/* Header */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 24 }}>
                <button onClick={() => navigate(`/groups/${id}`)} style={{
                    background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                    width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: 'var(--text-secondary)', fontSize: 18,
                }}>
                    <ion-icon name="chevron-back-outline" />
                </button>

```
