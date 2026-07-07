# Knowledge Document: AdminService.java (Chunk 15/16)

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
  "chunk_index": 14,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
al().getTeam().getName()
                : "");
        map.put("memberId", task.getMember() != null ? task.getMember().getId().toString() : "");
        map.put("memberName", task.getMember() != null ? task.getMember().getUsername() : "");
        map.put("priority", task.getPriority());
        map.put("status", task.getStatus());
        map.put("acceptanceStatus", task.getAcceptanceStatus());
        map.put("completionPercentage", task.getCompletionPercentage() != null ? task.getCompletionPercentage() : 0);
        map.put("deadline", task.getDeadline() != null ? task.getDeadline().toString() : null);
        map.put("createdAt", task.getCreatedAt() != null ? task.getCreatedAt().toString() : null);
        return map;
    }

    private Map<String, Object> toPaymentMap(PaymentTransaction payment) {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", payment.getId().toString());
        map.put("txnRef", payment.getTxnRef());
        map.put("userId", payment.getUser() != null ? payment.getUser().getId().toString() : "");
        map.put("username", payment.getUser() != null ? payment.getUser().getUsername() : "");
        map.put("fullName", payment.getUser() != null ? safeText(payment.getUser().getFullName(), "") : "");
        map.put("email", payment.getUser() != null ? safeText(payment.getUser().getEmail(), "") : "");
        map.put("planId", payment.getPlanId());
        map.put("amount", payment.getAmount());
        map.put("status", payment.getStatus());
        map.put("bankCode", safeText(payment.getBankCode(), ""));
        map.put("paymentMethod", safeText(payment.getPaymentMethod(), ""));
        map.put("createdAt", payment.getCreatedAt() != null ? payment.getCreatedAt().toString() : null);
        map.put("paidAt", payment.getPaidAt() != null ? payment.getPaidAt().toString() : null);
        return map;
    }

    private String safeText(String value, String fallback) {
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

```
