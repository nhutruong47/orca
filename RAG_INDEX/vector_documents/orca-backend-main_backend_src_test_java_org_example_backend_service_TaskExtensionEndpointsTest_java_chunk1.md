# Knowledge Document: TaskExtensionEndpointsTest.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/TaskExtensionEndpointsTest.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
fix + UUID.randomUUID());
        u.setPassword("pass");
        u.setEmail(prefix + UUID.randomUUID() + "@example.com");
        return userRepo.save(u);
    }

    private void addMember(Team team, User user) {
        TeamMember tm = new TeamMember();
        tm.setTeam(team);
        tm.setUser(user);
        tm.setGroupRole(GroupRole.MEMBER);
        teamMemberRepo.save(tm);
    }

    @Test
    void setSupervisor_persists() {
        var dto = taskService.setSupervisor(task.getId(), supervisor.getId());
        assertEquals(supervisor.getId().toString(), dto.getSupervisorId());

        Task reloaded = taskRepo.findById(task.getId()).orElseThrow();
        assertNotNull(reloaded.getSupervisor());
        assertEquals(supervisor.getId(), reloaded.getSupervisor().getId());
    }

    @Test
    void transfer_rotatesOwnership_andPersistsHistory() {
        var dto = taskService.transferTask(task.getId(), assignee.getId(), "reassign", "MANAGER", owner);
        assertEquals(assignee.getId().toString(), dto.getMemberId());

        var transfers = taskService.getTransfers(task.getId());
        assertEquals(1, transfers.size());
        Map<?, ?> row = transfers.get(0);
        assertEquals("MANAGER", row.get("actorType"));
        assertEquals("reassign", row.get("reason"));
    }

    @Test
    void addDependency_createsLink() {
        Task dep = new Task();
        dep.setTitle("Dep " + UUID.randomUUID());
        dep.setGoal(task.getGoal());
        dep = taskRepo.save(dep);

        var link = taskService.addDependency(task.getId(), dep.getId(), "FINISH_TO_START");
        assertNotNull(link.get("id"));
        assertEquals("FINISH_TO_START", link.get("dependencyType"));

        var deps = taskService.getDependencies(task.getId());
        assertEquals(1, deps.size());
    }
}
```
