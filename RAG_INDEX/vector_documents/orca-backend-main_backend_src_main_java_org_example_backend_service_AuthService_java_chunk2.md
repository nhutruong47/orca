# Knowledge Document: AuthService.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AuthService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
    private AuthResponse buildResponse(String token, User user) {
        AuthResponse r = new AuthResponse();
        r.setToken(token);
        r.setId(user.getId() != null ? user.getId().toString() : null);
        r.setUsername(user.getUsername());
        r.setFullName(user.getFullName());
        r.setEmail(user.getEmail());
        r.setRole(user.getRole().name());
        return r;
    }

    private String generateUniqueChipId() {
        String chipId;
        do {
            chipId = "USR-" + UUID.randomUUID();
        } while (userRepository.findByChipId(chipId).isPresent());
        return chipId;
    }
}

```
