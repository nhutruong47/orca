# Knowledge Document: Goal.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/Goal.java",
  "language": "java",
  "module": "entity",
  "business_domain": "chat",
  "tags": [
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: chat

## Source Code Chunk
```java
  return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public Team getTeam() {
        return team;
    }

    public void setTeam(Team team) {
        this.team = team;
    }

    public User getOwner() {
        return owner;
    }

    public void setOwner(User owner) {
        this.owner = owner;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getOutputTarget() {
        return outputTarget;
    }

    public void setOutputTarget(String outputTarget) {
        this.outputTarget = outputTarget;
    }

    public String getRawInstruction() {
        return rawInstruction;
    }

    public void setRawInstruction(String rawInstruction) {
        this.rawInstruction = rawInstruction;
    }

    public String getAiParsedData() {
        return aiParsedData;
    }

    public void setAiParsedData(String aiParsedData) {
        this.aiParsedData = aiParsedData;
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

    public LocalDateTime getDeadline() {
        return deadline;
    }

    public void setDeadline(LocalDateTime deadline) {
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

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public String getChatLog() {
        return chatLog;
    }

    public void setChatLog(String chatLog) {
        this.chatLog = chatLog;
    }
}

```
