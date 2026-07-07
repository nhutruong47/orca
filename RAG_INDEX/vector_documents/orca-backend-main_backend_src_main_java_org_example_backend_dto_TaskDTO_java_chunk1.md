# Knowledge Document: TaskDTO.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java

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
    }

    public Double getActualOutput() {
        return actualOutput;
    }

    public void setActualOutput(Double actualOutput) {
        this.actualOutput = actualOutput;
    }

    public LocalDateTime getDeadline() {
        return deadline;
    }

    public void setDeadline(LocalDateTime deadline) {
        this.deadline = deadline;
    }

    public String getProductionStage() { return productionStage; }
    public void setProductionStage(String productionStage) { this.productionStage = productionStage; }

    public LocalDateTime getDueTime() { return dueTime; }
    public void setDueTime(LocalDateTime dueTime) { this.dueTime = dueTime; }

    public String getGoalId() {
        return goalId;
    }

    public void setGoalId(String goalId) {
        this.goalId = goalId;
    }

    public String getGoalTitle() {
        return goalTitle;
    }

    public void setGoalTitle(String goalTitle) {
        this.goalTitle = goalTitle;
    }

    public String getMemberId() {
        return memberId;
    }

    public void setMemberId(String memberId) {
        this.memberId = memberId;
    }

    public String getMemberName() {
        return memberName;
    }

    public void setMemberName(String memberName) {
        this.memberName = memberName;
    }

    public String getBackupMemberId() { return backupMemberId; }
    public void setBackupMemberId(String backupMemberId) { this.backupMemberId = backupMemberId; }

    public String getBackupMemberName() { return backupMemberName; }
    public void setBackupMemberName(String backupMemberName) { this.backupMemberName = backupMemberName; }

    public String getSupervisorId() { return supervisorId; }
    public void setSupervisorId(String supervisorId) { this.supervisorId = supervisorId; }

    public String getSupervisorName() { return supervisorName; }
    public void setSupervisorName(String supervisorName) { this.supervisorName = supervisorName; }

    public LocalDateTime getCreatedAt() {

```
