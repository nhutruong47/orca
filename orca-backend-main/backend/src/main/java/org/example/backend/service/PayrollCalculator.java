package org.example.backend.service;

import java.math.BigDecimal;
import java.math.RoundingMode;

public final class PayrollCalculator {
    private PayrollCalculator() {}

    public static long multiply(BigDecimal hours, long hourlyRateVnd, BigDecimal multiplier) {
        if (hours == null || hourlyRateVnd <= 0 || multiplier == null) return 0L;
        return hours.multiply(BigDecimal.valueOf(hourlyRateVnd))
                .multiply(multiplier)
                .setScale(0, RoundingMode.HALF_UP)
                .longValueExact();
    }

    public static long net(long regularPay, long overtimePay, long allowance, long deduction, long advance) {
        return Math.addExact(Math.addExact(regularPay, overtimePay), allowance) - deduction - advance;
    }
}
