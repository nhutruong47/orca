# Knowledge Document: GoalService.java (Chunk 10/10)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/GoalService.java",
  "language": "java",
  "module": "service",
  "business_domain": "employee",
  "tags": [
    "employee",
    "admin",
    "production",
    "chat"
  ],
  "logical_type": "Service",
  "chunk_index": 9,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
alue instanceof String text && !text.trim().isEmpty()) {
                return text.trim();
            }
        }
        return null;
    }

    private Optional<User> findTeamUser(List<TeamMember> members, String name) {
        String normalized = name.trim().toLowerCase(Locale.ROOT);
        return members.stream()
                .map(TeamMember::getUser)
                .filter(user -> {
                    String username = user.getUsername() != null ? user.getUsername().toLowerCase(Locale.ROOT) : "";
                    String fullName = user.getFullName() != null ? user.getFullName().toLowerCase(Locale.ROOT) : "";
                    return username.equals(normalized)
                            || fullName.equals(normalized)
                            || username.contains(normalized)
                            || fullName.contains(normalized);
                })
                .findFirst();
    }
}

```
