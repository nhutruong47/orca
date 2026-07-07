# Knowledge Document: AdminService.java (Chunk 5/16)

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
  "chunk_index": 4,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
                 && !"COMPLETED".equals(task.getStatus()))
                .count());
        overview.put("totalOrders", orders.size());
        overview.put("activeOrders", orders.stream()
                .filter(order -> "PENDING".equals(order.getStatus()) || "ACCEPTED".equals(order.getStatus()))
                .count());
        overview.put("totalProductionOrders", productionOrders.size());
        overview.put("activeProductionOrders", productionOrders.stream()
                .filter(order -> isActiveStatus(order.getStatus()))
                .count());
        overview.put("overdueProductionOrders", productionOrders.stream()
                .filter(order -> order.getInternalDeadline() != null
                        && order.getInternalDeadline().isBefore(now)
                        && isActiveStatus(order.getStatus()))
                .count());
        overview.put("totalBatches", productionBatches.size());
        overview.put("activeBatches", productionBatches.stream()
                .filter(batch -> isActiveStatus(batch.getStatus()))
                .count());
        overview.put("completedBatches", productionBatches.stream()
                .filter(batch -> isCompletedStatus(batch.getStatus()))
                .count());
        overview.put("paidPayments", payments.stream().filter(this::isPaidPayment).count());
        overview.put("totalPayments", payments.size());
        overview.put("revenueThisMonth", sumPaidBetween(payments, monthStart, now));
        overview.put("revenuePreviousMonth", sumPaidBetween(payments, previousMonthStart, monthStart));
        overview.put("revenueThisYear", sumPaidBetween(payments, yearStart, now));
        overview.put("revenuePreviousYear", sumPaidBetween(payments, previousYearStart, yearStart));
        overview.put("revenueTotal", payments.stream()
                .filter(this::isPaidPayment)
                .mapToLong(PaymentTransaction::getAmount)
                .sum());
        overview.put("orderStatusCounts", countByStatus(orders, InterGroupOrder::getStatus));
        overview.put("productionOrderStatusCounts", countByStatus(productionOrders, ProductionOrder::getStatus));
        overview.put("batchStatusCounts", countByStatus(productionBatches, ProductionBatch::getStatus));
        overview.put("taskStatusCounts", countByStatus(tasks, Task::getStatus));

```
