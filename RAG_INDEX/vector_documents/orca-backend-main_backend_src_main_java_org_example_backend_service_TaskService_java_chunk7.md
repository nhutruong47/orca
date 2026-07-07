# Knowledge Document: TaskService.java (Chunk 8/15)

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
  "chunk_index": 7,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
: totalWorkload;
            dto.setEstimatedSalary((billableRegular * avgRate) + (totalOvertimeHours * defaultOvertimeRate));
            report.add(dto);
        }
        return report;
    }

    public void delete(UUID id) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        UUID goalId = t.getGoal() != null ? t.getGoal().getId() : null;
        checklistRepo.deleteAll(checklistRepo.findByTaskIdOrderBySortOrderAsc(id));
        taskRepo.deleteById(id);
        if (goalId != null) {
            updateGoalProgress(goalId);
        }
    }

    // === Checklist ===
    public List<Map<String, Object>> getChecklist(UUID taskId) {
        return checklistRepo.findByTaskIdOrderBySortOrderAsc(taskId).stream()
                .map(c -> {
                    Map<String, Object> m = new HashMap<>();
                    m.put("id", c.getId().toString());
                    m.put("content", c.getContent());
                    m.put("checked", c.getChecked());
                    m.put("sortOrder", c.getSortOrder());
                    return m;
                }).collect(Collectors.toList());
    }

    public Map<String, Object> addChecklistItem(UUID taskId, String content) {
        Task t = taskRepo.findById(taskId).orElseThrow(() -> new RuntimeException("Task not found"));
        TaskChecklist c = new TaskChecklist();
        c.setTask(t);
        c.setContent(content);
        c.setChecked(false);
        int count = checklistRepo.findByTaskIdOrderBySortOrderAsc(taskId).size();
        c.setSortOrder(count);
        checklistRepo.save(c);
        Map<String, Object> m = new HashMap<>();
        m.put("id", c.getId().toString());
        m.put("content", c.getContent());
        m.put("checked", c.getChecked());
        return m;
    }

    public void toggleChecklistItem(UUID checklistId) {
        TaskChecklist c = checklistRepo.findById(checklistId)
                .orElseThrow(() -> new RuntimeException("Checklist item not found"));
        c.setChecked(!c.getChecked());
        checklistRepo.save(c);

        // Update task completion percentage
        UUID taskId = c.getTask().getId();
        List<TaskChecklist> items = checklistRepo.findByTaskIdOrderBySortOrderAsc(taskId);
        long checked = items.stream().filter(TaskChecklist::getChecked).count();

```
