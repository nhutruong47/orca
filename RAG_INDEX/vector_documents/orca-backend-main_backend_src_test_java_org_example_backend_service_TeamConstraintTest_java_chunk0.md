# Knowledge Document: TeamConstraintTest.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/TeamConstraintTest.java",
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

import java.util.UUID;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@Transactional
public class TeamConstraintTest {

    @Autowired private TeamRepository teamRepo;
    @Autowired private UserRepository userRepo;
    @Autowired private GoalRepository goalRepo;
    @Autowired private TaskRepository taskRepo;
    @Autowired private TeamMemberRepository teamMemberRepo;

    @PersistenceContext
    private EntityManager entityManager;

    private User owner;
    private Team team;
    private Goal goal;
    private Task task;

    @BeforeEach
    void setUp() {
        owner = new User();
        owner.setUsername("owner_delete_" + UUID.randomUUID());
        owner.setPassword("pass");
        owner = userRepo.save(owner);

        team = new Team();
        team.setName("Team to Delete");
        team.setOwner(owner);
        team = teamRepo.save(team);

        TeamMember tm = new TeamMember();
        tm.setTeam(team);
        tm.setUser(owner);
        teamMemberRepo.save(tm);

        goal = new Goal();
        goal.setTitle("Delete Goal");
        goal.setTeam(team);
        goal.setOwner(owner);
        goal = goalRepo.save(goal);

        task = new Task();
        task.setTitle("Delete Task");
        task.setGoal(goal);
        task = taskRepo.save(task);
    }

    @Test
    void deleteTeam_ShouldCascadeDeleteGoalsAndTasks() {
        // Assert initial state
        assertTrue(teamRepo.findById(team.getId()).isPresent());
        assertTrue(goalRepo.findById(goal.getId()).isPresent());
        assertTrue(taskRepo.findById(task.getId()).isPresent());
        assertFalse(teamMemberRepo.findByTeamId(team.getId()).isEmpty());

        // Clear persistence context so managed entities don't cause TransientObjectException on flush
        entityManager.clear();

        // Delete team
        teamRepo.deleteById(team.getId());
        teamRepo.flush();


```
