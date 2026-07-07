# Knowledge Document: ManufacturingRequestService.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ManufacturingRequestService.java",
  "language": "java",
  "module": "service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
    ManufacturingRequestDTO dto = new ManufacturingRequestDTO();
        dto.setId(req.getId().toString());
        dto.setType(req.getType());
        dto.setTitle(req.getTitle());
        dto.setCoffeeType(req.getCoffeeType());
        dto.setQuantity(req.getQuantity());
        dto.setDeadline(req.getDeadline());
        dto.setRegion(req.getRegion());
        dto.setDetails(req.getDetails());
        dto.setCreatedAt(req.getCreatedAt() != null ? req.getCreatedAt().toString() : null);
        if (req.getBuyerTeam() != null) {
            dto.setBuyerTeamId(req.getBuyerTeam().getId().toString());
        }
        return dto;
    }
}

```
