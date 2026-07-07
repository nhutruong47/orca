# Knowledge Document: GoalService.java (Chunk 6/10)

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
  "chunk_index": 5,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
al rỗng, user tự thêm task thủ công
            saved.setTotalTasks(0);
            saved.setCompletedTasks(0);
            saved.setStatus("PUBLISHED");
            saved.setAiParsedData(null);
        }

        goalRepo.save(saved);

        return toDTO(saved);
    }

    private double extractQuantity(String raw) {
        if (raw == null || raw.isBlank()) {
            return 0.0;
        }
        Matcher matcher = Pattern.compile("(\\d+(?:\\.\\d+)?)\\s*(kg|g|tấn|tan|ton|t)?", Pattern.CASE_INSENSITIVE).matcher(raw.toLowerCase());
        if (!matcher.find()) {
            return 0.0;
        }
        double value = Double.parseDouble(matcher.group(1));
        String unit = matcher.group(2);
        if (unit == null) {
            return value;
        }
        return switch (unit) {
            case "tấn", "tan", "ton", "t" -> value * 1000.0;
            case "kg" -> value;
            case "g" -> value / 1000.0;
            default -> value;
        };
    }

    public GoalDTO getDetail(UUID id) {
        Goal g = goalRepo.findById(id).orElseThrow(() -> new RuntimeException("Goal not found"));
        return toDTO(g);
    }

    public GoalDTO updateStatus(UUID id, String status) {
        Goal g = goalRepo.findById(id).orElseThrow(() -> new RuntimeException("Goal not found"));
        g.setStatus(status);

        List<Task> tasks = taskRepo.findByGoalId(id);
        long completed = tasks.stream().filter(t -> "COMPLETED".equals(t.getStatus())).count();
        g.setCompletedTasks((int) completed);
        g.setTotalTasks(tasks.size());

        if (completed == tasks.size() && !tasks.isEmpty()) {
            g.setStatus("DONE");
        }

        return toDTO(goalRepo.save(g));
    }

    public GoalDTO updateStatus(UUID id, String status, User actor) {
        Goal g = goalRepo.findById(id).orElseThrow(() -> new RuntimeException("Goal not found"));
        if (!isTeamManager(g.getTeam(), actor)) {
            throw new RuntimeException("Only managers can update production plans");
        }
        return updateStatus(id, status);
    }

    public void delete(UUID id) {
        taskRepo.deleteAll(taskRepo.findByGoalId(id));
        goalRepo.deleteById(id);
    }

    public void delete(UUID id, User actor) {
        Goal g = goalRepo.findById(id).orElseThrow(() -> new RuntimeException("Goal not found"));

```
