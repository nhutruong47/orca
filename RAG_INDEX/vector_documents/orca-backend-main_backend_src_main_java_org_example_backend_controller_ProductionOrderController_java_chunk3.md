# Knowledge Document: ProductionOrderController.java (Chunk 4/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ProductionOrderController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "production",
  "tags": [
    "production",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, authentication, security

## Source Code Chunk
```java
expectedLoss"));
        o.setUnit(getString(body, "unit"));
        o.setOrderDate(getLocalDate(body, "orderDate"));
        o.setConfirmDate(getLocalDate(body, "confirmDate"));
        o.setProductionStartDate(getLocalDate(body, "productionStartDate"));
        o.setCustomerDeliveryDate(getLocalDate(body, "customerDeliveryDate"));
        o.setSafetyBufferDays(getInt(body, "safetyBufferDays"));
        o.setRecipientName(getString(body, "recipientName"));
        o.setRecipientPhone(getString(body, "recipientPhone"));
        o.setShippingNote(getString(body, "shippingNote"));
        return o;
    }

    private String getString(Map<String, Object> body, String key) {
        Object v = body.get(key);
        return v != null ? v.toString() : null;
    }

    private Double getDouble(Map<String, Object> body, String key) {
        Object v = body.get(key);
        if (v == null) return null;
        if (v instanceof Number) return ((Number) v).doubleValue();
        try { return Double.parseDouble(v.toString()); } catch (Exception e) { return null; }
    }

    private Integer getInt(Map<String, Object> body, String key) {
        Object v = body.get(key);
        if (v == null) return null;
        if (v instanceof Number) return ((Number) v).intValue();
        try { return Integer.parseInt(v.toString()); } catch (Exception e) { return null; }
    }

    private java.time.LocalDate getLocalDate(Map<String, Object> body, String key) {
        Object v = body.get(key);
        if (v == null) return null;
        try { return java.time.LocalDate.parse(v.toString().substring(0, 10)); } catch (Exception e) { return null; }
    }
}

```
