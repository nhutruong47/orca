# Knowledge Document: TaskController.java (Chunk 1/7)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/TaskController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.TaskDTO;
import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.TaskService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.HttpEntity;
import org.springframework.http.ResponseEntity;

import java.io.ByteArrayOutputStream;

@RestController
@RequestMapping("/api/tasks")
public class TaskController {

    @Autowired
    private TaskService taskService;

    @Autowired
    private AccessControlService accessControlService;

    @GetMapping
    public ResponseEntity<List<TaskDTO>> getAll(@AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.getAll());
    }

    @GetMapping("/by-goal/{goalId}")
    public ResponseEntity<?> getByGoal(@PathVariable UUID goalId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireGoalAccess(user, goalId);
            return ResponseEntity.ok(taskService.getByGoal(goalId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/my-tasks")
    public ResponseEntity<List<TaskDTO>> getMyTasks(@AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.getByMember(user.getId()));
    }

    @GetMapping("/my-kpi")
    public ResponseEntity<?> getMyKpi(@AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.getMemberKpi(user.getId()));
    }

    @GetMapping("/member/{memberId}")
    public ResponseEntity<?> getByMember(@PathVariable UUID memberId, @AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.getByMember(memberId));
    }

    @GetMapping("/member/{memberId}/kpi")

```
