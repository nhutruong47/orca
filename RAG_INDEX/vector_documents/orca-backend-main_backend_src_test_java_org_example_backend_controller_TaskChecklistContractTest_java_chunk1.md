# Knowledge Document: TaskChecklistContractTest.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/java/org/example/backend/controller/TaskChecklistContractTest.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, security

## Source Code Chunk
```java
       // Accept 4xx (forbidden) or 2xx — but never 404 / 405
        if (status == 404 || status == 405) {
            throw new AssertionError("Expected route to exist; got " + status);
        }
    }

    @Test
    @WithMockUser(username = "contract-user", roles = "MEMBER")
    void singular_checklist_toggle_alias_route_exists() throws Exception {
        UUID checklistId = UUID.randomUUID();
        int status = mockMvc.perform(patch("/api/tasks/checklist/" + checklistId + "/toggle"))
                .andReturn().getResponse().getStatus();
        if (status == 404 || status == 405) {
            throw new AssertionError("Expected route to exist; got " + status);
        }
    }
}
```
