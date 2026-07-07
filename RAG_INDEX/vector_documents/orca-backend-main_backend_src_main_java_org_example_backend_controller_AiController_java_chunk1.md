# Knowledge Document: AiController.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AiController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "inventory",
  "tags": [
    "inventory",
    "payment",
    "authentication",
    "security",
    "authorization"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, authentication, security, authorization

## Source Code Chunk
```java
Active()) {
            throw new org.springframework.web.server.ResponseStatusException(
                    org.springframework.http.HttpStatus.PAYMENT_REQUIRED,
                    "Hết hạn gói miễn phí. Bạn cần nâng cấp gói để sử dụng tốt hơn."
            );
        }
        int limit = 10;
        if ("enterprise".equalsIgnoreCase(user.getAiPlan())) {
            limit = Integer.MAX_VALUE;
        } else if ("professional".equalsIgnoreCase(user.getAiPlan()) || "plus".equalsIgnoreCase(user.getAiPlan())) {
            limit = 100;
        }
        int updated = userRepository.incrementAiUsageIfUnderLimit(user.getId(), limit);
        if (updated == 0) {
            throw new org.springframework.web.server.ResponseStatusException(
                    org.springframework.http.HttpStatus.PAYMENT_REQUIRED,
                    "Bạn đã đạt giới hạn sử dụng AI. Vui lòng nâng cấp gói dịch vụ."
            );
        }

        System.out.println("DEBUG AiController - parseText called with: " + payload);
        String text = payload.getOrDefault("text", "");
        String teamIdStr = payload.get("teamId");
        if (text.isBlank()) {
            return ResponseEntity.badRequest().build();
        }

        java.util.UUID teamId = null;
        if (teamIdStr != null && !teamIdStr.isBlank()) {
            try { teamId = java.util.UUID.fromString(teamIdStr); } catch (Exception ignored) {}
        }

        // Authorization: must be a team member to read inventory/labels/tasks.
        if (teamId != null) {
            accessControlService.validateTeamAccess(user.getId(), teamId);
        }

        // Build member context only after authorization passes.
        String memberContext = "";
        if (teamId != null) {
            List<TeamMember> members = teamMemberRepo.findByTeamId(teamId);
            StringBuilder sb = new StringBuilder();
            for (TeamMember tm : members) {
                String name = tm.getUser().getUsername();
                List<String> labels = tm.getJobLabels();
                sb.append("- ").append(name);
                if (labels != null && !labels.isEmpty()) {
                    sb.append(" (Nhãn: ").append(String.join(", ", labels)).append(")");
                } else {
                    sb.append(" (Chưa gán nhãn)");
                }
                sb.append("\n");
            }

```
