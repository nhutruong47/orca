# Knowledge Document: AdminService.java (Chunk 9/16)

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
  "chunk_index": 8,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
ils.getOrDefault("password", "123456");
        user.setPassword(passwordEncoder.encode(rawPassword));
        user.setRole(Role.valueOf(safeText(details.get("role"), "USER").toUpperCase(Locale.ROOT)));
        user.setAiPlan("free");
        return toUserMap(userRepository.save(user));
    }

    @Transactional
    public Map<String, Object> updateUser(UUID userId, Map<String, String> details) {
        User user = userRepository.findById(userId).orElseThrow(() -> new RuntimeException("User not found"));
        if (details.containsKey("fullName")) user.setFullName(details.get("fullName"));
        if (details.containsKey("email")) user.setEmail(details.get("email"));
        if (details.containsKey("role")) {
            user.setRole(Role.valueOf(details.get("role").toUpperCase(Locale.ROOT)));
        }
        return toUserMap(userRepository.save(user));
    }

    @Transactional
    public String resetUserPassword(UUID userId) {
        User user = userRepository.findById(userId).orElseThrow(() -> new RuntimeException("User not found"));
        String newPassword = UUID.randomUUID().toString().substring(0, 8);
        user.setPassword(passwordEncoder.encode(newPassword));
        userRepository.save(user);
        return newPassword;
    }

    @Transactional
    public Map<String, Object> updateTeam(UUID teamId, Map<String, String> details) {
        Team team = teamRepository.findById(teamId).orElseThrow(() -> new RuntimeException("Team not found"));
        if (details.containsKey("name")) team.setName(details.get("name"));
        if (details.containsKey("description")) team.setDescription(details.get("description"));
        if (details.containsKey("specialty")) team.setSpecialty(details.get("specialty"));
        if (details.containsKey("capacity")) team.setCapacity(details.get("capacity"));
        if (details.containsKey("region")) team.setRegion(details.get("region"));
        return toTeamMap(teamRepository.save(team));
    }

    @Transactional
    public void deleteTeam(UUID teamId) {
        Team team = teamRepository.findById(teamId).orElseThrow(() -> new RuntimeException("Team not found"));
        // Mark as deleted or locked instead of hard delete to avoid foreign key issues
        team.setPublished(false);
        teamRepository.save(team);
    }

    @Transactional

```
