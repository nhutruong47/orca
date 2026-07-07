# Knowledge Document: GoalService.java (Chunk 5/10)

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
  "chunk_index": 4,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: employee, admin, production, chat

## Source Code Chunk
```java
ng aiBackupAssignee = firstText(tp,
                        "backupMember",
                        "backupAssignee",
                        "backupWorker",
                        "replacement",
                        "substitute",
                        "secondaryAssignee",
                        "backupPerson");
                if (aiBackupAssignee != null && !aiBackupAssignee.isEmpty()) {
                    Optional<User> matchedBackup = findTeamUser(assignableMembers, aiBackupAssignee.trim());
                    if (matchedBackup.isPresent() && !matchedBackup.get().getId().equals(assignedUser != null ? assignedUser.getId() : null)) {
                        task.setBackupMember(matchedBackup.get());
                        System.out.println("✅ AI gán người thay cho task '" + task.getTitle() + "': " + aiBackupAssignee);
                    }
                } else if (assignedUser != null && !explicitApprovedTasks && !memberNames.isEmpty()) {
                    final User currentAssignee = assignedUser;
                    List<User> candidateBackups = assignableMembers.stream()
                            .map(TeamMember::getUser)
                            .filter(user -> !user.getId().equals(currentAssignee.getId()))
                            .collect(Collectors.toList());
                    if (!candidateBackups.isEmpty()) {
                        User backupUser = candidateBackups.get(memberIndex % candidateBackups.size());
                        task.setBackupMember(backupUser);
                        System.out.println("✅ AI gán người thay fallback cho task '" + task.getTitle() + "': " + backupUser.getUsername());
                    }
                }

                taskRepo.save(task);
            }

            saved.setTotalTasks(totalTaskCount);
            saved.setCompletedTasks(0);
            saved.setStatus("PUBLISHED");
        } else {
            // HẾT HẠN → Tạo goal rỗng, user tự thêm task thủ công
            saved.setTotalTasks(0);
            saved.setCompletedTasks(0);
            saved.setStatus("PUBLISHED");
            saved.setAiParsedData(null);
        }

        goalRepo.save(saved);

        return toDTO(saved);
    }

    private double extractQuantity(String raw) {
        if (raw == null || raw.isBlank()) {
            return 0.0;
        }

```
