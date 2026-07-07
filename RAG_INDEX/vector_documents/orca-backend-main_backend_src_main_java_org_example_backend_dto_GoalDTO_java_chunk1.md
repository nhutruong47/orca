# Knowledge Document: GoalDTO.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/GoalDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "chat",
  "tags": [
    "chat"
  ],
  "logical_type": "DTO",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: chat

## Source Code Chunk
```java
        this.status = status;
    }

    public String getDeadline() {
        return deadline;
    }

    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }

    public Integer getTotalTasks() {
        return totalTasks;
    }

    public void setTotalTasks(Integer totalTasks) {
        this.totalTasks = totalTasks;
    }

    public Integer getCompletedTasks() {
        return completedTasks;
    }

    public void setCompletedTasks(Integer completedTasks) {
        this.completedTasks = completedTasks;
    }

    public String getTeamId() {
        return teamId;
    }

    public void setTeamId(String teamId) {
        this.teamId = teamId;
    }

    public String getTeamName() {
        return teamName;
    }

    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    public String getOwnerId() {
        return ownerId;
    }

    public void setOwnerId(String ownerId) {
        this.ownerId = ownerId;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public Boolean getUseAi() {
        return useAi;
    }

    public void setUseAi(Boolean useAi) {
        this.useAi = useAi;
    }

    public String getChatLog() {
        return chatLog;
    }

    public void setChatLog(String chatLog) {
        this.chatLog = chatLog;
    }
}

```
