# Knowledge Document: MockDataInitializer.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/config/MockDataInitializer.java",
  "language": "java",
  "module": "config",
  "business_domain": "factory",
  "tags": [
    "factory",
    "admin",
    "inventory",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in config.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, inventory, security

## Source Code Chunk
```java
package org.example.backend.config;

import org.example.backend.entity.Role;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.example.backend.service.InventoryService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.DependsOn;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

@Component
@DependsOn("defaultAdminInitializer")
public class MockDataInitializer implements CommandLineRunner {

    private final TeamRepository teamRepository;
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final String adminUsername;
    private final InventoryService inventoryService;

    public MockDataInitializer(
            TeamRepository teamRepository,
            UserRepository userRepository,
            PasswordEncoder passwordEncoder,
            InventoryService inventoryService,
            @Value("${app.default-admin.username:admin}") String adminUsername) {
        this.teamRepository = teamRepository;
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.inventoryService = inventoryService;
        this.adminUsername = adminUsername;
    }

    @Override
    public void run(String... args) {
        if (teamRepository.count() > 0) {
            return;
        }

        User admin = userRepository.findByUsername(adminUsername).orElse(null);
        if (admin == null) {
            return;
        }

        String[] specialties = {"Cung ứng cà phê nhân", "Rang cà phê", "Đóng gói", "Gia công OEM", "Xử lý sau thu hoạch"};
        List<String> images = Arrays.asList(
            "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=500&q=80",
            "https://images.unsplash.com/photo-1514432324607-a09d9b4aefda?w=500&q=80",
            "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=500&q=80",
            "https://images.unsplash.com/photo-1504630083234-14187a9df0f5?w=500&q=80",

```
