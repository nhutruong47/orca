# Knowledge Document: VnpayPaymentService.java (Chunk 11/11)

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
  "chunk_index": 10,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
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
        return value == null ? "" : String.valueOf(value);
    }

    private Map<String, Object> result(String txnRef, String planId, String status, String message, String rspCode) {
        Map<String, Object> result = new LinkedHashMap<>();
        result.put("txnRef", txnRef);
        result.put("planId", planId);
        result.put("status", status);
        result.put("message", message);
        if (rspCode != null) {
            result.put("RspCode", rspCode);
            result.put("Message", message);
        }
        return result;
    }

    private record Plan(String id, String name, long monthlyPrice, long tokenLimit) {
    }
}

```
