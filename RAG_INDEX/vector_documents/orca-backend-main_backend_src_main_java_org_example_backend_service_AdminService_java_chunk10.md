# Knowledge Document: AdminService.java (Chunk 11/16)

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
  "chunk_index": 10,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java

        taskService.updateStatus(taskId, normalized);
        Task task = taskRepository.findById(taskId)
                .orElseThrow(() -> new RuntimeException("Task not found"));
        return toTaskMap(task);
    }

    public List<SubscriptionPlan> getPlans() {
        return planRepository.findAll();
    }

    @Transactional
    public SubscriptionPlan createPlan(SubscriptionPlan plan) {
        return planRepository.save(plan);
    }

    @Transactional
    public SubscriptionPlan updatePlan(UUID id, SubscriptionPlan details) {
        SubscriptionPlan plan = planRepository.findById(id).orElseThrow(() -> new RuntimeException("Plan not found"));
        plan.setName(details.getName());
        plan.setPrice(details.getPrice());
        plan.setPeriod(details.getPeriod());
        plan.setMaxUsers(details.getMaxUsers());
        plan.setMaxOrders(details.getMaxOrders());
        plan.setMaxBatches(details.getMaxBatches());
        plan.setMaxWorkshops(details.getMaxWorkshops());
        plan.setAiLimit(details.getAiLimit());
        plan.setFeatures(details.getFeatures());
        return planRepository.save(plan);
    }

    @Transactional
    public void deletePlan(UUID id) {
        planRepository.deleteById(id);
    }

    public Map<String, String> getAiConfigs() {
        return aiConfigRepository.findAll().stream()
                .collect(Collectors.toMap(AiConfig::getConfigKey, AiConfig::getConfigValue));
    }

    @Transactional
    public void updateAiConfigs(Map<String, String> configs) {
        configs.forEach((key, value) -> {
            AiConfig config = aiConfigRepository.findById(key).orElse(new AiConfig(key, value));
            config.setConfigValue(value);
            aiConfigRepository.save(config);
        });
    }

    private <T> Map<String, Long> countByStatus(List<T> items, Function<T, String> statusGetter) {
        return items.stream()
                .collect(Collectors.groupingBy(
                        item -> safeText(statusGetter.apply(item), "UNKNOWN"),
                        LinkedHashMap::new,
                        Collectors.counting()));
    }

    private Map<String, Object> toUserMap(User user) {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", user.getId().toString());
        map.put("username", user.getUsername());

```
