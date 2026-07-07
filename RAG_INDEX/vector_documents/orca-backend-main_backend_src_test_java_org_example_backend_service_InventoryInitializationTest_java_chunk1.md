# Knowledge Document: InventoryInitializationTest.java (Chunk 2/2)

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
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory

## Source Code Chunk
```java
ent() {
        Team team = new Team();
        team.setName("Idempotency Team");
        team.setOwner(testUser);
        team = teamRepository.save(team);

        // Initialize first time
        inventoryService.initializeDefaultInventory(team.getId());
        long countFirst = inventoryRepository.findByTeamIdOrderByLastUpdatedDesc(team.getId()).size();
        assertEquals(16, countFirst);

        // Initialize second time
        inventoryService.initializeDefaultInventory(team.getId());
        long countSecond = inventoryRepository.findByTeamIdOrderByLastUpdatedDesc(team.getId()).size();

        assertEquals(countFirst, countSecond, "Inventory count should not change on second initialization");
    }

    @Test
    void testBackfillRunnerCorrectlyInitializesEmptyTeams() throws Exception {
        // Create an "old" team with NO inventory items
        Team oldTeam = new Team();
        oldTeam.setName("Old Legacy Team");
        oldTeam.setOwner(testUser);
        oldTeam = teamRepository.save(oldTeam);

        assertFalse(inventoryRepository.existsByTeamId(oldTeam.getId()), "Old team should have no inventory initially");

        // Execute runner
        InventoryBackfillRunner runner = new InventoryBackfillRunner(teamRepository, inventoryService);
        runner.run();

        assertTrue(inventoryRepository.existsByTeamId(oldTeam.getId()), "Runner should have initialized inventory for the old team");
        assertEquals(16, inventoryRepository.findByTeamIdOrderByLastUpdatedDesc(oldTeam.getId()).size());
    }
}

```
