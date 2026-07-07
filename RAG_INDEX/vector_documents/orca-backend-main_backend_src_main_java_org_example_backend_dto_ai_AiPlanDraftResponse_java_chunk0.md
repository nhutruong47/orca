# Knowledge Document: AiPlanDraftResponse.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ai/AiPlanDraftResponse.java",
  "language": "java",
  "module": "ai",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in ai.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.dto.ai;

import java.util.ArrayList;
import java.util.List;

public class AiPlanDraftResponse {
    private String goalTitle;
    private String outputTarget;
    private String deadline;
    private Integer priority;
    private List<AiTaskDraft> tasks = new ArrayList<>();

    public String getGoalTitle() {
        return goalTitle;
    }

    public void setGoalTitle(String goalTitle) {
        this.goalTitle = goalTitle;
    }

    public String getOutputTarget() {
        return outputTarget;
    }

    public void setOutputTarget(String outputTarget) {
        this.outputTarget = outputTarget;
    }

    public String getDeadline() {
        return deadline;
    }

    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }

    public Integer getPriority() {
        return priority;
    }

    public void setPriority(Integer priority) {
        this.priority = priority;
    }

    public List<AiTaskDraft> getTasks() {
        return tasks;
    }

    public void setTasks(List<AiTaskDraft> tasks) {
        this.tasks = tasks;
    }
}

```
