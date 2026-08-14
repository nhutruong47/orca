package org.example.backend.service;

import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.time.LocalTime;

import static org.junit.jupiter.api.Assertions.*;

class AttendanceCalculatorTest {
    @Test
    void configuredDayCapsRegularHours() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 9, 0),
                LocalDateTime.of(2026, 8, 14, 17, 30),
                LocalTime.of(17, 30), new BigDecimal("7.50"));
        assertEquals(new BigDecimal("7.50"), result.totalHours());
        assertEquals(new BigDecimal("7.50"), result.regularHours());
        assertEquals(new BigDecimal("0.00"), result.overtimeHours());
    }

    @Test
    void overtimeStartsAfterConfiguredEndTime() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 9, 0),
                LocalDateTime.of(2026, 8, 14, 19, 30),
                LocalTime.of(17, 30), new BigDecimal("7.50"));
        assertEquals(new BigDecimal("9.50"), result.totalHours());
        assertEquals(new BigDecimal("7.50"), result.regularHours());
        assertEquals(new BigDecimal("2.00"), result.overtimeHours());
    }

    @Test
    void oneHourAfterShiftEndIsOneHourOvertime() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 9, 0),
                LocalDateTime.of(2026, 8, 14, 18, 30),
                LocalTime.of(17, 30), new BigDecimal("7.50"));
        assertEquals(new BigDecimal("8.50"), result.totalHours());
        assertEquals(new BigDecimal("7.50"), result.regularHours());
        assertEquals(new BigDecimal("1.00"), result.overtimeHours());
    }

    @Test
    void lateArrivalStillUsesElapsedTimeUpToStandardCap() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 10, 0),
                LocalDateTime.of(2026, 8, 14, 17, 30),
                LocalTime.of(17, 30), new BigDecimal("7.50"));
        assertEquals(new BigDecimal("7.50"), result.regularHours());
        assertEquals(new BigDecimal("0.00"), result.overtimeHours());
    }

    @Test
    void earlyCheckoutUsesActualElapsedTime() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 9, 0),
                LocalDateTime.of(2026, 8, 14, 16, 0),
                LocalTime.of(17, 30), new BigDecimal("7.50"));
        assertEquals(new BigDecimal("7.00"), result.regularHours());
        assertEquals(new BigDecimal("0.00"), result.overtimeHours());
    }

    @Test
    void checkoutBeforeCheckinIsRejected() {
        assertThrows(IllegalArgumentException.class, () -> AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 17, 0),
                LocalDateTime.of(2026, 8, 14, 8, 0),
                LocalTime.of(17, 30), new BigDecimal("7.50")));
    }

    @Test
    void openAttendanceHasNoCalculatedHours() {
        var result = AttendanceCalculator.calculate(
                LocalDateTime.of(2026, 8, 14, 8, 0), null,
                LocalTime.of(17, 30), new BigDecimal("7.50"));
        assertEquals(BigDecimal.ZERO, result.totalHours());
        assertEquals(BigDecimal.ZERO, result.overtimeHours());
    }

    @Test
    void legacyRecordStillSubtractsItsStoredBreak() {
        var result = AttendanceCalculator.calculateLegacy(
                LocalDateTime.of(2026, 8, 7, 6, 0),
                LocalDateTime.of(2026, 8, 7, 14, 0), 30);
        assertEquals(new BigDecimal("7.50"), result.totalHours());
        assertEquals(new BigDecimal("7.50"), result.regularHours());
        assertEquals(new BigDecimal("0.00"), result.overtimeHours());
    }
}
