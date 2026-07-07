# Knowledge Document: TaskService.java (Chunk 2/15)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/TaskService.java",
  "language": "java",
  "module": "service",
  "business_domain": "report",
  "tags": [
    "report",
    "production",
    "attendance",
    "employee",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
r(UUID memberId) {
        return taskRepo.findByMemberId(memberId).stream().map(this::toDTO).collect(Collectors.toList());
    }

    public List<TaskDTO> getAll() {
        return taskRepo.findAll().stream().map(this::toDTO).collect(Collectors.toList());
    }

    public TaskDTO getById(UUID id) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        return toDTO(t);
    }

    public TaskDTO create(TaskDTO dto) {
        Task t = new Task();
        t.setTitle(dto.getTitle());
        t.setDescription(dto.getDescription());
        t.setPriority(dto.getPriority() != null ? dto.getPriority() : 1);
        t.setDeadline(dto.getDeadline());
        t.setStatus("PENDING");
        t.setWorkload(dto.getWorkload());

        if (dto.getGoalId() != null) {
            goalRepo.findById(UUID.fromString(dto.getGoalId())).ifPresent(t::setGoal);
        }
        if (dto.getMemberId() != null) {
            userRepo.findById(UUID.fromString(dto.getMemberId())).ifPresent(t::setMember);
        }
        return toDTO(taskRepo.save(t));
    }

    public TaskDTO updateStatus(UUID id, String status) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        t.setStatus(status);
        if ("COMPLETED".equals(status)) {
            t.setCompletionPercentage(100);
        }
        Task saved = taskRepo.save(t);

        // Update goal progress
        if (saved.getGoal() != null) {
            updateGoalProgress(saved.getGoal().getId());
        }

        return toDTO(saved);
    }

    public TaskDTO updateProgress(UUID id, int percentage) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        t.setCompletionPercentage(percentage);
        if (percentage == 100) {
            t.setStatus("COMPLETED");
        } else if (percentage > 0 && "PENDING".equals(t.getStatus())) {
            t.setStatus("IN_PROGRESS");
        }
        Task saved = taskRepo.save(t);
        if (saved.getGoal() != null) {
            updateGoalProgress(saved.getGoal().getId());
        }
        return toDTO(saved);
    }

    public TaskDTO updateWorkload(UUID id, Double actualWorkload) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        t.setActualWorkload(actualWorkload);

```
