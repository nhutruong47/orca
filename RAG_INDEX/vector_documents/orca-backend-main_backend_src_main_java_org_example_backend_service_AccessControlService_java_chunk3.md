# Knowledge Document: AccessControlService.java (Chunk 4/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AccessControlService.java",
  "language": "java",
  "module": "service",
  "business_domain": "admin",
  "tags": [
    "admin",
    "workspace",
    "production",
    "attendance",
    "inventory",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, workspace, production, attendance, inventory, security

## Source Code Chunk
```java
ew RuntimeException("Daily target not found"));
        requireTeamMember(user, target.getOrder().getTeam().getId());
    }

    public void requireInventoryItemAccess(User user, UUID itemId) {
        InventoryItem item = inventoryRepository.findById(itemId)
                .orElseThrow(() -> new RuntimeException("Item not found"));
        requireTeamMember(user, item.getTeam().getId());
    }

    public void requireGoalAccess(User user, UUID goalId) {
        var goal = goalRepository.findById(goalId)
                .orElseThrow(() -> new RuntimeException("Goal not found"));
        requireTeamMember(user, goal.getTeam().getId());
    }

    public void requireTaskAccess(User user, UUID taskId) {
        Task task = taskRepository.findById(taskId)
                .orElseThrow(() -> new RuntimeException("Task not found"));
        if (task.getGoal() == null || task.getGoal().getTeam() == null) {
            throw forbidden();
        }
        requireTeamMember(user, task.getGoal().getTeam().getId());
    }

    public void requireChecklistAccess(User user, UUID checklistId) {
        Task task = taskChecklistRepository.findById(checklistId)
                .map(checklist -> checklist.getTask())
                .orElseThrow(() -> new RuntimeException("Checklist item not found"));
        if (task.getGoal() == null || task.getGoal().getTeam() == null) {
            throw forbidden();
        }
        requireTeamMember(user, task.getGoal().getTeam().getId());
    }

    public void requireInterGroupOrderAccess(User user, UUID orderId) {
        InterGroupOrder order = interGroupOrderRepository.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));
        requireInterGroupOrderAccess(user, order);
    }

    public void requireAttendanceAccess(User user, UUID attendanceId) {
        var attendance = attendanceRepository.findById(attendanceId)
                .orElseThrow(() -> new RuntimeException("Attendance record not found"));
        requireSelfOrTeamAdmin(user, attendance.getUser().getId(), attendance.getTeam().getId());
    }

    public void requireInterGroupOrderAccess(User user, InterGroupOrder order) {
        UUID userId = requireUserId(user);
        if (isSystemAdmin(userId)) {
            return;
        }

```
