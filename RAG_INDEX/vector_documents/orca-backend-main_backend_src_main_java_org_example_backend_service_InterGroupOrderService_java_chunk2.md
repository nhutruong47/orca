# Knowledge Document: InterGroupOrderService.java (Chunk 3/18)

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
  "chunk_index": 2,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
+ ": " + order.getTitle(),
                    "ORDER_CREATED", null);

            // Notify buyer (confirmation)
            notifyUser(currentUser,
                    "Đã gửi đơn hàng",
                    "Đơn hàng \"" + order.getTitle() + "\" đã được gửi đến " + sellerTeam.getName() + ". Chờ phản hồi.",
                    "ORDER_CREATED", null);

            return toDTO(saved);
        }

        Team buyerTeam = teamRepo.findById(UUID.fromString(dto.getBuyerTeamId()))
                .orElseThrow(() -> new RuntimeException("Buyer team not found"));

        Team sellerTeam = teamRepo.findById(UUID.fromString(dto.getSellerTeamId()))
                .orElseThrow(() -> new RuntimeException("Seller team not found"));

        if (!buyerTeam.getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Only the team owner can place inter-group orders.");
        }

        // Trust check: block if trust score < 30% and has >= 3 orders
        if (buyerTeam.getTotalOrders() >= 3) {
            int trustScore = (int) ((double) buyerTeam.getCompletedOrders() / buyerTeam.getTotalOrders() * 100);
            if (trustScore < 30) {
                throw new RuntimeException("Uy tín quá thấp (" + trustScore + "%). Không thể đặt hàng.");
            }
        }

        InterGroupOrder order = new InterGroupOrder();
        order.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle(dto.getTitle());
        order.setDescription(dto.getDescription());
        order.setQuantity(dto.getQuantity());
        order.setDeadline(dto.getDeadline());
        order.setStatus("RFQ_CREATED");
        order.setMaterialSource(dto.getMaterialSource());
        order.setServices(dto.getServices());
        order.setProductType(dto.getProductType());
        order.setUnit(dto.getUnit());
        mapDeliveryFields(order, dto);

        // Increment buyer total orders
        buyerTeam.setTotalOrders(buyerTeam.getTotalOrders() + 1);
        teamRepo.save(buyerTeam);

        InterGroupOrder saved = orderRepo.save(order);

        // Notify seller team owner about new order
        notifyUser(sellerTeam.getOwner(),
                "Đơn hàng mới",
                "Bạn có đơn hàng mới từ " + buyerTeam.getName() + ": " + order.getTitle(),
                "ORDER_CREATED", null);

        // Notify buyer (confirmation)

```
