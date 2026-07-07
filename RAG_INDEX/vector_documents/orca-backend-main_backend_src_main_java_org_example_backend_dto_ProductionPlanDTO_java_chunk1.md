# Knowledge Document: ProductionPlanDTO.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ProductionPlanDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
.totalRoastKg = totalRoastKg; }
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
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public List<DailyTargetDTO> getDailyTargets() { return dailyTargets; }
    public void setDailyTargets(List<DailyTargetDTO> dailyTargets) { this.dailyTargets = dailyTargets; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public LocalDateTime getApprovedAt() { return approvedAt; }
    public void setApprovedAt(LocalDateTime approvedAt) { this.approvedAt = approvedAt; }
    public String getApprovedBy() { return approvedBy; }
    public void setApprovedBy(String approvedBy) { this.approvedBy = approvedBy; }
}

```
