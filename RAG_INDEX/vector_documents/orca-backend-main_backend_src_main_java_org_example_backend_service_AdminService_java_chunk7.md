# Knowledge Document: AdminService.java (Chunk 8/16)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AdminService.java",
  "language": "java",
  "module": "service",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "admin",
    "production",
    "factory",
    "payment",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 7,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
timeException("Role is required");
        }

        Role nextRole;
        try {
            nextRole = Role.valueOf(role.toUpperCase(Locale.ROOT));
        } catch (IllegalArgumentException ex) {
            throw new RuntimeException("Role is invalid");
        }

        User target = userRepository.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));

        if (target.getId().equals(currentUser.getId()) && nextRole != Role.ADMIN) {
            throw new RuntimeException("You cannot remove your own admin access");
        }

        long adminCount = userRepository.findAll().stream()
                .filter(user -> user.getRole() == Role.ADMIN)
                .count();
        if (target.getRole() == Role.ADMIN && nextRole != Role.ADMIN && adminCount <= 1) {
            throw new RuntimeException("At least one admin account is required");
        }

        target.setRole(nextRole);
        return toUserMap(userRepository.save(target));
    }

    @Transactional
    public Map<String, Object> updateUserLock(UUID userId, boolean locked, User currentUser) {
        User target = userRepository.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));

        if (target.getId().equals(currentUser.getId()) && locked) {
            throw new RuntimeException("You cannot lock your own account");
        }

        target.setLocked(locked);
        return toUserMap(userRepository.save(target));
    }

    @Transactional
    public Map<String, Object> createUser(Map<String, String> details) {
        if (userRepository.findByUsername(details.get("username")).isPresent()) {
            throw new RuntimeException("Username already exists");
        }
        User user = new User();
        user.setUsername(details.get("username"));
        user.setEmail(details.get("email"));
        user.setFullName(details.get("fullName"));
        String rawPassword = details.getOrDefault("password", "123456");
        user.setPassword(passwordEncoder.encode(rawPassword));
        user.setRole(Role.valueOf(safeText(details.get("role"), "USER").toUpperCase(Locale.ROOT)));
        user.setAiPlan("free");
        return toUserMap(userRepository.save(user));
    }

    @Transactional
    public Map<String, Object> updateUser(UUID userId, Map<String, String> details) {

```
