# Knowledge Document: TaskServiceIntegrationTest.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/service/TaskServiceIntegrationTest.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
rowException() {
        Exception exception = assertThrows(RuntimeException.class, () -> {
            taskService.assign(task.getId(), stranger.getId());
        });
        
        assertTrue(exception.getMessage().contains("Người dùng không thuộc xưởng này"));
    }

    @Test
    void assignTaskToMember_ShouldSucceed() {
        TaskDTO dto = taskService.assign(task.getId(), owner.getId());
        assertNotNull(dto);
        assertEquals(owner.getId().toString(), dto.getMemberId());
    }
}

```
