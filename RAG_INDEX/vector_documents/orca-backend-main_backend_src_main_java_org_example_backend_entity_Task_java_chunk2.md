# Knowledge Document: Task.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/Task.java",
  "language": "java",
  "module": "entity",
  "business_domain": "report",
  "tags": [
    "report",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production

## Source Code Chunk
```java
alWorkload;
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

    public LocalDateTime getDeadline() {
        return deadline;
    }

    public void setDeadline(LocalDateTime deadline) {
        this.deadline = deadline;
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

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public String getAcceptanceStatus() { return acceptanceStatus; }
    public void setAcceptanceStatus(String acceptanceStatus) { this.acceptanceStatus = acceptanceStatus; }

    public Double getHourlyRate() { return hourlyRate; }
    public void setHourlyRate(Double hourlyRate) { this.hourlyRate = hourlyRate; }

    public String getProductionStage() { return productionStage; }
    public void setProductionStage(String productionStage) { this.productionStage = productionStage; }

    public LocalDateTime getDueTime() { return dueTime; }
    public void setDueTime(LocalDateTime dueTime) { this.dueTime = dueTime; }

    public User getSupervisor() { return supervisor; }
    public void setSupervisor(User supervisor) { this.supervisor = supervisor; }
}

```
