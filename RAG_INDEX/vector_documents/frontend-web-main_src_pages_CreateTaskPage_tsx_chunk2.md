# Knowledge Document: CreateTaskPage.tsx (Chunk 3/66)

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
  "chunk_index": 2,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
 const numberMatch = normalized.match(
        /\b(?:xoa|bo|loai bo)(?:\s+di)?\s+(?:muc|task|cong viec)?\s*(?:so)?\s*(\d+)\b/
    );
    if (numberMatch) {
        const index = Number(numberMatch[1]) - 1;
        return index >= 0 && index < taskCount ? index : null;
    }

    if (/\b(?:muc|task|cong viec)?\s*cuoi\b/.test(normalized)) {
        return taskCount > 0 ? taskCount - 1 : null;
    }
    return null;
};

const applyDeterministicRevision = (
    instruction: string,
    original: AiV2PlanDraft
): AiV2PlanDraft | null => {
    const removedTaskIndex = getRequestedRemovedTaskIndex(instruction, original.tasks.length);
    if (removedTaskIndex !== null) {
        return {
            ...original,
            tasks: original.tasks.filter((_, index) => index !== removedTaskIndex),
        };
    }

    const addedTaskTitle = getRequestedAddedTaskTitle(instruction);
    if (addedTaskTitle) {
        return {
            ...original,
            tasks: [
                ...original.tasks,
                {
                    title: addedTaskTitle,
                    description: `Thực hiện công việc ${addedTaskTitle.toLowerCase()} theo yêu cầu của kế hoạch.`,
                    priority: 3,
                    workload: 1,
                    suggestedAssigneeId: null,
                    suggestedAssigneeName: null,
                    suggestedReason: 'Chưa tìm thấy người phụ trách phù hợp. Bạn có thể chọn thủ công.',
                },
            ],
        };
    }

    return null;
};

const ensureRequestedRevision = (
    instruction: string,
    original: AiV2PlanDraft,
    revised: AiV2PlanDraft
) => {
    const addedTaskTitle = getRequestedAddedTaskTitle(instruction);
    if (addedTaskTitle && revised.tasks.length <= original.tasks.length) {
        return {
            ...revised,
            tasks: [
                ...original.tasks,
                {
                    title: addedTaskTitle,
                    description: `Thực hiện công việc ${addedTaskTitle.toLowerCase()} theo yêu cầu của kế hoạch.`,
                    priority: 3,
                    workload: 1,
                    suggestedAssigneeId: null,
                    suggestedAssigneeName: null,
                    suggestedReason: 'Chưa tìm thấy người phụ trách phù hợp. Bạn có thể chọn thủ công.',
                },
            ],
        };
    }


```
