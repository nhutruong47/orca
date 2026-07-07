# Knowledge Document: VnpayPaymentService.java (Chunk 10/11)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/VnpayPaymentService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "payment"
  ],
  "logical_type": "Service",
  "chunk_index": 9,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
          .filter(plan -> plan.id().equalsIgnoreCase(planId))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Goi AI khong hop le"));
    }



    private String normalizePaymentMethod(String method) {
        String normalized = method == null ? "VNPAY" : method.trim().toUpperCase(Locale.ROOT);
        if (!List.of("MB_BANK", "VNPAY").contains(normalized)) {
            throw new RuntimeException("Phuong thuc thanh toan khong hop le");
        }
        return normalized;
    }

    private String paymentMethodLabel(String method) {
        return "MB_BANK".equalsIgnoreCase(method) ? "MB Bank" : "VNPay";
    }

    private String buildVirtualQrPayload(String method, String txnRef, Plan plan) {
        return String.join("|",
                "ORCA",
                normalizePaymentMethod(method),
                txnRef,
                plan.id(),
                plan.name(),
                String.valueOf(plan.monthlyPrice()),
                "Thanh toan goi " + plan.name());
    }

    private void activatePlan(User user, String planId) {
        user.setAiPlan(planId);
        
        if ("enterprise".equalsIgnoreCase(planId)) {
            user.setAiPlanExpiresAt(LocalDateTime.now().plusDays(30));
        } else if ("professional".equalsIgnoreCase(planId) || "plus".equalsIgnoreCase(planId)) {
            user.setAiUsageCount(0); // Reset usages to 0 to give 100 new uses
            user.setAiPlanExpiresAt(null); // Optional: if Plus doesn't expire by time
        } else {
            user.setAiPlanExpiresAt(LocalDateTime.now().plusMonths(1));
        }
        
        userRepository.save(user);
    }

    private String clientIp(HttpServletRequest request) {
        String forwardedFor = request.getHeader("X-Forwarded-For");
        if (forwardedFor != null && !forwardedFor.isBlank()) {
            return forwardedFor.split(",")[0].trim();
        }
        return request.getRemoteAddr();
    }

    private long parseLong(String value) {
        try {
            return Long.parseLong(value);
        } catch (Exception ex) {
            return 0;
        }
    }

    private int parseInt(Object value) {
        try {
            return Integer.parseInt(safeString(value));
        } catch (Exception ex) {
            return -1;
        }
    }

    private String safeString(Object value) {

```
