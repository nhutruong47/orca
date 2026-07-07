# Knowledge Document: TeamService.java (Chunk 8/9)

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
  "chunk_index": 7,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
ionRejectReason());

        // Trust
        dto.setCompletedOrders(team.getCompletedOrders());
        dto.setCancelledOrders(team.getCancelledOrders());
        dto.setTotalOrders(team.getTotalOrders());
        int trust = team.getTotalOrders() > 0
                ? (int) ((double) team.getCompletedOrders() / team.getTotalOrders() * 100)
                : 0;
        dto.setTrustScore(trust);

        // Detailed Factory Information
        dto.setMoq(team.getMoq());
        dto.setLeadTime(team.getLeadTime());
        dto.setYearsInOperation(team.getYearsInOperation());
        dto.setStatusBadge(team.getStatusBadge());
        dto.setEmployeeCount(team.getEmployeeCount());
        dto.setFactorySize(team.getFactorySize());
        dto.setMetadata(team.getMetadata());
        dto.setRating(team.getRating());
        dto.setReviewCount(team.getReviewCount());

        List<TeamMember> members = teamMemberRepository.findByTeamId(team.getId());
        dto.setMemberCount(members.size());

        if (includeMembers) {
            dto.setMembers(members.stream().map(tm -> {
                TeamDTO.MemberInfo mi = new TeamDTO.MemberInfo();
                mi.setUserId(tm.getUser().getId());
                mi.setUsername(tm.getUser().getUsername());
                mi.setFullName(tm.getUser().getFullName());
                mi.setGroupRole(tm.getGroupRole().name());
                mi.setJoinedAt(tm.getJoinedAt().toString());
                mi.setJobLabels(tm.getJobLabels());

                // Task stats mặc định = 0, sẽ được tính riêng khi cần
                mi.setTotalTasks(0);
                mi.setCompletedTasks(0);
                mi.setCompletionRate(0);

                return mi;
            }).collect(Collectors.toList()));
        }

        return dto;
    }

    private void checkAdminRole(Team team, User requester) {
        TeamMember requesterMember = teamMemberRepository.findByTeamIdAndUserId(team.getId(), requester.getId())
                .orElseThrow(() -> new RuntimeException("Requester is not a member of the group"));
        if (requesterMember.getGroupRole() != GroupRole.ADMIN) {
            throw new RuntimeException("Only group ADMINs can perform this action");
        }
    }

    private void updateVerificationFields(Team team, TeamDTO dto) {
        if (dto.getBusinessLicense() != null)

```
