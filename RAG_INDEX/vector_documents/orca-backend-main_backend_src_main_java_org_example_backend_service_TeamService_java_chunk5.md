# Knowledge Document: TeamService.java (Chunk 6/9)

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
  "chunk_index": 5,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
oryImageUrl() != null)
            team.setFactoryImageUrl(dto.getFactoryImageUrl());
        if (dto.getFactoryImages() != null)
            team.setFactoryImages(packList(dto.getFactoryImages()));
        if (dto.getDescription() != null)
            team.setDescription(dto.getDescription());

        team = teamRepository.save(team);
        return toDTO(team, false);
    }

    @Transactional
    public TeamDTO submitVerification(UUID teamId, TeamDTO dto, String requesterUsername) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        checkAdminRole(team, requester);

        updateVerificationFields(team, dto);
        team.setVerificationStatus("PENDING");
        team.setVerificationRejectReason(null);

        return toDTO(teamRepository.save(team), false);
    }

    /**
     * Tắt quảng cáo (Unpublish) khỏi Marketplace
     */
    @Transactional
    public void unpublishTeam(UUID teamId, String requesterUsername) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        checkAdminRole(team, requester);

        team.setPublished(false);
        teamRepository.save(team);
    }

    /**
     * Tham gia nhóm bằng Invite Code (6 ký tự)
     */
    @Transactional
    public TeamDTO joinByCode(String inviteCode, String username) {

        Team team = teamRepository.findByInviteCode(inviteCode.toUpperCase())
                .orElseThrow(() -> new RuntimeException("Mã mời không hợp lệ hoặc không tồn tại"));

        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found"));

        // Check if already a member
        if (teamMemberRepository.findByTeamIdAndUserId(team.getId(), user.getId()).isPresent()) {
            throw new RuntimeException("Bạn đã là thành viên của nhóm này rồi");
        }

        TeamMember tm = new TeamMember();
        tm.setTeam(team);
        tm.setUser(user);

```
