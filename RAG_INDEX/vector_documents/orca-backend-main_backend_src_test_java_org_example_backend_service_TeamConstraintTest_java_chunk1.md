# Knowledge Document: TeamConstraintTest.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/TeamConstraintTest.java",
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
yId(goal.getId()).isPresent());
        assertTrue(taskRepo.findById(task.getId()).isPresent());
        assertFalse(teamMemberRepo.findByTeamId(team.getId()).isEmpty());

        // Clear persistence context so managed entities don't cause TransientObjectException on flush
        entityManager.clear();

        // Delete team
        teamRepo.deleteById(team.getId());
        teamRepo.flush();

        // Assert cascade deletion
        assertFalse(teamRepo.findById(team.getId()).isPresent());
        
        // Goals and Tasks should be deleted by DB cascade if configured correctly,
        // or by JPA. We just check if they still exist.
        // NOTE: In testing with H2, OnDelete CASCADE works.
        assertFalse(goalRepo.findById(goal.getId()).isPresent(), "Goal should be cascaded");
        assertFalse(taskRepo.findById(task.getId()).isPresent(), "Task should be cascaded");
        assertTrue(teamMemberRepo.findByTeamId(team.getId()).isEmpty(), "Team members should be cascaded");
    }
}

```
