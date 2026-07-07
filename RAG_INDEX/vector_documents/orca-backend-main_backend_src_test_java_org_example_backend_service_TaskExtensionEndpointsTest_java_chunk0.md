# Knowledge Document: TaskExtensionEndpointsTest.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/TaskExtensionEndpointsTest.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.entity.*;
import org.example.backend.repository.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.Map;
import java.util.UUID;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Verifies the new task endpoints:
 *  - supervisor assignment
 *  - transfer (record persists, ownership rotates)
 *  - dependency creation
 */
@SpringBootTest
@Transactional
public class TaskExtensionEndpointsTest {

    @Autowired private TaskService taskService;
    @Autowired private TaskRepository taskRepo;
    @Autowired private GoalRepository goalRepo;
    @Autowired private TeamRepository teamRepo;
    @Autowired private UserRepository userRepo;
    @Autowired private TeamMemberRepository teamMemberRepo;

    private User owner;
    private User supervisor;
    private User assignee;
    private Team team;
    private Task task;

    @BeforeEach
    void setUp() {
        owner = persistUser("owner_");
        supervisor = persistUser("super_");
        assignee = persistUser("assignee_");

        team = new Team();
        team.setName("Team " + UUID.randomUUID());
        team.setOwner(owner);
        team = teamRepo.save(team);

        addMember(team, owner);
        addMember(team, supervisor);
        addMember(team, assignee);

        Goal goal = new Goal();
        goal.setTitle("Goal " + UUID.randomUUID());
        goal.setTeam(team);
        goal.setOwner(owner);
        goal = goalRepo.save(goal);

        task = new Task();
        task.setTitle("Task " + UUID.randomUUID());
        task.setGoal(goal);
        task = taskRepo.save(task);
    }

    private User persistUser(String prefix) {
        User u = new User();
        u.setUsername(prefix + UUID.randomUUID());
        u.setPassword("pass");
        u.setEmail(prefix + UUID.randomUUID() + "@example.com");
        return userRepo.save(u);
    }

    private void addMember(Team team, User user) {
        TeamMember tm = new TeamMember();
        tm.setTeam(team);
        tm.setUser(user);
        tm.setGroupRole(GroupRole.MEMBER);
        teamMemberRepo.save(tm);
    }

    @Test

```
