# Knowledge Document: ProductionOrderController.java (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, authentication, security

## Source Code Chunk
```java
.updateStatus(orderId, body.get("status"));
            return ResponseEntity.ok(orderService.toDTO(updated));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @DeleteMapping("/orders/{orderId}")
    public ResponseEntity<?> deleteOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        accessControlService.requireProductionOrderAccess(user, orderId);
        try {
            orderService.deleteOrder(orderId);
            return ResponseEntity.noContent().build();
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/teams/{teamId}/orders/active")
    public ResponseEntity<?> getActiveOrders(@PathVariable UUID teamId, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamMember(user, teamId);
        List<ProductionOrder> orders = orderService.getActiveOrders(teamId);
        List<ProductionOrderDTO> dtos = orders.stream()
                .map(orderService::toDTO)
                .collect(Collectors.toList());
        return ResponseEntity.ok(dtos);
    }

    private ProductionOrder mapToOrder(Map<String, Object> body) {
        ProductionOrder o = new ProductionOrder();
        o.setTitle(getString(body, "title"));
        o.setDescription(getString(body, "description"));
        o.setCustomerName(getString(body, "customerName"));
        o.setProductType(getString(body, "productType"));
        o.setProcessType(getString(body, "processType"));
        o.setRoastLevel(getString(body, "roastLevel"));
        o.setPackageSize(getString(body, "packageSize"));
        o.setTotalPackages(getInt(body, "totalPackages"));
        o.setOutputTarget(getDouble(body, "outputTarget"));
        o.setExpectedYield(getDouble(body, "expectedYield"));
        o.setExpectedLoss(getDouble(body, "expectedLoss"));
        o.setUnit(getString(body, "unit"));
        o.setOrderDate(getLocalDate(body, "orderDate"));
        o.setConfirmDate(getLocalDate(body, "confirmDate"));
        o.setProductionStartDate(getLocalDate(body, "productionStartDate"));
        o.setCustomerDeliveryDate(getLocalDate(body, "customerDeliveryDate"));
        o.setSafetyBufferDays(getInt(body, "safetyBufferDays"));

```
