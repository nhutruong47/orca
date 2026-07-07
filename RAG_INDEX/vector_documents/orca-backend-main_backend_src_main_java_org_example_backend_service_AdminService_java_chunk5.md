# Knowledge Document: AdminService.java (Chunk 6/16)

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
  "chunk_index": 5,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
m());
        overview.put("orderStatusCounts", countByStatus(orders, InterGroupOrder::getStatus));
        overview.put("productionOrderStatusCounts", countByStatus(productionOrders, ProductionOrder::getStatus));
        overview.put("batchStatusCounts", countByStatus(productionBatches, ProductionBatch::getStatus));
        overview.put("taskStatusCounts", countByStatus(tasks, Task::getStatus));
        overview.put("recentUsers", users.stream()
                .sorted(this::compareCreatedAtDesc)
                .limit(5)
                .map(this::toUserMap)
                .toList());
        overview.put("recentTeams", teams.stream()
                .sorted(this::compareCreatedAtDesc)
                .limit(5)
                .map(this::toTeamMap)
                .toList());

        return overview;
    }

    private long countCreatedBetweenUsers(List<User> users, LocalDateTime start, LocalDateTime end) {
        return users.stream().filter(user -> isBetween(user.getCreatedAt(), start, end)).count();
    }

    private long countCreatedBetweenTeams(List<Team> teams, LocalDateTime start, LocalDateTime end) {
        return teams.stream().filter(team -> isBetween(team.getCreatedAt(), start, end)).count();
    }

    private long sumPaidBetween(List<PaymentTransaction> payments, LocalDateTime start, LocalDateTime end) {
        return payments.stream()
                .filter(this::isPaidPayment)
                .filter(payment -> isBetween(payment.getPaidAt() != null ? payment.getPaidAt() : payment.getCreatedAt(), start, end))
                .mapToLong(PaymentTransaction::getAmount)
                .sum();
    }

    private boolean isBetween(LocalDateTime value, LocalDateTime start, LocalDateTime end) {
        return value != null && !value.isBefore(start) && value.isBefore(end);
    }

    private boolean isPaidPayment(PaymentTransaction payment) {
        return "PAID".equalsIgnoreCase(safeText(payment.getStatus(), ""));
    }

    private boolean isActiveStatus(String status) {
        String normalized = safeText(status, "").toUpperCase(Locale.ROOT);
        return !List.of("COMPLETED", "COMPLETE", "DONE", "CANCELLED", "CANCELED", "REJECTED").contains(normalized);
    }

    private boolean isCompletedStatus(String status) {
        String normalized = safeText(status, "").toUpperCase(Locale.ROOT);

```
