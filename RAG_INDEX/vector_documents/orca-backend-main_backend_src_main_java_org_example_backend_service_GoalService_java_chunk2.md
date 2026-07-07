# Knowledge Document: GoalService.java (Chunk 3/10)

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
  "chunk_index": 2,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
ception e) {
                System.err.println("Lỗi lưu JSON aiParsedData: " + e.getMessage());
            }

            generatedTasks = parseResult.getTasks() != null ? parseResult.getTasks() : new ArrayList<>();
        } else if (generatedTasks != null && !generatedTasks.isEmpty()) {
            System.out.println("✅ Using explicitly passed approved tasks count: " + generatedTasks.size());
        } else {
            generatedTasks = new ArrayList<>();
        }
        
        List<TeamMember> assignableMembers = teamMemberRepo.findByTeamId(team.getId());
        List<String> memberNames = assignableMembers.stream()
                .map(tm -> tm.getUser().getUsername())
                .collect(Collectors.toList());


        if (!generatedTasks.isEmpty()) {
            // Tạo tasks từ AI plan
            int totalTaskCount = generatedTasks.size();
            int memberIndex = 0;
            double totalGoalTarget = extractQuantity(saved.getOutputTarget());
            for (Map<String, Object> tp : generatedTasks) {
                Task task = new Task();
                task.setGoal(saved);
                task.setTitle(requireTaskTitle(tp));
                String suggestedRole = (String) tp.get("assigneeRole");
                String desc = (String) tp.get("description");
                if (suggestedRole != null) {
                    desc = "[Vai trò gợi ý: " + suggestedRole + "] " + (desc != null ? desc : "");
                }
                task.setDescription(desc);

                task.setWorkload(parseWorkload(tp.get("workload"), explicitApprovedTasks));
                task.setPriority(parsePriority(tp.get("priority")));
                
                task.setDeadline(parsedDeadline);
                task.setOutputTarget(totalGoalTarget > 0 ? totalGoalTarget : 0.0);
                task.setActualOutput(0.0);
                task.setStatus("READY");

                // FE-approved task ưu tiên memberId/suggestedAssigneeId. Legacy AI task vẫn fallback round-robin.
                boolean assigned = false;
                User assignedUser = null;
                String memberId = firstNonBlank(asString(tp.get("memberId")), asString(tp.get("suggestedAssigneeId")));
                if (memberId != null) {
                    assignedUser = resolveTeamMember(team.getId(), memberId);
                    task.setMember(assignedUser);

```
