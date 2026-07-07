# Knowledge Document: FactoryDashboardController.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/FactoryDashboardController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "production",
    "dashboard"
  ],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, production, dashboard

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.service.FactoryDashboardService;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/production/dashboard")
@CrossOrigin("*")
public class FactoryDashboardController {

    private final FactoryDashboardService dashboardService;

    public FactoryDashboardController(FactoryDashboardService dashboardService) {
        this.dashboardService = dashboardService;
    }

    @GetMapping("/{teamId}")
    public ResponseEntity<?> getDashboard(@PathVariable UUID teamId) {
        return ResponseEntity.ok(dashboardService.getDashboard(teamId));
    }

    @GetMapping("/{teamId}/productivity")
    public ResponseEntity<?> getProductivity(
            @PathVariable UUID teamId,
            @RequestParam @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate startDate,
            @RequestParam @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate endDate) {
        return ResponseEntity.ok(dashboardService.getProductivitySummary(teamId, startDate, endDate));
    }
}

```
