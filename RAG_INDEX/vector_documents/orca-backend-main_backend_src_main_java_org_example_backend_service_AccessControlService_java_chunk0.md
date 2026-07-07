# Knowledge Document: AccessControlService.java (Chunk 1/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AccessControlService.java",
  "language": "java",
  "module": "service",
  "business_domain": "admin",
  "tags": [
    "admin",
    "workspace",
    "production",
    "attendance",
    "inventory",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, workspace, production, attendance, inventory, security

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.entity.GroupRole;
import org.example.backend.entity.InterGroupOrder;
import org.example.backend.entity.InventoryItem;
import org.example.backend.entity.ProductionOrder;
import org.example.backend.entity.Role;
import org.example.backend.entity.Task;
import org.example.backend.entity.TeamMember;
import org.example.backend.entity.User;
import org.example.backend.repository.AttendanceRepository;
import org.example.backend.repository.GoalRepository;
import org.example.backend.repository.InterGroupOrderRepository;
import org.example.backend.repository.InventoryRepository;
import org.example.backend.repository.ProductionOrderRepository;
import org.example.backend.repository.TaskChecklistRepository;
import org.example.backend.repository.TaskRepository;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.UserRepository;
import org.example.backend.repository.ProductionPlanRepository;
import org.example.backend.repository.DailyTargetRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class AccessControlService {

    private final TeamMemberRepository teamMemberRepository;
    private final UserRepository userRepository;
    private final ProductionOrderRepository productionOrderRepository;
    private final InterGroupOrderRepository interGroupOrderRepository;
    private final InventoryRepository inventoryRepository;
    private final GoalRepository goalRepository;
    private final TaskRepository taskRepository;
    private final TaskChecklistRepository taskChecklistRepository;
    private final AttendanceRepository attendanceRepository;
    private final ProductionPlanRepository productionPlanRepository;
    private final DailyTargetRepository dailyTargetRepository;

    public AccessControlService(
            TeamMemberRepository teamMemberRepository,
            UserRepository userRepository,
            ProductionOrderRepository productionOrderRepository,
            InterGroupOrderRepository interGroupOrderRepository,
            InventoryRepository inventoryRepository,
            GoalRepository goalRepository,
            TaskRepository taskRepository,

```
