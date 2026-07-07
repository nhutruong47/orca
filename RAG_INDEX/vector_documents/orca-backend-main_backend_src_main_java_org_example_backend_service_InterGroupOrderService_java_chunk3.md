# Knowledge Document: InterGroupOrderService.java (Chunk 4/18)

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
  "chunk_index": 3,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
ers() + 1);
        teamRepo.save(buyerTeam);

        InterGroupOrder saved = orderRepo.save(order);

        // Notify seller team owner about new order
        notifyUser(sellerTeam.getOwner(),
                "Đơn hàng mới",
                "Bạn có đơn hàng mới từ " + buyerTeam.getName() + ": " + order.getTitle(),
                "ORDER_CREATED", null);

        // Notify buyer (confirmation)
        notifyUser(currentUser,
                "Đã gửi đơn hàng",
                "Đơn hàng \"" + order.getTitle() + "\" đã được gửi đến " + sellerTeam.getName() + ". Chờ phản hồi.",
                "ORDER_CREATED", null);

        return toDTO(saved);
    }

    public InterGroupOrderDTO acceptOrder(UUID orderId, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        Team sellerTeam = order.getSellerTeam();
        if (!sellerTeam.getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Only the receiving team owner can accept orders.");
        }

        if (!"RFQ_CREATED".equals(order.getStatus()) && !"QUOTED".equals(order.getStatus()) && !"PENDING".equals(order.getStatus())) {
            throw new RuntimeException("Đơn hàng không ở trạng thái có thể xác nhận.");
        }

        // 1. Change Order Status
        order.setStatus("CONFIRMED");
        order.setBuyerViewed(false);

        // 2. Automatically generate a Goal in the seller's Team
        Goal autoGoal = new Goal();
        autoGoal.setTeam(sellerTeam);
        autoGoal.setOwner(currentUser);
        autoGoal.setTitle("[Đơn Hàng] " + order.getTitle());
        autoGoal.setOutputTarget("SL: " + order.getQuantity() + " | " + order.getDescription());
        autoGoal.setPriority(2); // Normal priority
        autoGoal.setDeadline(order.getDeadline());
        autoGoal.setStatus("PUBLISHED");
        autoGoal.setTotalTasks(0);
        autoGoal.setCompletedTasks(0);

        Goal savedGoal = goalRepo.save(autoGoal);

        // 3. Link the goal to the order
        order.setLinkedGoalId(savedGoal.getId());

        InterGroupOrder saved = orderRepo.save(order);

        // Notify buyer that order was accepted
        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify,

```
