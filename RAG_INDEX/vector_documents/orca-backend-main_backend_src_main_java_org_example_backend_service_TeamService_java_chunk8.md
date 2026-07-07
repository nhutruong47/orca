# Knowledge Document: TeamService.java (Chunk 9/9)

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
  "chunk_index": 8,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
requester.getId())
                .orElseThrow(() -> new RuntimeException("Requester is not a member of the group"));
        if (requesterMember.getGroupRole() != GroupRole.ADMIN) {
            throw new RuntimeException("Only group ADMINs can perform this action");
        }
    }

    private void updateVerificationFields(Team team, TeamDTO dto) {
        if (dto.getBusinessLicense() != null)
            team.setBusinessLicense(dto.getBusinessLicense().trim());
        if (dto.getBusinessAddress() != null)
            team.setBusinessAddress(dto.getBusinessAddress().trim());
        if (dto.getWebsiteUrl() != null)
            team.setWebsiteUrl(dto.getWebsiteUrl().trim());
        if (dto.getFacebookUrl() != null)
            team.setFacebookUrl(dto.getFacebookUrl().trim());
        if (dto.getCertificates() != null)
            team.setCertificates(packList(dto.getCertificates()));
        if (dto.getCertificationDocument() != null)
            team.setCertificationDocument(dto.getCertificationDocument().trim());
    }

    private boolean isBlank(String value) {
        return value == null || value.isBlank();
    }

    private String packList(List<String> values) {
        if (values == null) {
            return null;
        }
        return values.stream()
                .filter(value -> value != null && !value.isBlank())
                .map(String::trim)
                .collect(Collectors.joining("\n"));
    }

    private List<String> unpackList(String value) {
        if (isBlank(value)) {
            return List.of();
        }
        return value.lines()
                .map(String::trim)
                .filter(item -> !item.isBlank())
                .toList();
    }

    // Cả ADMIN và MEMBER đều có thể mời thành viên mới
    private void checkAdminOrMember(Team team, User requester) {
        teamMemberRepository.findByTeamIdAndUserId(team.getId(), requester.getId())
                .orElseThrow(() -> new RuntimeException("Requester is not a member of the group"));
        // Không cần kiểm tra role, thành viên nào cũng có thể mời
    }
}

```
