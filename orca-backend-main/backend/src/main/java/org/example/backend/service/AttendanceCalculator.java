package org.example.backend.service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.LocalTime;

/** Pure attendance calculation rules. Timestamps are the source of truth. */
public final class AttendanceCalculator {
    private AttendanceCalculator() {}

    public static Result calculate(LocalDateTime checkIn, LocalDateTime checkOut,
                                   LocalTime scheduledEnd, BigDecimal standardHours) {
        if (checkIn == null || checkOut == null) {
            return new Result(BigDecimal.ZERO, BigDecimal.ZERO, BigDecimal.ZERO);
        }
        if (scheduledEnd == null || standardHours == null || standardHours.signum() <= 0) {
            throw new IllegalArgumentException("Cấu hình chấm công không hợp lệ");
        }
        if (!checkOut.isAfter(checkIn)) {
            throw new IllegalArgumentException("Giờ ra phải sau giờ vào");
        }
        long elapsedMinutes = Duration.between(checkIn, checkOut).toMinutes();
        
        long standardMinutes = standardHours.multiply(BigDecimal.valueOf(60)).longValue();
        
        long regularMinutes = Math.min(elapsedMinutes, standardMinutes);
        long overtimeMinutes = Math.max(elapsedMinutes - standardMinutes, 0);

        BigDecimal regular = BigDecimal.valueOf(regularMinutes)
                .divide(BigDecimal.valueOf(60), 2, RoundingMode.HALF_UP);
        BigDecimal overtime = BigDecimal.valueOf(overtimeMinutes)
                .divide(BigDecimal.valueOf(60), 2, RoundingMode.HALF_UP);
        BigDecimal total = regular.add(overtime).setScale(2, RoundingMode.HALF_UP);
        return new Result(total, regular, overtime);
    }

    /** Keeps corrections to pre-settings attendance records compatible with their original calculation. */
    public static Result calculateLegacy(LocalDateTime checkIn, LocalDateTime checkOut, int breakMinutes) {
        if (checkIn == null || checkOut == null) {
            return new Result(BigDecimal.ZERO, BigDecimal.ZERO, BigDecimal.ZERO);
        }
        if (!checkOut.isAfter(checkIn)) {
            throw new IllegalArgumentException("Giờ ra phải sau giờ vào");
        }
        long elapsedMinutes = Duration.between(checkIn, checkOut).toMinutes();
        long payableMinutes = Math.max(0, elapsedMinutes - Math.max(0, breakMinutes));
        BigDecimal total = BigDecimal.valueOf(payableMinutes)
                .divide(BigDecimal.valueOf(60), 2, RoundingMode.HALF_UP);
        BigDecimal regular = total.min(new BigDecimal("8.00"));
        BigDecimal overtime = total.subtract(regular).max(BigDecimal.ZERO);
        return new Result(total, regular, overtime);
    }

    public record Result(BigDecimal totalHours, BigDecimal regularHours, BigDecimal overtimeHours) {}
}
