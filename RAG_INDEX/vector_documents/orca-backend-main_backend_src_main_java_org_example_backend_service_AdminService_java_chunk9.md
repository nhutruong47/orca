# Knowledge Document: AdminService.java (Chunk 10/16)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AdminService.java",
  "language": "java",
  "module": "service",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "admin",
    "production",
    "factory",
    "payment",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 9,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
toTeamMap(teamRepository.save(team));
    }

    @Transactional
    public void deleteTeam(UUID teamId) {
        Team team = teamRepository.findById(teamId).orElseThrow(() -> new RuntimeException("Team not found"));
        // Mark as deleted or locked instead of hard delete to avoid foreign key issues
        team.setPublished(false);
        teamRepository.save(team);
    }

    @Transactional
    public Map<String, Object> updateTeamPublication(UUID teamId, boolean published) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        team.setPublished(published);
        return toTeamMap(teamRepository.save(team));
    }

    @Transactional
    public Map<String, Object> updateTeamVerification(UUID teamId, String status, String rejectReason) {
        if (status == null || status.isBlank()) {
            throw new RuntimeException("Verification status is required");
        }
        String normalized = status.toUpperCase(Locale.ROOT);
        if (!List.of("APPROVED", "REJECTED").contains(normalized)) {
            throw new RuntimeException("Verification status is invalid");
        }

        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        team.setVerificationStatus(normalized);
        team.setVerificationRejectReason("REJECTED".equals(normalized) ? safeText(rejectReason, "") : "");
        return toTeamMap(teamRepository.save(team));
    }

    @Transactional
    public Map<String, Object> updateTaskStatus(UUID taskId, String status) {
        if (status == null || status.isBlank()) {
            throw new RuntimeException("Status is required");
        }

        String normalized = status.toUpperCase(Locale.ROOT);
        if (!List.of("PENDING", "IN_PROGRESS", "COMPLETED").contains(normalized)) {
            throw new RuntimeException("Task status is invalid");
        }

        taskService.updateStatus(taskId, normalized);
        Task task = taskRepository.findById(taskId)
                .orElseThrow(() -> new RuntimeException("Task not found"));
        return toTaskMap(task);
    }

    public List<SubscriptionPlan> getPlans() {
        return planRepository.findAll();
    }

    @Transactional
    public SubscriptionPlan createPlan(SubscriptionPlan plan) {

```
