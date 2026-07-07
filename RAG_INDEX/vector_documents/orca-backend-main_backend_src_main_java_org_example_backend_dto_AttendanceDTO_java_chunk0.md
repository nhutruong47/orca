# Knowledge Document: AttendanceDTO.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/AttendanceDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class AttendanceDTO {
    private String id;
    private String userId;
    private String userName;
    private String teamId;
    private LocalDate date;
    private String shiftType;
    private String shiftStartTime;
    private String shiftEndTime;
    private LocalDateTime checkInTime;
    private LocalDateTime checkOutTime;
    private String productionStage;
    private String orderId;
    private String orderTitle;
    private Integer breakMinutes;
    private Double actualWorkHours;
    private Double regularHours;
    private Double overtimeHours;
    private String attendanceStatus;
    private String notes;

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getUserId() { return userId; }
    public void setUserId(String userId) { this.userId = userId; }
    public String getUserName() { return userName; }
    public void setUserName(String userName) { this.userName = userName; }
    public String getTeamId() { return teamId; }
    public void setTeamId(String teamId) { this.teamId = teamId; }
    public LocalDate getDate() { return date; }
    public void setDate(LocalDate date) { this.date = date; }
    public String getShiftType() { return shiftType; }
    public void setShiftType(String shiftType) { this.shiftType = shiftType; }
    public String getShiftStartTime() { return shiftStartTime; }
    public void setShiftStartTime(String shiftStartTime) { this.shiftStartTime = shiftStartTime; }
    public String getShiftEndTime() { return shiftEndTime; }
    public void setShiftEndTime(String shiftEndTime) { this.shiftEndTime = shiftEndTime; }
    public LocalDateTime getCheckInTime() { return checkInTime; }
    public void setCheckInTime(LocalDateTime checkInTime) { this.checkInTime = checkInTime; }
    public LocalDateTime getCheckOutTime() { return checkOutTime; }
    public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }
    public String getProductionStage() { return productionStage; }
    public void setProductionStage(String productionStage) { this.productionStage = productionStage; }
    public String getOrderId() { return orderId; }
    public void setOrderId(String orderId) { this.orderId = orderId; }

```
