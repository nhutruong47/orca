# Knowledge Document: TaskService.java (Chunk 5/15)

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
  "chunk_index": 4,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
eException("Người dùng không thuộc xưởng này. Không thể giao việc.");
            }
        }

        t.setMember(member);
        t.setAcceptanceStatus("WAITING");
        Task saved = taskRepo.save(t);

        // Send notification to assigned member
        notificationService.createAndSend(
            member,
            "Nhiệm vụ mới",
            "Bạn được giao nhiệm vụ: " + t.getTitle(),
            "TASK_ASSIGNED",
            t.getId()
        );

        return toDTO(saved);
    }

    /** Employee accepts or rejects assigned task */
    public TaskDTO respondToTask(UUID taskId, UUID userId, boolean accepted) {
        Task t = taskRepo.findById(taskId).orElseThrow(() -> new RuntimeException("Task not found"));
        if (t.getMember() == null || !t.getMember().getId().equals(userId)) {
            throw new RuntimeException("Bạn không được giao nhiệm vụ này");
        }
        t.setAcceptanceStatus(accepted ? "ACCEPTED" : "REJECTED");
        if (accepted) {
            t.setStatus("IN_PROGRESS");
            Task saved = taskRepo.save(t);
            // Notify group owner
            notifyOwnerOfResponse(t, true);
            return toDTO(saved);
        } else {
            // If rejected and there is a backup member, promote backup to assigned and notify
            User backup = t.getBackupMember();
            if (backup != null) {
                t.setMember(backup);
                t.setBackupMember(null);
                t.setAcceptanceStatus("WAITING");
                Task saved = taskRepo.save(t);

                // Notify the new assignee
                notificationService.createAndSend(
                    backup,
                    "Bạn được chọn làm sao lưu",
                    "Bạn được chỉ định thay thế nhiệm vụ: " + t.getTitle(),
                    "TASK_ASSIGNED",
                    t.getId()
                );

                // Notify owner about replacement
                notifyOwnerOfResponse(t, false);

                return toDTO(saved);
            } else {
                t.setAcceptanceStatus("REJECTED");
                Task saved = taskRepo.save(t);
                notifyOwnerOfResponse(t, false);
                return toDTO(saved);
            }
        }
    }

    private void notifyOwnerOfResponse(Task t, boolean accepted) {
        Goal goal = t.getGoal();

```
