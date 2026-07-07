# Knowledge Document: ProductionPlanService.java (Chunk 8/8)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionPlanService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 7,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
t.getOrder().getId().toString());
        dto.setOrderTitle(t.getOrder().getTitle());
        dto.setTargetDate(t.getTargetDate());
        dto.setTargetQuantityKg(t.getTargetQuantityKg());
        dto.setTargetRoastKg(t.getTargetRoastKg());
        dto.setTargetQcKg(t.getTargetQcKg());
        dto.setTargetPackagedKg(t.getTargetPackagedKg());
        dto.setTargetPackages(t.getTargetPackages());
        dto.setActualRoastKg(t.getActualRoastKg());
        dto.setActualQcKg(t.getActualQcKg());
        dto.setActualQcFailKg(t.getActualQcFailKg());
        dto.setActualPackagedKg(t.getActualPackagedKg());
        dto.setActualPackages(t.getActualPackages());
        dto.setTotalActualKg(t.getTotalActualKg());
        dto.setCompletionRate(t.getCompletionRate());
        dto.setIsHoliday(t.getIsHoliday());
        dto.setNotes(t.getNotes());
        dto.setIssues(t.getIssues());
        dto.setStatus(t.getStatus().name());
        dto.setTotalWorkerHours(t.getTotalWorkerHours());
        dto.setProductivityKgPerHour(t.getProductivityKgPerHour());
        return dto;
    }
}

```
