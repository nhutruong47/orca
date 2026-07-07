# Knowledge Document: groupService.ts (Chunk 5/8)

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
  "chunk_index": 4,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts
ate: string, endDate: string) =>
        api.get<any>(`/api/production/dashboard/${teamId}/productivity`, {
            params: { startDate, endDate }
        }).then(r => r.data),

    // === NEW: Daily Production Board ===
    getDailyBoard: (teamId: string) =>
        api.get<any>(`/api/production/board/${teamId}/today`).then(r => r.data),

    getBoardByDate: (teamId: string, date: string) =>
        api.get<any>(`/api/production/board/${teamId}/date/${date}`).then(r => r.data),

    getCalendarBoard: (teamId: string, startDate: string, endDate: string) =>
        api.get<any[]>(`/api/production/board/${teamId}/calendar`, {
            params: { startDate, endDate }
        }).then(r => r.data),

    getWorkforce: (teamId: string) =>
        api.get<any>(`/api/production/board/${teamId}/workforce`).then(r => r.data),

    // === NEW: Analytics ===
    getAnalytics: (teamId: string, startDate: string, endDate: string) =>
        api.get<any>(`/api/production/analytics/${teamId}`, {
            params: { startDate, endDate }
        }).then(r => r.data),

    getReplan: (orderId: string) =>
        api.get<any>(`/api/production/analytics/orders/${orderId}/replan`).then(r => r.data),

    applyReplan: (orderId: string, revisedTargets: any[]) =>
        api.post<any>(`/api/production/analytics/orders/${orderId}/replan/apply`, revisedTargets).then(r => r.data),
};

import type { DailyTarget } from '../types/types';
import type { ProductionPlan } from '../types/types';

export const workforceService = {
    getSkills: (teamId: string) =>
        api.get(`/api/workforce/teams/${teamId}/skills`).then(r => r.data),
    createSkill: (teamId: string, data: { name: string; description?: string }) =>
        api.post(`/api/workforce/teams/${teamId}/skills`, data).then(r => r.data),
    getSkillMatrix: (teamId: string) =>
        api.get(`/api/workforce/teams/${teamId}/skill-matrix`).then(r => r.data),
    setWorkerSkill: (teamMemberId: string, skillId: string, level: number) =>
        api.put(`/api/workforce/members/${teamMemberId}/skills/${skillId}`, { level }).then(r => r.data),
};

export const aiPlanService = {
    getByTeam: (teamId: string) =>
        api.get(`/api/ai-plans/teams/${teamId}`).then(r => r.data),
    createDraft: (teamId: string, data: any) =>
        api.post(`/api/ai-plans/teams/${teamId}`, data).then(r => r.data),

```
