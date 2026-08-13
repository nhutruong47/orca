package org.example.backend.repository;

import org.example.backend.entity.PayrollAttendanceLine;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.UUID;

public interface PayrollAttendanceLineRepository extends JpaRepository<PayrollAttendanceLine, UUID> {
    List<PayrollAttendanceLine> findByPayrollItemIdOrderByAttendanceDateAscCheckInTimeAsc(UUID payrollItemId);
    List<PayrollAttendanceLine> findByPayrollItemId(UUID payrollItemId);
}
