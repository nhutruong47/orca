# Knowledge Document: AdminService.java (Chunk 7/16)

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
  "chunk_index": 6,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
tus(), ""));
    }

    private boolean isActiveStatus(String status) {
        String normalized = safeText(status, "").toUpperCase(Locale.ROOT);
        return !List.of("COMPLETED", "COMPLETE", "DONE", "CANCELLED", "CANCELED", "REJECTED").contains(normalized);
    }

    private boolean isCompletedStatus(String status) {
        String normalized = safeText(status, "").toUpperCase(Locale.ROOT);
        return List.of("COMPLETED", "COMPLETE", "DONE").contains(normalized);
    }

    @Transactional(readOnly = true)
    public List<Map<String, Object>> getUsers() {
        return userRepository.findAll().stream()
                .sorted(this::compareCreatedAtDesc)
                .map(this::toUserMap)
                .toList();
    }

    @Transactional(readOnly = true)
    public List<Map<String, Object>> getTeams() {
        return teamRepository.findAll().stream()
                .sorted(this::compareCreatedAtDesc)
                .map(this::toTeamMap)
                .toList();
    }

    @Transactional(readOnly = true)
    public List<Map<String, Object>> getOrders() {
        return orderRepository.findAll().stream()
                .sorted(this::compareCreatedAtDesc)
                .map(this::toOrderMap)
                .toList();
    }

    @Transactional(readOnly = true)
    public List<Map<String, Object>> getTasks() {
        return taskRepository.findAll().stream()
                .sorted(this::compareCreatedAtDesc)
                .map(this::toTaskMap)
                .toList();
    }

    @Transactional(readOnly = true)
    public List<Map<String, Object>> getPayments() {
        return paymentRepository.findAll().stream()
                .sorted(this::comparePaidAtDesc)
                .map(this::toPaymentMap)
                .toList();
    }

    @Transactional
    public Map<String, Object> updateUserRole(UUID userId, String role, User currentUser) {
        if (role == null || role.isBlank()) {
            throw new RuntimeException("Role is required");
        }

        Role nextRole;
        try {
            nextRole = Role.valueOf(role.toUpperCase(Locale.ROOT));
        } catch (IllegalArgumentException ex) {
            throw new RuntimeException("Role is invalid");
        }

        User target = userRepository.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));


```
