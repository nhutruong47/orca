# Knowledge Document: TaskService.java (Chunk 6/15)

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
  "chunk_index": 5,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
wnerOfResponse(t, false);

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
        if (goal != null && goal.getTeam() != null) {
            UUID ownerId = goal.getTeam().getOwner().getId();
            User owner = userRepo.findById(ownerId).orElse(null);
            if (owner != null) {
                String status = accepted ? "CHẤP NHẬN" : "TỪ CHỐI";
                notificationService.createAndSend(
                    owner,
                    "Phản hồi nhiệm vụ",
                    t.getMember().getUsername() + " đã " + status + " nhiệm vụ: " + t.getTitle(),
                    accepted ? "TASK_ACCEPTED" : "TASK_REJECTED",
                    t.getId()
                );
            }
        }
    }

    /** Calculate salary report for all members in a team */
    public List<SalaryDTO> getSalaryReport(UUID teamId) {
        List<TeamMember> members = teamMemberRepo.findByTeamId(teamId);
        List<SalaryDTO> report = new ArrayList<>();

        for (TeamMember tm : members) {
            User member = tm.getUser();
            List<Task> tasks = taskRepo.findByMemberId(member.getId());
            // Filter tasks belonging to this team's goals
            List<Task> teamTasks = tasks.stream()
                .filter(t -> t.getGoal() != null && t.getGoal().getTeam() != null
                    && t.getGoal().getTeam().getId().equals(teamId))
                .collect(Collectors.toList());

            int totalTasks = teamTasks.size();
            int completed = (int) teamTasks.stream().filter(t -> "COMPLETED".equals(t.getStatus())).count();
            double totalWorkload = teamTasks.stream()
                .filter(t -> "COMPLETED".equals(t.getStatus()))
                .mapToDouble(t -> t.getActualWorkload() != null ? t.getActualWorkload() : (t.getWorkload() != null ? t.getWorkload() : 0))
                .sum();

            // Get attendance data for this member and team
            List<Attendance> attendances = attendanceRepo.findByUserIdAndTeamId(member.getId(), teamId);

```
