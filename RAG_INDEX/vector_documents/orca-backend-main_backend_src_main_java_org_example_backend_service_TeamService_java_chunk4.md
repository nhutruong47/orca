# Knowledge Document: TeamService.java (Chunk 5/9)

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
  "chunk_index": 4,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
orElseThrow(() -> new RuntimeException("Member not found in group"));

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
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        checkAdminRole(team, requester);

        // Xóa tất cả members trước
        List<TeamMember> members = teamMemberRepository.findByTeamId(teamId);
        teamMemberRepository.deleteAll(members);

        teamRepository.delete(team);
    }

    /**
     * Bật quảng cáo (Publish) Team lên Marketplace
     */
    @Transactional
    public TeamDTO advertiseTeam(UUID teamId, TeamDTO dto, String requesterUsername) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        User requester = userRepository.findByUsername(requesterUsername)
                .orElseThrow(() -> new RuntimeException("User not found"));
        checkAdminRole(team, requester);

        team.setPublished(true);
        if (dto.getSpecialty() != null)
            team.setSpecialty(dto.getSpecialty());
        if (dto.getCapacity() != null)
            team.setCapacity(dto.getCapacity());
        if (dto.getRegion() != null)
            team.setRegion(dto.getRegion());
        if (dto.getFactoryType() != null)
            team.setFactoryType(dto.getFactoryType());
        if (dto.getCapacityValue() != null)
            team.setCapacityValue(dto.getCapacityValue());
        if (dto.getCapacityUnit() != null)
            team.setCapacityUnit(dto.getCapacityUnit());
        if (dto.getFactoryImageUrl() != null)
            team.setFactoryImageUrl(dto.getFactoryImageUrl());
        if (dto.getFactoryImages() != null)
            team.setFactoryImages(packList(dto.getFactoryImages()));
        if (dto.getDescription() != null)
            team.setDescription(dto.getDescription());

        team = teamRepository.save(team);
        return toDTO(team, false);
    }

    @Transactional

```
