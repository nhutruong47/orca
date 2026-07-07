# Knowledge Document: GoalService.java (Chunk 1/10)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/GoalService.java",
  "language": "java",
  "module": "service",
  "business_domain": "employee",
  "tags": [
    "employee",
    "admin",
    "production",
    "chat"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.GoalDTO;
import org.example.backend.dto.AiParseResult;
import org.example.backend.entity.*;
import org.example.backend.repository.*;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

@Service
public class GoalService {

    private final GoalRepository goalRepo;
    private final TaskRepository taskRepo;
    private final UserRepository userRepo;
    private final TeamRepository teamRepo;
    private final TeamMemberRepository teamMemberRepo;
    private final AiServiceClient aiServiceClient;

    public GoalService(GoalRepository goalRepo, TaskRepository taskRepo, UserRepository userRepo,
            TeamRepository teamRepo, TeamMemberRepository teamMemberRepo, AiServiceClient aiServiceClient) {
        this.goalRepo = goalRepo;
        this.taskRepo = taskRepo;
        this.userRepo = userRepo;
        this.teamRepo = teamRepo;
        this.teamMemberRepo = teamMemberRepo;
        this.aiServiceClient = aiServiceClient;
    }

    /** Lấy goals theo team */
    public List<GoalDTO> getByTeam(UUID teamId) {
        return goalRepo.findByTeamId(teamId).stream()
                .map(this::toDTO).collect(Collectors.toList());
    }

    /** Tạo goal trong team — Owner nhập mục tiêu + deadline, AI chia task */
    public GoalDTO create(GoalDTO dto, User currentUser) {
        Team team = teamRepo.findById(UUID.fromString(dto.getTeamId()))
                .orElseThrow(() -> new RuntimeException("Team not found"));

        // Chỉ Owner được tạo goal
        if (!isTeamManager(team, currentUser)) {
            throw new RuntimeException("Only managers can create production plans");
        }

        Goal g = new Goal();
        g.setTitle(dto.getTitle());
        g.setOutputTarget(dto.getOutputTarget());
        g.setRawInstruction(dto.getRawInstruction());
        g.setPriority(dto.getPriority() != null ? dto.getPriority() : 1);
        g.setChatLog(dto.getChatLog());

        // Parse deadline from string
        LocalDateTime parsedDeadline = parseDeadline(dto.getDeadline());
        g.setDeadline(parsedDeadline);

        g.setTeam(team);

```
