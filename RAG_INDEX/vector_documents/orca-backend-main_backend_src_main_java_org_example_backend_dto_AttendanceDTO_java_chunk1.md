# Knowledge Document: AttendanceDTO.java (Chunk 2/2)

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
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
utTime; }
    public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }
    public String getProductionStage() { return productionStage; }
    public void setProductionStage(String productionStage) { this.productionStage = productionStage; }
    public String getOrderId() { return orderId; }
    public void setOrderId(String orderId) { this.orderId = orderId; }
    public String getOrderTitle() { return orderTitle; }
    public void setOrderTitle(String orderTitle) { this.orderTitle = orderTitle; }
    public Integer getBreakMinutes() { return breakMinutes; }
    public void setBreakMinutes(Integer breakMinutes) { this.breakMinutes = breakMinutes; }
    public Double getActualWorkHours() { return actualWorkHours; }
    public void setActualWorkHours(Double actualWorkHours) { this.actualWorkHours = actualWorkHours; }
    public Double getRegularHours() { return regularHours; }
    public void setRegularHours(Double regularHours) { this.regularHours = regularHours; }
    public Double getOvertimeHours() { return overtimeHours; }
    public void setOvertimeHours(Double overtimeHours) { this.overtimeHours = overtimeHours; }
    public String getAttendanceStatus() { return attendanceStatus; }
    public void setAttendanceStatus(String attendanceStatus) { this.attendanceStatus = attendanceStatus; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
}

```
