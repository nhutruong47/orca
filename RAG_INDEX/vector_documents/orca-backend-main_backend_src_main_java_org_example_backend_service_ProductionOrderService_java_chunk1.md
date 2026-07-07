# Knowledge Document: ProductionOrderService.java (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        ProductionOrder order = new ProductionOrder();
        order.setTeam(team);
        applyEditableFields(order, raw);
        order.setStatus("PENDING");

        validateOrder(order);
        order.calculateInputRequired();

        return orderRepo.save(order);
    }

    @Transactional
    public ProductionOrder updateOrder(UUID orderId, ProductionOrder raw) {
        ProductionOrder order = getById(orderId);
        applyEditableFields(order, raw);
        if (raw.getStatus() != null && !raw.getStatus().isBlank()) {
            order.setStatus(raw.getStatus());
        }

        validateOrder(order);
        order.calculateInputRequired();

        return orderRepo.save(order);
    }

    @Transactional
    public void deleteOrder(UUID orderId) {
        ProductionOrder order = getById(orderId);

        List<Attendance> attendances = attendanceRepo.findByOrderId(orderId);
        attendances.forEach(attendance -> attendance.setProductionOrder(null));
        attendanceRepo.saveAll(attendances);

        List<ProductionBatch> batches = batchRepo.findByOrderIdOrderByCreatedAtDesc(orderId);
        batches.forEach(batch -> batch.setOrder(null));
        batchRepo.saveAll(batches);

        dailyTargetRepo.deleteAll(dailyTargetRepo.findByOrderIdOrderByTargetDateAsc(orderId));
        List<ProductionPlan> plans = planRepo.findByOrderIdOrderByCreatedAtDesc(orderId);
        planRepo.deleteAll(plans);

        orderRepo.delete(order);
    }

    private void applyEditableFields(ProductionOrder order, ProductionOrder raw) {
        order.setTitle(raw.getTitle());
        order.setDescription(raw.getDescription());
        order.setCustomerName(raw.getCustomerName());
        order.setProductType(raw.getProductType());
        order.setProcessType(raw.getProcessType());
        order.setRoastLevel(raw.getRoastLevel());
        order.setPackageSize(raw.getPackageSize());
        order.setTotalPackages(raw.getTotalPackages());
        order.setOutputTarget(raw.getOutputTarget());
        order.setExpectedYield(raw.getExpectedYield());
        order.setExpectedLoss(raw.getExpectedLoss());
        order.setUnit(raw.getUnit());
        order.setOrderDate(raw.getOrderDate() != null ? raw.getOrderDate() : LocalDate.now());

```
