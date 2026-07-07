# Knowledge Document: UpdateAttendanceRequest.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/UpdateAttendanceRequest.java",
  "language": "java",
  "module": "dto",
  "business_domain": "attendance",
  "tags": [
    "attendance"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;

public class UpdateAttendanceRequest {
    private LocalDateTime checkInTime;
    private LocalDateTime checkOutTime;

    public LocalDateTime getCheckInTime() {
        return checkInTime;
    }

    public void setCheckInTime(LocalDateTime checkInTime) {
        this.checkInTime = checkInTime;
    }

    public LocalDateTime getCheckOutTime() {
        return checkOutTime;
    }

    public void setCheckOutTime(LocalDateTime checkOutTime) {
        this.checkOutTime = checkOutTime;
    }
}

```
