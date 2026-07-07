# Knowledge Document: AdminService.java (Chunk 2/16)

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
  "chunk_index": 1,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
final TaskRepository taskRepository;
    private final InterGroupOrderRepository orderRepository;
    private final ProductionOrderRepository productionOrderRepository;
    private final ProductionBatchRepository productionBatchRepository;
    private final PaymentTransactionRepository paymentRepository;
    private final TaskService taskService;
    private final PasswordEncoder passwordEncoder;
    private final SubscriptionPlanRepository planRepository;
    private final AiConfigRepository aiConfigRepository;

    public AdminService(
            UserRepository userRepository,
            TeamRepository teamRepository,
            TeamMemberRepository teamMemberRepository,
            GoalRepository goalRepository,
            TaskRepository taskRepository,
            InterGroupOrderRepository orderRepository,
            ProductionOrderRepository productionOrderRepository,
            ProductionBatchRepository productionBatchRepository,
            PaymentTransactionRepository paymentRepository,
            TaskService taskService,
            PasswordEncoder passwordEncoder,
            SubscriptionPlanRepository planRepository,
            AiConfigRepository aiConfigRepository) {
        this.userRepository = userRepository;
        this.teamRepository = teamRepository;
        this.teamMemberRepository = teamMemberRepository;
        this.goalRepository = goalRepository;
        this.taskRepository = taskRepository;
        this.orderRepository = orderRepository;
        this.productionOrderRepository = productionOrderRepository;
        this.productionBatchRepository = productionBatchRepository;
        this.paymentRepository = paymentRepository;
        this.taskService = taskService;
        this.passwordEncoder = passwordEncoder;
        this.planRepository = planRepository;
        this.aiConfigRepository = aiConfigRepository;
    }

    @PostConstruct
    public void seedDefaultPlans() {
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

```
