# Knowledge Document: AttendanceRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/AttendanceRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.Attendance;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface AttendanceRepository extends JpaRepository<Attendance, UUID> {
    Optional<Attendance> findByUserIdAndTeamIdAndDate(UUID userId, UUID teamId, LocalDate date);
    List<Attendance> findByTeamId(UUID teamId);
    List<Attendance> findByTeamIdAndDateBetween(UUID teamId, LocalDate startDate, LocalDate endDate);
    List<Attendance> findByUserIdAndTeamId(UUID userId, UUID teamId);

    @Query("SELECT a FROM Attendance a WHERE a.team.id = :teamId AND a.date = :date")
    List<Attendance> findByTeamIdAndDate(@Param("teamId") UUID teamId, @Param("date") LocalDate date);

    @Query("SELECT a FROM Attendance a WHERE a.productionOrder.id = :orderId AND a.date >= :fromDate")
    List<Attendance> findByOrderIdAndDateAfter(@Param("orderId") UUID orderId, @Param("fromDate") LocalDate fromDate);

    @Query("SELECT a FROM Attendance a WHERE a.productionOrder.id = :orderId")
    List<Attendance> findByOrderId(@Param("orderId") UUID orderId);

    @Query("SELECT SUM(a.regularHours + a.overtimeHours) FROM Attendance a " +
           "WHERE a.team.id = :teamId AND a.date = :date AND a.checkOutTime IS NOT NULL")
    Double sumWorkerHoursByTeamAndDate(@Param("teamId") UUID teamId, @Param("date") LocalDate date);

    @Query("SELECT COUNT(a) FROM Attendance a WHERE a.team.id = :teamId AND a.date = :date AND a.checkOutTime IS NULL")
    long countNotCheckedOut(@Param("teamId") UUID teamId, @Param("date") LocalDate date);
}

```
