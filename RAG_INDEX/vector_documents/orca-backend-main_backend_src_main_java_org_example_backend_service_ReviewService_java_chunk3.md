# Knowledge Document: ReviewService.java (Chunk 4/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ReviewService.java",
  "language": "java",
  "module": "service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
e(r.getDeliverySchedule());
        dto.setCustomerSupport(r.getCustomerSupport());
        dto.setOverallRating(r.getOverallRating());
        dto.setComment(r.getComment());
        dto.setImages(r.getImages());
        dto.setDeliveryResult(r.getDeliveryResult());
        dto.setCreatedAt(r.getCreatedAt());
        if (r.getBuyerTeam() != null) dto.setBuyerTeamName(r.getBuyerTeam().getName());
        if (r.getBuyerUser() != null) {
            String name = r.getBuyerUser().getFullName();
            dto.setBuyerUserName(name != null && !name.isBlank() ? name : r.getBuyerUser().getUsername());
        }
        return dto;
    }
}

```
