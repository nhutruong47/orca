# Knowledge Document: ReplanDTO.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ReplanDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
   public String getReplanStrategy() { return replanStrategy; }
    public void setReplanStrategy(String replanStrategy) { this.replanStrategy = replanStrategy; }
    public List<String> getRecommendations() { return recommendations; }
    public void setRecommendations(List<String> recommendations) { this.recommendations = recommendations; }
    public String getRiskLevel() { return riskLevel; }
    public void setRiskLevel(String riskLevel) { this.riskLevel = riskLevel; }
    public boolean isNeedsReplan() { return needsReplan; }
    public void setNeedsReplan(boolean needsReplan) { this.needsReplan = needsReplan; }
}

```
