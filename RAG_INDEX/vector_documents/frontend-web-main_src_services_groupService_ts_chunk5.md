# Knowledge Document: groupService.ts (Chunk 6/8)

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
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in services.
- **Dependencies**: Refer to module imports.
- **Tags**: report, analytics, dashboard, chat, production, inventory, employee, notification

## Source Code Chunk
```ts
illId: string, level: number) =>
        api.put(`/api/workforce/members/${teamMemberId}/skills/${skillId}`, { level }).then(r => r.data),
};

export const aiPlanService = {
    getByTeam: (teamId: string) =>
        api.get(`/api/ai-plans/teams/${teamId}`).then(r => r.data),
    createDraft: (teamId: string, data: any) =>
        api.post(`/api/ai-plans/teams/${teamId}`, data).then(r => r.data),
    updateStatus: (planId: string, status: string) =>
        api.patch(`/api/ai-plans/${planId}/status`, { status }).then(r => r.data),
};

// === Trial Status ===
export const getTrialStatus = () =>
    api.get<{ aiTrialActive: boolean; daysRemaining: number; aiUsageCount: number; aiMaxUsage: number; aiPlan: string }>('/api/auth/trial-status').then(r => r.data);

// === AI Service ===
export interface AiParseResult {
    title: string;
    description: string;
    quantity: string | null;
    quantityNumber: number | null;
    unit: string | null;
    deadline: string | null;
    priority: string;
    needsClarification: boolean;
    source: string;
    suggestedQuestions?: string[];
    tasks?: { title: string, description: string, priority: number, workload: number, suggestedAssignee?: string, suggestedAssigneeId?: string | null, suggestedReason?: string | null, assignee?: string, assigneeRole?: string }[];
}

export const aiService = {
    parseText: (text: string, teamId: string, history?: string) =>
        api.post<AiParseResult>('/api/ai/parse', { text, teamId, history }).then(r => r.data),
};

export interface AiV2ExtractResponse {
    intent: 'PRODUCTION_PLAN' | 'OPERATION_TASK' | 'UNKNOWN';
    confidence: number;
    fields: Record<string, any>;
    missingFields: string[];
    clarifyingQuestion?: string | null;
}

export interface AiV2TaskDraft {
    title: string;
    description?: string | null;
    priority: number;
    workload: number;
    suggestedAssigneeId?: string | null;
    suggestedAssigneeName?: string | null;
    suggestedReason?: string | null;
}

export interface AiV2PlanDraft {
    goalTitle: string;
    outputTarget: string;
    deadline?: string | null;
    priority: number;
    tasks: AiV2TaskDraft[];
}

export const aiWorkflowService = {
    extract: (teamId: string, text: string) =>
        api.post<AiV2ExtractResponse>('/api/ai/v2/extract', { teamId, text }).then(r => r.data),

```
