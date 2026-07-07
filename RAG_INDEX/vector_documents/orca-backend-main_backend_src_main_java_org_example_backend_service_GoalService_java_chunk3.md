# Knowledge Document: GoalService.java (Chunk 4/10)

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
  "chunk_index": 3,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
k vẫn fallback round-robin.
                boolean assigned = false;
                User assignedUser = null;
                String memberId = firstNonBlank(asString(tp.get("memberId")), asString(tp.get("suggestedAssigneeId")));
                if (memberId != null) {
                    assignedUser = resolveTeamMember(team.getId(), memberId);
                    task.setMember(assignedUser);
                    assigned = true;
                }

                String aiAssignee = firstText(tp,
                        "assignee",
                        "suggestedAssignee",
                        "primaryWorker",
                        "worker",
                        "member",
                        "employee",
                        "nhanSu",
                        "personnel");
                if (aiAssignee != null && !aiAssignee.isEmpty()) {
                    Optional<User> matchedUser = findTeamUser(assignableMembers, aiAssignee.trim());
                    if (matchedUser.isPresent()) {
                        assignedUser = matchedUser.get();
                        task.setMember(assignedUser);
                        assigned = true;
                        System.out.println("✅ AI giao task '" + task.getTitle() + "' cho: " + aiAssignee);
                    }
                }
                if (!assigned && !explicitApprovedTasks && !memberNames.isEmpty()) {
                    String fallback = memberNames.get(memberIndex % memberNames.size());
                    assignedUser = userRepo.findByUsername(fallback).orElse(null);
                    if (assignedUser != null) {
                        task.setMember(assignedUser);
                    }
                    memberIndex++;
                    System.out.println("⚠️ Fallback round-robin giao task '" + task.getTitle() + "' cho: " + fallback);
                }

                String aiBackupAssignee = firstText(tp,
                        "backupMember",
                        "backupAssignee",
                        "backupWorker",
                        "replacement",
                        "substitute",
                        "secondaryAssignee",
                        "backupPerson");
                if (aiBackupAssignee != null && !aiBackupAssignee.isEmpty()) {

```
