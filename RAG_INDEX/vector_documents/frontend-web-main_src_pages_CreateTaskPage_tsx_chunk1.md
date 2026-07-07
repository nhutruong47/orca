# Knowledge Document: CreateTaskPage.tsx (Chunk 2/66)

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
  "chunk_index": 1,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
: AiParseResult): AiV2PlanDraft => ({
    goalTitle: result.title || 'Mục tiêu mới',
    outputTarget: result.quantity || result.description || '',
    deadline: result.deadline,
    priority: priorityNumber(result.priority),
    tasks: (result.tasks || []).map((task) => ({
        title: task.title || task.description || 'Công việc mới',
        description: task.description || task.title || '',
        priority: task.priority || 2,
        workload: task.workload || 1,
        suggestedAssigneeId: task.suggestedAssigneeId || null,
        suggestedAssigneeName: task.suggestedAssignee || null,
        suggestedReason: task.suggestedReason || null,
    })),
});

const normalizeVietnameseText = (value: string) =>
    value
        .toLowerCase()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .replace(/đ/g, 'd')
        .replace(/\s+/g, ' ')
        .trim();

const getRequestedAddedTaskTitle = (instruction: string) => {
    const normalized = normalizeVietnameseText(instruction);
    const match = normalized.match(
        /\bthem(?:\s+\d+)?\s+(?:muc|task|cong viec)(?:\s+nua)?(?:\s+(?:la|ve|cho))?\s*[:\-]?\s*(.+)$/
    );
    if (!match) return null;

    const title = match[1]
        .replace(/^(?:muc|task|cong viec)\s*(?:so)?\s*\d+\s*(?:la|:|-)?\s*/, '')
        .replace(/^[\s.,:;-]+|[\s.,:;-]+$/g, '');
    if (!title) return null;

    const knownTitles: Record<string, string> = {
        'van chuyen': 'Vận chuyển',
        'giao hang': 'Giao hàng',
        'giao hang thanh pham': 'Giao hàng thành phẩm',
        'ban giao': 'Bàn giao',
        'dong goi': 'Đóng gói',
        'kiem tra chat luong': 'Kiểm tra chất lượng',
    };
    return knownTitles[title] || `${title.charAt(0).toUpperCase()}${title.slice(1)}`;
};

const getRequestedRemovedTaskIndex = (instruction: string, taskCount: number) => {
    const normalized = normalizeVietnameseText(instruction);
    if (!/\b(xoa|bo|loai bo)\b/.test(normalized)) return null;

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

```
