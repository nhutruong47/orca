# Knowledge Document: CreateTaskPage.tsx (Chunk 51/66)

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
  "chunk_index": 50,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
             @keyframes slideUp {
                    from { transform: translateY(20px); opacity: 0; }
                    to { transform: translateY(0); opacity: 1; }
                }
                .markdown-content { white-space: pre-wrap; font-size: 14px; }
                .markdown-content table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 13px; background: #fff; }
                .markdown-content th, .markdown-content td { border: 1px solid #fde68a; padding: 10px; text-align: left; }
                .markdown-content th { background: #fef3c7; font-weight: 700; color: #92400e; }
                .markdown-content p { margin: 8px 0; }
                .markdown-content h3 { margin: 16px 0 8px; font-size: 16px; font-weight: 800; color: #92400e; }
            `}</style>
        </div>
    );
}
/**
 * Component to refine and edit the AI parse result before creation.
 * Matches the design in the user's screenshot.
 */
function AiResultRefinementForm({ result, members, onConfirm, onAsk, isConfirmed, isCancelled, isArchived, onCancel }: { result: AiParseResult, members: TeamMemberInfo[], onConfirm: (data: AiParseResult) => void, onAsk: (q: string) => void, isConfirmed?: boolean, isCancelled?: boolean, isArchived?: boolean, onCancel?: () => void }) {
    const [editedResult, setEditedResult] = useState<AiParseResult>({
        ...result,
        tasks: result.tasks ? [...result.tasks] : []
    });

    const updateField = (field: keyof AiParseResult, value: any) => {
        setEditedResult(prev => ({ ...prev, [field]: value }));
    };

    const updateTaskTitle = (index: number, value: string) => {
        const newTasks = [...(editedResult.tasks || [])];
        newTasks[index] = { ...newTasks[index], title: value };
        updateField('tasks', newTasks);
    };

    const updateTaskDescription = (index: number, value: string) => {
        const newTasks = [...(editedResult.tasks || [])];
        newTasks[index] = { ...newTasks[index], description: value };
        updateField('tasks', newTasks);
    };

    const updateTaskAssignee = (index: number, userId: string) => {
        const newTasks = [...(editedResult.tasks || [])];
        if (!userId) {
            newTasks[index] = {
                ...newTasks[index],
                suggestedAssignee: undefined,
                suggestedAssigneeId: null,

```
