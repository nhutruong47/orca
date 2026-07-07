# Knowledge Document: TaskService.java (Chunk 11/15)

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
  "chunk_index": 10,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
().toString() : null);
        dto.setBackupMemberName(t.getBackupMember() != null ? t.getBackupMember().getUsername() : null);
        dto.setSupervisorId(t.getSupervisor() != null ? t.getSupervisor().getId().toString() : null);
        dto.setSupervisorName(t.getSupervisor() != null ? t.getSupervisor().getUsername() : null);
        dto.setCreatedAt(t.getCreatedAt());
        return dto;
    }

    public TaskDTO setBackup(UUID id, UUID memberId) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        User member = userRepo.findById(memberId).orElseThrow(() -> new RuntimeException("User not found"));

        // Validate if member is in the team
        if (t.getGoal() != null && t.getGoal().getTeam() != null) {
            UUID teamId = t.getGoal().getTeam().getId();
            boolean isMember = teamMemberRepo.findByTeamId(teamId).stream()
                .anyMatch(tm -> tm.getUser().getId().equals(memberId));
            if (!isMember) {
                throw new RuntimeException("Người dùng không thuộc xưởng này. Không thể làm người sao lưu.");
            }
        }

        t.setBackupMember(member);
        Task saved = taskRepo.save(t);

        // Notify backup member
        notificationService.createAndSend(
            member,
            "Bạn được chọn làm sao lưu",
            "Bạn được chỉ định làm sao lưu cho nhiệm vụ: " + t.getTitle(),
            "TASK_ASSIGNED",
            t.getId()
        );

        return toDTO(saved);
    }

    public TaskDTO setSupervisor(UUID id, UUID supervisorId) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        User supervisor = userRepo.findById(supervisorId)
                .orElseThrow(() -> new RuntimeException("User not found"));

        if (t.getGoal() != null && t.getGoal().getTeam() != null) {
            UUID teamId = t.getGoal().getTeam().getId();
            boolean isMember = teamMemberRepo.findByTeamId(teamId).stream()
                    .anyMatch(tm -> tm.getUser().getId().equals(supervisorId));
            if (!isMember) {
                throw new RuntimeException("Người dùng không thuộc xưởng này. Không thể chỉ định giám sát.");
            }
        }

        t.setSupervisor(supervisor);
        return toDTO(taskRepo.save(t));
    }


```
