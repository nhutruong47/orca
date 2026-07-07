# Knowledge Document: TaskService.java (Chunk 3/15)

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
  "chunk_index": 2,
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
        Task saved = taskRepo.save(t);
        if (saved.getGoal() != null) {
            updateGoalProgress(saved.getGoal().getId());
        }
        return toDTO(saved);
    }

    public TaskDTO updateWorkload(UUID id, Double actualWorkload) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        t.setActualWorkload(actualWorkload);
        return toDTO(taskRepo.save(t));
    }

    public TaskDTO update(UUID id, Map<String, Object> updates) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        if (updates.containsKey("title")) t.setTitle((String) updates.get("title"));
        if (updates.containsKey("description")) t.setDescription((String) updates.get("description"));
        if (updates.containsKey("priority")) {
            Object p = updates.get("priority");
            t.setPriority(p instanceof Integer ? (Integer) p : (p instanceof Number ? ((Number) p).intValue() : t.getPriority()));
        }
        if (updates.containsKey("actualOutput")) {
            Object val = updates.get("actualOutput");
            t.setActualOutput(val != null ? Double.valueOf(val.toString()) : null);
        }
        if (updates.containsKey("outputTarget")) {
            Object val = updates.get("outputTarget");
            t.setOutputTarget(val != null ? Double.valueOf(val.toString()) : null);
        }
        if (updates.containsKey("productionStage")) {
            t.setProductionStage((String) updates.get("productionStage"));
        }
        if (updates.containsKey("dueTime")) {
            String due = (String) updates.get("dueTime");
            t.setDueTime(due != null ? java.time.LocalDateTime.parse(due) : null);
        }
        if (updates.containsKey("deadline")) {
            String dead = (String) updates.get("deadline");
            t.setDeadline(dead != null ? java.time.LocalDateTime.parse(dead) : null);
        }

        if (updates.containsKey("actualOutput") || updates.containsKey("outputTarget")) {
            Double target = t.getOutputTarget() != null ? t.getOutputTarget() : (t.getWorkload() != null ? t.getWorkload() : 0.0);
            Double actual = t.getActualOutput() != null ? t.getActualOutput() : 0.0;
            
            if (target > 0) {
                if (actual >= target) {

```
