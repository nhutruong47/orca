# Knowledge Document: TaskDTO.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/TaskDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
backupMemberName = backupMemberName; }

    public String getSupervisorId() { return supervisorId; }
    public void setSupervisorId(String supervisorId) { this.supervisorId = supervisorId; }

    public String getSupervisorName() { return supervisorName; }
    public void setSupervisorName(String supervisorName) { this.supervisorName = supervisorName; }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public String getAcceptanceStatus() { return acceptanceStatus; }
    public void setAcceptanceStatus(String acceptanceStatus) { this.acceptanceStatus = acceptanceStatus; }

    public Double getHourlyRate() { return hourlyRate; }
    public void setHourlyRate(Double hourlyRate) { this.hourlyRate = hourlyRate; }

    public String getTeamId() { return teamId; }
    public void setTeamId(String teamId) { this.teamId = teamId; }
}

```
