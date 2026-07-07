# Knowledge Document: CreateTaskPage.tsx (Chunk 1/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
import { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { useParams, useNavigate } from 'react-router-dom';
import { teamService, aiWorkflowService, goalService, getTrialStatus } from '../services/groupService';
import { isPaymentRequiredError } from '../services/api';
import type { AiParseResult, AiV2PlanDraft } from '../services/groupService';
import type { Team, TeamMemberInfo } from '../types/types';
import { estimateTokens, formatTokenCount } from '../utils/tokenUsage';

interface ChatMessage {
    id: string;
    role: 'user' | 'assistant';
    content: string;
    result?: AiParseResult;
    timestamp: Date;
    isConfirmed?: boolean;
    isCancelled?: boolean;
    isArchived?: boolean;
}

const priorityLabel = (priority: number) => {
    if (priority >= 4) return 'high';
    if (priority <= 1) return 'low';
    return 'medium';
};

const priorityNumber = (priority?: string) => {
    const value = priority?.toLowerCase();
    if (value === 'high') return 4;
    if (value === 'low') return 1;
    return 2;
};

const draftToResult = (draft: AiV2PlanDraft): AiParseResult => ({
    title: draft.goalTitle || 'Mục tiêu mới',
    description: `Tôi đã tạo bản nháp gồm ${draft.tasks?.length || 0} công việc. Vui lòng xem lại trước khi lưu.`,
    quantity: draft.outputTarget || null,
    quantityNumber: null,
    unit: null,
    deadline: draft.deadline || null,
    priority: priorityLabel(draft.priority || 2),
    needsClarification: false,
    source: 'ai-v2',
    tasks: (draft.tasks || []).map((task) => ({
        title: task.title,
        description: task.description || '',
        priority: task.priority,
        workload: task.workload,
        suggestedAssignee: task.suggestedAssigneeName || undefined,
        suggestedAssigneeId: task.suggestedAssigneeId,
        suggestedReason: task.suggestedReason,
    })),
});

const resultToDraft = (result: AiParseResult): AiV2PlanDraft => ({
    goalTitle: result.title || 'Mục tiêu mới',
    outputTarget: result.quantity || result.description || '',
    deadline: result.deadline,
    priority: priorityNumber(result.priority),
    tasks: (result.tasks || []).map((task) => ({
        title: task.title || task.description || 'Công việc mới',
        description: task.description || task.title || '',

```
