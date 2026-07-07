# Knowledge Document: AdminService.java (Chunk 3/16)

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
  "chunk_index": 2,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
        if (planRepository.count() == 0) {
            SubscriptionPlan basic = new SubscriptionPlan();
            basic.setName("Cơ bản");
            basic.setPrice(499000.0);
            basic.setPeriod("Tháng");
            basic.setMaxUsers(5);
            basic.setMaxOrders(100);
            basic.setMaxBatches(300);
            basic.setMaxWorkshops(1);
            basic.setAiLimit(5000);
            basic.setFeatures("Bảng đơn hàng,Theo dõi lô sản xuất,Báo cáo cơ bản");
            
            SubscriptionPlan growth = new SubscriptionPlan();
            growth.setName("Tăng trưởng");
            growth.setPrice(1499000.0);
            growth.setPeriod("Tháng");
            growth.setMaxUsers(30);
            growth.setMaxOrders(1000);
            growth.setMaxBatches(5000);
            growth.setMaxWorkshops(5);
            growth.setAiLimit(40000);
            growth.setFeatures("Quy trình QC,Trợ lý AI,Xuất dữ liệu thanh toán");

            SubscriptionPlan enterprise = new SubscriptionPlan();
            enterprise.setName("Doanh nghiệp");
            enterprise.setPrice(0.0);
            enterprise.setPeriod("Năm");
            enterprise.setMaxUsers(500);
            enterprise.setMaxOrders(99999);
            enterprise.setMaxBatches(99999);
            enterprise.setMaxWorkshops(50);
            enterprise.setAiLimit(500000);
            enterprise.setFeatures("Cam kết dịch vụ,Quy trình tùy chỉnh,Giới hạn AI riêng");

            planRepository.saveAll(List.of(basic, growth, enterprise));
        }
    }

    @Transactional(readOnly = true)
    public Map<String, Object> getOverview() {
        List<User> users = userRepository.findAll();
        List<Team> teams = teamRepository.findAll();
        List<Goal> goals = goalRepository.findAll();
        List<Task> tasks = taskRepository.findAll();
        List<InterGroupOrder> orders = orderRepository.findAll();
        List<ProductionOrder> productionOrders = productionOrderRepository.findAll();
        List<ProductionBatch> productionBatches = productionBatchRepository.findAll();
        List<PaymentTransaction> payments = paymentRepository.findAll();
        LocalDateTime now = LocalDateTime.now();
        LocalDateTime monthStart = LocalDate.now().withDayOfMonth(1).atStartOfDay();
        LocalDateTime previousMonthStart = monthStart.minusMonths(1);

```
