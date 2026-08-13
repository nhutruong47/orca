package org.example.backend.service;

import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class AttendanceCalculatorTest {
    @Test
    void regularDaySubtractsConfiguredBreak() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 8, 0),
                LocalDateTime.of(2026, 8, 14, 17, 0), 60);
        assertEquals(new BigDecimal("8.00"), result.totalHours());
        assertEquals(new BigDecimal("8.00"), result.regularHours());
        assertEquals(new BigDecimal("0.00"), result.overtimeHours());
    }

    @Test
    void overtimeIsOnlyTimeBeyondEightPayableHours() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 8, 0),
                LocalDateTime.of(2026, 8, 14, 18, 30), 60);
        assertEquals(new BigDecimal("9.50"), result.totalHours());
        assertEquals(new BigDecimal("8.00"), result.regularHours());
        assertEquals(new BigDecimal("1.50"), result.overtimeHours());
    }

    @Test
    void overnightShiftCalculatesAcrossMidnight() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 22, 0),
                LocalDateTime.of(2026, 8, 15, 7, 0), 30);
        assertEquals(new BigDecimal("8.50"), result.totalHours());
        assertEquals(new BigDecimal("0.50"), result.overtimeHours());
    }

    @Test
    void checkoutBeforeCheckinIsRejected() {
        assertThrows(IllegalArgumentException.class, () -> AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 17, 0),
                LocalDateTime.of(2026, 8, 14, 8, 0), 60));
    }

    @Test
    void openAttendanceHasNoCalculatedHours() {
        var result = AttendanceCalculator.calculate(LocalDateTime.of(2026, 8, 14, 8, 0), null, 60);
        assertEquals(BigDecimal.ZERO, result.totalHours());
        assertEquals(BigDecimal.ZERO, result.overtimeHours());
    }
}
