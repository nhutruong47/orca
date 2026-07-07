# Knowledge Document: TaskDTO.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/TaskDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;

public class TaskDTO {
    private String id;
    private String title;
    private String description;
    private Integer priority;
    private String status;
    private String acceptanceStatus;
    private Double hourlyRate;
    private Double workload;
    private Double actualWorkload;
    private Integer completionPercentage;
    private Double outputTarget;
    private Double actualOutput;
    private LocalDateTime deadline;
    private String productionStage;
    private LocalDateTime dueTime;
    private String goalId;
    private String goalTitle;
    private String memberId;
    private String memberName;
    private String backupMemberId;
    private String backupMemberName;
    private String supervisorId;
    private String supervisorName;
    private LocalDateTime createdAt;
    private String teamId;

    // === Getters & Setters ===
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Integer getPriority() {
        return priority;
    }

    public void setPriority(Integer priority) {
        this.priority = priority;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Double getWorkload() {
        return workload;
    }

    public void setWorkload(Double workload) {
        this.workload = workload;
    }

    public Double getActualWorkload() {
        return actualWorkload;
    }

    public void setActualWorkload(Double actualWorkload) {
        this.actualWorkload = actualWorkload;
    }

    public Integer getCompletionPercentage() {
        return completionPercentage;
    }

    public void setCompletionPercentage(Integer completionPercentage) {
        this.completionPercentage = completionPercentage;
    }

    public Double getOutputTarget() {
        return outputTarget;
    }

    public void setOutputTarget(Double outputTarget) {
        this.outputTarget = outputTarget;

```
