# Knowledge Document: DefaultAdminInitializer.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/config/DefaultAdminInitializer.java",
  "language": "java",
  "module": "config",
  "business_domain": "factory",
  "tags": [
    "factory",
    "admin",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in config.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, security

## Source Code Chunk
```java
       .chipId(java.util.UUID.randomUUID().toString())
                .build();

        userRepository.save(admin);
    }

    private void promoteToAdmin(User user) {
        boolean changed = false;

        if (user.getRole() != Role.ADMIN) {
            user.setRole(Role.ADMIN);
            changed = true;
        }

        if (!passwordEncoder.matches(adminPassword, user.getPassword())) {
            user.setPassword(passwordEncoder.encode(adminPassword));
            changed = true;
        }

        if (changed) {
            userRepository.save(user);
        }
    }
}

```
