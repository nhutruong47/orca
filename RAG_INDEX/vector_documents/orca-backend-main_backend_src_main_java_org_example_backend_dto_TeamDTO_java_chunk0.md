# Knowledge Document: TeamDTO.java (Chunk 1/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/TeamDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "factory",
  "tags": [
    "factory",
    "admin",
    "employee"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, employee

## Source Code Chunk
```java
package org.example.backend.dto;

import java.util.List;
import java.util.UUID;
import com.fasterxml.jackson.annotation.JsonProperty;

public class TeamDTO {
    private UUID id;
    private String name;
    private String description;
    private UUID ownerId;
    private String ownerName;
    private int memberCount;
    private List<MemberInfo> members;
    private String createdAt;
    private String inviteCode;

    // Advertisement fields
    private boolean isPublished;
    private String specialty;
    private String capacity;
    private String region;
    private String factoryType;
    private Double capacityValue;
    private String capacityUnit;
    private String factoryImageUrl;
    private List<String> factoryImages;
    private String verificationStatus;
    private String businessLicense;
    private String businessAddress;
    private String websiteUrl;
    private String facebookUrl;
    private List<String> certificates;
    private String certificationDocument;
    private String verificationRejectReason;

    // Trust fields
    private int completedOrders;
    private int cancelledOrders;
    private int totalOrders;
    private int trustScore;

    // Additional Factory Info
    private String moq;
    private String leadTime;
    private Integer yearsInOperation;
    private String statusBadge;
    private Integer employeeCount;
    private String factorySize;
    private String metadata;
    private Double rating;
    private Integer reviewCount;

    public static class MemberInfo {
        private UUID userId;
        private String username;
        private String fullName;
        private String groupRole; // ADMIN / MEMBER
        private String joinedAt;
        private List<String> jobLabels;
        private int totalTasks;
        private int completedTasks;
        private int completionRate;

        public UUID getUserId() {
            return userId;
        }

        public void setUserId(UUID userId) {
            this.userId = userId;
        }

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public String getFullName() {
            return fullName;
        }

        public void setFullName(String fullName) {
            this.fullName = fullName;
        }


```
