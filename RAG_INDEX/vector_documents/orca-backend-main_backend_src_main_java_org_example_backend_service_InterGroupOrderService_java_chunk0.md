# Knowledge Document: InterGroupOrderService.java (Chunk 1/18)

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
  "chunk_index": 0,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.InterGroupOrderDTO;
import org.example.backend.entity.Goal;
import org.example.backend.entity.InterGroupOrder;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.GoalRepository;
import org.example.backend.repository.InterGroupOrderRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.ReviewRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;
import org.springframework.transaction.annotation.Transactional;

@Service
public class InterGroupOrderService {

    private final InterGroupOrderRepository orderRepo;
    private final TeamRepository teamRepo;
    private final GoalRepository goalRepo;
    private final NotificationService notificationService;
    private final ReviewRepository reviewRepo;
    private final InventoryService inventoryService;

    public InterGroupOrderService(InterGroupOrderRepository orderRepo, TeamRepository teamRepo,
            GoalRepository goalRepo, NotificationService notificationService,
            ReviewRepository reviewRepo, InventoryService inventoryService) {
        this.orderRepo = orderRepo;
        this.teamRepo = teamRepo;
        this.goalRepo = goalRepo;
        this.notificationService = notificationService;
        this.reviewRepo = reviewRepo;
        this.inventoryService = inventoryService;
    }

    public List<InterGroupOrderDTO> getOutboundOrders(UUID buyerTeamId) {
        return orderRepo.findByBuyerTeamIdOrderByCreatedAtDesc(buyerTeamId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public List<InterGroupOrderDTO> getMyOutboundOrders(User currentUser) {
        return orderRepo.findByBuyerUserIdOrderByCreatedAtDesc(currentUser.getId())
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public List<InterGroupOrderDTO> getInboundOrders(UUID sellerTeamId) {
        return orderRepo.findBySellerTeamIdOrderByCreatedAtDesc(sellerTeamId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public InterGroupOrderDTO getById(UUID orderId) {
        InterGroupOrder order = orderRepo.findById(orderId)

```
