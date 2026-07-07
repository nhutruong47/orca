# Knowledge Document: AiWorkflowService.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication

## Source Code Chunk
```java
quireTeamId(request != null ? request.getTeamId() : null);
        validateTeamAccess(teamId, currentUser);
        request.setMembers(loadTeamMembers(teamId));
        return post("/plan", request, AiPlanDraftResponse.class);
    }

    public AiPlanDraftResponse revise(AiReviseRequest request, User currentUser) {
        UUID teamId = requireTeamId(request != null ? request.getTeamId() : null);
        validateTeamAccess(teamId, currentUser);
        request.setMembers(loadTeamMembers(teamId));
        return post("/revise", request, AiPlanDraftResponse.class);
    }

    private <T> T post(String path, Object body, Class<T> responseType) {
        try {
            T response = restTemplate.postForObject(aiServiceUrl + path, body, responseType);
            if (response == null) {
                throw new ResponseStatusException(HttpStatus.BAD_GATEWAY, "AI service returned empty response");
            }
            return response;
        } catch (ResponseStatusException e) {
            throw e;
        } catch (RestClientException e) {
            throw new ResponseStatusException(HttpStatus.BAD_GATEWAY, "Cannot reach AI service: " + e.getMessage(), e);
        }
    }

    private List<AiTeamMemberContext> loadTeamMembers(UUID teamId) {
        return teamMemberRepository.findByTeamId(teamId).stream()
                .map(this::toContext)
                .toList();
    }

    private AiTeamMemberContext toContext(TeamMember teamMember) {
        User user = teamMember.getUser();
        AiTeamMemberContext context = new AiTeamMemberContext();
        context.setUserId(user.getId().toString());
        context.setUsername(user.getUsername());
        context.setFullName(user.getFullName());
        context.setJobLabels(teamMember.getJobLabels() != null ? teamMember.getJobLabels() : Collections.emptyList());
        return context;
    }

    private void validateText(String text) {
        if (text == null || text.trim().isEmpty()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Text is required");
        }
    }

    private UUID requireTeamId(String teamId) {
        if (teamId == null || teamId.isBlank()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "teamId is required");
        }
        return parseTeamId(teamId);
    }

    private UUID parseTeamId(String teamId) {
        try {

```
