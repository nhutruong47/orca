# Knowledge Document: GroupsPage.tsx (Chunk 2/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
rror('');
    setShowJoinModal(true);
  };

  const closeJoinModal = () => {
    if (saving) return;
    setShowJoinModal(false);
    setInviteCode('');
    setError('');
  };

  const handleCreateGroup = async (event: FormEvent) => {
    event.preventDefault();
    if (!name.trim()) {
      setError('Vui lòng nhập tên nhóm.');
      return;
    }

    setSaving(true);
    setError('');
    try {
      const created = await teamService.create({
        name: name.trim(),
        description: description.trim() || undefined,
      });
      setGroups(current => [created, ...current.filter(group => group.id !== created.id)]);
      setShowCreateModal(false);
      resetCreateForm();
      navigate(`/groups/${created.id}`);
    } catch (err: any) {
      setError(err?.response?.data?.error || err?.response?.data?.message || 'Khong the tao nhom moi.');
    } finally {
      setSaving(false);
    }
  };
  const handleJoinGroup = async (event: FormEvent) => {
    event.preventDefault();
    const code = inviteCode.trim().toUpperCase();
    if (!code) {
      setError('Nhap ma moi.');
      return;
    }

    setSaving(true);
    setError('');
    try {
      const joined = await teamService.joinByCode(code);
      setGroups(current => [joined, ...current.filter(group => group.id !== joined.id)]);
      setShowJoinModal(false);
      setInviteCode('');
      navigate(`/groups/${joined.id}`);
    } catch (err: any) {
      setError(err?.response?.data?.error || err?.response?.data?.message || 'Khong the tham gia nhom bang ma nay.');
    } finally {
      setSaving(false);
    }
  };


  const openManageModal = (group: Team) => {
    setManagedTeam(group);
    setEditName(group.name || '');
    setEditDescription(group.description || '');
    setError('');
  };

  const closeManageModal = () => {
    if (saving) return;
    setManagedTeam(null);
    setEditName('');
    setEditDescription('');
    setError('');
  };

  const handleUpdateTeam = async (event: FormEvent) => {
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

```
