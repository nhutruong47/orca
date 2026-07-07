# Knowledge Document: TaskService.java (Chunk 1/15)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/TaskService.java",
  "language": "java",
  "module": "service",
  "business_domain": "report",
  "tags": [
    "report",
    "production",
    "attendance",
    "employee",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.TaskDTO;
import org.example.backend.dto.SalaryDTO;
import org.example.backend.entity.*;
import org.example.backend.repository.*;
import org.springframework.stereotype.Service;

import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.ByteArrayOutputStream;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class TaskService {

    private final TaskRepository taskRepo;
    private final GoalRepository goalRepo;
    private final UserRepository userRepo;
    private final TaskChecklistRepository checklistRepo;
    private final NotificationService notificationService;
    private final TeamMemberRepository teamMemberRepo;
    private final AttendanceRepository attendanceRepo;
    private final TaskTransferRepository transferRepo;
    private final TaskDependencyRepository dependencyRepo;

    public TaskService(TaskRepository taskRepo, GoalRepository goalRepo,
            UserRepository userRepo, TaskChecklistRepository checklistRepo,
            NotificationService notificationService, TeamMemberRepository teamMemberRepo,
            AttendanceRepository attendanceRepo,
            TaskTransferRepository transferRepo, TaskDependencyRepository dependencyRepo) {
        this.taskRepo = taskRepo;
        this.goalRepo = goalRepo;
        this.userRepo = userRepo;
        this.checklistRepo = checklistRepo;
        this.notificationService = notificationService;
        this.teamMemberRepo = teamMemberRepo;
        this.attendanceRepo = attendanceRepo;
        this.transferRepo = transferRepo;
        this.dependencyRepo = dependencyRepo;
    }

    public List<TaskDTO> getByGoal(UUID goalId) {
        return taskRepo.findByGoalId(goalId).stream().map(this::toDTO).collect(Collectors.toList());
    }

    public List<TaskDTO> getByMember(UUID memberId) {
        return taskRepo.findByMemberId(memberId).stream().map(this::toDTO).collect(Collectors.toList());
    }

    public List<TaskDTO> getAll() {
        return taskRepo.findAll().stream().map(this::toDTO).collect(Collectors.toList());
    }

    public TaskDTO getById(UUID id) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));

```
