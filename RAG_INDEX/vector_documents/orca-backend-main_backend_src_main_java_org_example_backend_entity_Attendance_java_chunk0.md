# Knowledge Document: Attendance.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "attendances")
public class Attendance {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "team_id", nullable = false)
    private Team team;

    @Column(name = "attendance_date", nullable = false)
    private LocalDate date;

    @Enumerated(EnumType.STRING)
    @Column(name = "shift_type", length = 20)
    private ShiftType shiftType;

    @Column(name = "shift_start_time")
    private String shiftStartTime;

    @Column(name = "shift_end_time")
    private String shiftEndTime;

    @Column(name = "check_in_time")
    private LocalDateTime checkInTime;

    @Column(name = "check_out_time")
    private LocalDateTime checkOutTime;

    @Enumerated(EnumType.STRING)
    @Column(name = "production_stage", length = 50)
    private ProductionStage stage;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "production_order_id")
    private ProductionOrder productionOrder;

    @Column(name = "break_minutes")
    private Integer breakMinutes = 30;

    @Column(name = "actual_work_hours")
    private Double actualWorkHours;

    @Column(name = "regular_hours")
    private Double regularHours = 0.0;

    @Column(name = "overtime_hours")
    private Double overtimeHours = 0.0;

    @Enumerated(EnumType.STRING)
    @Column(name = "attendance_status", length = 20)
    private AttendanceStatus attendanceStatus = AttendanceStatus.ON_TIME;

    @Column(columnDefinition = "TEXT")
    private String notes;

    public enum ShiftType {
        SANG,    // Ca sang: 6:00 - 14:00
        CHIEU,   // Ca chieu: 14:00 - 22:00
        DEM,     // Ca dem: 22:00 - 6:00
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

```
