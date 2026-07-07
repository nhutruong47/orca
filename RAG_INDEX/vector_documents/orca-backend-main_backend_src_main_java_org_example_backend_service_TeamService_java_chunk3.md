# Knowledge Document: TeamService.java (Chunk 4/9)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/TeamService.java",
  "language": "java",
  "module": "service",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security",
    "factory",
    "inventory",
    "employee"
  ],
  "logical_type": "Service",
  "chunk_index": 3,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
i " + email);
            } else {
                // Dev mode: chưa có SMTP thật, hiển link để copy
                return Map.of(
                        "status", "INVITED",
                        "message", "Chưa có email SMTP, copy link bên dưới để gửi thủ công",
                        "inviteLink", inviteLink);
            }
        }
    }

    /**
     * Xóa thành viên khỏi nhóm
     */
    @Transactional
    public void removeMember(UUID teamId, UUID userId, String requesterUsername) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        checkAdminRole(team, requester);

        // Không cho xóa owner/admin tạo ra team (tránh mất kiểm soát)
        if (team.getOwner().getId().equals(userId)) {
            throw new RuntimeException("Cannot remove the group owner");
        }

        TeamMember tm = teamMemberRepository.findByTeamIdAndUserId(teamId, userId)
                .orElseThrow(() -> new RuntimeException("Member not found in group"));
        teamMemberRepository.delete(tm);
    }

    /**
     * Cập nhật danh sách nhãn dán (Job Labels) cho thành viên (chỉ Owner/Admin).
     */
    @Transactional
    public List<String> updateMemberLabels(UUID teamId, UUID userId, List<String> labels, String requesterUsername) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        // Yêu cầu quyền ADMIN
        checkAdminRole(team, requester);

        TeamMember tm = teamMemberRepository.findByTeamIdAndUserId(teamId, userId)
                .orElseThrow(() -> new RuntimeException("Member not found in group"));

        // Cập nhật nhãn và lưu
        tm.setJobLabels(labels);
        teamMemberRepository.save(tm);

        return tm.getJobLabels();
    }

    /**
     * Xóa nhóm (chỉ Owner)
     */
    @Transactional
    public void deleteTeam(UUID teamId, String requesterUsername) {
        Team team = teamRepository.findById(teamId)

```
