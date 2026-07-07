# Knowledge Document: AuthorizationAndLifecycleTest.java (Chunk 3/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/AuthorizationAndLifecycleTest.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "admin",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, authorization

## Source Code Chunk
```java
Lifecycle_createAcceptDeliverConfirm() {
        // 1. Buyer creates RFQ
        InterGroupOrderDTO dto = new InterGroupOrderDTO();
        dto.setSellerTeamId(sellerTeam.getId().toString());
        dto.setBuyerTeamId(buyerTeam.getId().toString());
        dto.setTitle("Lifecycle Test Order");
        dto.setDescription("desc");
        dto.setQuantity(50);
        dto.setStatus("RFQ_CREATED");

        InterGroupOrderDTO created = interGroupOrderService.createOrder(dto, buyer);
        assertEquals("RFQ_CREATED", created.getStatus());

        // 2. Seller accepts -> CONFIRMED
        InterGroupOrderDTO accepted = interGroupOrderService.acceptOrder(
                UUID.fromString(created.getId()), seller);
        assertEquals("CONFIRMED", accepted.getStatus());
        assertNotNull(accepted.getLinkedGoalId());

        // 3. Seller delivers -> DELIVERED
        InterGroupOrderDTO delivered = interGroupOrderService.deliverOrder(
                UUID.fromString(created.getId()), "Giao tai kho", seller);
        assertEquals("DELIVERED", delivered.getStatus());
        assertFalse(Boolean.TRUE.equals(delivered.getDeliveryConfirmed()));

        // 4. Buyer confirms -> COMPLETED
        InterGroupOrderDTO confirmed = interGroupOrderService.confirmDelivery(
                UUID.fromString(created.getId()), "ON_TIME", 5, "OK", buyer);
        assertEquals("COMPLETED", confirmed.getStatus());
        assertTrue(Boolean.TRUE.equals(confirmed.getDeliveryConfirmed()));
        assertEquals("ON_TIME", confirmed.getDeliveryStatus());

        // A review should have been saved
        long reviewCount = reviewRepo.findAll().stream()
                .filter(r -> r.getOrder() != null && r.getOrder().getId().equals(UUID.fromString(created.getId())))
                .count();
        assertTrue(reviewCount >= 1, "Review should have been recorded");
    }

    @Test
    void deliverOrder_byBuyer_shouldThrow() {
        InterGroupOrder order = new InterGroupOrder();
        order.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle("Auth Test");
        order.setQuantity(10);
        order.setStatus("CONFIRMED");
        InterGroupOrder saved = orderRepo.save(order);

        // Buyer is not the seller
        assertThrows(RuntimeException.class,
                () -> interGroupOrderService.deliverOrder(saved.getId(), null, buyer));

```
