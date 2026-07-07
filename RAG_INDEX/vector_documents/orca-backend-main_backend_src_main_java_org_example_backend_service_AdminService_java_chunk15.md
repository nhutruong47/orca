# Knowledge Document: AdminService.java (Chunk 16/16)

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
  "chunk_index": 15,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
    return value != null ? value : fallback;
    }

    private List<String> splitList(String value) {
        if (value == null || value.isBlank()) {
            return List.of();
        }
        return value.lines()
                .map(String::trim)
                .filter(item -> !item.isBlank())
                .toList();
    }

    private int compareCreatedAtDesc(User left, User right) {
        return compareDateDesc(left.getCreatedAt(), right.getCreatedAt());
    }

    private int compareCreatedAtDesc(Team left, Team right) {
        return compareDateDesc(left.getCreatedAt(), right.getCreatedAt());
    }

    private int compareCreatedAtDesc(InterGroupOrder left, InterGroupOrder right) {
        return compareDateDesc(left.getCreatedAt(), right.getCreatedAt());
    }

    private int compareCreatedAtDesc(Task left, Task right) {
        return compareDateDesc(left.getCreatedAt(), right.getCreatedAt());
    }

    private int comparePaidAtDesc(PaymentTransaction left, PaymentTransaction right) {
        LocalDateTime leftDate = left.getPaidAt() != null ? left.getPaidAt() : left.getCreatedAt();
        LocalDateTime rightDate = right.getPaidAt() != null ? right.getPaidAt() : right.getCreatedAt();
        return compareDateDesc(leftDate, rightDate);
    }

    private int compareDateDesc(LocalDateTime left, LocalDateTime right) {
        return Comparator.nullsLast(Comparator.<LocalDateTime>naturalOrder())
                .reversed()
                .compare(left, right);
    }
}

```
