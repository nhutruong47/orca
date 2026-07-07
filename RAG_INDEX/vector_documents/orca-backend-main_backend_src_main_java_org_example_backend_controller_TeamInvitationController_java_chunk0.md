# Knowledge Document: TeamInvitationController.java (Chunk 1/2)

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
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import io.jsonwebtoken.Claims;
import org.example.backend.entity.GroupRole;
import org.example.backend.entity.Team;
import org.example.backend.entity.TeamMember;
import org.example.backend.entity.User;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.example.backend.security.JwtUtil;
import org.example.backend.service.EmailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/teams")
public class TeamInvitationController {

        @Autowired
        private TeamRepository teamRepository;

        @Autowired
        private TeamMemberRepository teamMemberRepository;

        @Autowired
        private UserRepository userRepository;

        @Autowired
        private JwtUtil jwtUtil;

        @Autowired
        private EmailService emailService;

        @PostMapping("/{teamId}/invite")
        public ResponseEntity<?> inviteMember(@PathVariable UUID teamId,
                        @RequestBody Map<String, String> payload,
                        @AuthenticationPrincipal UserDetails userDetails) {
                String email = payload.get("email");
                String roleStr = payload.getOrDefault("role", "MEMBER");

                User inviter = userRepository.findByUsername(userDetails.getUsername())
                                .orElseThrow(() -> new RuntimeException("User not found"));

                Team team = teamRepository.findById(teamId)
                                .orElseThrow(() -> new RuntimeException("Team not found"));

                // Generate invitation token
                String token = jwtUtil.generateInviteToken(email, teamId, roleStr);

                // Link for the frontend
                String inviteLink = "http://localhost:5173/invite?token=" + token;

                // Send email
                emailService.sendInvitationEmail(email, team.getName(),

```
