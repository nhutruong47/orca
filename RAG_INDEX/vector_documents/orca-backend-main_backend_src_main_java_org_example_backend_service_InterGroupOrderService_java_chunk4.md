# Knowledge Document: InterGroupOrderService.java (Chunk 5/18)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/InterGroupOrderService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "production",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 4,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
.setCompletedTasks(0);

        Goal savedGoal = goalRepo.save(autoGoal);

        // 3. Link the goal to the order
        order.setLinkedGoalId(savedGoal.getId());

        InterGroupOrder saved = orderRepo.save(order);

        // Notify buyer that order was accepted
        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify,
                    "Đơn hàng được chấp nhận",
                    "Đơn hàng \"" + order.getTitle() + "\" đã được " + sellerTeam.getName() + " chấp nhận và bắt đầu gia công.",
                    "ORDER_ACCEPTED", null);
        }

        return toDTO(saved);
    }

    public InterGroupOrderDTO rejectOrder(UUID orderId, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        Team sellerTeam = order.getSellerTeam();
        if (!sellerTeam.getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Only the receiving team owner can reject orders.");
        }

        if (!"RFQ_CREATED".equals(order.getStatus()) && !"QUOTED".equals(order.getStatus()) && !"PENDING".equals(order.getStatus())) {
            throw new RuntimeException("Order is not in PENDING state.");
        }

        order.setStatus("REJECTED");
        order.setBuyerViewed(false);
        InterGroupOrder saved = orderRepo.save(order);

        // Notify buyer that order was rejected
        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify,
                    "Đơn hàng bị từ chối",
                    "Đơn hàng \"" + order.getTitle() + "\" đã bị " + sellerTeam.getName() + " từ chối.",
                    "ORDER_REJECTED", null);
        }

        return toDTO(saved);
    }

    private InterGroupOrderDTO toDTO(InterGroupOrder order) {
        InterGroupOrderDTO dto = new InterGroupOrderDTO();
        dto.setId(order.getId().toString());
        dto.setBuyerTeamId(order.getBuyerTeam() != null ? order.getBuyerTeam().getId().toString() : null);
        dto.setBuyerTeamName(order.getBuyerTeam() != null ? order.getBuyerTeam().getName() : null);
        dto.setBuyerUserId(order.getBuyerUser() != null ? order.getBuyerUser().getId().toString() : null);

```
