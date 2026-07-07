# Knowledge Document: AiWorkflowService.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AiWorkflowService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.ai.AiExtractRequest;
import org.example.backend.dto.ai.AiExtractResponse;
import org.example.backend.dto.ai.AiPlanDraftResponse;
import org.example.backend.dto.ai.AiPlanRequest;
import org.example.backend.dto.ai.AiReviseRequest;
import org.example.backend.dto.ai.AiTeamMemberContext;
import org.example.backend.entity.TeamMember;
import org.example.backend.entity.User;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.TeamRepository;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.server.ResponseStatusException;

import java.util.Collections;
import java.util.List;
import java.util.UUID;

@Service
public class AiWorkflowService {

    private final TeamMemberRepository teamMemberRepository;
    private final TeamRepository teamRepository;
    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${ai.v2.service-url:http://127.0.0.1:8000}")
    private String aiServiceUrl;

    public AiWorkflowService(TeamMemberRepository teamMemberRepository, TeamRepository teamRepository) {
        this.teamMemberRepository = teamMemberRepository;
        this.teamRepository = teamRepository;
    }

    public AiExtractResponse extract(AiExtractRequest request, User currentUser) {
        validateText(request != null ? request.getText() : null);
        if (request.getTeamId() != null && !request.getTeamId().isBlank()) {
            validateTeamAccess(parseTeamId(request.getTeamId()), currentUser);
        }
        return post("/extract", request, AiExtractResponse.class);
    }

    public AiPlanDraftResponse plan(AiPlanRequest request, User currentUser) {
        UUID teamId = requireTeamId(request != null ? request.getTeamId() : null);
        validateTeamAccess(teamId, currentUser);
        request.setMembers(loadTeamMembers(teamId));
        return post("/plan", request, AiPlanDraftResponse.class);
    }

    public AiPlanDraftResponse revise(AiReviseRequest request, User currentUser) {
        UUID teamId = requireTeamId(request != null ? request.getTeamId() : null);

```
