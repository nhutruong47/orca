# Knowledge Document: GoalService.java (Chunk 2/10)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/GoalService.java",
  "language": "java",
  "module": "service",
  "business_domain": "employee",
  "tags": [
    "employee",
    "admin",
    "production",
    "chat"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
());
        g.setOutputTarget(dto.getOutputTarget());
        g.setRawInstruction(dto.getRawInstruction());
        g.setPriority(dto.getPriority() != null ? dto.getPriority() : 1);
        g.setChatLog(dto.getChatLog());

        // Parse deadline from string
        LocalDateTime parsedDeadline = parseDeadline(dto.getDeadline());
        g.setDeadline(parsedDeadline);

        g.setTeam(team);
        g.setOwner(currentUser);
        g.setStatus("PLANNING");

        Goal saved = goalRepo.save(g);

        List<Map<String, Object>> generatedTasks = dto.getTasks();
        boolean explicitApprovedTasks = generatedTasks != null && !generatedTasks.isEmpty();
        boolean wantAi = dto.getUseAi() != null && dto.getUseAi();

        if ((generatedTasks == null || generatedTasks.isEmpty()) && wantAi && currentUser.isAiTrialActive()) {
            // ONLY re-generate if no explicit tasks list was provided from the frontend preview
            List<TeamMember> teamMembers = teamMemberRepo.findByTeamId(team.getId());
            Map<String, List<String>> memberLabels = new java.util.LinkedHashMap<>();
            List<String> memberNames = new ArrayList<>();
            for (TeamMember tm : teamMembers) {
                String name = tm.getUser().getUsername();
                memberNames.add(name);
                memberLabels.put(name, tm.getJobLabels() != null ? tm.getJobLabels() : Collections.emptyList());
            }

            AiParseResult parseResult = aiServiceClient.generateTaskPlan(
                    dto.getOutputTarget(),
                    dto.getDeadline() != null ? dto.getDeadline() : "",
                    saved.getPriority(),
                    team.getId(),
                    memberLabels);

            try {
                com.fasterxml.jackson.databind.ObjectMapper mapper = new com.fasterxml.jackson.databind.ObjectMapper();
                saved.setAiParsedData(mapper.writeValueAsString(parseResult));
            } catch (Exception e) {
                System.err.println("Lỗi lưu JSON aiParsedData: " + e.getMessage());
            }

            generatedTasks = parseResult.getTasks() != null ? parseResult.getTasks() : new ArrayList<>();
        } else if (generatedTasks != null && !generatedTasks.isEmpty()) {
            System.out.println("✅ Using explicitly passed approved tasks count: " + generatedTasks.size());

```
