# Knowledge Document: groupService.ts (Chunk 1/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/services/groupService.ts",
  "language": "ts",
  "module": "services",
  "business_domain": "report",
  "tags": [
    "report",
    "analytics",
    "dashboard",
    "chat",
    "production",
    "inventory",
    "employee",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts
import api from './api';
import type { Team, Goal, Task, ProductionOrder } from '../types/types';
import type { AppNotification, SalaryReport } from '../types/types';

// === Team/Group API ===
export const teamService = {
    getAllTeams: () => api.get<Team[]>('/api/teams/all').then(r => r.data),
    getMyTeams: () => api.get<Team[]>('/api/teams').then(r => r.data),
    getDetail: (id: string) => api.get<Team>(`/api/teams/${id}`).then(r => r.data),
    create: (data: { name: string; description?: string }) =>
        api.post<Team>('/api/teams', data).then(r => r.data),
    update: (id: string, data: { name?: string; description?: string; metadata?: string }) =>
        api.put<Team>(`/api/teams/${id}`, data).then(r => r.data),
    addMember: (teamId: string, email: string) =>
        api.post<{ status: string; message: string; inviteLink?: string }>(`/api/teams/${teamId}/members`, { email }).then(r => r.data),
    removeMember: (teamId: string, userId: string) =>
        api.delete(`/api/teams/${teamId}/members/${userId}`),
    updateMemberLabels: (teamId: string, userId: string, labels: string[]) =>
        api.put<string[]>(`/api/teams/${teamId}/members/${userId}/labels`, { labels }).then(r => r.data),
    deleteTeam: (id: string) => api.delete(`/api/teams/${id}`),
    joinByCode: (inviteCode: string) =>
        api.post<Team>('/api/teams/join', { inviteCode }).then(r => r.data),

    // Advertisement
    advertise: (teamId: string, data: Partial<Team>) =>
        api.put<Team>(`/api/teams/${teamId}/advertise`, data).then(r => r.data),
    submitVerification: (teamId: string, data: Partial<Team>) =>
        api.put<Team>(`/api/teams/${teamId}/verification`, data).then(r => r.data),
    unpublish: (teamId: string) =>
        api.put(`/api/teams/${teamId}/unpublish`).then(r => r.data),
};

// === Goal API ===
export const goalService = {
    getByTeam: (teamId: string) =>
        api.get<Goal[]>(`/api/goals?teamId=${teamId}`).then(r => r.data),
    getDetail: (id: string) => api.get<Goal>(`/api/goals/${id}`).then(r => r.data),
    create: (data: Partial<Goal>) =>
        api.post<Goal>('/api/goals', data).then(r => r.data),
    updateStatus: (id: string, status: string) =>
        api.patch<Goal>(`/api/goals/${id}/status`, { status }).then(r => r.data),
    delete: (id: string) => api.delete(`/api/goals/${id}`),
};

// === Task API ===

```
