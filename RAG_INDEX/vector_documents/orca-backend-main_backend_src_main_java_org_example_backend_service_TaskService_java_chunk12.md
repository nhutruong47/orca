# Knowledge Document: TaskService.java (Chunk 13/15)

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
  "chunk_index": 12,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
rn transferRepo.findByTaskIdOrderByCreatedAtDesc(taskId).stream()
                .map(tx -> {
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("id", tx.getId().toString());
                    m.put("taskId", tx.getTask().getId().toString());
                    m.put("fromUserId", tx.getFromUser() != null ? tx.getFromUser().getId().toString() : null);
                    m.put("fromUserName", tx.getFromUser() != null ? tx.getFromUser().getUsername() : null);
                    m.put("toUserId", tx.getToUser().getId().toString());
                    m.put("toUserName", tx.getToUser().getUsername());
                    m.put("actorType", tx.getActorType());
                    m.put("reason", tx.getReason());
                    m.put("createdAt", tx.getCreatedAt() != null ? tx.getCreatedAt().toString() : null);
                    return m;
                }).collect(Collectors.toList());
    }

    public Map<String, Object> addDependency(UUID taskId, UUID dependsOnTaskId, String dependencyType) {
        Task t = taskRepo.findById(taskId).orElseThrow(() -> new RuntimeException("Task not found"));
        Task dep = taskRepo.findById(dependsOnTaskId).orElseThrow(() -> new RuntimeException("Dependency task not found"));
        if (t.getId().equals(dep.getId())) {
            throw new RuntimeException("Task không thể phụ thuộc vào chính nó");
        }
        TaskDependency d = new TaskDependency();
        d.setTask(t);
        d.setDependsOnTask(dep);
        d.setDependencyType(dependencyType != null ? dependencyType : "FINISH_TO_START");
        TaskDependency saved = dependencyRepo.save(d);

        Map<String, Object> m = new LinkedHashMap<>();
        m.put("id", saved.getId().toString());
        m.put("taskId", t.getId().toString());
        m.put("dependsOnTaskId", dep.getId().toString());
        m.put("dependencyType", saved.getDependencyType());
        return m;
    }

    public List<Map<String, Object>> getDependencies(UUID taskId) {
        return dependencyRepo.findByTaskId(taskId).stream()
                .map(d -> {
                    Task dep = d.getDependsOnTask();
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("id", d.getId().toString());
                    m.put("taskId", taskId.toString());

```
