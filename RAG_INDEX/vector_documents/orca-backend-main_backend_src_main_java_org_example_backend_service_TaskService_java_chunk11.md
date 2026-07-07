# Knowledge Document: TaskService.java (Chunk 12/15)

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
  "chunk_index": 11,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
        boolean isMember = teamMemberRepo.findByTeamId(teamId).stream()
                    .anyMatch(tm -> tm.getUser().getId().equals(supervisorId));
            if (!isMember) {
                throw new RuntimeException("Người dùng không thuộc xưởng này. Không thể chỉ định giám sát.");
            }
        }

        t.setSupervisor(supervisor);
        return toDTO(taskRepo.save(t));
    }

    public TaskDTO transferTask(UUID id, UUID toMemberId, String reason, String actorType, User actor) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        User to = userRepo.findById(toMemberId).orElseThrow(() -> new RuntimeException("User not found"));

        if (t.getGoal() != null && t.getGoal().getTeam() != null) {
            UUID teamId = t.getGoal().getTeam().getId();
            boolean isMember = teamMemberRepo.findByTeamId(teamId).stream()
                    .anyMatch(tm -> tm.getUser().getId().equals(toMemberId));
            if (!isMember) {
                throw new RuntimeException("Người dùng không thuộc xưởng này. Không thể chuyển giao.");
            }
        }

        User from = t.getMember();

        TaskTransfer tx = new TaskTransfer();
        tx.setTask(t);
        tx.setFromUser(from);
        tx.setToUser(to);
        tx.setActorType(actorType != null ? actorType : (actor != null ? "MANAGER" : "MEMBER"));
        tx.setReason(reason);
        transferRepo.save(tx);

        t.setMember(to);
        t.setAcceptanceStatus("WAITING");
        Task saved = taskRepo.save(t);

        notificationService.createAndSend(
            to,
            "Bạn được chuyển giao nhiệm vụ",
            "Bạn được chuyển giao nhiệm vụ: " + t.getTitle(),
            "TASK_TRANSFERRED",
            t.getId()
        );

        return toDTO(saved);
    }

    public List<Map<String, Object>> getTransfers(UUID taskId) {
        return transferRepo.findByTaskIdOrderByCreatedAtDesc(taskId).stream()
                .map(tx -> {
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("id", tx.getId().toString());
                    m.put("taskId", tx.getTask().getId().toString());
                    m.put("fromUserId", tx.getFromUser() != null ? tx.getFromUser().getId().toString() : null);

```
