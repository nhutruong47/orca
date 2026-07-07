# Knowledge Document: GoalService.java (Chunk 8/10)

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
  "chunk_index": 7,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
.setCreatedAt(g.getCreatedAt());
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
        } catch (DateTimeParseException e1) {
            try {
                // If it's a number (like "10"), treat it as days from now
                int days = Integer.parseInt(deadlineStr.trim());
                return LocalDateTime.now().plusDays(days);
            } catch (NumberFormatException e2) {
                // Fallback: 7 days
                return LocalDateTime.now().plusDays(7);
            }
        }
    }

    private String requireTaskTitle(Map<String, Object> taskPayload) {
        String title = asString(taskPayload.get("title"));
        if (title == null || title.isBlank()) {
            title = asString(taskPayload.get("description"));
        }
        if (title == null || title.isBlank()) {
            throw new RuntimeException("Task title is required");
        }
        return title.trim();
    }

    private Double parseWorkload(Object workloadObj, boolean required) {
        Double workload = null;
        if (workloadObj instanceof Number number) {
            workload = number.doubleValue();
        } else if (workloadObj instanceof String str && !str.isBlank()) {
            try {
                workload = Double.parseDouble(str);
            } catch (NumberFormatException e) {
                throw new RuntimeException("Task workload must be a number");
            }
        }

        if (workload == null) {
            if (required) {
                throw new RuntimeException("Task workload is required");
            }
            return 1.0;
        }
        if (workload <= 0) {
            throw new RuntimeException("Task workload must be greater than 0");
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

```
