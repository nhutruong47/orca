# Knowledge Document: AdminService.java (Chunk 13/16)

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
  "chunk_index": 12,
  "total_chunks": 16
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, admin, production, factory, payment, security

## Source Code Chunk
```java
Published());
        map.put("specialty", safeText(team.getSpecialty(), ""));
        map.put("capacity", safeText(team.getCapacity(), ""));
        map.put("region", safeText(team.getRegion(), ""));
        map.put("factoryType", safeText(team.getFactoryType(), ""));
        map.put("capacityValue", team.getCapacityValue());
        map.put("capacityUnit", safeText(team.getCapacityUnit(), ""));
        map.put("factoryImageUrl", safeText(team.getFactoryImageUrl(), ""));
        map.put("factoryImages", splitList(team.getFactoryImages()));
        map.put("verificationStatus", safeText(team.getVerificationStatus(), "NOT_SUBMITTED"));
        map.put("businessLicense", safeText(team.getBusinessLicense(), ""));
        map.put("businessAddress", safeText(team.getBusinessAddress(), ""));
        map.put("websiteUrl", safeText(team.getWebsiteUrl(), ""));
        map.put("facebookUrl", safeText(team.getFacebookUrl(), ""));
        map.put("certificates", splitList(team.getCertificates()));
        map.put("certificationDocument", safeText(team.getCertificationDocument(), ""));
        map.put("verificationRejectReason", safeText(team.getVerificationRejectReason(), ""));
        map.put("completedOrders", team.getCompletedOrders());
        map.put("cancelledOrders", team.getCancelledOrders());
        map.put("totalOrders", team.getTotalOrders());
        map.put("trustScore", team.getTotalOrders() > 0
                ? (int) ((double) team.getCompletedOrders() / team.getTotalOrders() * 100)
                : 0);
        return map;
    }

    private Map<String, Object> toOrderMap(InterGroupOrder order) {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", order.getId().toString());
        map.put("title", order.getTitle());
        map.put("description", safeText(order.getDescription(), ""));
        map.put("buyerTeamId", order.getBuyerTeam() != null ? order.getBuyerTeam().getId().toString() : "");
        String buyerUserName = order.getBuyerUser() != null
                ? safeText(order.getBuyerUser().getFullName(), order.getBuyerUser().getUsername())
                : "";
        map.put("buyerTeamName", order.getBuyerTeam() != null ? order.getBuyerTeam().getName() : buyerUserName);
        map.put("buyerUserId", order.getBuyerUser() != null ? order.getBuyerUser().getId().toString() : "");

```
