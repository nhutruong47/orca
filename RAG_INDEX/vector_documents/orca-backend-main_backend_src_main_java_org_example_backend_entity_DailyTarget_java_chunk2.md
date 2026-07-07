# Knowledge Document: DailyTarget.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/DailyTarget.java",
  "language": "java",
  "module": "entity",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
actualQcFailKg) { this.actualQcFailKg = actualQcFailKg; }
    public Double getActualPackagedKg() { return actualPackagedKg; }
    public void setActualPackagedKg(Double actualPackagedKg) { this.actualPackagedKg = actualPackagedKg; }
    public Integer getActualPackages() { return actualPackages; }
    public void setActualPackages(Integer actualPackages) { this.actualPackages = actualPackages; }
    public Double getTotalActualKg() { return totalActualKg; }
    public void setTotalActualKg(Double totalActualKg) { this.totalActualKg = totalActualKg; }
    public Double getCompletionRate() { return completionRate; }
    public void setCompletionRate(Double completionRate) { this.completionRate = completionRate; }
    public Boolean getIsHoliday() { return isHoliday; }
    public void setIsHoliday(Boolean isHoliday) { this.isHoliday = isHoliday; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
    public String getIssues() { return issues; }
    public void setIssues(String issues) { this.issues = issues; }
    public TargetStatus getStatus() { return status; }
    public void setStatus(TargetStatus status) { this.status = status; }
    public Double getTotalWorkerHours() { return totalWorkerHours; }
    public void setTotalWorkerHours(Double totalWorkerHours) { this.totalWorkerHours = totalWorkerHours; }
    public Double getProductivityKgPerHour() { return productivityKgPerHour; }
    public void setProductivityKgPerHour(Double productivityKgPerHour) { this.productivityKgPerHour = productivityKgPerHour; }

    public void calculateCompletionRate() {
        if (targetQuantityKg != null && targetQuantityKg > 0) {
            double actual = totalActualKg != null ? totalActualKg : 0;
            this.completionRate = Math.round((actual / targetQuantityKg) * 1000.0) / 10.0;
        }
    }

    public void calculateProductivity() {
        if (totalActualKg != null && totalWorkerHours != null && totalWorkerHours > 0) {
            this.productivityKgPerHour = Math.round((totalActualKg / totalWorkerHours) * 100.0) / 100.0;
        }
    }
}

```
