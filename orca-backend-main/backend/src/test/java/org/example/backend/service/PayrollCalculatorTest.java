package org.example.backend.service;

import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import static org.junit.jupiter.api.Assertions.assertEquals;

class PayrollCalculatorTest {
    @Test
    void calculatesRegularAndOvertimeInWholeVnd() {
        assertEquals(2_000_000L, PayrollCalculator.multiply(new BigDecimal("40"), 50_000L, BigDecimal.ONE));
        assertEquals(75_000L, PayrollCalculator.multiply(new BigDecimal("1"), 50_000L, new BigDecimal("1.50")));
    }

    @Test
    void calculatesApprovedWorkshopExamples() {
        long regular = PayrollCalculator.multiply(new BigDecimal("7.50"), 50_000L, BigDecimal.ONE);
        long overtime = PayrollCalculator.multiply(new BigDecimal("2.00"), 50_000L, new BigDecimal("1.50"));
        assertEquals(375_000L, regular);
        assertEquals(150_000L, overtime);
        assertEquals(525_000L, Math.addExact(regular, overtime));
    }

    @Test
    void calculatesExactNetWithAdjustments() {
        assertEquals(2_125_000L, PayrollCalculator.net(2_000_000, 75_000, 100_000, 25_000, 25_000));
        assertEquals(-100_000L, PayrollCalculator.net(100_000, 0, 0, 200_000, 0));
    }
}
