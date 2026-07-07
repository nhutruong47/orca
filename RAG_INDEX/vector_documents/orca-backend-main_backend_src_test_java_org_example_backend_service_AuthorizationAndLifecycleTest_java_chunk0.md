# Knowledge Document: AuthorizationAndLifecycleTest.java (Chunk 1/4)

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
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, authorization

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.InterGroupOrderDTO;
import org.example.backend.entity.*;
import org.example.backend.repository.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.transaction.annotation.Transactional;

import java.util.UUID;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Verifies the new contract:
 *  - Users outside a team receive 403 / AccessDeniedException when touching team-scoped data.
 *  - Inter-group order lifecycle: RFQ_CREATED -> CONFIRMED -> SHIPPING -> DELIVERED -> COMPLETED.
 */
@SpringBootTest
@Transactional
public class AuthorizationAndLifecycleTest {

    @Autowired private AccessControlService accessControlService;
    @Autowired private InterGroupOrderService interGroupOrderService;
    @Autowired private InterGroupOrderRepository orderRepo;
    @Autowired private TeamRepository teamRepo;
    @Autowired private UserRepository userRepo;
    @Autowired private TeamMemberRepository teamMemberRepo;
    @Autowired private ReviewRepository reviewRepo;

    private User seller;
    private User buyer;
    private User stranger;
    private Team sellerTeam;
    private Team buyerTeam;

    @BeforeEach
    void setUp() {
        seller = persistUser("seller_");
        buyer = persistUser("buyer_");
        stranger = persistUser("stranger_");

        sellerTeam = createTeamWithOwner(seller);
        buyerTeam = createTeamWithOwner(buyer);
    }

    private User persistUser(String prefix) {
        User u = new User();
        u.setUsername(prefix + UUID.randomUUID());
        u.setPassword("pass");
        u.setEmail(prefix + UUID.randomUUID() + "@example.com");
        return userRepo.save(u);
    }

    private Team createTeamWithOwner(User owner) {
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

```
