# Knowledge Document: AdminService.java (Chunk 4/16)

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
  "chunk_index": 3,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
roductionOrderRepository.findAll();
        List<ProductionBatch> productionBatches = productionBatchRepository.findAll();
        List<PaymentTransaction> payments = paymentRepository.findAll();
        LocalDateTime now = LocalDateTime.now();
        LocalDateTime monthStart = LocalDate.now().withDayOfMonth(1).atStartOfDay();
        LocalDateTime previousMonthStart = monthStart.minusMonths(1);
        LocalDateTime yearStart = LocalDate.of(now.getYear(), 1, 1).atStartOfDay();
        LocalDateTime previousYearStart = yearStart.minusYears(1);

        Map<String, Object> overview = new LinkedHashMap<>();
        overview.put("totalUsers", users.size());
        overview.put("adminUsers", users.stream().filter(user -> user.getRole() == Role.ADMIN).count());
        overview.put("memberUsers", users.stream().filter(user -> user.getRole() != Role.ADMIN).count());
        overview.put("newUsersThisMonth", countCreatedBetweenUsers(users, monthStart, now));
        overview.put("newUsersPreviousMonth", countCreatedBetweenUsers(users, previousMonthStart, monthStart));
        overview.put("totalTeams", teams.size());
        overview.put("publishedTeams", teams.stream().filter(Team::isPublished).count());
        overview.put("newTeamsThisMonth", countCreatedBetweenTeams(teams, monthStart, now));
        overview.put("newTeamsPreviousMonth", countCreatedBetweenTeams(teams, previousMonthStart, monthStart));
        overview.put("totalGoals", goals.size());
        overview.put("activeGoals", goals.stream().filter(goal -> !"DONE".equals(goal.getStatus())).count());
        overview.put("totalTasks", tasks.size());
        overview.put("completedTasks", tasks.stream().filter(task -> "COMPLETED".equals(task.getStatus())).count());
        overview.put("overdueTasks", tasks.stream()
                .filter(task -> task.getDeadline() != null
                        && task.getDeadline().isBefore(now)
                        && !"COMPLETED".equals(task.getStatus()))
                .count());
        overview.put("totalOrders", orders.size());
        overview.put("activeOrders", orders.stream()
                .filter(order -> "PENDING".equals(order.getStatus()) || "ACCEPTED".equals(order.getStatus()))
                .count());
        overview.put("totalProductionOrders", productionOrders.size());

```
