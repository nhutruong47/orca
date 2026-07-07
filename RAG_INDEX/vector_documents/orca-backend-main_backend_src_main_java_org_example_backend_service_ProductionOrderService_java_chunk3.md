# Knowledge Document: ProductionOrderService.java (Chunk 4/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionOrderService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
veryDate() != null && order.getProductionStartDate() != null
                && !order.getCustomerDeliveryDate().isAfter(order.getProductionStartDate())) {
            throw new RuntimeException("Ngay giao hang phai sau ngay bat dau san xuat");
        }
    }

    public List<ProductionOrder> getOrdersByTeam(UUID teamId) {
        return orderRepo.findByTeamIdOrderByCreatedAtDesc(teamId);
    }

    public List<ProductionOrder> getActiveOrders(UUID teamId) {
        return orderRepo.findByTeamIdAndStatusInOrderByDeadline(teamId,
                List.of("CONFIRMED", "PLANNING", "IN_PRODUCTION"));
    }

    public ProductionOrder getById(UUID orderId) {
        return orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay don hang"));
    }

    public ProductionOrder updateStatus(UUID orderId, String status) {
        ProductionOrder order = getById(orderId);
        order.setStatus(status);
        return orderRepo.save(order);
    }

    public ProductionOrder updateCompletedQuantity(UUID orderId, Double quantity) {
        ProductionOrder order = getById(orderId);
        order.setCompletedQuantity(quantity);
        return orderRepo.save(order);
    }

    public ProductionOrderDTO toDTO(ProductionOrder o) {
        ProductionOrderDTO dto = new ProductionOrderDTO();
        dto.setId(o.getId().toString());
        dto.setTeamId(o.getTeam().getId().toString());
        dto.setOrderCode(o.getOrderCode());
        dto.setTitle(o.getTitle());
        dto.setDescription(o.getDescription());
        dto.setCustomerName(o.getCustomerName());
        dto.setProductType(o.getProductType());
        dto.setProcessType(o.getProcessType());
        dto.setRoastLevel(o.getRoastLevel());
        dto.setPackageSize(o.getPackageSize());
        dto.setTotalPackages(o.getTotalPackages());
        dto.setOutputTarget(o.getOutputTarget());
        dto.setExpectedYield(o.getExpectedYield());
        dto.setExpectedLoss(o.getExpectedLoss());
        dto.setInputRequired(o.getInputRequired());
        dto.setUnit(o.getUnit());
        dto.setOrderDate(o.getOrderDate());
        dto.setConfirmDate(o.getConfirmDate());
        dto.setProductionStartDate(o.getProductionStartDate());
        dto.setInternalDeadline(o.getInternalDeadline());
        dto.setCustomerDeliveryDate(o.getCustomerDeliveryDate());

```
