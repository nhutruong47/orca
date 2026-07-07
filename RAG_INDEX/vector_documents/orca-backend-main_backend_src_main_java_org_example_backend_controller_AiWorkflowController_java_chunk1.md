# Knowledge Document: AiWorkflowController.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AiWorkflowController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "payment",
  "tags": [
    "payment",
    "security",
    "authentication"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, security, authentication

## Source Code Chunk
```java
AYMENT_REQUIRED,
                    "Bạn đã đạt giới hạn sử dụng AI. Vui lòng nâng cấp gói dịch vụ."
            );
        }
    }

    @PostMapping("/extract")
    public ResponseEntity<?> extract(@RequestBody AiExtractRequest request, @AuthenticationPrincipal User user) {
        enforceAndIncrementUsage(user);
        return ResponseEntity.ok(aiWorkflowService.extract(request, user));
    }

    @PostMapping("/plan")
    public ResponseEntity<?> plan(@RequestBody AiPlanRequest request, @AuthenticationPrincipal User user) {
        enforceAndIncrementUsage(user);
        return ResponseEntity.ok(aiWorkflowService.plan(request, user));
    }

    @PostMapping("/revise")
    public ResponseEntity<?> revise(@RequestBody AiReviseRequest request, @AuthenticationPrincipal User user) {
        enforceAndIncrementUsage(user);
        return ResponseEntity.ok(aiWorkflowService.revise(request, user));
    }
}

```
