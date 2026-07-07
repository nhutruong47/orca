# Knowledge Document: ProductionPlan.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/ProductionPlan.java",
  "language": "java",
  "module": "entity",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
his.createdAt = LocalDateTime.now();
        if (this.planCode == null || this.planCode.isBlank()) {
            this.planCode = "PLAN-" + System.currentTimeMillis();
        }
    }

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public ProductionOrder getOrder() { return order; }
    public void setOrder(ProductionOrder order) { this.order = order; }
    public String getPlanCode() { return planCode; }
    public void setPlanCode(String planCode) { this.planCode = planCode; }
    public Integer getTotalDays() { return totalDays; }
    public void setTotalDays(Integer totalDays) { this.totalDays = totalDays; }
    public Integer getTotalWorkingDays() { return totalWorkingDays; }
    public void setTotalWorkingDays(Integer totalWorkingDays) { this.totalWorkingDays = totalWorkingDays; }
    public Double getDailyTargetKg() { return dailyTargetKg; }
    public void setDailyTargetKg(Double dailyTargetKg) { this.dailyTargetKg = dailyTargetKg; }
    public Double getTotalInputKg() { return totalInputKg; }
    public void setTotalInputKg(Double totalInputKg) { this.totalInputKg = totalInputKg; }
    public Double getTotalRoastKg() { return totalRoastKg; }
    public void setTotalRoastKg(Double totalRoastKg) { this.totalRoastKg = totalRoastKg; }
    public Double getTotalQcKg() { return totalQcKg; }
    public void setTotalQcKg(Double totalQcKg) { this.totalQcKg = totalQcKg; }
    public Double getTotalPackagedKg() { return totalPackagedKg; }
    public void setTotalPackagedKg(Double totalPackagedKg) { this.totalPackagedKg = totalPackagedKg; }
    public Integer getTotalPackages() { return totalPackages; }
    public void setTotalPackages(Integer totalPackages) { this.totalPackages = totalPackages; }
    public String getAiRecommendations() { return aiRecommendations; }
    public void setAiRecommendations(String aiRecommendations) { this.aiRecommendations = aiRecommendations; }
    public String getRiskFactors() { return riskFactors; }
    public void setRiskFactors(String riskFactors) { this.riskFactors = riskFactors; }
    public PlanStatus getStatus() { return status; }
    public void setStatus(PlanStatus status) { this.status = status; }
    public List<DailyTarget> getDailyTargets() { return dailyTargets; }
    public void setDailyTargets(List<DailyTarget> dailyTargets) { this.dailyTargets = dailyTargets; }

```
