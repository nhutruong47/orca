# Knowledge Document: TaskService.java (Chunk 10/15)

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
  "chunk_index": 9,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
lter(t -> "COMPLETED".equals(t.getStatus())).count();
        long inProgress = tasks.stream().filter(t -> "IN_PROGRESS".equals(t.getStatus())).count();

        goalRepo.findById(goalId).ifPresent(g -> {
            g.setTotalTasks(tasks.size());
            g.setCompletedTasks((int) completed);
            if (completed == tasks.size() && !tasks.isEmpty()) {
                g.setStatus("DONE");
            } else if (completed > 0 || inProgress > 0) {
                g.setStatus("IN_PROGRESS");
            } else {
                g.setStatus("PENDING");
            }
            goalRepo.save(g);
        });
    }

    private TaskDTO toDTO(Task t) {
        TaskDTO dto = new TaskDTO();
        dto.setId(t.getId() != null ? t.getId().toString() : null);
        dto.setTitle(t.getTitle());
        dto.setDescription(t.getDescription());
        dto.setPriority(t.getPriority());
        dto.setStatus(t.getStatus());
        dto.setAcceptanceStatus(t.getAcceptanceStatus());
        dto.setHourlyRate(t.getHourlyRate());
        dto.setWorkload(t.getWorkload());
        dto.setActualWorkload(t.getActualWorkload());
        dto.setCompletionPercentage(t.getCompletionPercentage());
        dto.setOutputTarget(t.getOutputTarget());
        dto.setActualOutput(t.getActualOutput());
        dto.setDeadline(t.getDeadline());
        dto.setDueTime(t.getDueTime());
        dto.setProductionStage(t.getProductionStage());
        dto.setGoalId(t.getGoal() != null ? t.getGoal().getId().toString() : null);
        dto.setGoalTitle(t.getGoal() != null ? t.getGoal().getTitle() : null);
        dto.setTeamId(t.getGoal() != null && t.getGoal().getTeam() != null ? t.getGoal().getTeam().getId().toString() : null);
        dto.setMemberId(t.getMember() != null ? t.getMember().getId().toString() : null);
        dto.setMemberName(t.getMember() != null ? t.getMember().getUsername() : null);
        dto.setBackupMemberId(t.getBackupMember() != null ? t.getBackupMember().getId().toString() : null);
        dto.setBackupMemberName(t.getBackupMember() != null ? t.getBackupMember().getUsername() : null);
        dto.setSupervisorId(t.getSupervisor() != null ? t.getSupervisor().getId().toString() : null);
        dto.setSupervisorName(t.getSupervisor() != null ? t.getSupervisor().getUsername() : null);
        dto.setCreatedAt(t.getCreatedAt());
        return dto;
    }


```
