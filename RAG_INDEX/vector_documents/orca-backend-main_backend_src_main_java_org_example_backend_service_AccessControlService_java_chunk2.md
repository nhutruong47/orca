# Knowledge Document: AccessControlService.java (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, workspace, production, attendance, inventory, security

## Source Code Chunk
```java
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

    public void requireSelfOrTeamAdmin(User user, UUID targetUserId, UUID teamId) {
        UUID currentUserId = requireUserId(user);
        if (currentUserId.equals(targetUserId)) {
            requireTeamMember(currentUserId, teamId);
            return;
        }
        requireTeamAdmin(currentUserId, teamId);
    }

    public void validateTeamAccess(UUID userId, UUID teamId) {
        requireTeamMember(userId, teamId);
    }

    public void validateWorkspaceAccess(UUID userId, UUID workspaceId) {
        requireTeamMember(userId, workspaceId);
    }

    public void validateOrderAccess(UUID userId, UUID orderId) {
        requireProductionOrderAccess(userId, orderId);
    }

    public void requireProductionOrderAccess(User user, UUID orderId) {
        requireProductionOrderAccess(requireUserId(user), orderId);
    }

    public void requireProductionOrderAccess(UUID userId, UUID orderId) {
        ProductionOrder order = productionOrderRepository.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));
        requireTeamMember(userId, order.getTeam().getId());
    }

    public void requireProductionPlanAccess(User user, UUID planId) {
        var plan = productionPlanRepository.findById(planId)
                .orElseThrow(() -> new RuntimeException("Plan not found"));
        requireTeamMember(user, plan.getOrder().getTeam().getId());
    }

    public void requireDailyTargetAccess(User user, UUID targetId) {
        var target = dailyTargetRepository.findById(targetId)
                .orElseThrow(() -> new RuntimeException("Daily target not found"));
        requireTeamMember(user, target.getOrder().getTeam().getId());
    }

    public void requireInventoryItemAccess(User user, UUID itemId) {
        InventoryItem item = inventoryRepository.findById(itemId)
                .orElseThrow(() -> new RuntimeException("Item not found"));
        requireTeamMember(user, item.getTeam().getId());
    }


```
