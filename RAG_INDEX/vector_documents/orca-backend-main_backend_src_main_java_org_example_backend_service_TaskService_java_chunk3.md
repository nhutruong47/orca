# Knowledge Document: TaskService.java (Chunk 4/15)

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
  "chunk_index": 3,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
        }

        if (updates.containsKey("actualOutput") || updates.containsKey("outputTarget")) {
            Double target = t.getOutputTarget() != null ? t.getOutputTarget() : (t.getWorkload() != null ? t.getWorkload() : 0.0);
            Double actual = t.getActualOutput() != null ? t.getActualOutput() : 0.0;
            
            if (target > 0) {
                if (actual >= target) {
                    t.setStatus("COMPLETED");
                    t.setCompletionPercentage(100);
                } else {
                    t.setCompletionPercentage((int) Math.round((actual / target) * 100));
                    if (actual > 0) {
                        t.setStatus("IN_PROGRESS");
                    } else {
                        t.setStatus("PENDING");
                    }
                }
            } else {
                if (actual > 0) {
                    t.setStatus("IN_PROGRESS");
                    t.setCompletionPercentage(50); // fallback or keep current
                } else {
                    t.setStatus("PENDING");
                    t.setCompletionPercentage(0);
                }
            }
        }

        Task saved = taskRepo.save(t);
        if (saved.getGoal() != null) {
            updateGoalProgress(saved.getGoal().getId());
        }
        return toDTO(saved);
    }

    public TaskDTO assign(UUID id, UUID memberId) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        User member = userRepo.findById(memberId).orElseThrow(() -> new RuntimeException("User not found"));
        
        // Validate if member is in the team
        if (t.getGoal() != null && t.getGoal().getTeam() != null) {
            UUID teamId = t.getGoal().getTeam().getId();
            boolean isMember = teamMemberRepo.findByTeamId(teamId).stream()
                .anyMatch(tm -> tm.getUser().getId().equals(memberId));
            if (!isMember) {
                throw new RuntimeException("Người dùng không thuộc xưởng này. Không thể giao việc.");
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

```
