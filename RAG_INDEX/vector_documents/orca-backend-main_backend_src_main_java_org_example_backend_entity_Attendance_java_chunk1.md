# Knowledge Document: Attendance.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/Attendance.java",
  "language": "java",
  "module": "entity",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```java
     // Ca dem: 22:00 - 6:00
        NGAY     // Lam ca ngay: 6:00 - 18:00
    }

    public enum ProductionStage {
        RANH_VA_CHON,  // Rang va chon
        RANG,           // Rang
        XAY,            // Xay
        DONG_GOI,       // Dong goi
        QA              // Kiem tra chat luong
    }

    public enum AttendanceStatus {
        ON_TIME,
        LATE,
        MISSING_CHECKOUT,
        ABSENT
    }

    public Attendance() {}

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public User getUser() { return user; }
    public void setUser(User user) { this.user = user; }
    public Team getTeam() { return team; }
    public void setTeam(Team team) { this.team = team; }
    public LocalDate getDate() { return date; }
    public void setDate(LocalDate date) { this.date = date; }
    public ShiftType getShiftType() { return shiftType; }
    public void setShiftType(ShiftType shiftType) { this.shiftType = shiftType; }
    public String getShiftStartTime() { return shiftStartTime; }
    public void setShiftStartTime(String shiftStartTime) { this.shiftStartTime = shiftStartTime; }
    public String getShiftEndTime() { return shiftEndTime; }
    public void setShiftEndTime(String shiftEndTime) { this.shiftEndTime = shiftEndTime; }
    public LocalDateTime getCheckInTime() { return checkInTime; }
    public void setCheckInTime(LocalDateTime checkInTime) { this.checkInTime = checkInTime; }
    public LocalDateTime getCheckOutTime() { return checkOutTime; }
    public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }
    public ProductionStage getStage() { return stage; }
    public void setStage(ProductionStage stage) { this.stage = stage; }
    public ProductionOrder getProductionOrder() { return productionOrder; }
    public void setProductionOrder(ProductionOrder productionOrder) { this.productionOrder = productionOrder; }
    public Integer getBreakMinutes() { return breakMinutes; }
    public void setBreakMinutes(Integer breakMinutes) { this.breakMinutes = breakMinutes; }
    public Double getActualWorkHours() { return actualWorkHours; }
    public void setActualWorkHours(Double actualWorkHours) { this.actualWorkHours = actualWorkHours; }
    public Double getRegularHours() { return regularHours; }

```
