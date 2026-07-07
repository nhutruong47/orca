# Knowledge Document: AdminService.java (Chunk 12/16)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AdminService.java",
  "language": "java",
  "module": "service",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "admin",
    "production",
    "factory",
    "payment",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 11,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
groupingBy(
                        item -> safeText(statusGetter.apply(item), "UNKNOWN"),
                        LinkedHashMap::new,
                        Collectors.counting()));
    }

    private Map<String, Object> toUserMap(User user) {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", user.getId().toString());
        map.put("username", user.getUsername());
        map.put("fullName", safeText(user.getFullName(), ""));
        map.put("email", safeText(user.getEmail(), ""));
        boolean isOwner = !teamRepository.findByOwnerId(user.getId()).isEmpty();
        String displayRole = user.getRole().name().equals("ADMIN") ? "ADMIN" : (isOwner ? "FACTORY_OWNER" : "MEMBER");
        map.put("role", displayRole);
        map.put("chipId", safeText(user.getChipId(), ""));
        map.put("aiPlan", safeText(user.getAiPlan(), "free"));
        map.put("status", user.isLocked() ? "Locked" : "Active");
        map.put("aiPlanExpiresAt", user.getAiPlanExpiresAt() != null ? user.getAiPlanExpiresAt().toString() : null);
        map.put("createdAt", user.getCreatedAt() != null ? user.getCreatedAt().toString() : null);
        return map;
    }

    private Map<String, Object> toTeamMap(Team team) {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", team.getId().toString());
        map.put("name", team.getName());
        map.put("description", safeText(team.getDescription(), ""));
        map.put("ownerId", team.getOwner() != null ? team.getOwner().getId().toString() : "");
        map.put("ownerName", team.getOwner() != null ? team.getOwner().getUsername() : "");
        
        int dbCount = teamMemberRepository.findByTeamId(team.getId()).size();
        map.put("memberCount", dbCount > 0 ? dbCount : 1);
        
        map.put("createdAt", team.getCreatedAt() != null ? team.getCreatedAt().toString() : null);
        map.put("published", team.isPublished());
        map.put("specialty", safeText(team.getSpecialty(), ""));
        map.put("capacity", safeText(team.getCapacity(), ""));
        map.put("region", safeText(team.getRegion(), ""));
        map.put("factoryType", safeText(team.getFactoryType(), ""));
        map.put("capacityValue", team.getCapacityValue());
        map.put("capacityUnit", safeText(team.getCapacityUnit(), ""));

```
