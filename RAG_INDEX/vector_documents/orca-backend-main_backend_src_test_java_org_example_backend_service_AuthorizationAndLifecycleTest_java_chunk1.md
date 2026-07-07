# Knowledge Document: AuthorizationAndLifecycleTest.java (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, authorization

## Source Code Chunk
```java
ner) {
        Team t = new Team();
        t.setName("Team of " + owner.getUsername());
        t.setOwner(owner);
        Team saved = teamRepo.save(t);

        TeamMember tm = new TeamMember();
        tm.setTeam(saved);
        tm.setUser(owner);
        tm.setGroupRole(GroupRole.ADMIN);
        teamMemberRepo.save(tm);
        return saved;
    }

    // ===== Authorization =====

    @Test
    void requireTeamMember_shouldThrow_forStranger() {
        assertThrows(ResponseStatusException.class,
                () -> accessControlService.requireTeamMember(stranger, sellerTeam.getId()));
    }

    @Test
    void requireTeamMember_shouldPass_forMember() {
        assertDoesNotThrow(() -> accessControlService.requireTeamMember(seller, sellerTeam.getId()));
    }

    @Test
    void requireInterGroupOrderAccess_shouldThrow_forStranger() {
        InterGroupOrder order = new InterGroupOrder();
        order.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle("Test");
        order.setQuantity(10);
        order.setStatus("RFQ_CREATED");
        InterGroupOrder saved = orderRepo.save(order);

        assertThrows(ResponseStatusException.class,
                () -> accessControlService.requireInterGroupOrderAccess(stranger, saved));
    }

    @Test
    void requireInterGroupOrderAccess_shouldPass_forBuyerAndSeller() {
        InterGroupOrder order = new InterGroupOrder();
        order.setBuyerTeam(buyerTeam);
        order.setSellerTeam(sellerTeam);
        order.setTitle("Test");
        order.setQuantity(10);
        order.setStatus("RFQ_CREATED");
        InterGroupOrder saved = orderRepo.save(order);

        assertDoesNotThrow(() -> accessControlService.requireInterGroupOrderAccess(seller, saved));
        assertDoesNotThrow(() -> accessControlService.requireInterGroupOrderAccess(buyer, saved));
    }

    // ===== Inter-Group Lifecycle =====

    @Test
    void interGroupLifecycle_createAcceptDeliverConfirm() {
        // 1. Buyer creates RFQ
        InterGroupOrderDTO dto = new InterGroupOrderDTO();
        dto.setSellerTeamId(sellerTeam.getId().toString());
        dto.setBuyerTeamId(buyerTeam.getId().toString());
        dto.setTitle("Lifecycle Test Order");
        dto.setDescription("desc");
        dto.setQuantity(50);
        dto.setStatus("RFQ_CREATED");


```
