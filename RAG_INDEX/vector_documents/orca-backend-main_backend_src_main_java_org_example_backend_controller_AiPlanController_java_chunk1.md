# Knowledge Document: AiPlanController.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AiPlanController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "authentication",
  "tags": [
    "authentication",
    "security",
    "authorization"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: authentication, security, authorization

## Source Code Chunk
```java
}
    }

    @PatchMapping("/{planId}/status")
    public ResponseEntity<?> updateStatus(@PathVariable UUID planId,
                                          @RequestBody Map<String, Object> body,
                                          @AuthenticationPrincipal User user) {
        try {
            Map<String, Object> stub = new LinkedHashMap<>();
            stub.put("id", planId.toString());
            stub.put("status", body.getOrDefault("status", "DRAFT"));
            return ResponseEntity.ok(stub);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }
}
```
