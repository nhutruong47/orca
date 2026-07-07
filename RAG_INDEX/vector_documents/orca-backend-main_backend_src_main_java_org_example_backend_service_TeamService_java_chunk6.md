# Knowledge Document: TeamService.java (Chunk 7/9)

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
  "chunk_index": 6,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
)
                .orElseThrow(() -> new RuntimeException("User not found"));

        // Check if already a member
        if (teamMemberRepository.findByTeamIdAndUserId(team.getId(), user.getId()).isPresent()) {
            throw new RuntimeException("Bạn đã là thành viên của nhóm này rồi");
        }

        TeamMember tm = new TeamMember();
        tm.setTeam(team);
        tm.setUser(user);
        tm.setGroupRole(GroupRole.MEMBER);
        teamMemberRepository.save(tm);

        return toDTO(team, false);
    }

    // === Helper: Entity → DTO ===
    private TeamDTO toDTO(Team team, boolean includeMembers) {
        TeamDTO dto = new TeamDTO();
        dto.setId(team.getId());
        dto.setName(team.getName());
        dto.setDescription(team.getDescription());
        dto.setOwnerId(team.getOwner().getId());
        dto.setOwnerName(team.getOwner().getUsername());
        dto.setCreatedAt(team.getCreatedAt().toString());
        dto.setInviteCode(team.getInviteCode());

        dto.setPublished(team.isPublished());
        dto.setSpecialty(team.getSpecialty());
        dto.setCapacity(team.getCapacity());
        dto.setRegion(team.getRegion());
        dto.setFactoryType(team.getFactoryType());
        dto.setCapacityValue(team.getCapacityValue());
        dto.setCapacityUnit(team.getCapacityUnit());
        dto.setFactoryImageUrl(team.getFactoryImageUrl());
        dto.setFactoryImages(unpackList(team.getFactoryImages()));
        dto.setVerificationStatus(isBlank(team.getVerificationStatus()) ? "NOT_SUBMITTED" : team.getVerificationStatus());
        dto.setBusinessLicense(team.getBusinessLicense());
        dto.setBusinessAddress(team.getBusinessAddress());
        dto.setWebsiteUrl(team.getWebsiteUrl());
        dto.setFacebookUrl(team.getFacebookUrl());
        dto.setCertificates(unpackList(team.getCertificates()));
        dto.setCertificationDocument(team.getCertificationDocument());
        dto.setVerificationRejectReason(team.getVerificationRejectReason());

        // Trust
        dto.setCompletedOrders(team.getCompletedOrders());
        dto.setCancelledOrders(team.getCancelledOrders());
        dto.setTotalOrders(team.getTotalOrders());
        int trust = team.getTotalOrders() > 0
                ? (int) ((double) team.getCompletedOrders() / team.getTotalOrders() * 100)
                : 0;
        dto.setTrustScore(trust);


```
