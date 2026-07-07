# Knowledge Document: TeamInvitationController.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/TeamInvitationController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
 new RuntimeException("Team not found"));

                // Generate invitation token
                String token = jwtUtil.generateInviteToken(email, teamId, roleStr);

                // Link for the frontend
                String inviteLink = "http://localhost:5173/invite?token=" + token;

                // Send email
                emailService.sendInvitationEmail(email, team.getName(),
                                inviter.getFullName() != null ? inviter.getFullName() : inviter.getUsername(),
                                inviteLink);

                return ResponseEntity.ok(Map.of("message", "Invitation sent successfully"));
        }

        @PostMapping("/invites/accept")
        public ResponseEntity<?> acceptInvite(@RequestBody Map<String, String> payload,
                        @AuthenticationPrincipal UserDetails userDetails) {
                String token = payload.get("token");
                Claims claims = jwtUtil.parseInviteToken(token);

                UUID teamId = UUID.fromString(claims.get("teamId", String.class));
                GroupRole role = GroupRole.valueOf(claims.get("groupRole", String.class));

                User user = userRepository.findByUsername(userDetails.getUsername())
                                .orElseThrow(() -> new RuntimeException("User not found"));

                // Determine if user email matches invitation email.
                // We might want to allow it even if login is different, or strict match.
                // For now, let's just make sure user is logged in.

                Team team = teamRepository.findById(teamId)
                                .orElseThrow(() -> new RuntimeException("Team not found"));

                if (teamMemberRepository.findByTeamIdAndUserId(teamId, user.getId()).isPresent()) {
                        return ResponseEntity.badRequest()
                                        .body(Map.of("error", "User is already a member of this team"));
                }

                TeamMember tm = new TeamMember();
                tm.setTeam(team);
                tm.setUser(user);
                tm.setGroupRole(role);
                teamMemberRepository.save(tm);

                return ResponseEntity.ok(Map.of("message", "Joined team successfully", "teamId", teamId));
        }
}

```
