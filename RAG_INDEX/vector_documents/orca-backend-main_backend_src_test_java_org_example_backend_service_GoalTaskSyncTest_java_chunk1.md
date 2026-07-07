# Knowledge Document: GoalTaskSyncTest.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/GoalTaskSyncTest.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
);
        assertEquals("IN_PROGRESS", updatedGoal.getStatus());

        taskService.updateStatus(task2.getId(), "COMPLETED");
        
        updatedGoal = goalRepo.findById(goal.getId()).orElseThrow();
        assertEquals(2, updatedGoal.getCompletedTasks());
        assertEquals("DONE", updatedGoal.getStatus());
    }

    @Test
    void whenTaskRevertsToPending_GoalStatusRevertsFromDone() {
        taskService.updateStatus(task1.getId(), "COMPLETED");
        taskService.updateStatus(task2.getId(), "COMPLETED");
        
        Goal updatedGoal = goalRepo.findById(goal.getId()).orElseThrow();
        assertEquals("DONE", updatedGoal.getStatus());

        // Revert task 1
        taskService.updateStatus(task1.getId(), "PENDING");
        
        updatedGoal = goalRepo.findById(goal.getId()).orElseThrow();
        assertEquals(1, updatedGoal.getCompletedTasks());
        assertEquals("IN_PROGRESS", updatedGoal.getStatus());
    }
}

```
