# Knowledge Document: GoalService.java (Chunk 9/10)

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
  "chunk_index": 8,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
rkload must be greater than 0");
        }
        return workload;
    }

    private Integer parsePriority(Object priorityObj) {
        Integer priority = null;
        if (priorityObj instanceof Number number) {
            priority = number.intValue();
        } else if (priorityObj instanceof String str && !str.isBlank()) {
            try {
                priority = Integer.parseInt(str);
            } catch (NumberFormatException e) {
                throw new RuntimeException("Task priority must be a number from 1 to 5");
            }
        }

        if (priority == null) {
            return 2;
        }
        if (priority < 1 || priority > 5) {
            throw new RuntimeException("Task priority must be between 1 and 5");
        }
        return priority;
    }

    private User resolveTeamMember(UUID teamId, String userId) {
        UUID memberUuid;
        try {
            memberUuid = UUID.fromString(userId);
        } catch (IllegalArgumentException e) {
            throw new RuntimeException("Invalid task memberId");
        }

        if (!teamMemberRepo.existsByTeamIdAndUserId(teamId, memberUuid)) {
            throw new RuntimeException("Assigned member must belong to the team");
        }
        return userRepo.findById(memberUuid)
                .orElseThrow(() -> new RuntimeException("Assigned member not found"));
    }

    private String firstNonBlank(String first, String second) {
        if (first != null && !first.isBlank()) {
            return first;
        }
        if (second != null && !second.isBlank()) {
            return second;
        }
        return null;
    }

    private String asString(Object value) {
        return value != null ? value.toString() : null;
    }

    private String firstText(Map<String, Object> source, String... keys) {
        for (String key : keys) {
            Object value = source.get(key);
            if (value instanceof String text && !text.trim().isEmpty()) {
                return text.trim();
            }
        }
        return null;
    }

    private Optional<User> findTeamUser(List<TeamMember> members, String name) {
        String normalized = name.trim().toLowerCase(Locale.ROOT);
        return members.stream()
                .map(TeamMember::getUser)
                .filter(user -> {

```
