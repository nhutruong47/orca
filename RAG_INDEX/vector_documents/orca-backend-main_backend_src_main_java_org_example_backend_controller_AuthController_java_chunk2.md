# Knowledge Document: AuthController.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AuthController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
ser user) {
        Map<String, Object> info = new HashMap<>();
        info.put("id", user.getId().toString());
        info.put("username", user.getUsername());
        info.put("fullName", user.getFullName() != null ? user.getFullName() : "");
        info.put("email", user.getEmail() != null ? user.getEmail() : "");
        info.put("avatar", user.getAvatar() != null ? user.getAvatar() : "");
        info.put("role", user.getRole().name());
        info.put("chipId", user.getChipId() != null ? user.getChipId() : "");
        info.put("aiPlan", user.getAiPlan() != null ? user.getAiPlan() : "free");
        info.put("aiPlanExpiresAt", user.getAiPlanExpiresAt() != null ? user.getAiPlanExpiresAt().toString() : null);
        return ResponseEntity.ok(info);
    }

    @GetMapping("/trial-status")
    public ResponseEntity<?> getTrialStatus(@AuthenticationPrincipal User user) {
        Map<String, Object> status = new HashMap<>();
        status.put("aiTrialActive", true); // Bỏ chặn UI frontend
        status.put("daysRemaining", user.getAiTrialDaysRemaining());
        status.put("aiUsageCount", user.getAiUsageCount());
        status.put("aiPlan", user.getAiPlan() != null ? user.getAiPlan() : "free");
        
        int maxUsage = 10;
        if ("enterprise".equalsIgnoreCase(user.getAiPlan())) {
            maxUsage = -1; // unlimited
        } else if ("professional".equalsIgnoreCase(user.getAiPlan()) || "plus".equalsIgnoreCase(user.getAiPlan())) {
            maxUsage = 100;
        }
        status.put("aiMaxUsage", maxUsage);
        return ResponseEntity.ok(status);
    }
}

```
