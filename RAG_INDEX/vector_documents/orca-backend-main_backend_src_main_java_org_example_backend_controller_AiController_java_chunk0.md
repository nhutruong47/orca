# Knowledge Document: AiController.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, authentication, security, authorization

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.AiParseResult;
import org.example.backend.entity.TeamMember;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.AiServiceClient;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.web.bind.annotation.*;

import java.util.*;
import org.example.backend.repository.UserRepository;

@RestController
@RequestMapping("/api/ai")
public class AiController {

    private final AiServiceClient aiServiceClient;
    private final TeamMemberRepository teamMemberRepo;
    private final UserRepository userRepository;
    private final AccessControlService accessControlService;

    public AiController(AiServiceClient aiServiceClient,
                        TeamMemberRepository teamMemberRepo,
                        UserRepository userRepository,
                        AccessControlService accessControlService) {
        this.aiServiceClient = aiServiceClient;
        this.teamMemberRepo = teamMemberRepo;
        this.userRepository = userRepository;
        this.accessControlService = accessControlService;
    }

    /**
     * Frontend gọi trực tiếp để xem kết quả AI parse trước khi tạo Goal.
     * Giờ sẽ gửi kèm danh sách thành viên + nhãn dán để AI giao việc ngay.
     *
     * Authorization: user phải thuộc team mới được đọc member labels.
     */
    @PostMapping("/parse")
    public ResponseEntity<AiParseResult> parseText(@RequestBody Map<String, String> payload, @org.springframework.security.core.annotation.AuthenticationPrincipal org.example.backend.entity.User user) {
        if (user == null) {
            throw new AccessDeniedException("Authentication required");
        }
        if (!user.isAiTrialActive()) {
            throw new org.springframework.web.server.ResponseStatusException(
                    org.springframework.http.HttpStatus.PAYMENT_REQUIRED,
                    "Hết hạn gói miễn phí. Bạn cần nâng cấp gói để sử dụng tốt hơn."
            );
        }
        int limit = 10;
        if ("enterprise".equalsIgnoreCase(user.getAiPlan())) {
            limit = Integer.MAX_VALUE;

```
