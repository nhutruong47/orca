# Knowledge Document: AiWorkflowService.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AiWorkflowService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication"
  ],
  "logical_type": "Service",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication

## Source Code Chunk
```java
throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Text is required");
        }
    }

    private UUID requireTeamId(String teamId) {
        if (teamId == null || teamId.isBlank()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "teamId is required");
        }
        return parseTeamId(teamId);
    }

    private UUID parseTeamId(String teamId) {
        try {
            return UUID.fromString(teamId);
        } catch (IllegalArgumentException e) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Invalid teamId", e);
        }
    }

    private void validateTeamAccess(UUID teamId, User currentUser) {
        if (currentUser == null) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Authentication is required");
        }
        if (!teamRepository.existsById(teamId)) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Team not found");
        }
        if (!teamMemberRepository.existsByTeamIdAndUserId(teamId, currentUser.getId())) {
            throw new ResponseStatusException(HttpStatus.FORBIDDEN, "You are not a member of this team");
        }
    }
}

```
