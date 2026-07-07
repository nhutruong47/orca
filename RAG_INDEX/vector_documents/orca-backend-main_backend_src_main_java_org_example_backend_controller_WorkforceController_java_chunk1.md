# Knowledge Document: WorkforceController.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/WorkforceController.java",
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
tity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/teams/{teamId}/skill-matrix")
    public ResponseEntity<?> getSkillMatrix(@PathVariable UUID teamId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTeamMember(user, teamId);
            return ResponseEntity.ok(Map.of("members", List.of(), "skills", List.of()));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PutMapping("/members/{teamMemberId}/skills/{skillId}")
    public ResponseEntity<?> setWorkerSkill(@PathVariable UUID teamMemberId,
                                             @PathVariable UUID skillId,
                                             @RequestBody Map<String, Object> body,
                                             @AuthenticationPrincipal User user) {
        try {
            // Just return an acknowledgment — authorization can be expanded later.
            Map<String, Object> stub = new LinkedHashMap<>();
            stub.put("teamMemberId", teamMemberId.toString());
            stub.put("skillId", skillId.toString());
            stub.put("level", body.getOrDefault("level", 0));
            return ResponseEntity.ok(stub);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }
}
```
