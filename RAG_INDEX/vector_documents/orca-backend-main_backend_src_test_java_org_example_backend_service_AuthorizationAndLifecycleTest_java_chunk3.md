# Knowledge Document: AuthorizationAndLifecycleTest.java (Chunk 4/4)

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
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, authorization

## Source Code Chunk
```java
der.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle("Auth Test");
        order.setQuantity(10);
        order.setStatus("CONFIRMED");
        InterGroupOrder saved = orderRepo.save(order);

        // Buyer is not the seller
        assertThrows(RuntimeException.class,
                () -> interGroupOrderService.deliverOrder(saved.getId(), null, buyer));
    }

    @Test
    void confirmDelivery_bySeller_shouldThrow() {
        InterGroupOrder order = new InterGroupOrder();
        order.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle("Auth Test 2");
        order.setQuantity(10);
        order.setStatus("DELIVERED");
        InterGroupOrder saved = orderRepo.save(order);

        assertThrows(RuntimeException.class,
                () -> interGroupOrderService.confirmDelivery(saved.getId(), "ON_TIME", 5, "ok", seller));
    }

    @Test
    void deliverOrder_invalidStatus_shouldThrow() {
        InterGroupOrder order = new InterGroupOrder();
        order.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle("Status Test");
        order.setQuantity(10);
        order.setStatus("REJECTED");
        InterGroupOrder saved = orderRepo.save(order);

        assertThrows(RuntimeException.class,
                () -> interGroupOrderService.deliverOrder(saved.getId(), null, seller));
    }

    @Test
    void confirmDelivery_invalidStatus_shouldThrow() {
        InterGroupOrder order = new InterGroupOrder();
        order.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle("Status Test 2");
        order.setQuantity(10);
        order.setStatus("CONFIRMED");
        InterGroupOrder saved = orderRepo.save(order);

        assertThrows(RuntimeException.class,
                () -> interGroupOrderService.confirmDelivery(saved.getId(), "ON_TIME", 5, "ok", buyer));
    }
}
```
