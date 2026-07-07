# Knowledge Document: ProductionBoardService.java (Chunk 3/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionBoardService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
       if (t.getIsHoliday() != null && t.getIsHoliday()) continue;

            if ("roast".equals(stage)) {
                if (t.getTargetRoastKg() != null) targetKg += t.getTargetRoastKg();
                if (t.getActualRoastKg() != null) actualKg += t.getActualRoastKg();
            } else if ("qc".equals(stage)) {
                if (t.getTargetQcKg() != null) targetKg += t.getTargetQcKg();
                if (t.getActualQcKg() != null) actualKg += t.getActualQcKg();
            } else if ("packaging".equals(stage)) {
                if (t.getTargetPackagedKg() != null) targetKg += t.getTargetPackagedKg();
                if (t.getActualPackagedKg() != null) actualKg += t.getActualPackagedKg();
            }

            if (t.getTotalWorkerHours() != null) workerHours += t.getTotalWorkerHours();
            if (seenOrders.add(t.getOrder().getId())) orderCount++;
        }

        s.setTargetKg(targetKg);
        s.setActualKg(actualKg);
        s.setCompletionRate(targetKg > 0 ? Math.round(actualKg / targetKg * 10000.0) / 100.0 : 0.0);
        s.setOrderCount(orderCount);
        s.setWorkerHours(Math.round(workerHours * 10.0) / 10.0);
        return s;
    }

    private OrderStageRow buildOrderRow(ProductionOrder order, LocalDate date) {
        OrderStageRow r = new OrderStageRow();
        r.setOrderId(order.getId().toString());
        r.setOrderCode(order.getOrderCode());
        r.setTitle(order.getTitle());
        r.setCustomerName(order.getCustomerName());
        r.setOutputTarget(order.getOutputTarget() != null ? order.getOutputTarget() : 0);
        r.setCompletedQuantity(order.getCompletedQuantity() != null ? order.getCompletedQuantity() : 0);
        double remQty = order.getRemainingQuantity();
        r.setRemainingQuantity(remQty);
        double progPct = order.getProgressPercent();
        r.setProgressPercent(progPct);
        r.setRiskLevel(calcRiskLevel(order));

        Optional<DailyTarget> targetOpt = targetRepo.findByOrderIdAndTargetDate(order.getId(), date);
        if (targetOpt.isPresent()) {
            DailyTarget t = targetOpt.get();
            r.setRoastTarget(t.getTargetRoastKg() != null ? t.getTargetRoastKg() : 0);
            r.setQcTarget(t.getTargetQcKg() != null ? t.getTargetQcKg() : 0);
            r.setPackagingTarget(t.getTargetPackagedKg() != null ? t.getTargetPackagedKg() : 0);

```
