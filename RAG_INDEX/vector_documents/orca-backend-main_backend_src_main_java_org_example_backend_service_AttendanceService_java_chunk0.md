# Knowledge Document: AttendanceService.java (Chunk 1/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AttendanceService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.AttendanceDTO;
import org.example.backend.dto.UpdateAttendanceRequest;
import org.example.backend.entity.Attendance;
import org.example.backend.entity.Attendance.ShiftType;
import org.example.backend.entity.ProductionOrder;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.AttendanceRepository;
import org.example.backend.repository.ProductionOrderRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class AttendanceService {

    private final AttendanceRepository attendanceRepo;
    private final UserRepository userRepo;
    private final TeamRepository teamRepo;
    private final ProductionOrderRepository orderRepo;

    private static final Map<ShiftType, String[]> SHIFT_HOURS = Map.of(
        ShiftType.SANG, new String[]{"06:00", "14:00"},
        ShiftType.CHIEU, new String[]{"14:00", "22:00"},
        ShiftType.DEM, new String[]{"22:00", "06:00"},
        ShiftType.NGAY, new String[]{"06:00", "18:00"}
    );

    public AttendanceService(AttendanceRepository attendanceRepo, UserRepository userRepo,
                            TeamRepository teamRepo, ProductionOrderRepository orderRepo) {
        this.attendanceRepo = attendanceRepo;
        this.userRepo = userRepo;
        this.teamRepo = teamRepo;
        this.orderRepo = orderRepo;
    }

    public AttendanceDTO checkIn(UUID userId, UUID teamId, ShiftType shiftType,
                                 Attendance.ProductionStage stage, UUID orderId, Integer breakMinutes) {
        LocalDate today = LocalDate.now();
        Optional<Attendance> existing = attendanceRepo.findByUserIdAndTeamIdAndDate(userId, teamId, today);
        if (existing.isPresent()) {
            throw new RuntimeException("Ban da check-in hom nay roi");
        }

        User user = userRepo.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));
        Team team = teamRepo.findById(teamId)

```
