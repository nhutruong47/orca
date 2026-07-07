# Knowledge Document: AdminService.java (Chunk 14/16)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AdminService.java",
  "language": "java",
  "module": "service",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "admin",
    "production",
    "factory",
    "payment",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 13,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
     String buyerUserName = order.getBuyerUser() != null
                ? safeText(order.getBuyerUser().getFullName(), order.getBuyerUser().getUsername())
                : "";
        map.put("buyerTeamName", order.getBuyerTeam() != null ? order.getBuyerTeam().getName() : buyerUserName);
        map.put("buyerUserId", order.getBuyerUser() != null ? order.getBuyerUser().getId().toString() : "");
        map.put("buyerUserName", buyerUserName);
        map.put("sellerTeamId", order.getSellerTeam() != null ? order.getSellerTeam().getId().toString() : "");
        map.put("sellerTeamName", order.getSellerTeam() != null ? order.getSellerTeam().getName() : "");
        map.put("quantity", order.getQuantity());
        map.put("deadline", order.getDeadline() != null ? order.getDeadline().toString() : null);
        map.put("status", order.getStatus());
        map.put("linkedGoalId", order.getLinkedGoalId() != null ? order.getLinkedGoalId().toString() : null);
        map.put("createdAt", order.getCreatedAt() != null ? order.getCreatedAt().toString() : null);
        map.put("cancelledBy", safeText(order.getCancelledBy(), ""));
        return map;
    }

    private Map<String, Object> toTaskMap(Task task) {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", task.getId().toString());
        map.put("title", task.getTitle());
        map.put("description", safeText(task.getDescription(), ""));
        map.put("goalId", task.getGoal() != null ? task.getGoal().getId().toString() : "");
        map.put("goalTitle", task.getGoal() != null ? task.getGoal().getTitle() : "");
        map.put("teamId", task.getGoal() != null && task.getGoal().getTeam() != null
                ? task.getGoal().getTeam().getId().toString()
                : "");
        map.put("teamName", task.getGoal() != null && task.getGoal().getTeam() != null
                ? task.getGoal().getTeam().getName()
                : "");
        map.put("memberId", task.getMember() != null ? task.getMember().getId().toString() : "");
        map.put("memberName", task.getMember() != null ? task.getMember().getUsername() : "");
        map.put("priority", task.getPriority());
        map.put("status", task.getStatus());
        map.put("acceptanceStatus", task.getAcceptanceStatus());

```
