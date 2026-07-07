# Knowledge Document: PayosPaymentService.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/PayosPaymentService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "payment"
  ],
  "logical_type": "Service",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
eStr).orElse(null);
                if (transaction != null && !"PAID".equals(transaction.getStatus())) {
                    transaction.setStatus("PAID");
                    transaction.setPaidAt(LocalDateTime.now());
                    transaction.setVnpResponseCode("00");
                    transaction.setVnpTransactionStatus("00");
                    paymentRepository.save(transaction);

                    activatePlan(transaction.getUser(), transaction.getPlanId());
                }
            }
            return Map.of("success", true);
        } catch (Exception e) {
            e.printStackTrace();
            return Map.of("success", false, "error", e.getMessage());
        }
    }

    private void activatePlan(User user, String planId) {
        if (user == null) return;
        user.setAiPlan(planId);
        if ("enterprise".equalsIgnoreCase(planId)) {
            user.setAiPlanExpiresAt(LocalDateTime.now().plusDays(30));
        } else if ("professional".equalsIgnoreCase(planId) || "plus".equalsIgnoreCase(planId)) {
            user.setAiUsageCount(0);
            user.setAiPlanExpiresAt(null);
        } else {
            user.setAiPlanExpiresAt(LocalDateTime.now().plusMonths(1));
        }
        userRepository.save(user);
    }

    private Plan findPlan(String planId) {
        return PLANS.stream()
                .filter(plan -> plan.id().equalsIgnoreCase(planId))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Goi AI khong hop le"));
    }

    private record Plan(String id, String name, long monthlyPrice, long tokenLimit) {}
}

```
