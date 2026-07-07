# Knowledge Document: TaskService.java (Chunk 9/15)

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
  "chunk_index": 8,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
orElseThrow(() -> new RuntimeException("Checklist item not found"));
        c.setChecked(!c.getChecked());
        checklistRepo.save(c);

        // Update task completion percentage
        UUID taskId = c.getTask().getId();
        List<TaskChecklist> items = checklistRepo.findByTaskIdOrderBySortOrderAsc(taskId);
        long checked = items.stream().filter(TaskChecklist::getChecked).count();
        int pct = items.isEmpty() ? 0 : (int) (checked * 100 / items.size());

        Task t = taskRepo.findById(taskId).orElseThrow();
        t.setCompletionPercentage(pct);
        if (pct == 100)
            t.setStatus("COMPLETED");
        taskRepo.save(t);

        if (t.getGoal() != null) {
            updateGoalProgress(t.getGoal().getId());
        }
    }

    // === KPI ===
    public Map<String, Object> getMemberKpi(UUID memberId) {
        List<Task> tasks = taskRepo.findByMemberId(memberId);
        long total = tasks.size();
        long completed = tasks.stream().filter(t -> "COMPLETED".equals(t.getStatus())).count();
        long overdue = tasks.stream()
                .filter(t -> t.getDeadline() != null && t.getDeadline().isBefore(java.time.LocalDateTime.now())
                        && !"COMPLETED".equals(t.getStatus()))
                .count();
        double avgCompletion = tasks.stream()
                .mapToInt(t -> t.getCompletionPercentage() != null ? t.getCompletionPercentage() : 0).average()
                .orElse(0);

        Map<String, Object> kpi = new HashMap<>();
        kpi.put("totalTasks", total);
        kpi.put("completedTasks", completed);
        kpi.put("overdueTasks", overdue);
        kpi.put("completionRate", total > 0 ? (completed * 100 / total) : 0);
        kpi.put("avgCompletionPercentage", Math.round(avgCompletion));
        return kpi;
    }

    private void updateGoalProgress(UUID goalId) {
        List<Task> tasks = taskRepo.findByGoalId(goalId);
        long completed = tasks.stream().filter(t -> "COMPLETED".equals(t.getStatus())).count();
        long inProgress = tasks.stream().filter(t -> "IN_PROGRESS".equals(t.getStatus())).count();

        goalRepo.findById(goalId).ifPresent(g -> {
            g.setTotalTasks(tasks.size());
            g.setCompletedTasks((int) completed);
            if (completed == tasks.size() && !tasks.isEmpty()) {
                g.setStatus("DONE");

```
