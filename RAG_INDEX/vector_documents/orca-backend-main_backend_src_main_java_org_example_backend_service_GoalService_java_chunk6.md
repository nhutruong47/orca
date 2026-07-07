# Knowledge Document: GoalService.java (Chunk 7/10)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/GoalService.java",
  "language": "java",
  "module": "service",
  "business_domain": "employee",
  "tags": [
    "employee",
    "admin",
    "production",
    "chat"
  ],
  "logical_type": "Service",
  "chunk_index": 6,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
w new RuntimeException("Only managers can update production plans");
        }
        return updateStatus(id, status);
    }

    public void delete(UUID id) {
        taskRepo.deleteAll(taskRepo.findByGoalId(id));
        goalRepo.deleteById(id);
    }

    public void delete(UUID id, User actor) {
        Goal g = goalRepo.findById(id).orElseThrow(() -> new RuntimeException("Goal not found"));
        if (!isTeamManager(g.getTeam(), actor)) {
            throw new RuntimeException("Only managers can delete production plans");
        }
        delete(id);
    }

    private boolean isTeamManager(Team team, User user) {
        if (team == null || user == null) {
            return false;
        }
        if (user.getRole() == Role.ADMIN || (team.getOwner() != null && team.getOwner().getId().equals(user.getId()))) {
            return true;
        }
        return teamMemberRepo.findByTeamIdAndUserId(team.getId(), user.getId())
                .map(tm -> tm.getGroupRole() == GroupRole.ADMIN)
                .orElse(false);
    }

    private GoalDTO toDTO(Goal g) {
        GoalDTO dto = new GoalDTO();
        dto.setId(g.getId() != null ? g.getId().toString() : null);
        dto.setTitle(g.getTitle());
        dto.setOutputTarget(g.getOutputTarget());
        dto.setRawInstruction(g.getRawInstruction());
        dto.setAiParsedData(g.getAiParsedData());
        dto.setPriority(g.getPriority());
        dto.setStatus(g.getStatus());
        dto.setDeadline(g.getDeadline() != null ? g.getDeadline().toString() : null);
        dto.setTotalTasks(g.getTotalTasks());
        dto.setCompletedTasks(g.getCompletedTasks());
        dto.setTeamId(g.getTeam() != null ? g.getTeam().getId().toString() : null);
        dto.setTeamName(g.getTeam() != null ? g.getTeam().getName() : null);
        dto.setOwnerId(g.getOwner() != null ? g.getOwner().getId().toString() : null);
        dto.setOwnerName(g.getOwner() != null ? g.getOwner().getUsername() : null);
        dto.setCreatedAt(g.getCreatedAt());
        dto.setChatLog(g.getChatLog());
        return dto;
    }

    private LocalDateTime parseDeadline(String deadlineStr) {
        if (deadlineStr == null || deadlineStr.trim().isEmpty()) {
            return null;
        }
        try {
            // Try ISO format first
            return LocalDateTime.parse(deadlineStr, DateTimeFormatter.ISO_DATE_TIME);

```
