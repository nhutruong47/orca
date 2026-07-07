# Knowledge Document: AccessControlService.java (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, workspace, production, attendance, inventory, security

## Source Code Chunk
```java
    public AccessControlService(
            TeamMemberRepository teamMemberRepository,
            UserRepository userRepository,
            ProductionOrderRepository productionOrderRepository,
            InterGroupOrderRepository interGroupOrderRepository,
            InventoryRepository inventoryRepository,
            GoalRepository goalRepository,
            TaskRepository taskRepository,
            TaskChecklistRepository taskChecklistRepository,
            AttendanceRepository attendanceRepository,
            ProductionPlanRepository productionPlanRepository,
            DailyTargetRepository dailyTargetRepository) {
        this.teamMemberRepository = teamMemberRepository;
        this.userRepository = userRepository;
        this.productionOrderRepository = productionOrderRepository;
        this.interGroupOrderRepository = interGroupOrderRepository;
        this.inventoryRepository = inventoryRepository;
        this.goalRepository = goalRepository;
        this.taskRepository = taskRepository;
        this.taskChecklistRepository = taskChecklistRepository;
        this.attendanceRepository = attendanceRepository;
        this.productionPlanRepository = productionPlanRepository;
        this.dailyTargetRepository = dailyTargetRepository;
    }

    public void requireTeamMember(User user, UUID teamId) {
        requireTeamMember(requireUserId(user), teamId);
    }

    public void requireTeamMember(UUID userId, UUID teamId) {
        if (teamId == null || userId == null) {
            throw forbidden();
        }
        if (isSystemAdmin(userId)) {
            return;
        }
        if (!teamMemberRepository.existsByTeamIdAndUserId(teamId, userId)) {
            throw forbidden();
        }
    }

    public void requireTeamAdmin(User user, UUID teamId) {
        requireTeamAdmin(requireUserId(user), teamId);
    }

    public void requireTeamAdmin(UUID userId, UUID teamId) {
        if (teamId == null || userId == null) {
            throw forbidden();
        }
        if (isSystemAdmin(userId)) {
            return;
        }
        TeamMember membership = teamMemberRepository.findByTeamIdAndUserId(teamId, userId)
                .orElseThrow(this::forbidden);
        if (membership.getGroupRole() != GroupRole.ADMIN) {
            throw forbidden();
        }
    }


```
