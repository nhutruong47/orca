# Knowledge Document: TeamServiceJoinTest.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/TeamServiceJoinTest.java",
  "language": "java",
  "module": "service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
).thenReturn(Optional.of(team));
        when(userRepository.findByUsername("worker")).thenReturn(Optional.of(user));
        when(teamMemberRepository.findByTeamIdAndUserId(team.getId(), user.getId())).thenReturn(Optional.empty());
        when(teamMemberRepository.findByTeamId(team.getId())).thenReturn(List.of());

        ReflectionTestUtils.setField(service, "teamRepository", teamRepository);
        ReflectionTestUtils.setField(service, "teamMemberRepository", teamMemberRepository);
        ReflectionTestUtils.setField(service, "userRepository", userRepository);

        TeamDTO joined = service.joinByCode("abc123", "worker");

        assertEquals(team.getId(), joined.getId());
        assertEquals("Roastery", joined.getName());
        verify(teamMemberRepository).save(any(TeamMember.class));
    }
}

```
