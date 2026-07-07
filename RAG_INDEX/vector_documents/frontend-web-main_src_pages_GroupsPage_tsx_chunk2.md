# Knowledge Document: GroupsPage.tsx (Chunk 3/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
dleUpdateTeam = async (event: FormEvent) => {
    event.preventDefault();
    if (!managedTeam) return;
    if (!editName.trim()) {
      setError('Nhap ten nhom.');
      return;
    }

    setSaving(true);
    setError('');
    try {
      const updated = await teamService.update(managedTeam.id, {
        name: editName.trim(),
        description: editDescription.trim() || undefined,
      });
      setGroups(current => current.map(group => group.id === updated.id ? updated : group));
      setManagedTeam(updated);
    } catch (err: any) {
      setError(err?.response?.data?.error || err?.response?.data?.message || 'Khong the cap nhat nhom.');
    } finally {
      setSaving(false);
    }
  };

  const handleDeleteManagedTeam = async () => {
    if (!managedTeam) return;
    const ok = window.confirm(`Xoa nhom "${managedTeam.name}"? Hanh dong nay khong the hoan tac.`);
    if (!ok) return;

    setSaving(true);
    setError('');
    try {
      await teamService.deleteTeam(managedTeam.id);
      setGroups(current => current.filter(group => group.id !== managedTeam.id));
      closeManageModal();
    } catch (err: any) {
      setError(err?.response?.data?.error || err?.response?.data?.message || 'Khong the xoa nhom.');
    } finally {
      setSaving(false);
    }
  };
  return (
    <div className="page-container" style={{ padding: '28px 24px' }}>
      <header className="page-header glass-panel" style={{ marginBottom: 20, padding: 24 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 16, flexWrap: 'wrap' }}>
          <div>
            <h1 className="page-title" style={{ margin: 0 }}>Nhóm xưởng</h1>
            <p className="page-subtitle" style={{ margin: '6px 0 0' }}>
              Quản lý nhóm xưởng, thành viên, mục tiêu và hoạt động sản xuất.
            </p>
          </div>
          <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
            <button type="button" className="btn btn-secondary" onClick={loadGroups} disabled={loading}>
              <ion-icon name="refresh-outline" style={{ fontSize: 16 }}></ion-icon>
              {loading ? 'Đang tải...' : 'Làm mới'}
            </button>
            <button type="button" className="btn btn-secondary" onClick={openJoinModal}>
              <ion-icon name="enter-outline" style={{ fontSize: 16 }}></ion-icon>

```
