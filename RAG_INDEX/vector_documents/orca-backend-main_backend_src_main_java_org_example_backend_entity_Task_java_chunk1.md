# Knowledge Document: Task.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production

## Source Code Chunk
```java
umn(name = "actual_output")
    private Double actualOutput;

    private LocalDateTime deadline;

    @Column(name = "production_stage")
    private String productionStage;

    @Column(name = "due_time")
    private LocalDateTime dueTime;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "supervisor_id")
    @OnDelete(action = OnDeleteAction.SET_NULL)
    private User supervisor;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
    }

    // === Getters & Setters ===
    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public Goal getGoal() {
        return goal;
    }

    public void setGoal(Goal goal) {
        this.goal = goal;
    }

    public User getMember() {
        return member;
    }

    public void setMember(User member) {
        this.member = member;
    }

    public User getBackupMember() { return backupMember; }
    public void setBackupMember(User backupMember) { this.backupMember = backupMember; }

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

    public LocalDateTime getDeadline() {

```
