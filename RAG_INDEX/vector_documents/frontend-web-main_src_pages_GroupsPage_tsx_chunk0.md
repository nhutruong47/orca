# Knowledge Document: GroupsPage.tsx (Chunk 1/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
import { useEffect, useMemo, useState, type FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import { teamService } from '../services/groupService';
import type { Team } from '../types/types';

export default function GroupsPage() {
  const navigate = useNavigate();
  const [groups, setGroups] = useState<Team[]>([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [showJoinModal, setShowJoinModal] = useState(false);
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [inviteCode, setInviteCode] = useState('');
  const [managedTeam, setManagedTeam] = useState<Team | null>(null);
  const [editName, setEditName] = useState('');
  const [editDescription, setEditDescription] = useState('');
  const [error, setError] = useState('');

  const totalMembers = useMemo(
    () => groups.reduce((sum, group) => sum + (group.memberCount || group.members?.length || 0), 0),
    [groups],
  );

  const publishedCount = useMemo(
    () => groups.filter(group => group.isPublished).length,
    [groups],
  );

  const loadGroups = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await teamService.getMyTeams();
      setGroups(data);
    } catch (err: any) {
      setError(err?.response?.data?.error || 'Không thể tải danh sách nhóm.');
      setGroups([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadGroups();
  }, []);

  const resetCreateForm = () => {
    setName('');
    setDescription('');
    setError('');
  };

  const openCreateModal = () => {
    resetCreateForm();
    setShowCreateModal(true);
  };

  const closeCreateModal = () => {
    if (saving) return;
    setShowCreateModal(false);
    resetCreateForm();
  };

  const openJoinModal = () => {
    setInviteCode('');
    setError('');
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

```
