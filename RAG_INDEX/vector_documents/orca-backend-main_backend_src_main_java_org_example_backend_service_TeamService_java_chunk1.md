# Knowledge Document: TeamService.java (Chunk 2/9)

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
  "chunk_index": 1,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
List());
    }

    /**
     * Xem chi tiết nhóm (bao gồm danh sách thành viên)
     */
    @Transactional(readOnly = true)
    public TeamDTO getTeamDetail(UUID teamId) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        return toDTO(team, true);
    }

    /**
     * Tạo nhóm mới — user trở thành Owner
     */
    @Transactional
    public TeamDTO createTeam(TeamDTO dto, String username) {
        User owner = userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found"));

        Team team = new Team();
        team.setName(dto.getName());
        team.setDescription(dto.getDescription());
        team.setOwner(owner);
        team = teamRepository.save(team);

        // Thêm owner vào team_members với role ADMIN
        TeamMember ownerMember = new TeamMember();
        ownerMember.setTeam(team);
        ownerMember.setUser(owner);
        ownerMember.setGroupRole(GroupRole.ADMIN);
        teamMemberRepository.save(ownerMember);

        inventoryService.initializeDefaultInventory(team.getId());

        return toDTO(team, false);
    }

    @Transactional
    public TeamDTO updateTeam(UUID teamId, TeamDTO dto, String requesterUsername) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        checkAdminRole(team, requester);

        if (dto.getName() != null && !dto.getName().isBlank()) {
            team.setName(dto.getName().trim());
        }
        if (dto.getDescription() != null) {
            team.setDescription(dto.getDescription().trim());
        }
        if (dto.getMetadata() != null) {
            team.setMetadata(dto.getMetadata());
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

```
