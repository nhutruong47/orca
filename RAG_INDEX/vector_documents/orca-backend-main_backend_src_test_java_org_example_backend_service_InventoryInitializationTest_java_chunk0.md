# Knowledge Document: InventoryInitializationTest.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/InventoryInitializationTest.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.config.InventoryBackfillRunner;
import org.example.backend.dto.TeamDTO;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.InventoryRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.UUID;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@Transactional
public class InventoryInitializationTest {

    @Autowired private TeamService teamService;
    @Autowired private InventoryService inventoryService;
    @Autowired private TeamRepository teamRepository;
    @Autowired private UserRepository userRepository;
    @Autowired private InventoryRepository inventoryRepository;

    private User testUser;

    @BeforeEach
    void setUp() {
        testUser = new User();
        testUser.setUsername("testowner_" + UUID.randomUUID());
        testUser.setPassword("pass");
        testUser = userRepository.save(testUser);
    }

    @Test
    void testNewTeamGetsDefaultInventory() {
        TeamDTO dto = new TeamDTO();
        dto.setName("New Factory");
        dto.setDescription("Testing inventory creation");

        TeamDTO created = teamService.createTeam(dto, testUser.getUsername());
        UUID teamId = created.getId();

        assertTrue(inventoryRepository.existsByTeamId(teamId), "Inventory should be initialized upon team creation");
        assertEquals(16, inventoryRepository.findByTeamIdOrderByLastUpdatedDesc(teamId).size(), "Should have 16 default inventory items (4 types x 4 states)");
    }

    @Test
    void testInitializationIsIdempotent() {
        Team team = new Team();
        team.setName("Idempotency Team");
        team.setOwner(testUser);
        team = teamRepository.save(team);

        // Initialize first time
        inventoryService.initializeDefaultInventory(team.getId());
        long countFirst = inventoryRepository.findByTeamIdOrderByLastUpdatedDesc(team.getId()).size();
        assertEquals(16, countFirst);


```
