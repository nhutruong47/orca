# Knowledge Document: AccessControlService.java (Chunk 5/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AccessControlService.java",
  "language": "java",
  "module": "service",
  "business_domain": "admin",
  "tags": [
    "admin",
    "workspace",
    "production",
    "attendance",
    "inventory",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, workspace, production, attendance, inventory, security

## Source Code Chunk
```java
(attendanceId)
                .orElseThrow(() -> new RuntimeException("Attendance record not found"));
        requireSelfOrTeamAdmin(user, attendance.getUser().getId(), attendance.getTeam().getId());
    }

    public void requireInterGroupOrderAccess(User user, InterGroupOrder order) {
        UUID userId = requireUserId(user);
        if (isSystemAdmin(userId)) {
            return;
        }
        boolean buyerUser = order.getBuyerUser() != null && order.getBuyerUser().getId().equals(userId);
        boolean buyerTeamMember = order.getBuyerTeam() != null
                && teamMemberRepository.existsByTeamIdAndUserId(order.getBuyerTeam().getId(), userId);
        boolean sellerTeamMember = order.getSellerTeam() != null
                && teamMemberRepository.existsByTeamIdAndUserId(order.getSellerTeam().getId(), userId);
        if (!buyerUser && !buyerTeamMember && !sellerTeamMember) {
            throw forbidden();
        }
    }

    private UUID requireUserId(User user) {
        if (user == null || user.getId() == null) {
            throw forbidden();
        }
        return user.getId();
    }

    private boolean isSystemAdmin(UUID userId) {
        return userRepository.findById(userId)
                .map(User::getRole)
                .filter(Role.ADMIN::equals)
                .isPresent();
    }

    private RuntimeException forbidden() {
        return new org.springframework.web.server.ResponseStatusException(org.springframework.http.HttpStatus.FORBIDDEN, "Forbidden");
    }
}

```
