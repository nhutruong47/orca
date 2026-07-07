# Knowledge Document: DebugController.java (Chunk 1/8)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/DebugController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security",
    "factory",
    "inventory",
    "employee"
  ],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;
import java.util.List;
import java.util.UUID;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.InventoryRepository;
import jakarta.persistence.EntityManager;
import org.springframework.transaction.annotation.Transactional;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.entity.Role;
import org.example.backend.entity.InventoryItem;
import org.example.backend.entity.TeamMember;
import org.example.backend.entity.GroupRole;
import java.time.LocalDateTime;

@RestController
@RequestMapping("/api/debug")
public class DebugController {

    private final UserRepository userRepository;
    private final TeamRepository teamRepository;
    private final InventoryRepository inventoryRepository;
    private final PasswordEncoder passwordEncoder;
    private final EntityManager entityManager;
    private final String adminUsername;
    private final String adminPassword;

    public DebugController(
            UserRepository userRepository,
            TeamRepository teamRepository,
            InventoryRepository inventoryRepository,
            PasswordEncoder passwordEncoder,
            EntityManager entityManager,
            @Value("${app.default-admin.username:admin}") String adminUsername,
            @Value("${app.default-admin.password:Admin@123}") String adminPassword) {
        this.userRepository = userRepository;
        this.teamRepository = teamRepository;
        this.inventoryRepository = inventoryRepository;
        this.passwordEncoder = passwordEncoder;
        this.entityManager = entityManager;
        this.adminUsername = adminUsername;
        this.adminPassword = adminPassword;
    }

    @GetMapping("/ping")
    public String ping() {
        return "pong";
    }

    @GetMapping("/fix-images")
    @Transactional
    public Map<String, Object> fixImages() {
        List<Team> teams = teamRepository.findAll();

```
