# Knowledge Document: InterGroupOrderService.java (Chunk 2/18)

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
  "chunk_index": 1,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
map(this::toDTO).collect(Collectors.toList());
    }

    public List<InterGroupOrderDTO> getInboundOrders(UUID sellerTeamId) {
        return orderRepo.findBySellerTeamIdOrderByCreatedAtDesc(sellerTeamId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public InterGroupOrderDTO getById(UUID orderId) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));
        return toDTO(order);
    }

    @Transactional
    public InterGroupOrderDTO createOrder(InterGroupOrderDTO dto, User currentUser) {
        if (dto.getBuyerTeamId() == null || dto.getBuyerTeamId().isBlank()) {
            Team sellerTeam = teamRepo.findById(UUID.fromString(dto.getSellerTeamId()))
                    .orElseThrow(() -> new RuntimeException("Seller team not found"));

            InterGroupOrder order = new InterGroupOrder();
            order.setBuyerUser(currentUser);
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

            InterGroupOrder saved = orderRepo.save(order);

            // Notify seller team owner about new order
            String buyerName = currentUser.getFullName() != null && !currentUser.getFullName().isBlank()
                    ? currentUser.getFullName() : currentUser.getUsername();
            notifyUser(sellerTeam.getOwner(),
                    "Đơn hàng mới",
                    "Bạn có đơn hàng mới từ " + buyerName + ": " + order.getTitle(),
                    "ORDER_CREATED", null);

            // Notify buyer (confirmation)
            notifyUser(currentUser,
                    "Đã gửi đơn hàng",
                    "Đơn hàng \"" + order.getTitle() + "\" đã được gửi đến " + sellerTeam.getName() + ". Chờ phản hồi.",
                    "ORDER_CREATED", null);

            return toDTO(saved);
        }


```
