# Knowledge Document: TeamService.java (Chunk 3/9)

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
  "chunk_index": 2,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
}

        return toDTO(teamRepository.save(team), false);
    }

    /**
     * Thêm thành viên bằng EMAIL:
     * - Nếu email đã có tài khoản: thêm vào nhóm ngay
     * - Nếu chưa có tài khoản: gửi email mời có link
     */
    @Transactional
    public Map<String, String> addMemberByEmail(UUID teamId, String email, String requesterUsername) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        checkAdminRole(team, requester);

        Optional<User> existingUser = userRepository.findByEmail(email);

        if (existingUser.isPresent()) {
            User member = existingUser.get();

            if (teamMemberRepository.findByTeamIdAndUserId(teamId, member.getId()).isPresent()) {
                throw new RuntimeException("Đã là thành viên của nhóm này rồi!");
            }

            TeamMember tm = new TeamMember();
            tm.setTeam(team);
            tm.setUser(member);
            tm.setGroupRole(GroupRole.MEMBER);
            teamMemberRepository.save(tm);

            return Map.of(
                    "status", "ADDED",
                    "message", "Đã thêm " + member.getUsername() + " vào nhóm!");
        } else {
            String token = jwtUtil.generateInviteToken(email, teamId, "MEMBER");
            String inviteLink = "http://localhost:5173/invite?token=" + token;
            String inviterName = requester.getFullName() != null ? requester.getFullName() : requester.getUsername();

            boolean sent = emailService.sendInvitationEmail(email, team.getName(), inviterName, inviteLink);

            if (sent) {
                // Gửi email thành công
                return Map.of(
                        "status", "INVITED",
                        "message", "Đã gửi email mời thành công tới " + email);
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

```
