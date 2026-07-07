# Knowledge Document: ProductionPlanService.java (Chunk 7/8)

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
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
     }
        sb.append("- Ngay bat dau: ").append(order.getProductionStartDate()).append("\n");
        sb.append("- Han noi bo: ").append(order.getInternalDeadline()).append("\n");
        return sb.toString();
    }

    private int parsePackageSize(String packageSize) {
        try {
            if (packageSize == null) return 1;
            String num = packageSize.replaceAll("[^0-9]", "");
            return num.isEmpty() ? 1 : Integer.parseInt(num);
        } catch (Exception e) {
            return 1;
        }
    }

    private ProductionPlanDTO toPlanDTO(ProductionPlan p) {
        ProductionPlanDTO dto = new ProductionPlanDTO();
        dto.setId(p.getId().toString());
        dto.setOrderId(p.getOrder().getId().toString());
        dto.setOrderTitle(p.getOrder().getTitle());
        dto.setPlanCode(p.getPlanCode());
        dto.setTotalDays(p.getTotalDays());
        dto.setTotalWorkingDays(p.getTotalWorkingDays());
        dto.setDailyTargetKg(p.getDailyTargetKg());
        dto.setTotalInputKg(p.getTotalInputKg());
        dto.setTotalRoastKg(p.getTotalRoastKg());
        dto.setTotalQcKg(p.getTotalQcKg());
        dto.setTotalPackagedKg(p.getTotalPackagedKg());
        dto.setTotalPackages(p.getTotalPackages());
        dto.setAiRecommendations(p.getAiRecommendations());
        dto.setRiskFactors(p.getRiskFactors());
        dto.setStatus(p.getStatus().name());
        dto.setCreatedAt(p.getCreatedAt());
        dto.setApprovedAt(p.getApprovedAt());
        if (p.getDailyTargets() != null) {
            dto.setDailyTargets(p.getDailyTargets().stream()
                    .map(this::toTargetDTO)
                    .collect(Collectors.toList()));
        }
        return dto;
    }

    private DailyTargetDTO toTargetDTO(DailyTarget t) {
        DailyTargetDTO dto = new DailyTargetDTO();
        dto.setId(t.getId().toString());
        dto.setPlanId(t.getPlan().getId().toString());
        dto.setOrderId(t.getOrder().getId().toString());
        dto.setOrderTitle(t.getOrder().getTitle());
        dto.setTargetDate(t.getTargetDate());
        dto.setTargetQuantityKg(t.getTargetQuantityKg());
        dto.setTargetRoastKg(t.getTargetRoastKg());
        dto.setTargetQcKg(t.getTargetQcKg());
        dto.setTargetPackagedKg(t.getTargetPackagedKg());
        dto.setTargetPackages(t.getTargetPackages());

```
