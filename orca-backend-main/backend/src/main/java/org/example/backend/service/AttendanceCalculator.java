package org.example.backend.service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.Duration;
import java.time.LocalDateTime;

/** Pure attendance calculation rules. Timestamps are the source of truth. */
public final class AttendanceCalculator {
    public static final BigDecimal REGULAR_HOURS_PER_DAY = new BigDecimal("8.00");

    private AttendanceCalculator() {}

    public static Result calculate(LocalDateTime checkIn, LocalDateTime checkOut, int breakMinutes) {
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
        BigDecimal regular = total.min(REGULAR_HOURS_PER_DAY);
        BigDecimal overtime = total.subtract(regular).max(BigDecimal.ZERO);
        return new Result(total, regular, overtime);
    }

    public record Result(BigDecimal totalHours, BigDecimal regularHours, BigDecimal overtimeHours) {}
}
