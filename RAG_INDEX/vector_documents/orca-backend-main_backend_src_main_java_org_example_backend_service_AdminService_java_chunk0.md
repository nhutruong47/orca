# Knowledge Document: AdminService.java (Chunk 1/16)

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
  "chunk_index": 0,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.entity.Goal;
import org.example.backend.entity.InterGroupOrder;
import org.example.backend.entity.PaymentTransaction;
import org.example.backend.entity.ProductionBatch;
import org.example.backend.entity.ProductionOrder;
import org.example.backend.entity.Role;
import org.example.backend.entity.Task;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.GoalRepository;
import org.example.backend.repository.InterGroupOrderRepository;
import org.example.backend.repository.PaymentTransactionRepository;
import org.example.backend.repository.ProductionBatchRepository;
import org.example.backend.repository.ProductionOrderRepository;
import org.example.backend.repository.TaskRepository;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.example.backend.entity.SubscriptionPlan;
import org.example.backend.entity.AiConfig;
import org.example.backend.repository.SubscriptionPlanRepository;
import org.example.backend.repository.AiConfigRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.UUID;
import java.util.function.Function;
import java.util.stream.Collectors;

import jakarta.annotation.PostConstruct;

@Service
public class AdminService {

    private final UserRepository userRepository;
    private final TeamRepository teamRepository;
    private final TeamMemberRepository teamMemberRepository;
    private final GoalRepository goalRepository;
    private final TaskRepository taskRepository;
    private final InterGroupOrderRepository orderRepository;
    private final ProductionOrderRepository productionOrderRepository;
    private final ProductionBatchRepository productionBatchRepository;
    private final PaymentTransactionRepository paymentRepository;
    private final TaskService taskService;
    private final PasswordEncoder passwordEncoder;

```
